#!/usr/bin/env python
# coding: utf-8

# [![Open In colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/DatosGeograficos/2_Joins_y_Viz/ejercicio/ejercicio.ipynb)

# ## Introducción

# Trabajás en una importante Secretaría del Gobierno de la Ciudad de Buenos Aires, cumpliste tus tareas del día y, cuando te estás preparando para irte, escuchás que gritan tu nombre desde el final del pasillo... 
# 
#     - ¡Vení! ¡Rápido!, te vuelven a llamar...
#     - Uy, justo me estaba yendo, es fin de semana largo, ¿vió?, decís en tu mejor tono de 'me quiero ir'...
#     - Mirá, el tema es así, me llegó un mail pidiéndome información para hoy mismo acerca de qué tan lejos le quedan las comisarias a la gente en Buenos Aires. Está la hipótesis de que la gente no realiza denuncias porque la comisaria más cercana les queda muy lejos. Igual, no nos piden testear la hipótesis pero sí tener una noción de qué tan lejos estpan. 
#     - Ok, me quedo tranquilo, decís, sin saber bien qué acotar...
#     - Tranquilo o intranquilo, no importa eso, lo que sí importa es que tenemos que entregar algo bien hecho y ya mismo. Te pido lo siguiente, necesitamos saber cuál es la distancia promedio de una persona a la comisaria más cercana... 
#     - Mmm, hay 3 millones de personas, ¿cómo hacemos?
#     - Vamos a samplear puntos...
#     - ¿Eh?
#     - Sí, vamos a tirar puntos al azar en la ciudad y de ahí vamos a calcular la distancia a la comisaria más cercana.
#     - ¿Y pero cómo hago para generar un punto al azar? ¿Miro el mapa y decido más o menos a ojo?
#     - No, no, ¿cómo vas a hacer eso? Vamos a usar GeoPandas, generamos 1000 valores representativos de la superficie de la ciudad, luego calculamos la distancia de cada punto a la comisaria más cercana y mostramos cómo se distribuye esa distancia. Ojo, no es un problema trivial generar un punto al azar dentro de una geometría. Pensá que hay que garantizarse que caiga dentro del polígono... 
#     - ¿y algo más?
#     - Si, si, obviamente hay que mostrar un mapa, dónde cayeron los puntos, dónde están las comisarias... y también agregá la capa de los barrios. Todo filtrable, interactivo y lindo, nada de un .plot así nomás...
# 
# Y así, arrancaba la noche...Pasando en limpio el ejercio y algunos tips.
# 
# 1) Cargar barrios y comisarias y pasar a GKBA. Esto después nos va a servir para que la distancia que calculamos quede en metros.
# 
# 2) Los GeoDataFrames tienen el atributo .bounds que nos devuelve los valores más extremos de longitud y latitud. Esto es muy útil para acotar los valores de las muestras que vamos a tomar. Como queremos que caigan en la Ciudad de Buenos Aires pero sólo tenemos los barrios tenemos que usar **.dissolve** para quedarnos con un solo polígono. Luego, miren el .bounds de ese polígono.
# 
# 2bis) BONUS TRACK: generar un mapa donde se muestren los barrios y los 4 puntos más extremos según los valores obtenidos por .bounds. O sea, el valor más al SURESTE, SUROESTE, NORESTE Y NOROESTE.
# 
# 3) Generar una función que genere **n** puntos dentro de un polígono distribuidos al azar. Para hacer eso la función va a tomar los .bounds del polígono, generar un valor al azar de longitud y latitud (pueden usar **random.uniform** (googleen o pregunten si no lo encuentran) y luego fijarse si el polígono lo **contiene**. Si lo contiene guardar el punto en una lista y si no agregar += a un contador que registre cuántos puntos caen afuera (al final. Acuérdense de contar cuántos caen adentro para frenar el loop.
# 
# 4) Para cada punto calcular la distancia a la comisaria más cercana.
# 
# 5) Graficar un histograma.
# 
# 6) Con folium (u otra librería interactiva) mostrar los puntos, los barrios y las comisarias.
#     Para los puntos incluir como popup la distancia y el color del icono pintarlo en base a las siguientes reglas:
#     
#     if distancia < 500:
#         color = "green"
#     elif distancia > 500 and distancia < 1500:
#         color = "blue"
#     else:
#         color = "red"
#     
#     Para las comisarias incluir como popup el nombre.
# 
#     - Bueno... me voy yendo, acordate de mandar eso cuando lo tengas... ¡Buen finde!
#     - ¿Eh?, ¿no me vas a ayudar?, no lo podés creer...
#     - ¡No te escucho! ¿Saludos? Ah, sí, gracias y, ¡saludos también para tu familia! ¡Y usá GeoSeries.representative_point  de CABA, no para cada barrio!

# In[ ]:


# !pip install geopandas
# !apt install libspatialindex-dev
# !pip install rtree

# !pip install pysal
# !pip install contextily #--> Para importar mapa base
# !pip install folium


# In[12]:


import pandas as pd
import geopandas
import shapely.wkt
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Leo datasets

# In[13]:


def from_wkt(df, wkt_column, crs='EPSG:4326'):
    
    df["coordinates"]= df[wkt_column].apply(shapely.wkt.loads) # empleamos una función de shapely para leer WKT
        
    gdf = geopandas.GeoDataFrame(df, geometry='coordinates', crs=crs) # seteamos la columna de geometría
    
    return gdf


# In[14]:


def from_x_y(df, x, y, crs='EPSG:4326'):
    gdf = geopandas.GeoDataFrame(df.drop([x, y], axis=1), # eliminamos las columnas originales
                                crs=crs, # Agregamos CRS
                                geometry=geopandas.points_from_xy(df[x], df[y])) # junto "x" e "y" y lo paso a Point
    return gdf


# In[49]:


barrios = pd.read_csv("https://datasets-humai.s3.amazonaws.com/datasets/barrios.csv", encoding='latin1')


# In[51]:


barrios_gkba = barrios.to_crs(crs = "+proj=tmerc +lat_0=-34.629269 +lon_0=-58.4633 +k=0.9999980000000001 +x_0=100000 +y_0=100000 +ellps=intl +units=m +no_defs")


# ## Grafico .bounds

# In[1]:


# nota: depende la versión de GeoPandas tal vez puedan encontrarse con este error: ValueError: 'box_aspect' and 'fig_aspect' must be positive
# si ese es el caso cambien gdf.plot(ax=ax,color="red") por gdf.plot(ax=ax,color="red", aspect=1) 


# In[ ]:





# ## Armo función para samplear

# In[ ]:





# ## Calculo distancias y grafico histograma

# In[ ]:





# ## Mapa con folium

# In[ ]:


# nota: depende la versión el parámetro popup de Marker puede ser popup=folium.Popup(#valor a mostrar)
# o sólo popup=#valor a mostrar
# si tienen error vean https://stackoverflow.com/questions/46225588/folium-popup-gets-syntax-error-message

