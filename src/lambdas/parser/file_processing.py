import pandas as pd
from enum import Enum
from io import BytesIO
from src.lambdas.parser.utils.conversion import convert_floats_to_decimals
from utils.dynamodb import DynamoDB
from utils.s3 import S3
from constants import PENETRATAION_RATE, VOLUME_TARGET_ACHIEVEMENT

class FileTypeUnknownError(Exception):
    pass

class FileType(Enum):
    MATRICES = 1
    VOLUME_TARGETS = 2
    UKNOWN = 3
    
class FileMetadata:
    def __init__(self, file_name):
        self.file_name = file_name
        self.year = self._extract_year_from_file_name(file_name)
        self.file_type = self._get_file_type(file_name)

    def _get_file_type(self, file_name: str) -> FileType:
        if file_name.startswith("commission_matrices"):
            return FileType.MATRICES
        elif file_name.startswith("agent_volume_sales_targets"):
            return FileType.VOLUME_TARGETS
        else:
            return FileType.UKNOWN
    
    def _extract_year_from_file_name(self, file_name: str) -> str:
        year = file_name.split("_")[-1].split(".")[0]
        return year

class S3FileParser:
    def __init__(self, event, s3_client: S3, dynamodb_resource: DynamoDB):
        # AWS services.
        self.s3_client = s3_client
        self.dynamodb_resource = dynamodb_resource

        # File information and data.
        self.bucket_name = self._extract_bucket_name(event)
        self.file_metadata = FileMetadata(self._extract_file_name)
        self.file_content = s3_client.read_file(self.bucket_name, self.file_metadata.file_name)

    def parse_file(self):
        if self.file_metadata.file_type == FileType.MATRICES:
            commission_matrix_parser = CommissionMatricesParser()
            items = commission_matrix_parser.parse_matrices()
            self.dynamodb_resource.write_items(items)

        elif self.file_metadata.file_type == FileType.VOLUME_TARGETS:
            volume_targets_parser = VolumeTargetsParser()
            items = volume_targets_parser.parse_volume_targets()
            self.dynamodb_resource.write_items_batch(items)
        
        else:
            raise FileTypeUnknownError

    def _extract_bucket_and_key_from_event(self, event):
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        return bucket_name, file_key
    
    def _extract_bucket_name(self, event):
        return event['Records'][0]['s3']['bucket']['name']
    
    def _extract_file_name(self, event):
        return event['Records'][0]['s3']['object']['key']


class CommissionMatricesParser:
    def parse_matrices(self, file_content, year):
        """
        Processes Excel sheets containing commission matrices.
        Converts each sheet to a dictionary item and formats the data.

        Args:
        - file_content (bytes): The content of the Excel file.
        - year (str): The year extracted from the file name.

        Returns:
        - List[dict]: List of dictionaries, each representing a commission matrix.
        """
        try:
            all_sheets = pd.read_excel(BytesIO(file_content), header=None, sheet_name=None)
        except Exception as e:
            raise ValueError(f"Error reading Excel file: {e}")

        commission_matrices = []
        for sheet_name, df in all_sheets.items():
            matrix_data = self._extract_commission_matrix_from_dataframe(df)
            commission_matrices.append({
                "market": sheet_name,
                "year": year,
                "matrix": matrix_data
            })

        return convert_floats_to_decimals(commission_matrices)

    def _extract_commission_matrix_from_dataframe(self, df):
        # Repleace the cells containing "PENETRATION RATE" and "VOLUME TARGET ACHIEVEMENT" with None.
        df.replace(PENETRATAION_RATE, None, inplace=True)
        df.replace(VOLUME_TARGET_ACHIEVEMENT, None, inplace=True)

        # Drop all rows and tables that only contain NaN.
        df = df.dropna(how='all').dropna(how='all', axis=1)
        df = df.dropna(how='all').dropna(how='all', axis=0)

        # Extract y axis.
        y_axis = df.iloc[:-1, 0].to_list()[::-1]

        # Extract x-axis.
        x_axis = df.iloc[-1, 1:].to_list()

        # Extract matrix.
        matrix = df.iloc[:-1, 1:].values.tolist()

        # Construct json matrix data.
        data = {
            "x_axis": x_axis,
            "y_axis": y_axis,
            "matrix": matrix
        }

        return data    

class VolumeTargetsParser:
    def parse_volume_targets(file_content):
        try:
            df = pd.read_excel(BytesIO(file_content))
        except Exception as e:
            raise ValueError(f"Error reading Excel file: {e}")

        df = df.dropna(how='all').dropna(how='all', axis=1)
        columns = df.columns.to_list()
        items = [
            {
                'agent': row[columns[0]],
                'year_month': month,
                'target': int(row[month])
            }
            for index, row in df.iterrows()
            for month in columns[1:]
        ]

        return items


