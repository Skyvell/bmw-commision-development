from parsing.file_metadata import FileMetadata, FileType
from parsing.matrices_parser import CommissionMatricesParser
from parsing.volume_targets_parser import VolumeTargetsParser
from utils.s3 import S3
from utils.dynamodb import DynamoDB
from constants import EnvironmentVariables


class NoFileParsedError(Exception):
    def __init__(self, message=""):
        super().__init__(message)


class S3FileParser:
    def __init__(self, event, s3_client: S3, dynamodb_resource: DynamoDB):
        # AWS services.
        self.s3_client = s3_client
        self.dynamodb_resource = dynamodb_resource

        # File information and data.
        self.bucket_name = self._extract_bucket_name(event)
        self.file_metadata = FileMetadata(self._extract_file_name(event))
        self.file_content = s3_client.read_file(self.bucket_name, self.file_metadata.file_name)

    def parse_file(self):
        if self.file_metadata.file_type == FileType.MATRICES:
            commission_matrix_parser = CommissionMatricesParser()
            items = commission_matrix_parser.parse_matrices(self.file_content, self.file_metadata.year)
            self.dynamodb_resource.write_items(EnvironmentVariables.MATRICES_TABLE_NAME, items)

        elif self.file_metadata.file_type == FileType.VOLUME_TARGETS:
            volume_targets_parser = VolumeTargetsParser()
            items = volume_targets_parser.parse_volume_targets(self.file_content)
            self.dynamodb_resource.write_items_batch(EnvironmentVariables.SALES_TARGETS_TABLE_NAME, items)
        
        else:
            raise NoFileParsedError(f"Unknown file type: {self.file_metadata.file_type} for file: {self.file_metadata.file_name}")

    
    def _extract_bucket_name(self, event):
        return event['Records'][0]['s3']['bucket']['name']
    
    def _extract_file_name(self, event):
        return event['Records'][0]['s3']['object']['key']