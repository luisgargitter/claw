import os
import sys
import re

def extract_paragraphs(articles):
    for i, article in enumerate(articles):
        articles[i] = re.sub("\(ex-Artikel \d+ .+", " ", article).strip()

    # TODO:
    #   - remove footnotes.
    #   - split paragraphs.
    # Note: maybe it is easier to first split by paragraphs and the remove the footnotes,
    # because they do not match the internal numbering order of the paragraph (inspect document in legaldocs/.

    return articles

def split_articles(text):
    return re.split("\nArtikel \d+\n", text) 

def main(args):
    with open(args[1], "r") as f:
        text = f.read()
    articles = split_articles(text)[1:]
    articles = extract_paragraphs(articles)

    for a in articles:
        print(a)
        print("------------")

if __name__ == "__main__":
    main(sys.argv)
