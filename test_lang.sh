#!/bin/bash

# This script is used to validate bst program output.

# Check if a file was supplied as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <file>"
  exit 1
fi

# The file to validate
file=$1

# The keys that should be in the file
required_keys=("ADD_TEST" "CHECK_TEST" "LEN_TEST" "HEIGHT_TEST" "VALIDATION")

# Iterate over the required keys
for key in "${required_keys[@]}"; do
  # Check if the key is in the file
  if ! grep -q "^$key:" "$file"; then
    echo "Error: Key '$key' not found in file '$file'"
    exit 1
  fi
done

# Check the format of the VALIDATION key
if ! grep -qE '^VALIDATION:\d+:\d+$' "$file"; then
  echo "Error: 'VALIDATION' key is not in the correct format in file '$file'"
  exit 1
fi

# Check the format of the other keys
if grep -qE '^(ADD_TEST|CHECK_TEST|LEN_TEST|HEIGHT_TEST):[^0-9\.e-]+$' "$file"; then
  echo "Error: One or more keys are not in the correct format in file '$file'"
  exit 1
fi

# If we've made it this far, the file is valid
echo "File '$file' is valid"
exit 0
