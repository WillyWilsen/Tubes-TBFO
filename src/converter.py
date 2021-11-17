#Converter dari grammar.txt ke python nya#
from copy import deepcopy
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


