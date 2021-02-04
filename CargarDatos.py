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
#tabla_cargada= tabla_cargada.drop( tabla_cargada[((tabla_cargada['latitude']>=-0.19425) | (tabla_cargada['latitude'] <= -0.20341))|(( tabla_cargada['longitude']>=-78.49805 )|(tabla_cargada['longitude'] <= -78.51377))].index)
#tabla_cargada= tabla_cargada.drop( tabla_cargada[((tabla_cargada['latitude']>=0.026711) | (tabla_cargada['latitude'] <= -0.400294))|(( tabla_cargada['longitude']>=-78.270936 )|(tabla_cargada['longitude'] <= -78.591624))].index)
       


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
#tabla_cargada.loc[tabla_cargada['VelocidadCalculada']==0,'Rango']=0
#tabla_cargada.loc[tabla_cargada['VelocidadCalculada']<=0.555556,'Rango']=1
#tabla_cargada.loc[tabla_cargada['VelocidadCalculada']<=1.83333,'Rango']=2
#tabla_cargada.loc[tabla_cargada['VelocidadCalculada']<=3.583332,'Rango']=3
#tabla_cargada.loc[tabla_cargada['VelocidadCalculada']<=8.944444,'Rango']=4
#tabla_cargada.loc[tabla_cargada['VelocidadCalculada']>8.944444,'Rango']=5


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

#tabla_cargada.loc[tabla_cargada['activity1']=="TILTING",'activity1']=tabla_cargada['activity2']

#tabla_cargada= tabla_cargada.drop( tabla_cargada[((tabla_cargada['activity1']=="UNKNOWN") )].index)

#tabla_cargada= tabla_cargada.drop( tabla_cargada[((tabla_cargada['activity1']=="STILL") )].index)
#tabla_cargada= tabla_cargada.drop( tabla_cargada[((tabla_cargada['activity1']=="TILTING") )].index)



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
#plt.hist(Onfoot1["Ndia"], bins = 20)
plt.hist(datos2["activity1"], weights=np.ones(len(datos2)) / len(datos2), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.xticks(rotation='vertical')
plt.show()



#############################################################################################################
'''
tabla_cargada.loc[(tabla_cargada['Ruta']==-1) & (tabla_cargada['activity1'].isnull()==False),'activity1']=3

conditions = [
    ((tabla_cargada['activity1']==5) & ( tabla_cargada['Rango']==0)),
    ((tabla_cargada['activity1']==5) &  (tabla_cargada['Rango']==1)),
    ((tabla_cargada['activity1']==5) &  (tabla_cargada['Rango']==4)),
    ((tabla_cargada['activity1']==5) &  (tabla_cargada['Rango']==5))]
choices = [3,2,0,0]

tabla_cargada['activity1'] = np.select(conditions, choices, default=tabla_cargada['activity1'])
'''
#############################################################################################################
tabla_cargada.drop(tabla_cargada.columns[tabla_cargada.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

tabla_cargada.loc[tabla_cargada['activity1']=="NULL",'activity1']=np.NaN
tabla_cargada.loc[tabla_cargada['activity1']=="IN_VEHICLE",'activity1']=0
tabla_cargada.loc[tabla_cargada['activity1']=="ON_FOOT",'activity1']=2
tabla_cargada.loc[tabla_cargada['activity1']=="STILL",'activity1']=3
tabla_cargada.loc[tabla_cargada['activity1']=="TILTING",'activity1']=5



#still=tabla_cargada.loc[tabla_cargada['activity1']==3]
#muestraS=still.sample(n=300000)
#tilting=tabla_cargada.loc[tabla_cargada['activity1']==5]

#muestraT=tilting.sample(n=155163)

#tabla_cargada= tabla_cargada.drop( tabla_cargada[tabla_cargada['activity1']==5].index)
#tabla_cargada= tabla_cargada.drop( tabla_cargada[tabla_cargada['activity1']==3].index)
#tabla_cargada= tabla_cargada.drop( tabla_cargada[tabla_cargada['Ruta']==-1].index)
#tabla_cargada.drop(columns =["activity2"], inplace = True)
#tabla_cargada.drop(columns =["confidence1"], inplace = True)
#tabla_cargada.drop(columns =["confidence2"], inplace = True)

#result=tabla_cargada.append([muestraS,muestraT])


#tabla_cargada= tabla_cargada.drop( tabla_cargada[tabla_cargada['activity1']==5].sample(n=160000, replace=True, random_state=10).index)
#tabla_cargada= tabla_cargada.drop( tabla_cargada[tabla_cargada['activity1']==3].sample(n=609000, replace=True, random_state=10).index)


Entrenamiento=tabla_cargada.loc[(tabla_cargada['activity1'].isnull()==False)]
Tilting=tabla_cargada.loc[tabla_cargada['activity1']==5]
#Entrenamiento['activity1']=Entrenamiento['activity1'].astype(float)
#Entrenamiento=pd.to_numeric(Entrenamiento['activity1'])
#Entrenamiento=tabla_cargada.loc[tabla_cargada['Ruta']==-1]

Prediccion=tabla_cargada.loc[tabla_cargada['activity1'].isnull()==True]
#Prediccion['activity1']=Prediccion['activity1'].astype(float)
Entrenamiento= Entrenamiento.drop( Entrenamiento[Entrenamiento['activity1']==5].index)

Entrenamiento = Entrenamiento.reset_index()
Prediccion= Prediccion.reset_index()
Tilting= Tilting.reset_index()

Entrenamiento.drop(columns =["index"], inplace = True)
Prediccion.drop(columns =["index"], inplace = True)


Tilting.to_csv(directorio_salida+archivo_titling)
Entrenamiento.to_csv(directorio_salida+archivo_entrenamiento)
Prediccion.to_csv(directorio_salida+archivo_prediccion)