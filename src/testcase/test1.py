from math import __builtins__

def coba(x):
    s = 1
    T = [0 for i in range(x)]
    if (x == 10):
        print(10)
    elif (x == 3):
        print(3)
    else:
        x = 7
        T[3] = x

    for i in range(x):
        print(i)
        if (i == 6):
            s = "5"
            pass
    return s

y = 5
z = coba(y)
if (type(z) == str):
    raise TypeError