#Program Utama Compiler#
from converter import CFGfromTXT, CFGtoCNF, displayGrammar, turntoCNF
from CYK import CYK

def fileReader(path):
    with open(path, "r") as f:
        content = f.read()
    return content



CFG = CFGfromTXT("grammar.txt")
#displayGrammar(CFG)
CNF = CFGtoCNF(CFG)

displayGrammar(CNF)


def startCompiler():
    print()
