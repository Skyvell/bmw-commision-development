#!/bin/bash

# Path for all lambda layers.
LAYERS_DIR="../src/layers"

# Pupulate this array with all individual layer folders.
# When a new layer is added, add the folder name to this array.
LAYERS=("pandas")

# Output path for all lambda layer zip-files.
OUTPUT_DIR="../builds/layers"

# Iterate through all the layers and create the zipfiles in the output dir.
# Adds _layer.zip as an extension to the layer name.
for layer in "${LAYERS[@]}"; do
    zip -9 -r "${OUTPUT_DIR}/${layer}_layer.zip" "${LAYERS_DIR}/${layer}/python"
done