#!/bin/bash

# Distribute the corpus over the knowledge extractor

if [ $# -ne 2 ]; then
    echo "Usage: ./distribute.sh corpus-directory number-of-machines"
    exit 1
fi

corpus=$1
machineCount=$(($2 - 1))

# Create files containing paths
for i in $(seq 0 $machineCount);
do
    > "distributed_$i.txt"
done

iter=0
for file in $corpus/*.json;
do
    section=$(($iter % $machineCount))
    iter=$(($iter + 1))

    echo $file >> "distributed_$i.txt"
done

# Distribute the work over the network
mkdir -p data/extractions
for i in $(seq 0 $machineCount);
do
    pkscreen -S "distributed-$i" ssh -J arcade ens \
        "cd ift6285/project2; python knowledge.py distributed_$i.txt --listed > data/extractions/knowledge_$i.log"
done