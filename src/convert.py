import sys
import re

def remove_unwanted(text):
    # remove everything in front of Artikel 1
    text = text[re.search("<p>Artikel 1</p>", text).span()[1]:]
    # remove attachment
    text = text[:re.search("<p>Protokolle</p>", text).span()[0]]
    # remove (ex-Artikel ...)
    text = re.sub("<p>\(ex-Artikel \d+.+</p>", "", text)
    # remove TITEL X
    text = re.sub("<p>TITEL .+</p>", "", text)
    # remove titles
    text = re.sub("<p>[A-Z]+.+[A-Z]+</p>", "", text)
    # remove footnotes
    text = re.sub("<p>\[\d+\].+</p>", "", text)

    return text

def split_articles(text):
    temp = re.split("<p>Artikel \d+</p>", text)
    return list(filter(None, temp)) # rempove empty articles

def split_paragraphs(article):
    temp = re.split("<p>\(\d+\)", article.strip())
    return list(filter(None, temp)) # remove empty paragraphs

def split_sentences(paragraph):
    temp = re.split("\.\s", paragraph.strip())
    return list(filter(None, temp)) # remove empty paragraphs

def cleanup(sentence):
    temp = re.sub("<.+>", "", sentence)
    return re.sub("\n", "", temp)

def clawid(a, p, s):
    return "CLAWID={}:{}:{}\t".format(a + 1, p + 1, s + 1)

def convert(text):
    text = remove_unwanted(text)
    out = ""
    
    articlev = split_articles(text)
    res = [None] * len(articlev)
    for i in range(0, len(articlev)):
        temp = split_paragraphs(articlev[i])
        res[i] = [None] * len(temp)
        for j in range(0, len(temp)):
            res[i][j] = split_sentences(temp[j])
            for k in range(0, len(res[i][j])):
                out += clawid(i, j, k) + cleanup(res[i][j][k]) + "\n"

    return out

def main(argv):
    with open(argv[1], "r", encoding="utf-8") as f:
        text = f.read()

    result = convert(text)
    
    with open(argv[2], "w", encoding="utf-8") as f:
        f.write(result)

    """    
    for a in result:
        print("Article:")
        for p in a:
            print("\tParagraph:")
            for s in p:
                print("\t\tSentence:")
                print(s)
    """

    print(result)

if __name__ == "__main__":
    main(sys.argv)
