import fr_core_news_sm
import argparse

# Prune the copula extraction log

def main():
    parser = argparse.ArgumentParser(description="Prune the copula results")
    parser.add_argument("log")
    parser.add_argument("out")
    args = parser.parse_args()

    nlp = fr_core_news_sm.load()

    out = open(args.out, "w", encoding='UTF-8')

    with open(args.log, "r", encoding='UTF-8') as file:
        for line in file:
            subject, copula, attribute = line.split()

            # remove small words like c', ce, l', la
            if len(subject) <= 2:
                continue
            if len(attribute) <= 2:
                continue
            
            s = nlp(subject, disable=["ner", "dep"])[0]
            if not (s.pos_ == "NOUN" or s.pos_ == "PROPN"):
                continue

            a = nlp(attribute, disable=["ner", "dep"])[0]
            if not (a.pos_ == "NOUN" or a.pos_ == "PROPN"):
                continue
            
            print(subject, copula, attribute, file=out)
    out.close()

if __name__ == "__main__":
    main()