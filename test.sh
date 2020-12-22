#!/bin/bash

for file in data/test/*.json; do 
    python knowledge.py data/test/$file > data/extractions/$file
    python prune.py data/extractions/$file data/extractions/"${file%.*}".out
done