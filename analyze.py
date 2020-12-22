from typing import Dict

# check for duplicates
duplicates : Dict[str, int] = dict()

with open("pruned_copula.log", "r") as file:
    for line in file:
        line = line.strip()
        if line in duplicates:
            duplicates[line] += 1
        else:
            duplicates[line] = 1
