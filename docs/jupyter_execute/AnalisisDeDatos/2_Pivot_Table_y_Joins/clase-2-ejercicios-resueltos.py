#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/2_Pivot_Table_y_Joins/clase-2-ejercicios-resueltos.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>
# 
# 
# # Clase 2: ejercicios prácticos resueltos

# In[1]:


import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.style.use('ggplot')
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Parámetros y extracción de datos

# In[2]:


ESTIMACIONES_URL = "http://datos.agroindustria.gob.ar/dataset/9e1e77ba-267e-4eaa-a59f-3296e86b5f36/resource/95d066e6-8a0f-4a80-b59d-6f28f88eacd5/download/estimaciones-agricolas-al-30-09-2019.csv"
ESTIMACIONES_URL_S3 = "https://datasets-humai.s3.amazonaws.com/datasets/estimaciones_agricolas.zip"
ESTIMACIONES_PATH = "data/estimaciones-agricolas.csv"


# In[3]:


converters = {
    "id_provincia": lambda x: str(x).zfill(2),
    "id_departamento": lambda x: str(x).zfill(3),
}

#estimaciones = pd.read_csv(ESTIMACIONES_URL, encoding="latin1", converters=converters)estimaciones = pd.read_csv(ESTIMACIONES_URL, encoding="latin1", converters=converters)
estimaciones = pd.read_csv(ESTIMACIONES_URL_S3, encoding="utf8", converters=converters)
#estimaciones.to_csv(ESTIMACIONES_PATH, encoding="utf8", index=False)
#estimaciones = pd.read_csv(ESTIMACIONES_PATH, converters=converters)


# ## Ejercicio 1 

# Explorar descriptivamente el dataset de estimaciones agrícolas (https://datos.gob.ar/dataset/agroindustria-agricultura---estimaciones-agricolas) usando los elementos aprendidos en la clase 2, respondiendo las siguientes preguntas o mostrando:
# 
# * ¿Cuál es la producción total en toneladas estimada de todos los cultivos en la Argentina, cada año?
# * ¿Cómo se distribuye el rendimiento (kg por hectárea) estimado promedio del cultivo de soja entre los departamentos que la siembran? ¿Qué tipo de distribución probabilística tiene? ¿Cuál es (y en qué departamento está) el rendimiento mínimo, mediano y máximo? ¿Cuál es el rendimiento promedio? ¿Hay valores potencialmente anómalos?
# * Generá una tabla donde cada cultivo sea una columna, cada fila un año (una campaña) y los valores sean la producción total.

# In[4]:


estimaciones.head()


# In[5]:


estimaciones.columns


# Algunos campos tienen espacios al final, es mejor tener nombres de campos sin espacios.

# In[6]:


estimaciones.columns = [col.strip() for col in estimaciones.columns]


# ### Producción total anual 

# In[7]:


estimaciones[["campania_inicio","campania_fin"]] = estimaciones.campaña.str.split("/", n=1,expand=True)


# In[8]:


estimaciones["campania_inicio"] = estimaciones["campania_inicio"].astype(int)
estimaciones["campania_fin"] = estimaciones["campania_fin"].astype(int)


# In[9]:


# pasamos los valores a millones
estimaciones["produccion"] = estimaciones.produccion.astype(float) / 1000000


# In[10]:


produccion_anual = estimaciones.pivot_table(
    index="campania_fin",
    values="produccion",
    aggfunc="sum"
)


# In[11]:


produccion_anual.tail()


# In[12]:


produccion_anual.plot(
    figsize=(17, 8),
    title="Producción agrícola total anual (tn)"
)


# ¿Está bien ese pico en la campaña 2016/2017? Hay que buscar algún control. https://www.invenomica.com.ar/desempeno-de-la-cosecha-agricola-argentina-2017-2018/ Parece que los datos de 2016/2017 están duplicados! Busquemos cuál es el error en el dataset.

# In[13]:


estimaciones[estimaciones.campaña == "2016/2017"].produccion.sum()


# En realidad los datos de la campaña 2016/2017 parecen estar bien... el problema se da cuando sumamos por el el año de fin de campaña y 2017 aparece duplicado. Tal vez haya un error en los rótulos de las campañas.

# In[14]:


estimaciones[["campaña", "campania_fin"]][
    estimaciones.campania_fin > 2000
].drop_duplicates().sort_values("campania_fin")


# Parece que la campaña 2010/2011 está incorrectamente rotulada como 2010/2017. Antes de seguir adelante, hay que hacer esa corrección.

# In[15]:


estimaciones["campaña"] = estimaciones.campaña.str.replace("2010/2017", "2010/2011")

estimaciones[["campania_inicio","campania_fin"]] = estimaciones.campaña.str.split("/", n=1,expand=True)
estimaciones["campania_inicio"] = estimaciones["campania_inicio"].astype(int)
estimaciones["campania_fin"] = estimaciones["campania_fin"].astype(int)


# In[16]:


produccion_anual = estimaciones.pivot_table(
    index="campania_fin",
    values="produccion",
    aggfunc="sum"
)


# In[17]:


produccion_anual.plot(
    figsize=(17, 8),
    title="Producción agrícola total anual (tn)"
)


# In[18]:


produccion_anual.tail()


# La camapaña 2018/2019 está incompleta (el dataset fue actualizado en septiembre de 2019 por última vez) así que también debemos excluirla.

# In[19]:


estimaciones = estimaciones[estimaciones.campaña != "2018/2019"]


# ##  Rendimiento promedio de la soja por departamento

# In[20]:


estimaciones.cultivo.unique()


# Ya que nos piden hacer una comparación de rendimientos de la soja entre departamentos, nos conviene realizar los filtros al principio y quedarnos con la muestra que nos interesa en una sola variable.

# In[21]:


estimaciones_soja = estimaciones[
    (estimaciones.cultivo == "Soja total") &
    (estimaciones.campaña == "2017/2018")
]


# In[22]:


len(estimaciones_soja.departamento.unique())


# Hay 234 departamentos que producen Soja, y sobre los cuales hay que hacer el análisis.

# In[23]:


estimaciones_soja.rendimiento.hist(figsize=(17, 8), bins=15);


# Los valores que se separan mucho del histograma, a primera vista podrían sospecharse como anómalos (ie. departamentos con rendimientos superiores a los 4000 kg. por hectárea deberían analizarse más profundamente).

# In[24]:


estimaciones_soja.rendimiento.describe()


# In[25]:


estimaciones_soja[estimaciones_soja.rendimiento == estimaciones_soja.rendimiento.max()]


# In[26]:


estimaciones_soja = estimaciones_soja.copy()
estimaciones_soja['diferencia_mediana'] = np.abs(estimaciones_soja.rendimiento - estimaciones_soja['rendimiento'].median())


# In[27]:


estimaciones_soja[estimaciones_soja['rendimiento'] == estimaciones_soja['rendimiento'].median()]


# In[28]:


estimaciones_soja[estimaciones_soja['diferencia_mediana'] == estimaciones_soja['diferencia_mediana'].min()]


# In[29]:


estimaciones_soja[estimaciones_soja.rendimiento == estimaciones_soja.rendimiento.min()]


# ### Tabla de evolución de producción por cultivo 

# In[30]:


produccion_cultivo_evolucion = estimaciones.pivot_table(
    index="campaña",
    columns="cultivo",
    values="produccion",
    aggfunc="sum"
)
produccion_cultivo_evolucion


# In[ ]:




