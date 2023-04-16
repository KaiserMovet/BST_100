#!/bin/bash -x
image_name="python:3.11"
datasets_path="$(readlink -f $PWD/../../datasets)"
app_path="$(readlink -f $PWD/.)"

echo "============="
docker run \
    --name bst-python3-container \
    -v $datasets_path:/datasets \
    -v $app_path:/app \
    -it $image_name \
    bash -c "cd app && python main.py"
echo "============="

docker stop bst-python3-container
docker rm bst-python3-container
