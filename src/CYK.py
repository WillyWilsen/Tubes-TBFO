# Fungsi ini bertujuan untuk mengimplementasikan CYK dari CNF yang telah dibuat

def CYK(input, CNF, src):
    # Inisialisasi variabel yang diperlukan
    n = len(input)
    m = len(CNF)
    lines = {}
    posLines = []
    linesString = src.split('\n')
    countLines = 0
    for i in range(len(input)):
        if (input[i] == '\n'):
            countLines += 1
            lines[i] = countLines
            posLines.append(i)

    result = [[[0 for i in range(m + 1)] for i in range(n + 1)] for i in range(n + 1)]
    R = [None] * (m + 1)
    mp = {}

    # Menambahkan rule-rule 
    for i, variable in enumerate(CNF):
        mp[variable] = i + 1
        R[i + 1] = CNF[variable]

    # Implementasi algoritma CYK
    for s in range(1, n + 1):
        for v in range(1, m + 1):
            for e in R[v]:
                if (e[0] == input[s - 1]):
                    result[1][s][v] = True
                    break

    for l in range(2, n + 1):
        for s in range(1, (n - l + 2)):
            for p in range(1, l):
                for a in range(1, m + 1):
                    for e in R[a]:
                        if (len(e) != 1):
                            b = mp[e[0]]
                            c = mp[e[1]]
                            if (result[p][s][b] and result[l - p][s + p][c]):
                                result[l][s][a] = True
                                break

    # Hasil dari algoritma CYK
    # Apabila syntax pada python memenuhi
    if (result[n][1][1]):
        print("Accepted")
    # Sebaliknya tidak memenuhi
    else :
        j = 1
        for i in range(n, 0, -1):
            if (result[i][1][1]):
                break
            if (input[i - 1] == '\n'):
                j = lines[i - 1]
        while (linesString[j - 1][0] == ' '):
            linesString[j - 1] = linesString[j - 1][1:]
        # Mengeluarkan letak error
        print(linesString[j - 1])
        print("^Syntax Error in line", j)