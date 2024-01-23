from os import getenv

class EnvironmentVariables:
    """
    A class to encapsulate the environment variables used in the application.

    This class abstracts the fetching of environment variable values, providing 
    a centralized location for accessing these values throughout the application. 
    It helps in maintaining clean code and eases the process of reading and 
    managing environment-specific settings.

    Attributes:
    - MATRICES_TABLE_NAME (str): The name of the DynamoDB table for commission matrices,
                                 fetched from the DYNAMODB_TABLE_NAME_COMMISSION_MATRICES 
                                 environment variable.
    - SALES_TARGETS_TABLE_NAME (str): The name of the DynamoDB table for sales targets,
                                      fetched from the DYNAMODB_TABLE_NAME_VOLUME_TARGETS
                                      environment variable.
    """

    MATRICES_TABLE_NAME = getenv("DYNAMODB_TABLE_NAME_COMMISSION_MATRICES")
    SALES_TARGETS_TABLE_NAME = getenv("DYNAMODB_TABLE_NAME_VOLUME_TARGETS")


# Constants for cells to be replaced in the excel file.
PENETRATION_RATE = "PENETRATION RATE"
VOLUME_TARGET_ACHIEVEMENT = "VOLUME TARGET ACHIEVEMENT"