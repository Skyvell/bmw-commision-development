#!/bin/bash

# Get the directory where the script is located.
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Import functions from helper_functions.sh located in the scripts folder.
source "${SCRIPT_DIR}/helper_functions.sh"

# These files and directories should be included in final zip package.
FILES_TO_INCLUDE_IN_ZIP=(handler.py constants.py utils parsing)

# Get project root directory.
PROJECT_ROOT_DIR=$(find_path_ending_with $(pwd) "commission")

# Path for all lambda layers.
LAMBDA_DIR="${PROJECT_ROOT_DIR}/src/lambdas/parser"

# Output path for all lambda layer zip-files.
OUTPUT_DIR="${PROJECT_ROOT_DIR}/builds/lambdas"

# Add output directory in case it does not exist already.
mkdir -p "$OUTPUT_DIR"

# Install requirements to package.
pip3 install -r "${LAMBDA_DIR}/requirements.txt" -t "${LAMBDA_DIR}/package"

# Remove old zip file.
rm -f "${OUTPUT_DIR}/parser.zip"

# Enter lambda directory, zip and export.
cd "$LAMBDA_DIR"
if [ -d "./package" ]; then
    # If the package directory exists, include it in the zip command.
    zip -9 -r "${OUTPUT_DIR}/parser.zip" "${FILES_TO_INCLUDE_IN_ZIP[@]}" package
    rm -r package
else
    # If the package directory does not exist, only zip handler.py.
    zip -9 -r "${OUTPUT_DIR}/parser.zip" "${FILES_TO_INCLUDE_IN_ZIP[@]}"
fi