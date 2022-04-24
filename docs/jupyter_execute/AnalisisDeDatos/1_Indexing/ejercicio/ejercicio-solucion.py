#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/1_Indexing/ejercicio/ejercicio-solucion.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>
# 
# Para este ejercicio vamos a importar un conjunto de datos con el listado de colegios públicos de Bogotá del año 2016

# In[1]:


import pandas as pd


# In[2]:


df_colegios = pd.read_csv('https://www.datos.gov.co/api/views/qijw-htwa/rows.csv?accessType=DOWNLOAD')


# ¿Cuáles son las columnas? ¿Cuántas filas tiene?

# In[3]:


df_colegios.shape


# In[4]:


df_colegios.columns


# Seleccionen los colegios donde la propiedad de la planta física sea de una persona natural o comunidad religiosa.

# In[5]:


df_sub = df_colegios.query('(propiedad_Planta_Fisica == "PERSONA NATURAL") | (propiedad_Planta_Fisica == "COMUNIDAD RELIGIOSA")')


# ¿Hay alguno de estos colegios que sea para capacidades excepcionales?

# In[6]:


df_sub['capacidades_Excepcionales'].value_counts()


# ¿Cuáles son los colegios que ofrecen todos los niveles educativos? ¿Qué idiomas ofrecen?

# In[7]:


df_todos = df_colegios[df_colegios['niveles'] == 'PREESCOLAR,MEDIA,BÁSICA SECUNDARIA,BÁSICA PRIMARIA,PRIMERA INFANCIA']


# In[8]:


df_todos['idiomas'].value_counts(dropna=False)


# In[ ]:




