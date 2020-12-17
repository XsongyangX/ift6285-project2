import spacy
import argparse

# Prune the copula extraction log

def main():
    parser = argparse.ArgumentParser(description="Prune the copula results")
    parser.add_argument("log")
    args = parser.parse_args()

    with open(args.log, "r", encoding='UTF-8') as file:
        for line in file:
            subject, copula, attribute = line.split()
            print(subject, copula, attribute)
            break

if __name__ == "__main__":
    main()