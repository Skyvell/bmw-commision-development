import boto3


class DynamoDB:
    """
    A simple wrapper class for AWS Dynamodb operations using boto3.
    """

    def __init__(self):
        self.resource = boto3.resource("dynamodb")
    
    def write_items(self, table_name, items):
        """ Write items to the specified DynamoDB table.

        Args:
            table_name (str): The name of the DynamoDB table.
            items (list): List of items to write.

        Returns:
            None
        """
        table = self.resource.Table(table_name)
        for item in items:
            response = table.put_item(Item=item)

    def write_items_batch(self, table_name, items):
        """ Write items to the specified DynamoDB table in batch.

        Args:
            table_name (str): The name of the DynamoDB table.
            items (list): List of items to write.

        Returns:
            None
        """
        table = self.resource.Table(table_name)
        with table.batch_writer() as batch:
            for item in items:
                batch.put_item(item)