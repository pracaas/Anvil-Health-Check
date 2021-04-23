#!/bin/bash
# Note give permission to the script
# > chmod 777 <filename>
echo "Calling the file from script..."
fullpath="$0"
echo $fullpath
path=$(dirname $fullpath)
cd $path
paths=$(dirname $path)
echo $paths
cd $paths
python3 anvilhealthcheck.py