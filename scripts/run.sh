#!/bin/sh
cd $(dirname $0)/.. || exit 1
export  FILE_NAME=file.txt
export CONNECT_STRING=redis://localhost:6379
python main.py 