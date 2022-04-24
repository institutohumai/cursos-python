#!/usr/bin/env python
# coding: utf-8

# In[ ]:


<a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/APIs/1_APIs_Geograficas/clase-1-ejercicios.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
<div align="center"> Recordá abrir en una nueva pestaña </div>


# # APIs Geográficas: Ejercicios

# In[1]:


import requests
import pandas as pd
import geopandas as gpd
from urllib.parse import urlencode, urljoin
import matplotlib 
import helpers
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Ejercicio 1: API Georef 

# * Genera una lista en un dataframe de todas las calles que se llaman "San Martin" en la Argentina. Cuantas son?

# In[ ]:





# * Hace un mapa de las representaciones diplomaticas extranjeras en la Argentina. Para esto descarga las direcciones del dataset ["Guia Diplomatica"](https://datos.gob.ar/dataset/exterior-guia-diplomatica), georreferencialas, crea un GeoDataframe con ellas y mapealas sobre una capa de provincias de Argentina. Sugerencias:
#     - Usa `pd.read_excel()` directamente con la URL de descarga de la lista de representaciones extranjeras.
#     - Cuando descargues las embajadas, elimina aquellas que no tengan direccion, porque hace fallar la georreferenciacion (`embajadas.dropna(subset=['representacion_direccion']`)

# In[ ]:





# ## Ejercicio 2: API Nominatim

# Crea distintos mapas que tengan al mapa de las comunas de la Ciudad de Buenos Aires como base, y sobre el dibujen los puntos de coordenadas de:
# 
# * Los 10 restaurantes mas cercanos al centroide del barrio de Almagro
# * Los 10 hospitales mas cercanos al centroide de Villa Urquiza
# * Las 10 escuelas mas cercanas al centroide de Villa Devoto
# 
# Sugerencia: crea una funcion "buscar" que tome un texto de busqueda y haga la consulta a la API de Nominatim, y otra funcion "mapear" que tome un texto de busqueda y haga el mapa de los puntos sobre las comunas de la CABA. Usa la funcion mapear() para hacer los 3 mapas solicitados.

# In[ ]:




