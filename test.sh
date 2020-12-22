#!/bin/bash

for file in data/test/*.json; do 
    python knowledge.py $file > "${file%.*}".log
    python prune.py "${file%.*}".log "${file%.*}".out
done