import numpy as np
import statistics as sta
from tabulate import tabulate

# datos triglicedios antes
triglicedios_antes = [110,90,85,120,110,130,135,140,88,98,105,87,100,98,125]
# datos triglicedios despues
triglicedios_despues= [90,110,100,110,100,145,125,130,100,95,90,110,90,95,100]
# se calcula la diferencia
diferencia = list(np.array(triglicedios_antes) - np.array(triglicedios_despues))
# se calcula el calor n
n = len(diferencia)
# se imprime la tabla
tabla_datos = {'Antes': triglicedios_antes, 'Despues': triglicedios_despues,'Diferencia': diferencia}
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
# Conclusión: Como se puede apreciar, el cero le pertenece al intervalo, entonces no hubo
# diferencias significativas entre el antes y el después de haber hecho la dieta rigurosa,
# este estudio se realizó para 15 individuos con un nivel de significancia del 5 %.