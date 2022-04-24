#!/usr/bin/env python
# coding: utf-8

# [![Open In colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/DatosGeograficos/2_Joins_y_Viz/1_Visualizacion.ipynb)

# # GeoPandas Visualización

# I. Tabla de contenidos
# II. Geodatos y transporte
# 
#     I. Cargamos datos
#     II. Explorando polígonos
#         I. Ejercicio
#     III. Usando máscaras
#         I. Ejercicio
#     IV. Coropletas
#     V. Mapas interactivos
#         I. Ejercicio
#         II. Agregando marcadores
#         III. Agregando capas a Folium
#         IV. Clusters de marcadores
#         V. Ejercicio

# In[ ]:


get_ipython().system('pip install geopandas')
get_ipython().system('apt install libspatialindex-dev')
get_ipython().system('pip install rtree')

get_ipython().system('pip install pysal')
get_ipython().system('pip install contextily #--> Para importar mapa base')
get_ipython().system('pip install folium')


# In[ ]:


import pandas as pd
import geopandas
import shapely
import pysal
import zipfile
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Geodatos y transporte

# Sin lugar a dudas el entorno urbano es el lugar predilecto para los análisis con datos vectoriales y, además, el transporte es una de las fuentes de información más atractivas. No sólo por su riqueza como información en sí sino también por la relevancia del transporte en la vida cotidiana en las grandes ciudades, especialmente en América Latina donde el transporte suele ser un problema en sí mismo.
# 
# Es así que encontramos todo tipo de información en este rubro:
# 
# - Polígonos estáticos como barrios o jurisdicciones administrativas (educativas, por ej.) o censales (como radio o fracción censal en Argentina).
# 
# - Líneas o multilíneas estáticas como las rutas de los colectivos o el callejeros de la ciudad.
# 
# - Puntos estáticos como paradas de colectivos, estaciones de subtes y trenes.
# 
# - Puntos en tiempo real como la posición de colectivos, camiones de basura, cortes de tránsito, accidentes, etc.

# ## Cargamos datos

# Vamos a leer la información. Noten que en todos los casos vamos a usar WGS 84.

# In[ ]:


def from_wkt(df, wkt_column, crs='EPSG:4326'):
    
    df["coordinates"]= df[wkt_column].apply(shapely.wkt.loads) # empleamos una función de shapely para leer WKT
        
    gdf = geopandas.GeoDataFrame(df, geometry='coordinates', crs=crs) # seteamos la columna de geometría
    
    return gdf


# Es común que los archivos shapefile incluyan la información sobre el sistema de coordenadas empleado. Esta información se encuentra incluida en el archivo .prj

# En esta notebook vamos a trabajar con las paradas y recorridos de colectivos, la información del censo 2010 (el último en Argentina al momento de escribir ésto) y las geometrías de los barrios.
# 
# Acá pueden ver los links de los archivos originales:
# 
# - https://data.buenosaires.gob.ar/dataset/colectivos-paradas
# - https://data.buenosaires.gob.ar/dataset/colectivos-recorridos
# - https://data.buenosaires.gob.ar/dataset/informacion-censal-por-radio/archivo/juqdkmgo-1214-resource

# In[ ]:


get_ipython().system('wget "https://datasets-humai.s3.amazonaws.com/datasets/recorrido-colectivos.zip"')


# In[ ]:


folder = "recorrido-colectivos"
with zipfile.ZipFile(f"{folder}.zip", 'r') as f:
    f.extractall(folder)


# In[ ]:


recorridos = geopandas.read_file("recorrido-colectivos/recorrido-colectivos.shp")


# In[ ]:


recorridos.crs.name


# In[ ]:


get_ipython().system("wget 'https://datasets-humai.s3.amazonaws.com/datasets/paradas-de-colectivo.zip'")


# In[ ]:


folder = "paradas-de-colectivo"
with zipfile.ZipFile(f"{folder}.zip", 'r') as f:
    f.extractall(folder)


# In[ ]:


paradas = geopandas.read_file("paradas-de-colectivo/paradas-de-colectivo.shp")


# In[ ]:


paradas.crs.name


# In[ ]:


barrios = pd.read_csv("https://datasets-humai.s3.amazonaws.com/datasets/barrios.csv", encoding='latin1')


# In[ ]:


barrios = from_wkt(barrios, "WKT")


# In[ ]:


barrios.crs.name


# In[ ]:


get_ipython().system("wget 'https://datasets-humai.s3.amazonaws.com/datasets/informacion-censal-por-radio-2010.zip'")


# In[ ]:


folder = "informacion-censal-por-radio-2010"
with zipfile.ZipFile(f"{folder}.zip", 'r') as f:
    f.extractall(folder)


# In[ ]:


radios = geopandas.read_file("informacion-censal-por-radio-2010/informacion_censal_por_radio_2010.shp")


# In[ ]:


radios.crs.name


# ## Explorando polígonos

# Un problema común suele ser tener una ruta o un callejero mucho más grande que el área que necesitamos analizar, por ejemplo, una ciudad, un barrio o una región delimitada arbitrariamente.

# Para comenzar veamos las rutas de colectivos en el Área Metropolitana de Buenos Aires.

# In[ ]:


recorridos.plot(color="red")


# Ok, eso no nos dice demasiado... Sí podemos ver que hay a la izquierda una serie de rutas que no está muy claro qué son... Filtrémoslas y volvamos a plotear. Para ello vamos a quedarnos con las rutas al este de la longitud -60.5.
# 
# ### Ejercicio 
# Filtrar los recorridos que están al oeste de la longiud -60.5. Tip: pueden tomar las coordenadas del centroide de las rutas. Guardar el resultado en recorridos_amba y graficar.

# In[ ]:





# Bueno, ahora que filtramos se vé más prolijo pero, ¿qué estamos viendo realmente? Para entender un poco mejor qué estamos viendo sumemos la capa de barrios de capa y grafiquemos.

# In[ ]:





# Mmm no podemos ver nada, ¿qué podemos hacer? El método plot incluye un parámetro alpha que regula la opacidad de la misma. Ajustando eso vamos a tener un mejor resultado. Además, vamos a agrandar la imagen para poder verla mejor.

# In[ ]:


type(ax)


# In[ ]:


fig, ax = plt.subplots(figsize=(12, 8))
recorridos_amba.plot(ax=ax, color="red", alpha=0.008)
barrios.plot(ax=ax, color="black")
plt.show()


# Ok, ahora sí podemos notar que las rutas exceden en mucho la ciudad de Buenos Aires. Para trabajar con esta información va a ser conveniente reducir el tamaño de las rutas sólo a la ciudad de Buenos Aires.

# ## Usando máscaras

# Es común que en situaciones nos encontremos con que un polígono es demasiado grande para lo que necesitamos o que excede en tamaño a otro polígono. En estos casos vamos a tener que "cortar" un polígono para reducirlo al tamaño y forma necesarios.

# Para poder usar los polígonos de CABA vamos a comenzar uniendo los barrios en un solo polígono (en vez de tener un polígono por barrio nos vamos a quedar con un solo polígono de todo CABA). Recordando la clase pasada, para hacer eso necesitamos agregar una columna constante, en este caso "ciudad" que sólo va a tener el valor "CABA" y luego aplicar **disolve**.

# In[ ]:


barrios["ciudad"] = "CABA"
mascara = barrios.dissolve(by="ciudad")


# A continuación podemos "clipear" la capa de recorridos con la máscara.

# In[ ]:


recorridos_caba = geopandas.clip(recorridos, mascara)


# Ahora sí, sólo veremos los recorridos dentro de CABA. Pero antes de hacer el gráfico vamos a incluir algunas mejoras. Por empezar vamos a ver paletas de color de CartoDB (una empresa que provee visualizaciones de mapas) en https://carto.com/carto-colors/ . En este caso vamos a querer sólo pintar los barrios y las calles, así que vamos a elegir una paleta cualitativa.
# Elegimos la paleta **prism**. De allí tomamos, por ejemplo, el verde claro para marcar CABA y el gris oscuro para las calles.

# In[ ]:


# paleta: #5F4690,#1D6996,#38A6A5,#0F8554,#73AF48,#EDAD08,#E17C05,#CC503E,#94346E,#6F4070,#994E95,#666666


# Además, vamos a agregar un mapa de fondo. Para ello vamos a usar la librería contextily, que nos provee acceso a una enorme variedad de proveedores de mapas.

# In[ ]:


import contextily as cx


# En ctx.providers van a ver toda la lista:

# In[ ]:


cx.providers


# In[ ]:


cx.providers.keys() # cada proveedor tiene a su vez distintos estilos


# In[ ]:


cx.providers.Stamen.TonerBackground


# Contextily hace muy sencillo incluir un mapa base con la función add_basemap, allí tenemos que establecer los axes a usar, la fuente del mapa (source) y la proyección. Contextily sólo funciona con las proyecciones WGS84 (EPSG:4326) y Spheric Mercator (EPSG: 3857). 
# Spheric Mercator que es un sistema de coordenadas proyectadas (sobre un plano), usado en Google Maps. Se basa en el mismo datum y elipsoide que EPSG:4326(WGS84), pero proyectando las coordenadas en un plano (en vez de sobre el elispoide). Para ver más en detalles las diferencias dejamos los siguientes links:
# - https://gis.stackexchange.com/questions/48949/epsg-3857-or-4326-for-googlemaps-openstreetmap-and-leaflet
# - https://gis.stackexchange.com/questions/3334/difference-between-wgs84-and-epsg4326
# - https://epsg.io/4326
# - https://epsg.io/3857
# 
# 
# Pueden consultar la documentación acá: https://contextily.readthedocs.io/en/latest/. 
# Por default, la función supone que la proyección es Spheric Mercator, como estamos trabajando en WGS84 tenemos que setear el parámetro **crs** a 4326.

# In[ ]:


fig, ax = plt.subplots(figsize=(16, 12))
barrios.plot(ax=ax, color="#73AF48", alpha=0.3) # seteamos color y alpha
recorridos_caba.plot(ax=ax, color="#666666", alpha=0.5) # seteamos color y alpha
cx.add_basemap(ax, source=cx.providers.OpenStreetMap.Mapnik, crs=4326)


# ### Ejercicio
# 
# 1- Explorar el DataFrame de paradas.
# 
# 2- Filtrar las paradas en Mataderos, usando para ello una máscara.
# 
# 3- Generar un mapa mostrando estas paradas y usando algún fondo de contextily, busquen un estilo que les guste :-)

# In[ ]:





# In[ ]:





# ## Coropletas

# Por otra parte, nos gustaría agregar más información al mapa. Para eso vamos a usar la capa de radios censales, veamos qué información tiene.

# In[ ]:


radios.head()


# Podemos ver que contamos con la población en el radio, la suma nos da el total de población de CABA (en 2010).

# In[ ]:


radios["POBLACI"].sum()


# Vamos a pintar los radios por población, vamos a probar dos maneras:
# 
# 1- Generar una mapa de color propio y pasárselo a la función. Esto es útil si queremos darle nuestro propio estilo al mapa y nos da mayor flexibilidad.
# 
# 2- Usar los mapas de color predefinidos por matplotlib.
# 
# Por último, este tipo de gráficos se conoce como mapa de coropletas, porque agregan una capa de información basado en el color sobre las dimensiones geográficas. En este caso, vamos a pintar los radios censales según la cantidad de población.

# Para crear nuestro propio **colormap** en matplotlib usamos LinearSegmentedColormap y pasamos una lista de colores. Esta lista es la paleta OrYel de CartoDB. Es lo que se conoce como una paleta secuencial, porque el tono va creciendo continuamente.

# In[ ]:


from matplotlib.colors import LinearSegmentedColormap

cmap = LinearSegmentedColormap.from_list(
    "mycmap",['#ee4d5a', '#f66356', '#f97b57', '#f7945d', '#f3ad6a', '#efc47e', '#ecda9a']
)


# Para pasar el mapa de color usamos el parámetro **cmap**, **scheme** sirve para definir qué valor numérico de población mapear contra que valor de color y **k** es la cantidad de colores distintos a usar.

# In[ ]:


fig, ax = plt.subplots(figsize=(16, 12))
mapa = radios.plot(ax=ax, column="POBLACI", linewidth=0.03, cmap=cmap, scheme="quantiles", k=7, alpha=0.8)
recorridos_caba.plot(ax=ax, color="#666666", linewidth=1)
cx.add_basemap(ax, source=cx.providers.CartoDB.PositronNoLabels, crs=4326)


# Ahora veamos la segunda opción, que es por lo general la opción preferida. En esta referencia podrán encontrar las distintas paletas.
# Vamos a elegir una opción divergente: RdYlBu. Para valores altos usa rojo, para valores bajos usa azul, y en los valores centrales coloca amarillo. 

# In[ ]:


fig, ax = plt.subplots(figsize=(16, 12))
mapa = radios.plot(ax=ax, column="POBLACI", linewidth=0.03, cmap="RdYlBu", scheme="quantiles", k=7, alpha=0.6)
recorridos_caba.plot(ax=ax, color="#666666", linewidth=1)
cx.add_basemap(ax, source=cx.providers.CartoDB.PositronNoLabels, crs=4326)

salida = "mapa_1.svg"
plt.savefig(salida, format='svg') # con este comando guardamos la imagen


# ## Mapas interactivos

# Hasta el momento trabajamos con mapas estáticos, en ciertos ocasiones puede ser útil contar con un mapa interactivo. Para eso vamos a emplear la librería folium.

# In[ ]:


import folium

# Obelisco de Buenos Aires
lat, lon = -34.603668, -58.381345 


# In[ ]:


# En folium el crs default es EPSG:3857 vamos a usarlo porque encontramos problemas con 4326
m = folium.Map(location=(lat, lon), zoom_start=15) 
m


# Folium permite usar distintos estilos de mapas. Algunos requieren de API key y otros no:
# 
# - OpenStreetMap
# - Mapbox Bright (Niveles de zoom limitados para capa gratuita)
# - Mapbox Control Room (Niveles de zoom limitados para capa gratuita)
# - Stamen (Terrain, Toner, and Watercolor)
# - Cloudmade (Must pass API key)
# - Mapbox (Must pass API key)
# - CartoDB (positron and dark_matter)

# ### Ejercicio
# 
# 1- Prueben los parámetros zoom_start y tiles

# In[ ]:





# In[ ]:





# ### Agregando marcadores

# Folium también nos permite agregar marcadores... Recordemos que las coordenadas originales son del Obelisco...

# In[ ]:


m = folium.Map(location=(lat, lon), zoom_start=16)

lat_colon, lon_colon = -34.600917, -58.382692 # agregamos las coordenadas del Colón

folium.Marker(
    [lat_colon, lon_colon],
    popup="Teatro Colon", # Problema al pasar tildes
    icon=folium.Icon(color='green')).add_to(m)

folium.Marker(
    [lat, lon],
    popup='Obelisco',
    icon=folium.Icon(color='red')).add_to(m)


# In[ ]:


m # Prueben hacer clic!


# ### Agregando capas a Folium
# 
# Ahora vamos a ver cómo agregar capas a folium desde GeoPandas. Para eso vamos a comenzar filtrando una línea de colectivos, luego exportamos el objeto a JSON (lo que se conoce como GeoJSON, ya que tiene las coordenadas de los vértices). Finalmente lo importamos desde folium y lo agregamos al mapa "m".

# In[ ]:


from folium.plugins import MarkerCluster


# In[ ]:


recorrido_132 = recorridos_caba.query("linea == '132'")


# In[ ]:


recorrido_132_json = recorrido_132.to_json()


# In[ ]:


folium.GeoJson(
    recorrido_132_json,
    name='recorrido'
).add_to(m)


# In[ ]:


m # prueben el zoom out


# Para agregar estilo tenemos el parámetro **style_function**, el cual requiere que le pasemos una función, para lo cual empleamos una función **lambda**. Además, folium nos permite "prender" o "apagar" capas con LayerControl

# In[ ]:


estilo = {'fillColor': '#73AF48', 'color': '#73AF48'}


# In[ ]:


folium.GeoJson(
    barrios,
    name='barrios',
    style_function=lambda x: estilo
).add_to(m)

folium.LayerControl(autoZIndex=False, collapsed=False).add_to(m)


# In[ ]:


m


# ### Clusters de marcadores
# 
# Folium también nos permite ver muchos marcadores en simultaneo y agruparlos o desagregarlos según el nivel de zoom. Para ello usamos MarkerCluster. Este objeto se instancia pasándole una lista de tuplas, donde para cada tupla el primer elemento es la latitud y el segundo elemento es la longitud. Además, podemos incluir como popup el nombre pasándole una lista de la misma extensión.
# 
# Vamos a mapear las paradas de la línea 132, para eso filtramos usando *.str*

# In[ ]:


paradas_132 = paradas[paradas["route_shor"].str.contains("132")] # filtro

puntos_paradas = list(zip(paradas_132.geometry.y, paradas_132.geometry.x)) # lista de tuplas


# In[ ]:


# Armamos un nuevo mapa
m = folium.Map(location=(lat, lon), zoom_start=16)

folium.GeoJson(
    recorrido_132_json,
    name='recorrido'
).add_to(m)

folium.GeoJson(
    barrios,
    name='barrios',
    style_function=lambda x: estilo
).add_to(m)

marker_cluster = MarkerCluster(puntos_paradas, popups = paradas_132["stop_name"].tolist(), name="paradas")

marker_cluster.add_to(m)


# In[ ]:


folium.LayerControl(autoZIndex=False, collapsed=False).add_to(m)


# In[ ]:


m


# ### Ejercicio

# Un tipo de visualización muy popular es el mapa de calor (heatmap en inglés), el cual representa en una escala de color divergente la distribución de valores (en este caso paradas de colectivos) en un mapa. Por lo general, se usa el color rojo para valores altos y el azul o celeste para valores bajos.
# 
# Vamos a graficar un HeatMap para lo cual deben:
# 
# 1- Importar la clase HeatMap del módulo plugins de folium
# 
# 2- Instanciar un mapa
# 
# 3- Graficar un HeatMap de todas las paradas del AMBA, para lo cual les recomendamos leer a documentación (accesible desde Jupyter)
# 
# 
# Prueben variar el parámetro **radius** , **max_zoom**, **max_val**

# In[ ]:





# In[ ]:




