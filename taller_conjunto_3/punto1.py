
import os
from pandas import read_excel
import numpy as np
import pandas as pd
import statistics as sta
# variables iniciales
ruta_archivo = os.path.dirname(os.path.abspath(__file__))
my_sheet = 'Esperanza de vida'
file_name = ruta_archivo + '/3_Datos_Taller_3.xlsx' 
decada2000='2005'
decada2010='2015'
# leer archivo de excel
df = read_excel(file_name, sheet_name = my_sheet)
#calculos estadisticos
calculos_estadisticos = df.describe()
# nombres de filas y columnas para la tabla de resultados
columnas = ['Media', 'Varianza', 'Desviacion']
filas = [decada2000,decada2010]
# organizacion de datos
datos_resultados = [
    [calculos_estadisticos[decada2000]['mean'], sta.variance(df[decada2000]), calculos_estadisticos[decada2000]['std']],
    [calculos_estadisticos[decada2010]['mean'], sta.variance(df[decada2010]), calculos_estadisticos[decada2010]['std']]
    ]
tabla_resultados = pd.DataFrame(datos_resultados,index=filas,columns=columnas)
# mostrar datos
print(tabla_resultados)