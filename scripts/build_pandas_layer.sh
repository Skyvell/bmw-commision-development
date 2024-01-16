#!/bin/bash

# Constants.
DESTINATION="../builds/layers/"
ZIP_FILE_NAME="pandas_layer.zip"
SOURCE="../src/layers/"
PYTHON_RUNTIME="python3.11"

# Install dependencies using pip3.
pip3 install \
    --platform manylinux2014_x86_64 \
    --implementation cp \
    --only-binary=:all: \
    --upgrade \
    -r "${SOURCE}/requirements.txt" \
    --target "${SOURCE}/python/lib/${PYTHON_RUNTIME}/site-packages"

# Check if pip install was successful
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies"
    exit 1
fi

mkdir -p "$DESTINATION"

# Navigate to SOURCE directory and zip the installed packages.
zip -r "${DESTINATION}/${ZIP_FILE_NAME}" "${SOURCE}/python"

# Check if zip was successful
if [ $? -ne 0 ]; then
    echo "Failed to create ZIP file"
    exit 1
fi
