# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:32:12 2020

@author: User
"""


import pandas as pd

#Se carga el archivo del dataset
directorio_entrada="C:/Users/User/Desktop/TesisPrincipal/Marcos/Pruebas/"
archivo_entrada="DataSmartTotal.dat"

tabla_cargada = pd.read_table(directorio_entrada+archivo_entrada, sep=",")

datos = []
datos2 = []

#Función para cargar la ruta con puntos
for i in range(0,len(tabla_cargada)):
    if((tabla_cargada['Viaje'][i]==1)and(tabla_cargada['Ruta'][i]!=-1)and(tabla_cargada['Año'][i]==2018)and(tabla_cargada['Mes'][i]==1)and(tabla_cargada['Dia'][i]==16)):
        archivo=str(tabla_cargada['Ruta'][i])
        latitude=str(tabla_cargada['latitude'][i])
        longitude=str(tabla_cargada['longitude'][i])
        etiqueta=str(tabla_cargada['Viaje'][i])
        palabra="["+"'"+archivo+"'"+", "+latitude+", "+longitude+", "+"'"+etiqueta+"'"+"]"
        datos.append(palabra)
        palabra2="{lat: "+latitude+", "+"lng: "+longitude+"}"
        datos2.append(palabra2)
    
coordenadas=','.join(datos)  
coordenadas2=','.join(datos2) 

    
#Funcion para cargar los puntos en el mapa generado por Google Maps en un archivo HTML
mapapuntos="""<!DOCTYPE html>

    <html>
      <head>
        <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
        <meta charset="utf-8">
        <title>Recorridos Uce</title>
        <style>
          html, body {
            height: 100%;
            margin: 0;
            padding: 0;
          }
          #map {
            height: 100%;
          }
        </style>
      </head>
      <body>
        <div id="map"></div>
        <script>
    
    function initMap() {
    
    //coordenadas de rutas para puntos
      var locations = ["""+coordenadas+"""]; 
     
        
    //Mapa con propiedades  de configuracion 
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 17,
      center: new google.maps.LatLng(-0.200866, -78.50342890000002),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    
    //coordenadas de rutas trazar linea
    
    var flightPlanCoordinates = [
       """+coordenadas2+"""
      ];
    
    // Información de la ruta (coordenadas, color de línea, etc...)
      var flightPath = new google.maps.Polyline({
        path: flightPlanCoordinates,
        geodesic: true,
        strokeColor: '#FF0000',
        strokeOpacity: 1.0,
        strokeWeight: 2
      });
    
    var iconBase = 'http://maps.google.com/mapfiles/kml/paddle/';

    // Creando la ruta en el mapa
    flightPath.setMap(map);
    
    var infowindow = new google.maps.InfoWindow();

    var marker, i;


    //Bucle para añadir una marca correspondiente a cada punto de la ruta
    for (i = 0; i < locations.length; i++) {  
     if(i==0) {
       marker = new google.maps.Marker({
        
        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
        icon: iconBase + '1-lv.png',

        map: map
       });
       
     }else if(i==locations.length-1){
    
      marker = new google.maps.Marker({
        
        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
        icon: iconBase + '2-lv.png',

        map: map
      });
      
     }else {
    
      marker = new google.maps.Marker({
        
        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
        icon: iconBase + 'purple-circle-lv.png',

        map: map
      });
     }
     
     // Creando la ruta en el mapa
      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
          infowindow.setContent(locations[i][0]);
          infowindow.open(map, marker);
        }
      })(marker, i));
    }
     
    // Inicializando el mapa cuando se carga la página
    google.maps.event.addDomListener(window, 'load', initialize);
     
      
      
    }
    
        </script>
        <script async defer
             src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBe-bfPHrkzDdiq5MDw8z6liFIBQiqfbso&signed_in=true&callback=initMap"></script>
      </body>
    </html>"""
    
#Se guarda el archivo en un archivo html
archivo= open('mapapuntostrazada.html','w')
archivo.write(mapapuntos)
archivo.close()