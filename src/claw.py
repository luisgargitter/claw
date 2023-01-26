import sys
import re
import os

def help():
    print("""usage: claw <document> <article> <paragraph> <sentence>
    - supported documents: euv
    - leave parameters empty to perfom a partial search 
    (example: claw euv 26 1 -> returns all sentences under paragraph 1 of article 26)""")
    
def query(doc, clawid):
    filepath = re.sub("src/claw.py", "legaldocs/{}_de.claw".format(doc), __file__)
    with open(filepath, "r") as f:
        text = f.read()
    return re.findall("{}.+".format(clawid), text)

def claw_id(a, p, s):
    return "CLAWID={}:{}:{}".format(a, p, s)

def main(argv):
    if len(argv) < 4:
        print("error: not enough arguments, count: {} (threshold: {})".format(len(argv), 4)) 
        help()
        return -1
    if len(argv) > 5:
        print("error: too many arguments, count: {} (limit: {})".format(len(argv),5))
        help()
        return -1

    if(argv[1] == "--help" or argv[1] == "help"):
        help()
        return 0 

    argv.append("")
    argv.append("")

    ci = claw_id(argv[2], argv[3], argv[4])
    
    results = query(argv[1], ci)
    for r in results:
        print(r)

if __name__ == "__main__":
    main(sys.argv)
