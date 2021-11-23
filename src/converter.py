# Converter dari grammar.txt ke python nya#
from copy import deepcopy
from os import replace
import string

# fungsi ini bertujuan untuk mengubah grammar yang awalnya berada pada file txt,
# maka akan di ubah menjadi sebuah grammar dalam bahasa python, yang di simpan dalam bentuk
# dictionary

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
            #menambahkan variable atau non-terminal dan hasil penurunan nya ke dalam dictionary CFG
            #variable sebagai key dan hasil penurunan sebagai value
            CFG_Production_Rule.update({variable: production})
    return CFG_Production_Rule

# fungsi yang bertujuan untuk menampilkan seluruh grammar yang ada ke layar
# fungsi ini dibuat agar lebih mudah pada saat melakukan proses debugging

def displayGrammar(dict):
    for var in dict:
        print(var,"-> ",end="")
        for i in range(len(dict[var])):
            if i == len(dict[var]) - 1:
                print(dict[var][i])
            else:
                print(dict[var][i],"| ",end="")

# fungsi yang bertujuan untuk melakukan pengecekan apakah sebuah simbol pada
# grammar merupakan sebuah variabel atau simbol terminal pada sebuah CFG
# variabel/non-terminal jika diawali oleh huruf kapital
# simbol terminal jika dia diawali huruf kecil

def isVariableValid(item):
    #kalau panjang sama dengan satu maka dia adalah simbol terminal
    if len(item) == 1:
        return False
    # kalau variable diawali digit atau pemisahan kata tidak menggunakan underscore misal pakai '-' 
    # maka variable tidak valid berdasarkan grammar yang telah di buat.
    for char in item:
        if char not in (string.ascii_uppercase + '_' +string.digits):
            return False
    return True

# fungsi ini dibutuhkan pada saat akan mengubah CFG menjadi CNF
# fungsi ini bertujuan untuk menghilangkan produksi unit agar penurunan 
# dari grammar yang telah di buat lebih sederhana.
# Misal terdapat aturan :
# S -> C 
# C -> D
# D -> dd
# Maka akan di sederhanakan menjadi S -> dd 

def removeUnitProductioninCFG(CFG):
    for variable in CFG:
        productions = CFG[variable]
        repeat = True
        while repeat:
            repeat = False
            # Dicari yang merupakan produksi unit dari CFG
            for production in productions:
                # Jika hasil penurunan dari variable hanya berjumlah satu elemen dan dia merupakan variable juga
                # maka dia merupakan produksi unit dan akan dihapus, kemudian aturan produksi akan di sederhanakan,
                # dan ditambahkan ke aturan produksi yang baru. 
                if len(production) == 1 and isVariableValid(production[0]):
                    productions.remove(production)
                    newProduction = deepcopy([production for production in CFG[production[0]] if production not in productions])
                    # Update aturan produksi 
                    productions.extend(newProduction)
                    repeat = True
                    break
    return CFG

# fungsi ini dibutuhkan pada saat akan menggunakan algoritma CYK, karena CYK menerima masukan dalam bentuk CNF
# Hasil dari aturan produksi pada CNF harus berupa tepat satu simbol terminal atau 2 buah simbol non-terminal.

def turntoCNF(CFG):
    newCFG = {}
    
    # Mencari simbol terminal pada aturan produksi di CFG
    for variable in CFG:
        terminals = []
        productions = CFG[variable]
        # Akan dicari simbol terminal dari aturan produksi yang memiliki panjang lebih dari satu
        # yang panjang nya sudah sama dengan satu maka dia sudah termasuk CNF
        processProduction = [production for production in productions if len(production) > 1]
        for production in processProduction:
            for item in production:
                # Apabila telah ditemukan akan di cek apakah dia variable atau bukan
                # jika bukan, maka dia merupakan simbol terminal
                if not(isVariableValid(item)) and item not in terminals:
                    terminals.append(item)
        
        # Dibuat sebuah aturan produksi baru yang berdasarkan simbol 
        # terminal yang sudah di dapatkan
        
        for i, terminal in enumerate(terminals):
            newCFG.update({f"{variable}_TERM_{i + 1}":[[terminal]]})
            for idx, j in enumerate(productions):
                if len(j) > 1:
                    for k in range(len(j)):
                        if len(productions[idx][k]) == len(terminal):
                            productions[idx][k] = productions[idx][k].replace(terminal, f"{variable}_TERM_{i + 1}")
        
        idx = 1
        # Dibuat aturan produksi baru apabila hasil penurunan dari sebuah aturan produksi memiliki
        # panjang simbol non-terminal/variabel berjumlah lebih dari dua. 
        for i in range(len(productions)):
            while len(productions[i]) > 2:
                newCFG.update({f"{variable}_EXT_{idx}": [[productions[i][0], productions[i][1]]]})
                productions[i] = productions[i][1:]
                productions[i][0] = f"{variable}_EXT_{idx}"
                idx += 1
    # Update nilai dari CFG
    CFG.update(newCFG)
    return CFG


def CFGtoCNF(CFG):
    CFG = removeUnitProductioninCFG(CFG)
    CNF = turntoCNF(CFG)
    return CNF