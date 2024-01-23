from utils.dynamodb import DynamoDB
from utils.s3 import S3
from parsing.s3_parser import S3FileParser
import logging


def lambda_handler(event, context):
    # Setup logging.
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Setup AWS resources.
    s3 = S3()
    dynamodb = DynamoDB()
   
    # Parse the file contents from S3 to dynamoDB. All information about the file
    # is contain within the event.
    s3_file_parser = S3FileParser(event, s3, dynamodb)
    s3_file_parser.parse_file()