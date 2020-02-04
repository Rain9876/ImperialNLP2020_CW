import sys
def readFile(path):
    s = sys.path[0]+path
    with open(s,"r")as f:
        content= f.read().splitlines()
    f.close()
    return content


def processingString(string, noSapce, split, noNewLine):
    if noSapce:
        string = string.replace(" ","")
    if noNewLine:
        string = string.replace("\n","")
    if split:
        string = string.split(",")
    return string