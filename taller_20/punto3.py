import numpy as np
import statistics as sta
from tabulate import tabulate

# datos colesterol antes
colesterol_antes = [95,110,110,110,100,128,125,135,180,195,190,110,90,95,100]
# datos colesterol despues
colesterol_despues= [100,98,85,125,118,130,135,145,188,198,105,87,100,98,125]
# se calcula la diferencia
diferencia = list(np.array(colesterol_antes) - np.array(colesterol_despues))
# se calcula el calor n
n = len(diferencia)
# se imprime la tabla
tabla_datos = {'Antes': colesterol_antes, 'Despues': colesterol_despues,'Diferencia': diferencia}
print(tabulate(tabla_datos, headers='keys'))
print('\n')
# se calcula la varianza
varianza = sta.variance(diferencia)
# se calcula la media
media = np.mean(diferencia)
print('𝒚̅ = ' + str(round(media, 2)))
# se calcula la desviacion estandar
desviacion_estandar = sta.stdev(diferencia)
print('S(𝒚̅) = ' + str(round(desviacion_estandar, 2)))
# se calcula el error estandar
error_estandar = desviacion_estandar/np.sqrt(n)
print('ee(𝒚̅) = ' + str(round(error_estandar, 2)))
# se calcula el error maximo de estimacion
# t = 2.145 sale de la table de distribuciones
error_maximo_estimacion = 2.145 * error_estandar
print('e(𝒚̅) = ' + str(round(error_maximo_estimacion, 2)))
# se calcula los intervalos de confianza
intervalos_confianza= [ str(round(media - error_maximo_estimacion, 2)), str(round(media + error_maximo_estimacion, 2)) ]
print('I(𝒚̅) ±  e(𝒚̅)= ' + str(intervalos_confianza))
