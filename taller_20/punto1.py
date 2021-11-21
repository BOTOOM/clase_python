import numpy as np
import statistics as sta
from tabulate import tabulate
import matplotlib.pyplot as plt
import scipy.stats as stats
import math

datos = [182, 181, 182, 183, 180, 184, 185, 184, 183, 182, 181, 198 ]
tabla_datos = {'datos': datos}
print(tabulate(tabla_datos, headers='keys'))
media = round(np.mean(datos),3)
n = len(datos)
u = 180
desviacion_estandar = round(sta.stdev(datos), 3)
varianza = round(sta.variance(datos),2)
estadistico_prueba = round(abs( (media - u)/ (desviacion_estandar/ np.sqrt(n))), 3)
print('Estadistico de prueba = ' + str( estadistico_prueba))

# obtenido de la tabla de probabilidad
t = 1.796
centro = 0
valor = 0.22
raiz = math.sqrt(valor)
x = np.linspace(centro - 6*raiz, centro + 6*raiz, 100)
plt.vlines(-t, -0.1, 0.4, colors='g', lw=1, alpha=0.5, label=str(-t))
plt.vlines(t, -0.1, 0.4, colors='g', lw=1, alpha=0.5, label=str(t))
plt.vlines(round(estadistico_prueba,3), -0.1, 0.4, colors='r', lw=1, alpha=0.5, label=str(round(estadistico_prueba,3)))
plt.plot(x, stats.norm.pdf(x, centro, raiz))
plt.legend()
plt.show()