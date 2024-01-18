import pandas as pd
from json import dumps
from enum import Enum
from io import BytesIO
import boto3
import logging
import os

#FILEPATH_1 = "../../tests/test_matrices.xlsx"
#FILEPATH_2 = "../../tests/test_volume_targets.xlsx"
PENETRATAION_RATE = "PENETRATION RATE"
VOLUME_TARGET_ACHIEVEMENT = "VOLUME TARGET ACHIEVEMENT"

def lambda_handler(event, context):
    # Initialize logging.
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Get enviroment variables.
    matrix_table_name = os.environ.get("DYNAMODB_TABLE_NAME_COMMISSION_MATRICES")
    sales_targets_table_name = os.environ.get("DYNAMODB_TABLE_NAME_VOLUME_TARGETS")

    # Initialize aws resources.
    s3 = boto3.client("s3")
    dynamodb = boto3.resource('dynamodb')
    matrix_table = dynamodb.Table(matrix_table_name)
    sales_targets_table = dynamodb.Table(sales_targets_table_name)

    # Extract bucket name and file key from the s3 event that triggered the lambda.
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    # Read the file from s3.
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = response['Body'].read()

    # Read the contents into a dataframe.
    df = pd.read_excel(BytesIO(file_content))

    # Determine file type and execute code dependent on file type.
    file_type = get_file_type(file_key)
    year = extract_year(file_key)
    if file_type == FileType.MATRIX:
        data = extract_matrix_data(df)

    elif file_type == FileType.SALES_TARGET:
        pass
    else:
        logger.error(f"Filetype: {file_type.name}")


    # Log file key and bucket name.
    logger.info(f"Filekey: {file_key}; Bucketname: {bucket_name}")
    logger.info(f"Event: {event}")
    logger.info(f"Dataframe: {df}")

    #all_excel_sheets = pd.read_excel(FILEPATH_1, header=None, sheet_name=None)#
    #for sheet, matrix_df in all_excel_sheets.items():
    #    matrix_data = extract_matrix_data(matrix_df)
    #    
    #    print(f"Market: {sheet}: {matrix_data} \n")

def main2():
    # Initize AWS resources. Permissions decided by lambda execution role.
    # s3 = boto3.resource("s3")
    # dynamodb = boto3.resource('dynamodb')

    # Extract bucket name and file key from the s3 event that triggered the lambda.
    # bucket_name = event['Records'][0]['s3']['bucket']['name']
    # file_key = event['Records'][0]['s3']['object']['key']
    
    # Read the file.
    df = pd.read_excel(FILEPATH_2)

    # Remove all columns with only NaN values.
    df = df.dropna(how='all').dropna(how='all', axis=1)

    # Extract all column names. First one is agent column, the rest are dates on the form YYYY-MM
    columns = df.columns.to_list()

    # Loop through all the rows, construct 
    items = []
    for index, row in df.iterrows():
        agent_name = row[columns[0]]
        for month in columns[1:]:
        
            item = {
                'agent': agent_name,
                'year_month': month,
                'target': row[month]  # Convert value to int as DynamoDB requires specific #types
            }

        
            items.append(item)

        # Use writebatch here.
    print(items)
    print(df)

def extract_matrix_data(df) -> dict:
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

class CommissionMatrixParser:
    def __init__(self, file_name, dynamodb):
        self.file_name = file_name
        self.table = dynamodb.Table(os.environ.get("DYNAMODB_TABLE_NAME_COMMISSION_MATRICES"))

    def parse_matrix_file(self)

    def construct_dynamodb_item(self, market: str, year: str, matrix_data: dict) -> dict:
        item = {
            "market": market,
            "year": year,
            "matrix": matrix_data
        }
        return item
    
    def write_item_to_dynamodb(self, item):
        self.table.put_item(item)

class UnknownFileTypeException(Exception):
    pass 

class FileParser:
    def __init__(self, event, dynamodb, s3):
        self.file_name = event['Records'][0]['s3']['object']['key']
        self.bucket_name = event['Records'][0]['s3']['bucket']['name']
        self.file_type = get_file_type(self.file_name)
        self.year = extract_year_from_file_name(self.file_name)

    def parse_file(self):
        if self.file_type == FileType.MATRIX:
            self.parse_matrix_file()
        elif self.file_type == FileType.SALES_TARGET:
            self.parse_sales_targets_file()
        else:
            raise UnknownFileTypeException
        
    def parse_matrix_file():
        pass

    def extract_matrix_data(df):
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
    


def construct_matrix_item(market: str, year: str, matrix_data: dict) -> dict:
    item = {
        "market": market,
        "year": year,
        "matrix": matrix_data
    }
    return item

def construct_volume_target_item(agent: str, year_month: str, target: float):
    item = {
        "agent": agent,
        "year_month": year_month,
        "target": target
    }
    return item

#def write_item_to_dynamodb(table_name: str, item):



#if __name__ == "__main__":
#    main2()


# How to check if file is matrix file or target file:
# Filenames: matrix_2004.xlsx, sales_targets_2004.xlsx.
# startswith to

class FileType(Enum):
    MATRICES = 1
    VOLUME_TARGETS = 2
    UKNOWN = 3

def get_file_type(file_name: str) -> FileType:
    if file_name.startswith("matrix"):
        return FileType.MATRICES
    elif file_name.startswith("sales_targets"):
        return FileType.VOLUME_TARGETS
    else:
        return FileType.UKNOWN
    
def extract_year_from_file_name(file_name: str) -> str:
    year = file_name.split("_")[-1].split(".")[0]
    return year
    
    