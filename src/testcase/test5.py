from numpy.lib import scimath as smath

A = int(smath.log(1000))
B = int(smath.log(1500))
while(A >= 0 and B >= 0):
    A -= 1
    B -= 1
    if (A == 1):
        print("Woke")
        break
