import spacy

# Extract knowledge from dependency parsing

nlp = spacy.load("fr_core_news_sm")
doc = nlp("Le voisin est docteur")


def is_negation(token: spacy.tokens.Token) -> bool:
    """
    Detects whether the given subject token is predicated by a negation.

    Limits:
    The method does not look at relative clauses in the predicate.
    """
    assert(token.dep_ is "nsubj")

    children = set(x.text for x in token.head.children)
    if len(children.intersection(["n'", "ne"])) != 0:
        return True

    negation_words = children.intersection(["pas", "jamais"])
    if any(item in negation_words for item in [x.text for x in token.head.lefts]):
        return True

    return False


for token in doc:
    if token.dep_ == "nsubj" and token.pos_ != "PRON":
        if is_negation(token):
            print(f"{token.text} IS_NOT_A {token.head.text}")
        else:
            print(f"{token.text} IS_A {token.head.text}")
