import pandas as pd
from io import BytesIO
from src.lambdas.parser.utils.conversion import convert_floats_to_decimals
from src.lambdas.parser.constants import PENETRATION_RATE, VOLUME_TARGET_ACHIEVEMENT


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
        all_sheets = pd.read_excel(BytesIO(file_content), header=None, sheet_name=None)

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
        df.replace(PENETRATION_RATE, None, inplace=True)
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
            "values": matrix
        }

        return data