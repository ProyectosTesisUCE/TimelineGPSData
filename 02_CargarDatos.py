# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:21:23 2020

@author: User
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

#Este script sirve para crear los datasets de Entrenamiento y prediccion que serviran para el modelo de Random Forest

directorio_salida="C:/Users/User/Desktop/TesisPrincipal/Marcos/Pruebas/"
archivo_entrada="DataSmartTotal.dat"

archivo_entrenamiento="Entrenamiento.dat"
archivo_prediccion="Prediccion.dat"

archivo_titling="Tilting.dat"

tabla_cargada = pd.read_table(directorio_salida+archivo_entrada, sep=",")
    
tabla_cargada= tabla_cargada.drop( tabla_cargada[((tabla_cargada['VelocidadCalculada']==np.inf) )].index)

tabla_cargada= tabla_cargada.drop( tabla_cargada[((tabla_cargada['VelocidadCalculada']==np.inf) )].index)
       


##########################################################################################################
#Grafico 1
datos=tabla_cargada

datos.loc[datos['activity1'].isnull()==True,'activity1']="NULL"

plt.title("Distribucion Actividades")
plt.ylabel("Numero dias")
#plt.hist(Onfoot1["Ndia"], bins = 20)
plt.hist(datos["activity1"], weights=np.ones(len(datos)) / len(datos), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.xticks(rotation='vertical')
plt.show()


#Grafico 2

unkwon=tabla_cargada.loc[tabla_cargada['activity1']=="UNKNOWN"]

unkwon.loc[unkwon['activity2'].isnull()==True,'activity2']="NULL"


plt.title("Distribucion Unkown")
plt.ylabel("Numero dias")
#plt.hist(Onfoot1["Ndia"], bins = 20)
plt.hist(unkwon["activity2"], weights=np.ones(len(unkwon)) / len(unkwon), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.xticks(rotation='vertical')
plt.show()

#########################################################################################################

conditions = [
    (tabla_cargada['VelocidadCalculada']==0),
    (tabla_cargada['VelocidadCalculada']<0.555556),
    (tabla_cargada['VelocidadCalculada']<1.83333),
    (tabla_cargada['VelocidadCalculada']<3.583332),
    (tabla_cargada['VelocidadCalculada']<8.944444),
    (tabla_cargada['VelocidadCalculada']>=8.944444)]
choices = [0,1,1,1,4,5]


tabla_cargada['Rango'] = np.select(conditions, choices, default=-1)


##########################################################################################################

tabla_cargada.loc[tabla_cargada['activity1']=="UNKNOWN",'confidence1']=tabla_cargada['confidence2']
tabla_cargada.loc[tabla_cargada['activity1']=="UNKNOWN",'activity1']=tabla_cargada['activity2']


tabla_cargada.loc[tabla_cargada['activity1']=="IN_VEHICLE",'activity1']=0
tabla_cargada.loc[tabla_cargada['activity1']=="ON_BICYCLE",'activity1']=0
tabla_cargada.loc[tabla_cargada['activity1']=="ON_FOOT",'activity1']=2
tabla_cargada.loc[tabla_cargada['activity1']=="STILL",'activity1']=3
tabla_cargada.loc[tabla_cargada['activity1']=="TILTING",'activity1']=5
tabla_cargada.loc[tabla_cargada['activity1']=="WALKING",'activity1']=7
tabla_cargada.loc[tabla_cargada['activity1']=="RUNNING",'activity1']=8
tabla_cargada.loc[tabla_cargada['activity1']=="EXITING_VEHICLE",'activity1']=0
tabla_cargada.loc[tabla_cargada['activity1']=="IN_ROAD_VEHICLE",'activity1']=0
tabla_cargada.loc[tabla_cargada['activity1']=="IN_RAIL_VEHICLE",'activity1']=0



###########################################################################################################
#Grafico 3

datos2=tabla_cargada

datos2.loc[datos2['activity1'].isnull()==True,'activity1']="NULL"
datos2.loc[datos2['activity1']==0,'activity1']="IN_VEHICLE"
datos2.loc[datos2['activity1']==2,'activity1']="ON_FOOT"
datos2.loc[datos2['activity1']==3,'activity1']="STILL"
datos2.loc[datos2['activity1']==5,'activity1']="TILTING"

plt.title("Distribucion variables (Unificado)")
plt.ylabel("Numero dias")
plt.hist(datos2["activity1"], weights=np.ones(len(datos2)) / len(datos2), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.xticks(rotation='vertical')
plt.show()

#############################################################################################################
tabla_cargada.drop(tabla_cargada.columns[tabla_cargada.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

tabla_cargada.loc[tabla_cargada['activity1']=="NULL",'activity1']=np.NaN
tabla_cargada.loc[tabla_cargada['activity1']=="IN_VEHICLE",'activity1']=0
tabla_cargada.loc[tabla_cargada['activity1']=="ON_FOOT",'activity1']=2
tabla_cargada.loc[tabla_cargada['activity1']=="STILL",'activity1']=3
tabla_cargada.loc[tabla_cargada['activity1']=="TILTING",'activity1']=5


Entrenamiento=tabla_cargada.loc[(tabla_cargada['activity1'].isnull()==False)]
Tilting=tabla_cargada.loc[tabla_cargada['activity1']==5]

Prediccion=tabla_cargada.loc[tabla_cargada['activity1'].isnull()==True]
Entrenamiento= Entrenamiento.drop( Entrenamiento[Entrenamiento['activity1']==5].index)

Entrenamiento = Entrenamiento.reset_index()
Prediccion= Prediccion.reset_index()
Tilting= Tilting.reset_index()

Entrenamiento.drop(columns =["index"], inplace = True)
Prediccion.drop(columns =["index"], inplace = True)


Tilting.to_csv(directorio_salida+archivo_titling)
Entrenamiento.to_csv(directorio_salida+archivo_entrenamiento)
Prediccion.to_csv(directorio_salida+archivo_prediccion)