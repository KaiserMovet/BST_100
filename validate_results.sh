#!/bin/bash

file_path=$1
length=$2
height=$3

output=$(cat $file_path)

validation=$(echo "$output" | grep VALIDATION)
validation_length=$(echo $validation | cut -d':' -f2)
validation_height=$(echo $validation | cut -d':' -f3)

if [ "$validation_length" -eq "$length" ] && [ "$validation_height" -eq "$height" ]; then
    echo "VALIDATION SUCCESSFUL"
    exit 0
else
    echo "VALIDATION FAILED: Expected length $length and height $height but got length $validation_length and height $validation_height"
    exit 1
fi
