# -*- coding: utf-8 -*-


import pandas as pd
import pyreadr
from datetime import datetime, timedelta
from numpy import cos, sin, arcsin, sqrt
from math import radians
import datetime as dt

conmov=30  #condicion de movimiento

Nombre_Dia=[] #arreglo que guarda el nombre del dia de la semana de cada fila
acumulador1=0 #acumulador del tiempo acumulado
acumulador2=1 #acumulador de las etiquetas de viaje
tiempo=(4*60)*60 #minutos en segundos

#tabla_variables=pd.DataFrame()

directorio_entrada="C:/Users/User/Desktop/TesisPrincipal/Marcos/Pruebas/"
directorio_salida="C:/Users/User/Desktop/TesisPrincipal/Marcos/Pruebas/"

#directorio_entrada="/home/milton.moncayo/SmartGPS/timeline/"
#directorio_salida="/home/milton.moncayo/SmartGPS/data/"
archivo_salida="DataSmartTotal.dat"

#fecha_final = datetime.strptime('2019-11-30', '%Y-%m-%d')
#fecha_inicio = datetime.strptime('2019-09-01', '%Y-%m-%d')


archivo="tld0"+".RData"
enlace=directorio_entrada + archivo
print("sigue---> " +str(archivo) )
#Pongo try except.. xq existen archivos que dan error al momento de leerlos
try:
    original = pyreadr.read_r(enlace)
except:
    print("archivo dañado---> " +str(archivo) )
    #print("Tamaño del archivo: "+str(len(original['dataQuitoTotal'])))
print("Tamaño del archivo: "+str(len(original['dataQuitoTotal'])))
    #Inicializa dataframe y comprueba si ya existe
if('tabla_final_uce' not in globals() and 'tabla_final_todo' not in globals() ):
         tabla_final_uce=pd.DataFrame()
         tabla_final_uce=pd.DataFrame(columns=[])
       
#Aplica zona horaria del Ecuador a la fecha original 
original['dataQuitoTotal']['dateTimeLine'] = original['dataQuitoTotal']['dateTimeLine'] - dt.timedelta(hours=5)
#Separa fecha de hora
separador = original['dataQuitoTotal']['dateTimeLine'].astype(str).str.split(".", n = 1, expand = True) 
original['dataQuitoTotal']['Fecha']=separador[0] 
separador = original['dataQuitoTotal']['dateTimeLine'].astype(str).str.split(" ", n = 1, expand = True)  
original['dataQuitoTotal']['Fecha2']=separador[0] 
#Limitar coordenadas Campus Universidad Central del Ecuador
original['dataQuitoTotal']= original['dataQuitoTotal'].drop( original['dataQuitoTotal'][((original['dataQuitoTotal']['latitude']>=-0.19425) | (original['dataQuitoTotal']['latitude'] <= -0.20341))|(( original['dataQuitoTotal']['longitude']>=-78.49805 )|(original['dataQuitoTotal']['longitude'] <= -78.51377))].index)         
original['dataQuitoTotal'] = original['dataQuitoTotal'].reset_index()
print("acabo primer proceso")
#######################################################################################

###########################################################################################    
    #Colocar Etiqueta de movimiento (Verificar si esta cerca o no del mismo punto)
         
lon1 = original['dataQuitoTotal']['longitude'].map(radians).shift(1)
lat1 = original['dataQuitoTotal']['latitude'].map(radians).shift(1)
lon2 = original['dataQuitoTotal']['longitude'].map(radians)
lat2 = original['dataQuitoTotal']['latitude'].map(radians)
dlon = lon2 - lon1 
dlat = lat2 - lat1 
a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
c = 2 * arcsin(sqrt(a)) 
distancias= 6371000 * c
        
    
original['dataQuitoTotal']["DistMetros"]= distancias  
original['dataQuitoTotal'].loc[original['dataQuitoTotal']["DistMetros"].isnull()==True,'DistMetros']=0
original['dataQuitoTotal'].loc[original['dataQuitoTotal']['DistMetros']<=conmov ,'Movimiento']=0 
original['dataQuitoTotal'].loc[original['dataQuitoTotal']['DistMetros']>conmov ,'Movimiento']=1     
print("acabo segundo proceso")
   
##################################################################################################  
################################################################################################## 
    
#Poner etiquetas de viajes
contviajes=1  #Reinicio contador de viajes para cada nuevo archivo
etiquetas=[]  #arreglo para guardar la etiqueta de cada viaje
contrutas=0  #acumulador del campo Ruta
reco=[]   #Arreglo para guardar el seguimiento de cada punto generado por acumulador 3
for i in range(0,len(original['dataQuitoTotal'])):
            #en la primera iteracion guardo directamente los datos
            if (i==0):
                etiquetas.append(contviajes)
                reco.append(contrutas)
            else:
                #fecha3 y fecha4 son las fecha en formato año-mes-dia para comparar fechas
                fecha3 = datetime.strptime(original['dataQuitoTotal']["Fecha2"][i-1], '%Y-%m-%d')
                fecha4 = datetime.strptime(original['dataQuitoTotal']["Fecha2"][i], '%Y-%m-%d')  
                fecha1 = datetime.strptime(original['dataQuitoTotal']["Fecha"][i-1], '%Y-%m-%d %H:%M:%S')
                fecha2 = datetime.strptime(original['dataQuitoTotal']["Fecha"][i], '%Y-%m-%d %H:%M:%S') 
                Total=(fecha2-fecha1)/timedelta(seconds=1)
                if(fecha3!=fecha4):
                    #Los contadores se reinician en cada nuevo dia 
                   # acumulador1=0
                    contviajes=1
                    contrutas=0  
                    reco.append(contrutas)
                    etiquetas.append(contviajes)      
                 
                elif(Total>=tiempo):
                  #  acumulador1=0                   
                    contviajes=contviajes+1
                    contrutas=0  
                    reco.append(contrutas)
                    etiquetas.append(contviajes)     
                    
                #Cuando Movimiento es 0 se acumula el tiempo en el acumulador1
                elif(original['dataQuitoTotal']["Movimiento"][i]==0):
                    reco.append(-1)
                    etiquetas.append(contviajes)
    
                else: 
                    contrutas=contrutas+1
                    reco.append(contrutas)
                    etiquetas.append(contviajes)  
                    
    #se anexa los resultados al dataframe                 
original['dataQuitoTotal']["Viaje"]= etiquetas
original['dataQuitoTotal']["Ruta"]= reco
print("acabo tercer proceso")
    
    ##########################################################################
   
original['dataQuitoTotal'].loc[original['dataQuitoTotal']['Ruta']==0,'DistMetros']=0
print("acabo cuarto proceso")
    
    #########################################################################
    
original['dataQuitoTotal'].drop(columns =["index"], inplace = True) 
tabla_final_uce=  tabla_final_uce.append([ original['dataQuitoTotal']], ignore_index=True)


######################################################################################################

fecha1 = tabla_final_uce["Fecha"].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S')).shift(1)
fecha2 = tabla_final_uce["Fecha"].apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
tiempo=(fecha2-fecha1)/timedelta(seconds=1)


distancia=tabla_final_uce['DistMetros']


tabla_final_uce["VelocidadCalculada"]= distancia/tiempo
tabla_final_uce.loc[tabla_final_uce['VelocidadCalculada'].isnull()==True,'VelocidadCalculada']=0
tabla_final_uce["VelocidadOriginal"]= tabla_final_uce["velocity"]
tabla_final_uce.drop(columns =["velocity"], inplace = True) 

print("acabo quinto proceso")


#################################################################################################### 

#Separa fecha y hora    
separador = tabla_final_uce['dateTimeLine'].astype(str).str.split(" ", n = 1, expand = True) 

separador = separador[0].astype(str).str.split("-", n = 3, expand = True) 

tabla_final_uce["Año"]= separador[0] 
tabla_final_uce["Mes"]= separador[1] 
tabla_final_uce["Dia"]= separador[2] 

separador = tabla_final_uce['dateTimeLine'].astype(str).str.split(" ", n = 1, expand = True) 

separador = separador[1].astype(str).str.split(":", n = 2, expand = True) 

tabla_final_uce["Hora"]= separador[0] 
tabla_final_uce["Minuto"]= separador[1] 

separador = separador[2].astype(str).str.split(".", n = 2, expand = True) 
tabla_final_uce["Segundo"]= separador[0] 

tabla_final_uce.drop(columns =["dateTimeLine"], inplace = True) 

print("acabo sexto proceso")

#Etiquetar con el nombre del dia de la semana

tabla_final_uce['Dia'] = tabla_final_uce['Dia'].apply(pd.to_numeric)
tabla_final_uce['Mes'] = tabla_final_uce['Mes'].apply(pd.to_numeric)
tabla_final_uce['Año'] = tabla_final_uce['Año'].apply(pd.to_numeric)

dia=tabla_final_uce['Dia']
mes=tabla_final_uce['Mes']
año=tabla_final_uce['Año']

a=(14-mes)//12
y=año-a
m=mes+12 * a -2

d=(dia+año+(año//4)-(año//100)+(año//400)+((31*m)//12))%7

tabla_final_uce.loc[d==0 ,'Ndia']='Domingo'
tabla_final_uce.loc[d==1 ,'Ndia']='Lunes'
tabla_final_uce.loc[d==2 ,'Ndia']='Martes'
tabla_final_uce.loc[d==3 ,'Ndia']='Miércoles'
tabla_final_uce.loc[d==4 ,'Ndia']='Jueves'
tabla_final_uce.loc[d==5 ,'Ndia']='Viernes'
tabla_final_uce.loc[d==6 ,'Ndia']='Sábado'

print("acabo septimo proceso")

#Guardar dataframe en un archivo dat
tabla_final_uce.to_csv(directorio_salida+archivo_salida)  
#tabla_cargada = pd.read_table(directorio_salida+archivo_salida, sep=",")