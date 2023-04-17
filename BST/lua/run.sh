#!/bin/bash -x
image_name="nickblah/lua:5"
datasets_path="$(readlink -f $PWD/../../datasets)"
app_path="$(readlink -f $PWD/.)"


docker run \
    --name bst-cpp-container \
    -v $datasets_path:/datasets \
    -v $app_path:/app \
    -it $image_name \
    bash -c "cd app && lua main.lua"


docker stop bst-cpp-container
docker rm bst-cpp-container
