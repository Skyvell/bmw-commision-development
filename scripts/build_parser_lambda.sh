#!/bin/bash
PARSER_LAMBDA_DIR="../src/parser-lambda/"
DESTINATION="../../dist"

# Enter lambda dir and creates the .zip file from requirements file.
# See AWS doc for file structure.
cd "$PARSER_LAMBDA_DIR"
mkdir -p package
pip3 install -r requirements.txt -t ./package
cd package
#zip -9 -r ../parser_lambda.zip .

# Back to lambda dir.
cd ..

# Add handler.py to the existing zip file.
zip -9 -r parser_lambda.zip handler.py

# Creates the destination if it does not exist.
mkdir -p "$DESTINATION"

# Move the final zip file to the destination. Overwrites privious zipfiles in the destination dir.
mv parser_lambda.zip "$DESTINATION"

# Clean up the package directory.
rm -r package

