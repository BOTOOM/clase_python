import numpy as np
#definir funciones lambda
fx = lambda x: x**3+4*x**2-10
a=1
b=2
tolera=0.001
tramo= b-a

while not (tramo<tolera):
    c=(a+b)/2
    fa=fx(a)
    fb=fx(b)
    fc=fx(c)

    cambia = np.sign(fa)*np.sign(fc)

    if (cambia < 0):
        a = a
        b = c

    if (cambia > 0):
        a = c
        b = b 
    tramo= b-a
print (c)
print (tramo)