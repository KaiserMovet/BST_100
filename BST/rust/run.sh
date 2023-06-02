#!/bin/bash
if [ -z "$1" ]; then
  amount=10000000
else
  amount=$1
fi

image_name="rust:1.67"
container_name=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 10 | head -n 1)

script_dir="$(cd "$(dirname "$0")" && pwd)"
datasets_path="$(readlink -f "$script_dir/../../datasets")"
app_path="$(readlink -f "$script_dir")"

echo "============="
docker run \
    --name $container_name \
    -v $datasets_path:/datasets \
    -v $app_path:/app \
    $image_name \
    bash -c "cd app && rustc main.rs && ./main $amount"
echo "============="

docker stop $container_name
docker rm $container_name
