import pandas as pd
from json import dumps
import boto3

FILEPATH_1 = "../../tests/test_matrices.xlsx"
FILEPATH_2 = "../../tests/test_volume_targets.xlsx"
PENETRATAION_RATE = "PENETRATION RATE"
VOLUME_TARGET_ACHIEVEMENT = "VOLUME TARGET ACHIEVEMENT"

def main():
    # Initize AWS resources. Permissions decided by lambda execution role.
    # s3 = boto3.resource("s3")
    # dynamodb = boto3.resource('dynamodb')

    # Extract bucket name and file key from the s3 event that triggered the lambda.
    # bucket_name = event['Records'][0]['s3']['bucket']['name']
    # file_key = event['Records'][0]['s3']['object']['key']

    all_excel_sheets = pd.read_excel(FILEPATH_1, header=None, sheet_name=None)

    for sheet, matrix_df in all_excel_sheets.items():
        matrix_data = extract_matrix_data(matrix_df)
        
        print(f"Market: {sheet}: {matrix_data} \n")

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
                'AgentName': agent_name,
                'Month': month,
                'SalesVolume': int(row[month])  # Convert value to int as DynamoDB requires specific types
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
        "x-axis": x_axis,
        "y-axis": y_axis,
        "matrix": matrix
    }

    return data

if __name__ == "__main__":
    main2()