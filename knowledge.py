import os
import spacy
import argparse
import json

# Extract knowledge from dependency parsing


def is_negation(token: spacy.tokens.Token) -> bool:
    """
    Detects whether the given subject token is predicated by a negation.

    Limits:
    The method does not look at relative clauses in the predicate.
    """
    assert(token.dep_ == "nsubj")

    children = set(x.text for x in token.head.children)
    if len(children.intersection(["n'", "ne"])) != 0:
        return True

    negation_words = children.intersection(["pas", "jamais"])
    if any(item in negation_words for item in [x.text for x in token.head.lefts]):
        return True

    return False


def copula_knowledge(nlp, text):
    doc = nlp(text, disable=["ner"])
    for token in doc:
        if token.dep_ == "nsubj" and token.pos_ != "PRON" and "cop" in [x.dep_ for x in token.head.children]:
            if is_negation(token):
                print(f"{token.text} IS_NOT_A {token.head.text}")
            else:
                print(f"{token.text} IS_A {token.head.text}")


def main():
    parser = argparse.ArgumentParser(
        description="Extracts copula relationships from corpus directory")
    parser.add_argument("directory")
    args = parser.parse_args()

    nlp = spacy.load("fr_core_news_sm")
    
    for file in os.listdir(args.directory):
        path = os.path.join(args.directory, file)
        
        with open(path, "r") as file:
            article = json.load(file)

            for paragraph in article["BodyParagraphs"]:

                copula_knowledge(nlp, paragraph)


if __name__ == "__main__":
    main()
