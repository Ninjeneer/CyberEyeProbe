#!/bin/bash

FILES_TO_CREATE="main.py Dockerfile .dockerignore"

read -p "New probe name: " probe_name

mkdir $probe_name
cd $probe_name

mkdir connectivity
cd connectivity
ln -s ../../connectivity/* .
cd ..

python3 -m venv venv-$probe_name

for file in $FILES_TO_CREATE
do
    touch $file
done

echo "Probe [$probe_name] created successfully"
