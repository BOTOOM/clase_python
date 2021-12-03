
import os
from pandas import read_excel
import numpy as np
import pandas as pd
import statistics as sta
# variables iniciales
ruta_archivo = os.path.dirname(os.path.abspath(__file__))
hoja_esperanza_vida = 'Esperanza de vida'
hoja_tasa_fertilidad = 'Tasa de fertilidad'
file_name = ruta_archivo + '/3_Datos_Taller_3.xlsx' 
decada2000='2005'
decada2010='2015'
# leer archivo de excel y seleccion de 30 paises
dfEspVida = read_excel(file_name, sheet_name = hoja_esperanza_vida).loc[21:50]
dfTasaFer = read_excel(file_name, sheet_name = hoja_tasa_fertilidad).loc[21:50]
# print(dfTasaFer)
#calculos estadisticos
calculos_estadisticos_EspVida = dfEspVida.describe()
calculos_estadisticos_TasaFer = dfTasaFer.describe()
# print(calculos_estadisticos_EspVida)
# nombres de filas y columnas para la tabla de resultados
columnas = ['Muestra','Media', 'Varianza', 'Desviacion', 'n']
filas = [hoja_esperanza_vida + '-' + decada2000,decada2010]
# organizacion de datos
datos_organizados = [
    [hoja_esperanza_vida + '-' + decada2000, calculos_estadisticos_EspVida[decada2000]['mean'],
    sta.variance(dfEspVida[decada2000]), calculos_estadisticos_EspVida[decada2000]['std'],
    len(dfEspVida[decada2000])],
    [hoja_tasa_fertilidad + '-' + decada2000,calculos_estadisticos_TasaFer[decada2000]['mean'],
    sta.variance(dfTasaFer[decada2000]), calculos_estadisticos_TasaFer[decada2000]['std'],
    len(dfEspVida[decada2000])],
    [hoja_esperanza_vida + '-' + decada2010, calculos_estadisticos_EspVida[decada2010]['mean'],
    sta.variance(dfEspVida[decada2010]), calculos_estadisticos_EspVida[decada2010]['std'],
    len(dfEspVida[decada2010])],
    [hoja_tasa_fertilidad + '-' + decada2010,calculos_estadisticos_TasaFer[decada2010]['mean'],
    sta.variance(dfTasaFer[decada2010]), calculos_estadisticos_TasaFer[decada2010]['std'],
    len(dfEspVida[decada2010])]
    ]
tabla_organizada = pd.DataFrame(data=datos_organizados,columns=columnas).round(3)
# # mostrar datos estadisticos
print(tabla_organizada)
# Calculos datos deada 2000
numerador_EspVida = ((tabla_organizada['n'][0]-1)*tabla_organizada['Varianza'][0]) + ((tabla_organizada['n'][2] -1)*tabla_organizada['Varianza'][2])
denominador_EspVida = (tabla_organizada['n'][0] + tabla_organizada['n'][2] -2)
Sp2_EspVida = numerador_EspVida / denominador_EspVida
Sp_EspVida = np.sqrt(Sp2_EspVida)
# print('Sp² = ' + str(round(Sp2_EspVida,3)))
# print('Sp = ' + str(round(Sp_EspVida,3)))
X_EspVida = (tabla_organizada['Media'][0] - tabla_organizada['Media'][2])
# print('X1 - X2 = ' + str(round(X_EspVida, 3)))
n_m_EspVida =round((1/tabla_organizada['n'][0])+ (1/tabla_organizada['n'][2]),3)
# print('1/n+1/m *Sp = ' + str(n_m_EspVida))
# se calcula el error estandar
error_estandar_EspVida = round(np.sqrt(n_m_EspVida)*Sp_EspVida,3)
# print('ee = ' + str(error_estandar_EspVida))
# # se calcula el error maximo de estimacion
# # t = 1.971 sale de la table de distribuciones
# error_estimacion_EspVida = 1.971 * error_estandar
# print('e = ' + str(round(error_maximo_estimacion, 3)))
# # # se calcula los intervalos de confianza
# intervalos_confianza_EspVida= [ str(round(X - error_maximo_estimacion, 4)), str(round(X + error_maximo_estimacion, 4)) ]
# print('Intervalo de Confianza = ' + str(intervalos_confianza))

numerador_TasaFer = ((tabla_organizada['n'][1]-1)*tabla_organizada['Varianza'][1]) + ((tabla_organizada['n'][3] -1)*tabla_organizada['Varianza'][3])
denominador_TasaFer = (tabla_organizada['n'][1] + tabla_organizada['n'][3] -2)
Sp2_TasaFer = numerador_TasaFer / denominador_TasaFer
Sp_TasaFer = np.sqrt(Sp2_TasaFer)
# print('Sp² = ' + str(round(Sp2_TasaFer,3)))
# print('Sp = ' + str(round(Sp_TasaFer,3)))
X_TasaFer = (tabla_organizada['Media'][1] - tabla_organizada['Media'][3])
# print('X1 - X2 = ' + str(round(X_TasaFer, 3)))
n_m_TasaFer =round((1/tabla_organizada['n'][1])+ (1/tabla_organizada['n'][3]),3)
# print('1/n+1/m *Sp = ' + str(n_m_TasaFer))
# se calcula el error estandar
error_estandar_TasaFer = round(np.sqrt(n_m_TasaFer)*Sp_TasaFer,3)
print('ee = ' + str(error_estandar_TasaFer))
