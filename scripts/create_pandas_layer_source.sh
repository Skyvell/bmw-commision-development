#!/bin/bash

# Constants.
LAYER_PATH="../src/layers/pandas"
PYTHON_RUNTIME="python3.11"

# Install dependencies using pip3.
# Some of the arguments are needed for these packages to work on linux.
pip3 install \
    --platform manylinux2014_x86_64 \
    --implementation cp \
    --only-binary=:all: \
    --upgrade \
    -r "${LAYER_PATH}/requirements.txt" \
    --target "${LAYER_PATH}/python/lib/${PYTHON_RUNTIME}/site-packages"

# Check if pip install was successful.
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies."
    exit 1
fi
