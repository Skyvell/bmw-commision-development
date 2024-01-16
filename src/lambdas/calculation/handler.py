import json

def lambda_handler(event, context):
    # Extract the 'name' from the event object
    name = event.get('name', 'World')

    # Create a greeting message
    greeting = f"Hello, {name}!"

    # Return the response
    # 'statusCode' is important for AWS Lambda to understand the response
    # 'body' contains the actual message
    return {
        'statusCode': 200,
        'body': json.dumps(greeting)
    }
