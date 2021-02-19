import numpy as np
import sympy as sym

w = sym.Symbol("w")
f= lambda w: (32.17/(-2*w**2))  *  (  ((np.exp(w)-np.exp(-w))/2) - np.sin(w)   ) -1.7
a=-4
b=2
exactitud=0.00001    
y= b-a
distancia= np.absolute(y)

while not (distancia<exactitud):
    c=(a+b)/2
    fa=f(a)
    fb=f(b)
    fc=f(c)
    cambia = np.sign(fa)*np.sign(fc)
    if (cambia < 0):
        a = a
        b = c
    if (cambia > 0):
        a = c
        b = b
    distancia= b-a
    print (c)
print (c)