#!/bin/bash

# Import functions.
source ./helper_functions.sh

# Get project root directory.
PROJECT_ROOT_DIR=$(find_path_ending_with $(pwd) "commission")

# Path for all lambda layers.
LAYERS_DIR="${PROJECT_ROOT_DIR}/src/layers"

# Pupulate this array with all individual layer folders.
# When a new layer is added, add the folder name to this array.
LAYERS=("pandas")

# Output path for all lambda layer zip-files.
OUTPUT_DIR="${PROJECT_ROOT_DIR}/builds/layers"

# Add output directory in case it does not exist already.
mkdir -p "$OUTPUT_DIR"

# Iterate through all the layers and create the zipfiles in the output dir.
# Adds _layer.zip as an extension to the layer name.
for layer in "${LAYERS[@]}"; do
    cd "${LAYERS_DIR}/${layer}"
    rm -f "${OUTPUT_DIR}/${layer}.zip"
    zip -9 -r "${OUTPUT_DIR}/${layer}.zip" ./python
done