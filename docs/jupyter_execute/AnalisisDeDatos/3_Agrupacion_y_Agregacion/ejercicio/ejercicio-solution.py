#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/3_Agrupacion_y_Agregacion/ejercicio/ejercicio-solution.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>
# 
# Vamos a trabajar sobre el mismo DataFrame que usamos en clase pero agrupando a nivel de comunidad autónoma (Cod_CCAA). En este caso vamos a traer también las descripciones y vamos a hacer un join para formar un único data set.

# In[1]:


import pandas as pd
import plotly.express as px


# In[2]:


df = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/parodesprov.csv')


# In[3]:


df_descripciones = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/comunidades_descripcion.csv')


# Unan ambos DataFrames utilizando la función pd.merge()

# In[4]:


df = df.merge(df_descripciones,left_on='Cod_CCAA',right_on='Código')


# Construir el DataFrame de comunidades autónomas, incluyendo la densidad, la proporción de paro y la cantidad de municipios. 

# In[5]:


df_ccaa = df.groupby('Literal').aggregate({'Shape__Area':'sum',
                                       'PAD_1C02':'sum',
                                       'TotalParoRegistrado':'sum',
                                       'Codigo':'size'}).reset_index()


# In[6]:


df_ccaa['Densidad'] = df_ccaa['PAD_1C02'] / df_ccaa['Shape__Area']


# In[7]:


df_ccaa['Proporcion_Paro'] = df_ccaa['TotalParoRegistrado'] / df_ccaa['PAD_1C02']


# In[8]:


df_ccaa.columns


# In[9]:


df_ccaa.columns = ['CCAA', 'Area', 'Poblacion', 'TotalParoRegistrado',
       'Cantidad_Municipios', 'Densidad', 'Proporcion_Paro']


# Habíamos visto que el promedio de la proporción de paro en los municipios con una densidad menor a la mediana es más bajo.. ¿Se cumple lo mismo para las provincias?

# In[10]:


mediana_densidad = df_ccaa['Densidad'].median()


# In[11]:


df_ccaa.query('Densidad > @mediana_densidad')['Proporcion_Paro'].mean()


# In[12]:


df_ccaa.query('Densidad <= @mediana_densidad')['Proporcion_Paro'].mean()


# ¿Cuál es la comunidad autónoma con mayor cantidad de municipios?

# In[15]:


df_ccaa.sort_values('Cantidad_Municipios',ascending=False).head(1)


# In[ ]:




