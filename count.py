from typing import Dict
import nltk.tokenize
import argparse
import json
import os

# Counts the json corpus

def parse():
    parser = argparse.ArgumentParser(description="Counts the words in the json corpus")

    parser.add_argument("directory")

    return parser.parse_args()

def read_json(path: str, voc: Dict[str, int]):
    
    with open(path, "r") as file:
        article = json.load(file)

        for paragraph in article["BodyParagraphs"]:
            words = nltk.tokenize.word_tokenize(paragraph, language="french")
            
            for word in words:
                if word in voc:
                    voc[word] += 1
                else:
                    voc[word] = 1

def main():
    
    args = parse()

    voc = dict()

    # loop on files in the folder
    for file in os.listdir(args.directory):
        path = os.path.join(args.directory, file)

        read_json(path, voc)

    import pickle
    os.makedirs("data/voc", exist_ok=True)
    with open("data/voc/vocab.voc", 'wb') as file:
        pickle.dump(voc, file)

if __name__ == "__main__":
    main()