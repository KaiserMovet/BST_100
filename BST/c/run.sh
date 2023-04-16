#!/bin/bash -x
image_name="gcc:12"
datasets_path="$(readlink -f $PWD/../../datasets)"
app_path="$(readlink -f $PWD/.)"


docker run \
    --name bst-cpp-container \
    -v $datasets_path:/datasets \
    -v $app_path:/app \
    -it $image_name \
    bash -c "cd app && g++ -std=c99 -o main.out main.c node.c tree.c && ./main.out"


docker stop bst-cpp-container
docker rm bst-cpp-container
