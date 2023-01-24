import os
import sys
import re

// die header stimmen noch ned
header1 = "26.10.2012\n\nDE\n\n.\n\nC 326\w+\n\n"
header2 = "C 326\w+\n\nDE\n\n.\n\n26.10.2012\n\n" 

def strip_to_last_sentence(article):
    article += "\n"
    ind = article.rfind(".\n")
    if(ind <= 0):
        ind = len(article)-2
    return article[:ind+2]

def extract_paragraphs(articles):
    for i, article in enumerate(articles):
        articles[i]= strip_to_last_sentence(article).strip()

    # TODO:
    #   - remove footnotes.
    #   - split paragraphs.
    # Note: maybe it is easier to first split by paragraphs and the remove the footnotes,
    # because they do not match the internal numbering order of the paragraph (inspect document in legaldocs/.

    return articles

def split_articles(text):
    return re.split("\nArtikel\s+\d+\n", text) 

def remove_unwanted(text):
    res = re.sub("\(ex-Artikel\s+\d+\s.+", "", text)
    res = re.sub(header1, "", res)
    res = re.sub(header2, "", res)    

    return res

def main(args):
    with open(args[1], "r") as f:
        text = f.read()
    articles = split_articles(remove_unwanted(text))[1:]
    articles = extract_paragraphs(articles)

    for a in articles:
        print(a)
        print("------------")

if __name__ == "__main__":
    main(sys.argv)
