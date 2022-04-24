#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/5_Visualizacion/Ejercitacion/Ejercitacion_Extra.ipynb)

# # Ejercicios Visualización
# 
# Se pedirá realizar graficos con distintos dataset. Es importante que cada uno de ellos cuente con un título y los respectivos nombres en sus ejes.
# 
# 
# ## 1. Serie de tiempo
# 
# Se pide realizar un análisis exploratorio de una serie de datos macroeconomicos, para ello es necesario visualizar la serie y otros gráficos descriptivos de la misma que se indicarán a continuación.

# In[ ]:


# Imports
import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


df = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/data_macro.csv',sep=',')


# ### 1.1
# Graficar la serie de importaciones, en el eje de las abscisas deben ir los años, mientras que en el de las ordenadas la cantidad importada.

# ### 1.2
# 
# Graficar los cierres anuales para exportaciones, importaciones, consumo publico, consumo privado y PBI. Recuerde incorporar los años en el eje horizontal.

# ### 1.3 
# Graficar la serie de exportaciones junto a su media movil y su desvio estandar móvil.

# In[ ]:


import numpy as np


# In[ ]:


# Consejo: utilizar las funciones np.rolling

#media_movil = 
#desvio_movil = 


# ## 2. Iris Dataset
# 
# Utilizando el [Iris Dataset](https://es.wikipedia.org/wiki/Conjunto_de_datos_flor_iris), una base de datos que contiene información acerca de tres especies de flores distintas, vamos realizar algunos gráficos para entender mejor su comportamiento. Este dataset es ampliamente utilizado en el ámbito academico para la práctica de visualización de datos, es recomendable que investiguen y vean los distintos trabajos realizados sobre el mismo. 

# In[ ]:


df = pd.read_csv("https://datasets-humai.s3.amazonaws.com/datasets/data_iris.csv")


# ### 2.1 
# Graficar las distribución del largo del sepalo.

# ## 2.2
# Graficar la función de densidad del largo del sépalo.

# ## 3. Plotly

# In[ ]:


import plotly.graph_objects as go
import plotly.express as px


# ### 3.1
# 
# Con plotly express realizar un gráfico de dispersion donde el eje de ordenadas explique el largo del sepalo y el eje de abscisas explique el largo del pétalo con cada una de las especies.

# ### 3.2

# Realizar lo mismo que en el 3.1 pero con un *objeto gráfico* de plotly. Vemos que podemos hacer una mayor personalización.

# In[ ]:


# Especie versicolor
traza1 = 

# Especie setosa
traza2 = 

# Especies virginica
traza3 = 


# ## Extra
# 
# ### Visulización de imagenes

# Utilizando una imagen que tengan guardada en su computadora, vamos a visualizarla.

# In[ ]:


import matplotlib.image as mpimg

img = mpimg.imread('/ruta/de/la/imagen')


# In[ ]:


print(img)


# Utilice la función plt.imshow para visualizar la imagen.

# In[ ]:




