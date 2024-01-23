import boto3

class S3:
    """
    A simple wrapper class for AWS S3 operations using boto3.
    """
    
    def __init__(self):
        self.client = boto3.client("s3")
    
    def read_file(self, bucket_name, file_name):
        """
        Reads a file from an S3 bucket.

        Args:
            bucket_name (str): The name of the S3 bucket.
            file_name (str): The key of the file in the S3 bucket.

        Returns:
            bytes: The content of the file.
        """
        response = self.client.get_object(Bucket=bucket_name, Key=file_name)
        return response['Body'].read()
