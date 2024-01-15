#!/bin/bash
EXAMPLE_LAMBDA_DIR="../src/example-lambda/"
DESTINATION="../../dist"

# Enter lambda dir and creates the .zip file from requirements file.
# See AWS doc for file structure.
cd "$EXAMPLE_LAMBDA_DIR"
zip -9 -r example_lambda.zip handler.py

# Creates the destination if it does not exist.
mkdir -p "$DESTINATION"

# Move the final zip file to the destination. Overwrites privious zipfiles in the destination dir.
mv example_lambda.zip "$DESTINATION"