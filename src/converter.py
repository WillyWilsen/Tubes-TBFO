#Converter dari grammar.txt ke python nya#
from copy import deepcopy
from os import replace
import string

def CFGfromTXT(grammarPath):
    CFG_Production_Rule = {}
    with open(grammarPath,'r') as f:
        lines = [line.split('->')
                    for line in f.read().split('\n')
                    if len(line.split('->')) == 2]
        for line in lines:
            variable = line[0].replace(" ","")
            productionsRaw = [productionRaw.split() for productionRaw in line[1].split('|')]
            production = []
            for productionRaw in productionsRaw:
                production.append([" " if item == "__space__" else
                                   "|" if item == "__or_symbol__" else
                                   "\n" if item == "__new_line__" else
                                   item for item in productionRaw])
            CFG_Production_Rule.update({variable: production})
    return CFG_Production_Rule

def displayGrammar(dict):
    for var in dict:
        print(var,"-> ",end="")
        for i in range(len(dict[var])):
            if i == len(dict[var] - 1):
                print(dict[var][i])
            else:
                print(dict[var][i],"| ",end="")

def isVariableValid(item):
    #kalau panjang nya variable cuma satu maka tidak valid, karena tidak sesuai dengan penamaan variable python
    if len(item) == 1:
        return False
    #kalau variable diawali digits dan pemisahan kata tidak menggunakan underscore misal pakai '-' maka variable tidak valid
    #karena tidak sesuai dengan aturan penamaan variable pada python
    for char in item:
        if char not in (string.ascii_uppercase + '_' +string.digits):
            return False
    return True

def removeUnitProductioninCFG(CFG):
    for variable in CFG:
        productions = CFG[variable]
        repeat = True
        while repeat:
            repeat = False
            for production in productions:
                if len(production) == 1 and isVariableValid(production[0]):
                    productions.remove(production)
                    newProduction = deepcopy([production for production in CFG[production[0]] if production not in productions])
                    productions.extend(newProduction)
                    repeat = True
                    break
    return CFG