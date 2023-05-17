#!/bin/bash -x
image_name="rust:1.67"
datasets_path="$(readlink -f $PWD/../../datasets)"
app_path="$(readlink -f $PWD/.)"


docker run \
    --name bst-rust-container \
    -v $datasets_path:/datasets \
    -v $app_path:/app \
    -it $image_name \
    bash -c "cd app && rustc main.rs && ./main"


docker stop bst-rust-container
docker rm bst-rust-container
