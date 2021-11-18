import numpy as np
import statistics as sta

triglicedios_antes = [110,90,85,120,110,130,135,140,88,98,105,87,100,98,125]
triglicedios_despues= [90,110,100,110,100,145,125,130,100,95,90,110,90,95,100]
diferencia = list(np.array(triglicedios_antes) - np.array(triglicedios_despues))
n = len(diferencia)
print("{:<6} {:<8} {:<8}".format('Antes','Despues','Diferencia'))
for i in range(n):
    print("{:<6} {:<8} {:<8}".format(triglicedios_antes[i], triglicedios_despues[i], diferencia[i]))
varianza = sta.variance(diferencia)
media = np.mean(diferencia)
print('𝒚̅ = ' + str(round(media, 2)))
desviacion_estandar = sta.stdev(diferencia)
print('S(𝒚̅) = ' + str(round(desviacion_estandar, 2)))
error_estandar = desviacion_estandar/np.sqrt(n)
print('ee(𝒚̅) = ' + str(round(error_estandar, 2)))
error_maximo_estimacion = 2.145 * error_estandar
print('e(𝒚̅) = ' + str(round(error_maximo_estimacion, 2)))
intervalos_confianza= [ str(round(media - error_maximo_estimacion, 2)), str(round(media + error_maximo_estimacion, 2)) ]
print('I(𝒚̅) ±  e(𝒚̅)= ' + str(intervalos_confianza))
# Conclusión: Como se puede apreciar, el cero le pertenece al intervalo, entonces no hubo
# diferencias significativas entre el antes y el después de haber hecho la dieta rigurosa,
# este estudio se realizó para 15 individuos con un nivel de significancia del 5 %.