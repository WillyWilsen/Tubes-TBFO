#Program Utama Compiler#
from converter import CFGfromTXT, CFGtoCNF, displayGrammar, turntoCNF




CFG = CFGfromTXT("grammar.txt")
#displayGrammar(CFG)
CNF = CFGtoCNF(CFG)

displayGrammar(CNF)


def startCompiler():
    print()
