
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
tabla_organizada = pd.DataFrame(data=datos_organizados,columns=columnas)
# # mostrar datos estadisticos
print(tabla_organizada)
# numerador_EspVida = (tabla_organizada[])