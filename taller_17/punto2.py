import numpy as np
import statistics as sta
from tabulate import tabulate

# datos iniciales
empresa_A = [11,12,10,9,8,13,14,15]
empresa_B = [10,9,8,15,14,12,11,13,15]
# calcular n para cada empresa
n_A = len(empresa_A)
n_B = len(empresa_B)
# se calcula la media para cada empresa
media_A = round(np.mean(empresa_A),2)
media_B = round(np.mean(empresa_B),2)
# se calcula la varianza para cada empresa
varianza_A = round(sta.variance(empresa_A),2)
varianza_B = round(sta.variance(empresa_B),2)
# imprimir dador iniciales
tabla_datos = {'Empresa A': empresa_A, 'Empresa B': empresa_B}
print(tabulate(tabla_datos, headers='keys'))
print('\n')
# imprimir calculos iniciales
tabla_calculos_iniciales = [['','Empresa A', 'Empresa B'], ['Media', media_A, media_B], ['Varianza',varianza_A, varianza_B], ['n', n_A, n_B] ]
print(tabulate(tabla_calculos_iniciales, headers='firstrow'))
# calcular numerador y denominador
numerador = ((n_A-1)*varianza_A) + ((n_B-1)*varianza_B)
denominador = (n_A+n_B-2)
# imprimir numerador y denominador 
print('\n')
print('Numerador = ' +  str(numerador))
print('Denominador = ' +  str(denominador))
# calcular e imprimir SP 
Sp2 = numerador / denominador
Sp = np.sqrt(Sp2)
print('Sp² = ' + str(round(Sp2,2)))
print('Sp = ' + str(round(Sp,2)))