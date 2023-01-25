import os
import sys
import re

# die header stimmen
header1 = "26.10.2012\n\nDE\n\nAmtsblatt der Europäischen Union\n\nC 326\/\d+\n\n"
header2 = "C 326\/\d+\n\nDE\n\nAmtsblatt der Europäischen Union\n\n26.10.2012\n\n" 
footnote = "\(1\) Dieser Verweis hat lediglich hinweisenden Charakter\. Zur Vertiefung vgl\. die Übereinstimmungstabellen für die Ent\W+sprechung zwischen bisheriger und neuer Nummerierung der Verträge\."

def split_sentences(articles):
    for i, a in enumerate(articles):
        for j, p in enumerate(a):
            articles[i][j] = re.split("\.\s", p.strip())

    return articles    

def split_paragraphs(articles):
    for i, a in enumerate(articles):
        articles[i] = re.split("\(\d+\)", a)
    return articles

def strip_to_last_sentence(article):
    article += "\n"
    ind = article.rfind(".\n")
    if(ind <= 0):
        ind = len(article)-2
    return article[:ind+2]

def extract_paragraphs(articles):
    for i, article in enumerate(articles):
        articles[i]= strip_to_last_sentence(article).strip()

    return articles

def split_articles(text):
    return re.split("\nArtikel\s+\d+\n", text) 

def remove_unwanted(text):
    res = re.sub("\(ex-Artikel\s+\d+\s.+", "", text)
    res = re.sub(header1, "", res)
    res = re.sub(header2, "", res).replace("\f", "")
    res = re.sub(footnote, "", res)

    return res

def main(args):
    with open(args[1], "r", encoding="utf-8") as f:
        text = f.read()
    text = remove_unwanted(text)
    articles = split_articles(text)[1:]
    articles = extract_paragraphs(articles)
    articles = split_paragraphs(articles)
    articles = split_sentences(articles)

    for a in articles:
        print("\nARTIKEL: \n")
        for p in a:
            print("\n   PARAGRAPH: \n")
            for s in p:
                print("\n       SENTENCE: \n")
                print(s + ".")

if __name__ == "__main__":
    main(sys.argv)
