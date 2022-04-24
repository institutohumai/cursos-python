#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/APIs/1_APIs_Geograficas/clase-1-ejercicios-resueltos.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# # Clase 1: ejercicios prácticos resueltos

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

# In[25]:


calles_san_martin = pd.read_csv(
    'https://apis.datos.gob.ar/georef/api/calles?nombre=san%20martin&formato=csv&max=5000'
)
calles_san_martin


# * Hace un mapa de las representaciones diplomaticas extranjeras en la Argentina. Para esto descarga las direcciones del dataset ["Guia Diplomatica"](https://datos.gob.ar/dataset/exterior-guia-diplomatica), georreferencialas, crea un GeoDataframe con ellas y mapealas sobre una capa de provincias de Argentina. Sugerencias:
#     - Usa `pd.read_excel()` directamente con la URL de descarga de la lista de representaciones extranjeras.
#     - Cuando descargues las embajadas, elimina aquellas que no tengan direccion, porque hace fallar la georreferenciacion (`embajadas.dropna(subset=['representacion_direccion']`)

# In[6]:


embajadas = pd.read_excel(
    'https://cancilleria.gob.ar/userfiles/datos/representaciones-extranjeras.xlsx'
)


# In[7]:


embajadas = embajadas.dropna(subset=['representacion_direccion'])


# In[8]:


embajadas


# In[9]:


embajadas_direcciones = helpers.georreferenciar_direcciones(
    embajadas,
    nombre_campo='representacion_direccion',
    provincia_campo='representacion_provincia_descripcion'
)


# In[15]:


embajadas_direcciones


# In[19]:


embajadas_normalizadas = pd.concat([embajadas.reset_index(), embajadas_direcciones], axis=1)


# In[20]:


embajadas_gdf = gpd.GeoDataFrame(
    embajadas_normalizadas, 
    geometry=gpd.points_from_xy(
        embajadas_normalizadas.longitud.astype(float), 
        embajadas_normalizadas.latitud.astype(float)
    )
)


# In[22]:


provincias = gpd.read_file(
        'https://apis.datos.gob.ar/georef/api/provincias?max=100&formato=shp'
    )


# In[24]:


ax = provincias.plot(figsize=(10,10))

# se setean limites para no graficar la Antartida
ax.set_xlim(right=-50)
ax.set_ylim(bottom=-60)

embajadas_gdf.plot(ax=ax, color='orange')


# ## Ejercicio 2: API Nominatim

# Crea distintos mapas que tengan al mapa de las comunas de la Ciudad de Buenos Aires como base, y sobre el dibujen los puntos de coordenadas de:
# 
# * Los 10 restaurantes mas cercanos al centroide del barrio de Almagro
# * Los 10 hospitales mas cercanos al centroide de Villa Urquiza
# * Las 10 escuelas mas cercanas al centroide de Villa Devoto
# 
# Sugerencia: crea una funcion "buscar" que tome un texto de busqueda y haga la consulta a la API de Nominatim, y otra funcion "mapear" que tome un texto de busqueda y haga el mapa de los puntos sobre las comunas de la CABA. Usa la funcion mapear() para hacer los 3 mapas solicitados.

# In[110]:


def buscar(q, addressdetails=1, format='json', limit=50):
    '''Busca objetos geograficos en OSM.'''
    
    # toma los parametros de la funcion como un diccionario
    params = locals()
    
    # crea url de consulta
    url_base = 'https://nominatim.openstreetmap.org/?'
    query_string = urlencode(params)
    url = url_base + query_string
    print(url)
    
    # obtiene resultados y los convierte en un GeoDataframe
    resultados = requests.get(url).json()
    print(len(resultados), 'encontrados')
    
    df = pd.DataFrame(resultados)
    gdf = gpd.GeoDataFrame(
        df, 
        geometry=gpd.points_from_xy(df.lon.astype(float), 
                                    df.lat.astype(float))
    )
    
    return gdf


# In[111]:


def mapear(q):
    comunas_caba = gpd.read_file(
        'https://apis.datos.gob.ar/georef/api/departamentos?provincia=02&max=100&formato=shp'
    )
    objetos = buscar(q)
    ax = comunas_caba.plot(figsize=(10,10))
    return objetos.plot(ax=ax, color='orange')


# In[112]:


mapear('restaurantes, almagro, ciudad de buenos aires, argentina')


# In[113]:


mapear('centros de salud, caballito, ciudad de buenos aires, argentina')


# In[114]:


mapear('escuelas, devoto, ciudad de buenos aires, argentina')


# In[ ]:




