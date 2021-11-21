import numpy as np
import statistics as sta
from tabulate import tabulate
import matplotlib.pyplot as plt
import scipy.stats as stats
import math

media_AISI_1064 = 107.6
media_AISI_1078 = 123.6
desviacion_estandar_AISI_1064 = 1.3
desviacion_estandar_AISI_1078 = 2.0
n_AISI_1064 = 129
n_AISI_1078 = 129
varianza_AISI_1064 = desviacion_estandar_AISI_1064**2
varianza_AISI_1078 = desviacion_estandar_AISI_1078**2
numerador = ((varianza_AISI_1064/n_AISI_1064)+(varianza_AISI_1078/n_AISI_1078))**2
denominador = ( ((((varianza_AISI_1064)/n_AISI_1064)**2)/(n_AISI_1064-1)) + ((((varianza_AISI_1078)/n_AISI_1078)**2)/(n_AISI_1078-1)) )
print('\n')
print('Numerador = ' +  str(numerador))
print('Denominador = ' +  str(denominador))
# calcular e imprimir SP 
Sp2 = numerador / denominador
Sp = np.sqrt(Sp2)
print('Sp² = ' + str(round(Sp2,3)))
print('Sp² redondeado = ' + str(round(Sp2,0)))
print('Sp = ' + str(round(Sp,3)))
X = (media_AISI_1064 - media_AISI_1078)
print('X1 - X2 = ' + str(round(X, 3)))
S1_S2 = (varianza_AISI_1064/n_AISI_1064)+ (varianza_AISI_1078/n_AISI_1078)
print('S1²/n+S2²/m = ' + str(round(S1_S2, 3)))
# se calcula el error estandar
error_estandar = np.sqrt(S1_S2)
print('ee = ' + str(round(error_estandar, 3)))
# se calcula el error maximo de estimacion
# t = 1.971 sale de la table de distribuciones
error_maximo_estimacion = 1.971 * error_estandar
print('e = ' + str(round(error_maximo_estimacion, 3)))
# # se calcula los intervalos de confianza
intervalos_confianza= [ str(round(X - error_maximo_estimacion, 4)), str(round(X + error_maximo_estimacion, 4)) ]
print('Intervalo de Confianza = ' + str(intervalos_confianza))