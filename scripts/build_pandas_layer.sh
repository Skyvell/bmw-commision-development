#!/bin/bash

# Change to the desired directory
cd ../lambda_layers/pandas_layer

# Install dependencies using pip3.
pip3 install \
    --platform manylinux2014_x86_64 \
    --implementation cp \
    --only-binary=:all: \
    --upgrade \
    -r requirements.txt \
    --target ./python/lib/python3.11/site-packages

# Zip the installed packages.
zip -r pandas_layer.zip python

# Clean up.
rm -r ./python
