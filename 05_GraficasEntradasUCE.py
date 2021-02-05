# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 23:37:26 2020

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt

#Este Script Sirve para generar los graficos de las actividades en las principales entradas del campus principal de la Universidad Central del Ecuador

directorio_salida="C:/Users/User/Desktop/TesisPrincipal/Marcos/Pruebas/"
archivo_entrada="Estadisticas.dat"


tabla_cargada = pd.read_table(directorio_salida+archivo_entrada, sep=",")

tabla_cargada.loc[tabla_cargada['Actividad']==0,'Actividad']="VEHICULO"
tabla_cargada.loc[tabla_cargada['Actividad']==2,'Actividad']="A_PIE"
tabla_cargada.loc[tabla_cargada['Actividad']==3,'Actividad']="QUIETO"

tabla_carvajal= tabla_cargada.drop(tabla_cargada[((tabla_cargada['latitude']>=-0.19784) | (tabla_cargada['latitude'] <= -0.19803))|(( tabla_cargada['longitude']>=-78.50222 )|(tabla_cargada['longitude'] <= -78.50244))].index)

plt.title("Actividades Sector Calle Carvajal")
plt.ylabel("Proporcion de los registros capturados")
plt.hist(tabla_carvajal["Actividad"], bins = 20)
plt.show()


tabla_leiton= tabla_cargada.drop(tabla_cargada[((tabla_cargada['latitude']>=-0.19735) | (tabla_cargada['latitude'] <= -0.19744))|(( tabla_cargada['longitude']>=-78.50615 )|(tabla_cargada['longitude'] <= -78.50622))].index)

plt.title("Actividades Sector Calle Leiton")
plt.ylabel("Proporcion de los registros capturados")
plt.hist(tabla_leiton["Actividad"], bins = 20)
plt.show()


tabla_Puente= tabla_cargada.drop(tabla_cargada[((tabla_cargada['latitude']>=-0.19937) | (tabla_cargada['latitude'] <= -0.19993))|(( tabla_cargada['longitude']>=-78.50055 )|(tabla_cargada['longitude'] <= -78.50099))].index)

plt.title("Actividades Sector Puente Peatonal")
plt.ylabel("Proporcion de los registros capturados")
plt.hist(tabla_Puente["Actividad"], bins = 20)
plt.show()

tabla_Pileta= tabla_cargada.drop(tabla_cargada[((tabla_cargada['latitude']>=-0.20148) | (tabla_cargada['latitude'] <= -0.20186))|(( tabla_cargada['longitude']>=-78.50146 )|(tabla_cargada['longitude'] <= -78.50185))].index)

plt.title("Actividades Sector Pileta UCE")
plt.ylabel("Proporcion de los registros capturados")
plt.hist(tabla_Pileta["Actividad"], bins = 20)
plt.show()

tabla_Bolivia= tabla_cargada.drop(tabla_cargada[((tabla_cargada['latitude']>=-0.20193) | (tabla_cargada['latitude'] <= -0.20233))|(( tabla_cargada['longitude']>=-78.50672 )|(tabla_cargada['longitude'] <= -78.50706))].index)
    
plt.title("Actividades Sector Calle Bolivia")
plt.ylabel("Proporcion de los registros capturados")
plt.hist(tabla_Bolivia["Actividad"], bins = 20)
plt.show()  
