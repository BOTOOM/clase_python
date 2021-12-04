import os
from pandas import read_excel
import numpy as np
import pandas as pd
import statistics as sta
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
# %mathplotlib inline
# variables iniciales
ruta_archivo = os.path.dirname(os.path.abspath(__file__))
my_sheet = 'Esperanza de vida'
file_name = ruta_archivo + '/3_Datos_Taller_3.xlsx' 
# leer archivo de excel
df = read_excel(file_name, sheet_name = my_sheet)
dates = df.columns[4:63]
x = []
for date in dates:
    x.append(int(date))
# print(x)
# y = (df.loc[39][dates])
y = list(df.loc[39][dates])
# print(y)
# for n in datos:
#     print(n)
columnas = ['valx','valy']
datosDF = pd.DataFrame(data=list(zip(x, y)),columns=columnas)

# # print(datos)
# # sns.set_theme(style="darkgrid")
# # g = sns.jointplot(x="valx", y="valy", data=datosDF,
# #                   kind="reg", truncate=False,
# #                   xlim=(0, 60), ylim=(0, 12),
# #                   color="m", height=7)
# sns.lmplot(x='valx',y='valy',data=datosDF)
# plt.show()
# use line_kws to set line label for legend
# get coeffs of linear fit
slope, intercept, r_value, p_value, std_err = stats.linregress(datosDF['valx'],datosDF['valy'])

ax = sns.regplot(x="valx", y="valy", data=datosDF, color='b', 
 line_kws={'label':"y={0:.1f}x+{1:.1f}".format(slope,intercept)})

# plot legend
ax.legend()
print(slope, intercept, r_value, p_value, std_err)

# plt.show()
