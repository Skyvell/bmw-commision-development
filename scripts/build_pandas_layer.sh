#!/bin/bash
cd ../lambda_layers/pandas_layer
find . -type f -not -name 'requirements.txt' -delete
find . -type d -not -path './.*' -not -path '*/.*' -exec rm -rf {} +
pip3 install -r requirements.txt -t ./python/lib/python3.8/site-packages
zip -r pandas_layer.zip python