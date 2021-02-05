# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:34:02 2020

@author: User
"""


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.ensemble import RandomForestClassifier
from matplotlib.ticker import PercentFormatter
import numpy as np

#Este Script sirve para aplicar el modelo random forest a los datasets generados en el script 02_CargarDatos

#Se carga el dataset de entrenamiento
directorio_entrada="C:/Users/User/Desktop/TesisPrincipal/Marcos/Pruebas/"
archivo_entrada="Entrenamiento.dat"
archivo_estadistica="Estadisticas.dat"
tabla_entrenamiento = pd.read_table(directorio_entrada+archivo_entrada, sep=",",dtype='unicode')
tabla_entrenamiento.drop(tabla_entrenamiento.columns[tabla_entrenamiento.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

#Se reemplaza la variable del dia a categorico
tabla_entrenamiento.loc[tabla_entrenamiento['Ndia']=='Lunes' ,'Ndia']=1
tabla_entrenamiento.loc[tabla_entrenamiento['Ndia']=='Martes' ,'Ndia']=2
tabla_entrenamiento.loc[tabla_entrenamiento['Ndia']=='Miércoles' ,'Ndia']=3
tabla_entrenamiento.loc[tabla_entrenamiento['Ndia']=='Jueves' ,'Ndia']=4
tabla_entrenamiento.loc[tabla_entrenamiento['Ndia']=='Viernes' ,'Ndia']=5
tabla_entrenamiento.loc[tabla_entrenamiento['Ndia']=='Sábado' ,'Ndia']=6
tabla_entrenamiento.loc[tabla_entrenamiento['Ndia']=='Domingo' ,'Ndia']=7

#Se carga el dataset de prediccion
archivo_entrada2="Prediccion.dat"
tabla_prediccion = pd.read_table(directorio_entrada+archivo_entrada2, sep=",")
tabla_prediccion.drop(tabla_prediccion.columns[tabla_prediccion.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

#Se reemplaza la variable del dia a categorico
tabla_prediccion.loc[tabla_prediccion['Ndia']=='Lunes' ,'Ndia']=1
tabla_prediccion.loc[tabla_prediccion['Ndia']=='Martes' ,'Ndia']=2
tabla_prediccion.loc[tabla_prediccion['Ndia']=='Miércoles' ,'Ndia']=3
tabla_prediccion.loc[tabla_prediccion['Ndia']=='Jueves' ,'Ndia']=4
tabla_prediccion.loc[tabla_prediccion['Ndia']=='Viernes' ,'Ndia']=5
tabla_prediccion.loc[tabla_prediccion['Ndia']=='Sábado' ,'Ndia']=6
tabla_prediccion.loc[tabla_prediccion['Ndia']=='Domingo' ,'Ndia']=7

predecir=tabla_prediccion[["latitude","longitude","accuracy","Hora","VelocidadCalculada","DistMetros","Ndia"]]

archivo_entrada3="Tilting.dat"
tabla_tilting = pd.read_table(directorio_entrada+archivo_entrada3, sep=",")
tabla_tilting.drop(tabla_tilting.columns[tabla_tilting.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)

tabla_tilting.loc[tabla_tilting['Ndia']=='Lunes' ,'Ndia']=1
tabla_tilting.loc[tabla_tilting['Ndia']=='Martes' ,'Ndia']=2
tabla_tilting.loc[tabla_tilting['Ndia']=='Miércoles' ,'Ndia']=3
tabla_tilting.loc[tabla_tilting['Ndia']=='Jueves' ,'Ndia']=4
tabla_tilting.loc[tabla_tilting['Ndia']=='Viernes' ,'Ndia']=5
tabla_tilting.loc[tabla_tilting['Ndia']=='Sábado' ,'Ndia']=6
tabla_tilting.loc[tabla_tilting['Ndia']=='Domingo' ,'Ndia']=7

predecir2=tabla_tilting[["latitude","longitude","accuracy","Hora","VelocidadCalculada","DistMetros","Ndia"]]


#Se cargan las variables de entrada para el entrenamiento de RandomForest
X=tabla_entrenamiento[["latitude","longitude","accuracy","Hora","VelocidadCalculada","DistMetros","Ndia"]]
y=tabla_entrenamiento["activity1"]

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.20,random_state=50)
#X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.20,random_state=30)


#Se aplica especifica el numero de arboles de random forest
clf=RandomForestClassifier(n_estimators=100,random_state=50)
#clf=RandomForestClassifier(n_estimators=50,random_state=50)

#Se predice con modelo de Random Fores con las variables de entrada
clf.fit(X_train,y_train)

prediccion = clf.predict(X_test)

prediccion1 = clf.predict(predecir)
tabla_prediccion["Actividad"]= prediccion1

prediccion2 = clf.predict(predecir2)
tabla_tilting["Actividad"]= prediccion2

############################Grafico

tabla_prediccion.loc[tabla_prediccion['Actividad']=="0",'Actividad']="VEHICULO"
tabla_prediccion.loc[tabla_prediccion['Actividad']=="2",'Actividad']="A_PIE"
tabla_prediccion.loc[tabla_prediccion['Actividad']=="3",'Actividad']="QUIETO"

plt.title("Registro Prediccion Nulos")
plt.ylabel("Numero dias")
plt.hist(tabla_prediccion["Actividad"], weights=np.ones(len(tabla_prediccion)) / len(tabla_prediccion), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()


tabla_prediccion.loc[tabla_prediccion['Actividad']=="VEHICULO",'Actividad']=0
tabla_prediccion.loc[tabla_prediccion['Actividad']=="A_PIE",'Actividad']=2
tabla_prediccion.loc[tabla_prediccion['Actividad']=="QUIETO",'Actividad']=3

###########################Grafico

tabla_tilting.loc[tabla_tilting['Actividad']=="0",'Actividad']="VEHICULO"
tabla_tilting.loc[tabla_tilting['Actividad']=="2",'Actividad']="A_PIE"
tabla_tilting.loc[tabla_tilting['Actividad']=="3",'Actividad']="QUIETO"

plt.title("Registro Prediccion Tilting")
plt.ylabel("Numero dias")
plt.hist(tabla_tilting["Actividad"], weights=np.ones(len(tabla_tilting)) / len(tabla_tilting), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

tabla_tilting.loc[tabla_tilting['Actividad']=="VEHICULO",'Actividad']=0
tabla_tilting.loc[tabla_tilting['Actividad']=="A_PIE",'Actividad']=2
tabla_tilting.loc[tabla_tilting['Actividad']=="QUIETO",'Actividad']=3

###################################################################
tabla_entrenamiento["Actividad"]=tabla_entrenamiento["activity1"]
result=tabla_entrenamiento.append([tabla_prediccion,tabla_tilting])

print("Accuracy:",metrics.accuracy_score(y_test, prediccion))

#Medidor de Precision
print ("Train Accuracy :: ", accuracy_score(y_train, clf.predict(X_train)))
print ("Test Accuracy  :: ", accuracy_score(y_test, prediccion))
print (" Confusion matrix ")
#print (" 0  1  2  3  4 ")
print(confusion_matrix(y_test, prediccion))

print(classification_report(y_test,prediccion))

result.to_csv(directorio_entrada+archivo_estadistica)
