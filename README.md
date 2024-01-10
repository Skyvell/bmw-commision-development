/my-lambda-project
|-- /dist
|   |-- lambda_function_one.zip
|   `-- lambda_function_two.zip
|-- /lambdas
|   |-- /lambda_function_one
|   |   |-- /venv
|   |   |-- main.py
|   |   `-- requirements.txt
|   |-- /lambda_function_two
|   |   |-- /venv
|   |   |-- main.py
|   |   `-- requirements.txt
|   `-- ...
`-- ...


This should be the general structure if lambdas require their own environments.