#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/2_Pivot_Table_y_Joins/clase-2-ejercicios.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>
# 
# 
# # Ejercicios Pandas II

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
# * ¿Cómo se distribuye la superficie sembrada de Papa? ¿Es una distribución probabilística similar a la de la soja? ¿El rendimiento en kg producidos por hectárea es similar entre los departamentos que la cultivan, se distribuye más o menos "equitativamente" que el de la soja? ¿Hay valores potencialmente anómalos?
# * Generá una tabla donde cada cultivo sea una columna, cada fila un año (una campaña) y los valores sean la producción total.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




