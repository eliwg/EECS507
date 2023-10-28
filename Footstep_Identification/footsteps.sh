#!/bin/bash
#pwd

# Define the target directory
directory="data/raw"

# Check if the target is not a directory
if [ ! -d "$directory" ]; then
  exit 1
fi

# Run FootStepSplicer.py with all of raw data as arg
for file in "$directory"/*; do
  if [ -f "$file" ]; then
    echo "Getting footsteps from $file"
    python3  Footstep_Identification/FootStepSplicer.py -i "$file"
  fi
done