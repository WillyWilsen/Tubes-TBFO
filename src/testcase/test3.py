import numpy as np

def matriks(x):
    if (type(x) != int):
        raise TimeoutError
    else:
        i = 2
    x = np.add(x,x)
    y = np.transpose(x)
    for i in range(5):
        print("x"+x)
        if (i == 3):
            x = 3
            pass
        else:
            continue