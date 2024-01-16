#!/bin/bash

# Maybe specify directories to include in an array?
# Then include them in the zip file.

# Path for all lambda layers.
LAMBDA_DIR="../src/lambdas/parser"

# Output path for all lambda layer zip-files.
OUTPUT_DIR="../builds/lambdas"

# Add output directory in case it does not exist already.
mkdir -p "$OUTPUT_DIR"

# Install requirements to package.
pip3 install -r requirements.txt -t "${LAMBDA_DIR}/package"

# Check if the package directory exists
if [ -d "${LAMBDA_DIR}/package" ]; then
    # If the package directory exists, include it in the zip command.
    zip -9 -r "${OUTPUT_DIR}/parser.zip" "${LAMBDA_DIR}/handler.py" "${LAMBDA_DIR}/package"
    rm -r "${LAMBDA_DIR}/package"
else
    # If the package directory does not exist, only zip handler.py.
    zip -9 -r "${OUTPUT_DIR}/parser.zip" "${LAMBDA_DIR}/handler.py"
fi
