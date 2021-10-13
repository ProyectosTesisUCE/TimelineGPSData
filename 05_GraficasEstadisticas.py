# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 14:41:40 2020

@author: User
"""


import pandas as pd
import numpy
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
from datetime import datetime

#Este script sirve para generar los gráficos con los resultados obtenidos del Script Random Forest

directorio_salida="D:/TesisPrincipal/Marcos/Pruebas/"
archivo_entrada="Estadisticas.dat"


tabla_cargada = pd.read_table(directorio_salida+archivo_entrada, sep=",")


################################################################################################
tabla_cargada.loc[tabla_cargada['Actividad']==0,'Actividad']="CON_VEHICULO"
tabla_cargada.loc[tabla_cargada['Actividad']==2,'Actividad']="SIN_VEHICULO"
tabla_cargada.loc[tabla_cargada['Actividad']==3,'Actividad']="SIN_VEHICULO"
tabla_cargada.drop(tabla_cargada[ tabla_cargada['Actividad'] == 3 ].index , inplace=True)
#DATOS GLOBALES LISTADO
plt.title("Actividades")
plt.ylabel("Proporcion de los registros capturados (%)")
#plt.hist(Onfoot1["Ndia"], bins = 20)
plt.hist(tabla_cargada["Actividad"], weights=np.ones(len(tabla_cargada)) / len(tabla_cargada), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()
g101=str(tabla_cargada["Actividad"].value_counts())
tabla_cargada.loc[tabla_cargada['Actividad']=="CON_VEHICULO",'Actividad']=0
tabla_cargada.loc[tabla_cargada['Actividad']=="SIN_VEHICULO",'Actividad']=2
#tabla_cargada.loc[tabla_cargada['Actividad']=="QUIETO",'Actividad']=3


###########################################################################################################
tabla_cargada=tabla_cargada.sort_values('Ndia')

tabla_cargada.loc[tabla_cargada['Ndia']==1 ,'Ndia']='Lunes'
tabla_cargada.loc[tabla_cargada['Ndia']==2 ,'Ndia']='Martes'
tabla_cargada.loc[tabla_cargada['Ndia']==3 ,'Ndia']='Miércoles'
tabla_cargada.loc[tabla_cargada['Ndia']==4 ,'Ndia']='Jueves'
tabla_cargada.loc[tabla_cargada['Ndia']==5 ,'Ndia']='Viernes'
#tabla_cargada.loc[tabla_cargada['Ndia']==6 ,'Ndia']='Sábado'
#tabla_cargada.loc[tabla_cargada['Ndia']==7 ,'Ndia']='Domingo'

tabla_cargada.drop(tabla_cargada[ tabla_cargada['Ndia'] == 6 ].index , inplace=True)
tabla_cargada.drop(tabla_cargada[ tabla_cargada['Ndia'] == 7 ].index , inplace=True)

plt.title("Registro actividad (Días)")
plt.ylabel("Proporcion de los registros capturados (%)")
#plt.hist(Onfoot1["Ndia"], bins = 20)
plt.hist(tabla_cargada["Ndia"], weights=np.ones(len(tabla_cargada)) / len(tabla_cargada), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()


#DATOS GLOBALES DE ACTIVIDAD POR DIA

Onfoot1=tabla_cargada.loc[tabla_cargada["Actividad"]==2]

plt.title("Movimiento a pie registrado (Días)")
plt.ylabel("Proporcion de los registros capturados (%)")
#plt.hist(Onfoot1["Ndia"], bins = 20)
plt.hist(Onfoot1["Ndia"], weights=np.ones(len(Onfoot1)) / len(Onfoot1), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()
g16=str(Onfoot1["Ndia"].value_counts())

IV1=tabla_cargada.loc[tabla_cargada["Actividad"]==0]

plt.title("Movimiento en vehiculo registrado (Días)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(IV1["Ndia"], weights=np.ones(len(IV1)) / len(IV1), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()
g17=str(IV1["Ndia"].value_counts())
Still1=tabla_cargada.loc[tabla_cargada["Actividad"]==3]

plt.title("Registro Quieto registrado (Días)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(Still1["Ndia"], weights=np.ones(len(Still1)) / len(Still1), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()
g18=str(Still1["Ndia"].value_counts())

########################################################################################################
#DATOS SEPARADOS POR SEMESTRES

fecha_final_S1 = datetime.strptime('2019-09-08', '%Y-%m-%d')
fecha_inicio_S1 = datetime.strptime('2019-03-26', '%Y-%m-%d')

fecha_final_S2 = datetime.strptime('2020-03-02', '%Y-%m-%d')
fecha_inicio_S2 = datetime.strptime('2019-09-23', '%Y-%m-%d')

Onfoot1_S1=Onfoot1
Onfoot1_S1 = Onfoot1_S1.drop(Onfoot1_S1[(Onfoot1_S1['Fecha2'] <= str(fecha_inicio_S1))].index)
Onfoot1_S1 = Onfoot1_S1.drop(Onfoot1_S1[(Onfoot1_S1['Fecha2'] >= str(fecha_final_S1))].index)


plt.title("Movimiento a pie registrado Semestre Marzo 2019 - Agosto 2019 (Días)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(Onfoot1_S1["Ndia"], weights=np.ones(len(Onfoot1_S1)) / len(Onfoot1_S1), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()
g90=str(Onfoot1_S1["Ndia"].value_counts())

Onfoot1_S2=Onfoot1
Onfoot1_S2 = Onfoot1_S2.drop(Onfoot1_S2[(Onfoot1_S2['Fecha2'] <= str(fecha_inicio_S2))].index)
Onfoot1_S2 = Onfoot1_S2.drop(Onfoot1_S2[(Onfoot1_S2['Fecha2'] >= str(fecha_final_S2))].index)

plt.title("Movimiento a pie registrado Semestre Septiembre 2019 - Marzo 2020 (Días)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(Onfoot1_S2["Ndia"], weights=np.ones(len(Onfoot1_S2)) / len(Onfoot1_S2), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()
g91=str(Onfoot1_S2["Ndia"].value_counts())     
#################################################################################################
IV1_S1=IV1
IV1_S1 = IV1_S1.drop(IV1_S1[(IV1_S1['Fecha2'] <= str(fecha_inicio_S1))].index)
IV1_S1 = IV1_S1.drop(IV1_S1[(IV1_S1['Fecha2'] >= str(fecha_final_S1))].index)


plt.title("Movimiento en vehiculo registrado Semestre Marzo 2019 - Agosto 2019 (Días)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(IV1_S1["Ndia"], weights=np.ones(len(IV1_S1)) / len(IV1_S1), bins = 20)

plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()
g92=str(IV1_S1["Ndia"].value_counts()) 

IV1_S2=IV1
IV1_S2 = IV1_S2.drop(IV1_S2[(IV1_S2['Fecha2'] <= str(fecha_inicio_S2))].index)
IV1_S2 = IV1_S2.drop(IV1_S2[(IV1_S2['Fecha2'] >= str(fecha_final_S2))].index)

plt.title("Movimiento en vehiculo Semestre Septiembre 2019 - Marzo 2020 (Días)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(IV1_S2["Ndia"], weights=np.ones(len(IV1_S2)) / len(IV1_S2), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()
g93=str(IV1_S2["Ndia"].value_counts()) 
###################################################################################################

Still1_S1=Still1
Still1_S1 = Still1_S1.drop(Still1_S1[(Still1_S1['Fecha2'] <= str(fecha_inicio_S1))].index)
Still1_S1 = Still1_S1.drop(Still1_S1[(Still1_S1['Fecha2'] >= str(fecha_final_S1))].index)


plt.title("Sin movimiento registrado Semestre Marzo 2019 -Agosto 2019 (Días)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(Still1_S1["Ndia"], weights=np.ones(len(Still1_S1)) / len(Still1_S1), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

Still1_S2=Still1
Still1_S2 = Still1_S2.drop(Still1_S2[(Still1_S2['Fecha2'] <= str(fecha_inicio_S2))].index)
Still1_S2 = Still1_S2.drop(Still1_S2[(Still1_S2['Fecha2'] >= str(fecha_final_S2))].index)


plt.title("Sin Movimiento Semestre Septiembre 2019 - Marzo 2020 (Días)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(Still1_S2["Ndia"], weights=np.ones(len(Still1_S2)) / len(Still1_S2), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

############################################################################################
tabla_cargada_S1=tabla_cargada
tabla_cargada_S1 = tabla_cargada_S1.drop(tabla_cargada_S1[(tabla_cargada_S1['Fecha2'] <= str(fecha_inicio_S1))].index)
tabla_cargada_S1 = tabla_cargada_S1.drop(tabla_cargada_S1[(tabla_cargada_S1['Fecha2'] >= str(fecha_final_S1))].index)


#plt.title("Actividad registrado Semestre Marzo 2019 - Agosto 2019 (Días)")
#plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(tabla_cargada_S1["Ndia"], weights=np.ones(len(tabla_cargada_S1)) / len(tabla_cargada_S1), bins = 20,label='2019-2019')
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
#plt.show()

tabla_cargada_S2=tabla_cargada
tabla_cargada_S2 = Onfoot1_S2.drop(Onfoot1_S2[(Onfoot1_S2['Fecha2'] <= str(fecha_inicio_S2))].index)
tabla_cargada_S2 = Onfoot1_S2.drop(Onfoot1_S2[(Onfoot1_S2['Fecha2'] >= str(fecha_final_S2))].index)


plt.title("Actividad registrado por Semestre (Días)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(tabla_cargada_S2["Ndia"], weights=np.ones(len(tabla_cargada_S2)) / len(tabla_cargada_S2), bins = 40,label='2019-2020')
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
#plt.legend(loc='upper right')
plt.show()


#################################################################################################
#DATOS GLOBALES POR HORA

tabla_cargada=tabla_cargada.sort_values('Hora')

plt.title("Actividades por hora ")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(tabla_cargada["Hora"], weights=np.ones(len(tabla_cargada)) / len(tabla_cargada), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

g19=str(tabla_cargada["Hora"].value_counts())

#DATOS GLOBALES POR HORA
Onfoot1=Onfoot1.sort_values('Hora')

plt.title("Actividades por hora (A pie)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(Onfoot1["Hora"], weights=np.ones(len(Onfoot1)) / len(Onfoot1), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

g20=str(Onfoot1["Hora"].value_counts())

#DATOS GLOBALES POR HORA
IV1=IV1.sort_values('Hora')

plt.title("Actividades por hora (Vehiculo)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(IV1["Hora"], weights=np.ones(len(IV1)) / len(IV1), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

g21=str(IV1["Hora"].value_counts())

#DATOS GLOBALES POR HORA
Still1=Still1.sort_values('Hora')

plt.title("Actividades por hora  (Quieto) ")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(Still1["Hora"], weights=np.ones(len(Still1)) / len(Still1), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

g22=str(Still1["Hora"].value_counts())

#DATOS GLOBALES POR SEMESTRE Y POR HORA

Onfoot1_S1=Onfoot1_S1.sort_values('Hora')

plt.title("Movimiento a pie registrado Semestre Marzo 2019 - Agosto 2019 (Horas)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(Onfoot1_S1["Hora"], weights=np.ones(len(Onfoot1_S1)) / len(Onfoot1_S1), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

g23=str(Onfoot1_S1["Hora"].value_counts())

#DATOS GLOBALES POR SEMESTRE Y POR HORA

Onfoot1_S2=Onfoot1_S2.sort_values('Hora')

plt.title("Movimiento a pie registrado Semestre Septiembre 2019 - Marzo 2020 (Horas)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(Onfoot1_S2["Hora"], weights=np.ones(len(Onfoot1_S2)) / len(Onfoot1_S2), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

g24=str(Onfoot1_S2["Hora"].value_counts())

#DATOS GLOBALES POR SEMESTRE Y POR HORA

IV1_S1=IV1_S1.sort_values('Hora')

plt.title("Movimiento en vehiculo registrado Semestre Marzo 2019 - Agosto 2019 (Horas)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(IV1_S1["Hora"], weights=np.ones(len(IV1_S1)) / len(IV1_S1), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

g25=str(IV1_S1["Hora"].value_counts())

#DATOS GLOBALES POR SEMESTRE Y POR HORA

IV1_S2=IV1_S2.sort_values('Hora')

plt.title("Movimiento en vehiculo registrado Semestre Septiembre 2019 - Marzo 2020 (Horas)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(IV1_S2["Hora"], weights=np.ones(len(IV1_S2)) / len(IV1_S2), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

g26=str(IV1_S2["Hora"].value_counts())

#DATOS GLOBALES POR SEMESTRE Y POR HORA

Still1_S1=Still1_S1.sort_values('Hora')

plt.title("Sin Movimiento registrado Semestre Marzo 2019 - Agosto 2019 (Horas)")
plt.ylabel("Proporcion de los registros capturados (%)")
#plt.hist(Onfoot1["Ndia"], bins = 20)
plt.hist(Still1_S1["Hora"], weights=np.ones(len(Still1_S1)) / len(Still1_S1), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

g27=str(Still1_S1["Hora"].value_counts())

#DATOS GLOBALES POR SEMESTRE Y POR HORA

Still1_S2=Still1_S2.sort_values('Hora')

plt.title("Sin Movimiento registrado Semestre Septiembre 2019 - Marzo 2020 (Horas)")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(Still1_S2["Hora"], weights=np.ones(len(Still1_S2)) / len(Still1_S2), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

g28=str(Still1_S2["Hora"].value_counts())

###########################################################################################
#DATOS GLOBALES POR HORA
tabla_cargada_S1=tabla_cargada_S1.sort_values('Hora')

plt.title("Actividades por hora Semestre Marzo 2019 - Agosto 2019 ")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(tabla_cargada_S1["Hora"], weights=np.ones(len(tabla_cargada_S1)) / len(tabla_cargada_S1), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

g29=str(tabla_cargada_S1["Hora"].value_counts())

#DATOS GLOBALES POR HORA
tabla_cargada_S2=tabla_cargada_S2.sort_values('Hora')

plt.title("Actividades por hora Semestre Septiembre 2019 - Marzo 2020 ")
plt.ylabel("Proporcion de los registros capturados (%)")
plt.hist(tabla_cargada_S2["Hora"], weights=np.ones(len(tabla_cargada_S2)) / len(tabla_cargada_S2), bins = 20)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
plt.show()

g30=str(tabla_cargada_S2["Hora"].value_counts())