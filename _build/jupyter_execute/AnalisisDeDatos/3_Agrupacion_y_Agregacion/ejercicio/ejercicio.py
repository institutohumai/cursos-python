#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/3_Agrupacion_y_Agregacion/ejercicio/ejercicio.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>
# 
# Vamos a trabajar sobre el mismo DataFrame que usamos en clase pero agrupando a nivel de comunidad autónoma (Cod_CCAA). En este caso vamos a traer también las descripciones y vamos a hacer un join para formar un único data set.

# # Ejercicios Pandas III

# In[1]:


import pandas as pd
import plotly.express as px


# In[2]:


df = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/parodesprov.csv')


# In[3]:


df_descripciones = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/comunidades_descripcion.csv')


# Unan ambos DataFrames utilizando la función pd.merge()

# In[ ]:





# Construir el DataFrame de comunidades autónomas, incluyendo la densidad, la proporción de paro y la cantidad de municipios. 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Habíamos visto que el promedio de la proporción de paro en los municipios con una densidad menor a la mediana es más bajo.. ¿Se cumple lo mismo para las provincias?

# In[ ]:





# In[ ]:





# In[ ]:





# ¿Cuál es la comunidad autónoma con mayor cantidad de municipios?

# In[ ]:





# In[ ]:




