#!/usr/bin/env python
# coding: utf-8

# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/5_Visualizacion/Ejercitacion/Ejercitacion_Extra_Resuelta.ipynb)

# # Ejercicios extra visualización
# 
# Se pedirá realizar graficos con distintos dataset. Es importante que cada uno de ellos cuente con un título y los respectivos nombres en sus ejes.
# 
# 
# ## 1. Serie de tiempo
# 
# Se pide realizar un análisis exploratorio de una serie de datos macroeconomicos, para ello es necesario visualizar la serie y otros gráficos descriptivos de la misma que se indicarán a continuación.

# In[1]:


# Imports
import pandas as pd 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/data_macro.csv', sep=',', index_col=0)


# In[3]:


df.head()


# La función transform nos permite aplicar operaciones por grupos, por ejemplo para sacar el rango.

# In[6]:


df.groupby('Año').transform(lambda x: (x.max() - x.min()))


# In[7]:


# tomamos 1 por año
df.groupby('Año').transform(lambda x: (x.max() - x.min())).iloc[::4]


# ### 1.1
# Graficar la serie de importaciones, en el eje de las abscisas deben ir los años, mientras que en el de las ordenadas la cantidad importada.

# In[5]:


df['Importaciones_D'].plot();
años = df['Año'].unique()
plt.xticks(range(0, len(años)*4, 4), años, rotation=90);


# ### 1.2
# 
# Graficar los cierres anuales para exportaciones, importaciones, consumo publico, consumo privado y PBI. Recuerde incorporar los años en el eje horizontal.

# In[99]:


df.columns


# In[100]:


df['Año'].unique().shape[0]


# In[101]:


df.head()


# In[102]:


# Tomamos 1 trimestre por año
cols = ['Trimestre', 'PIB_D', 'Importaciones_D', 'Exportaciones_D', 'Consumo_Privado_D', 'Consumo_Publico_D']
# graficamos y especificamos un tamaño
df.loc[3::4, cols].plot(kind='bar', figsize=(10,5))
labels = df['Año'].unique()
plt.xticks(range(0, labels.shape[0]), labels);


# ### 1.3 
# Graficar la serie de exportaciones junto a su media movil y su desvio estandar móvil. Usar la función .rolling de pandas

# In[103]:


media_movil = df['Exportaciones_D'].rolling(4).mean()
desvio_movil = df['Exportaciones_D'].rolling(4).std()


# In[104]:


df['Exportaciones_D'].plot()
media_movil.plot()
desvio_movil.plot(kind='bar')
plt.xticks(range(1,65,4), df['Año'].unique(), rotation=60)
plt.xlabel('Año')
plt.title('Exportaciones, con media movil y desvio std')
plt.ylabel('Pesos');


# In[115]:


# seaborn puede complementarse con matplotlib
import seaborn as sns
sns.set_style('dark')


# In[116]:


df['Exportaciones_D'].plot()
media_movil.plot()
desvio_movil.plot(kind='bar')
plt.xticks(range(1,65,4), df['Año'].unique(), rotation=60)
plt.xlabel('Año')
plt.title('Exportaciones, con media movil y desvio std')
plt.ylabel('Pesos');


# ## 2. Iris Dataset
# 
# Utilizando el [Iris Dataset](https://es.wikipedia.org/wiki/Conjunto_de_datos_flor_iris), una base de datos que contiene información acerca de tres especies de flores distintas, vamos realizar algunos gráficos para entender mejor su comportamiento. Este dataset es ampliamente utilizado en el ámbito academico para la práctica de visualización de datos, es recomendable que investiguen y vean los distintos trabajos realizados sobre el mismo. 

# In[117]:


df = pd.read_csv("https://datasets-humai.s3.amazonaws.com/datasets/data_iris.csv")


# In[118]:


df.head()


# ### 2.1 
# Graficar las distribución del largo del sepalo.

# In[119]:


df['SepalLengthCm'].hist(bins=20);
plt.title('Distribución del largo del sépalo');


# # 2.2
# Graficar la función de densidad del largo del sépalo.

# In[120]:


df['SepalLengthCm'].plot.density();


# Extra: probar si sigue una distribución normal con [prueba KS](https://en.wikipedia.org/wiki/Kolmogorov%E2%80%93Smirnov_test)

# In[121]:


from scipy.stats import kstest
x = df['SepalLengthCm']
# normalizamos 
norm = (x - x.mean())/x.std()
kstest(norm, 'norm')


# In[122]:


import seaborn as sns
sns.histplot(df['SepalLengthCm'], kde=True)
plt.xlim(3, 9);


# ## 3. Plotly

# In[123]:


import plotly.graph_objects as go
import plotly.express as px


# ### 3.1
# 
# Con plotly express realizar un gráfico de dispersion donde el eje de ordenadas explique el largo del sepalo y el eje de abscisas explique el largo del pétalo con cada una de las especies.

# In[124]:


fig = px.scatter(df, x='PetalLengthCm', y='SepalLengthCm', color='Species', title='Iris')
fig.show()


# ### 3.2

# Realizar lo mismo que en el 3.1 pero con un *objeto gráfico* de plotly. Vemos que podemos hacer una mayor personalización.

# In[125]:


# Especie versicolor
t1 = go.Scatter(x=df['PetalLengthCm'][df['Species'] == 'Iris-versicolor'],
                    y=df['SepalLengthCm'][df['Species'] == 'Iris-versicolor'],
                    mode='markers',
                    marker_color='rgb(140, 190, 20)', 
                    marker_symbol='star-square',
                    name='versicolor')

# Especie setosa
t2 = go.Scatter(x=df['PetalLengthCm'][df['Species'] == 'Iris-setosa'],
                    y=df['SepalLengthCm'][df['Species'] == 'Iris-setosa'],
                    mode='markers',
                    marker_color='rgb(240, 90, 20)', 
                    marker_symbol='star-triangle-up')

# Especies virginica
t3 = go.Scatter(x=df['PetalLengthCm'][df['Species'] == 'Iris-virginica'],
                    y=df['SepalLengthCm'][df['Species'] == 'Iris-virginica'],
                    mode='markers',
                    marker_color='rgb(40, 190, 100)', 
                    marker_symbol='star-square')


# In[126]:


fig = go.Figure([t1,t2,t3])
fig.show()


# ## Extra
# 
# ### Visulización de imagenes

# Utilizando una imagen que tengan guardada en su computadora, vamos a visualizarla.

# In[127]:


get_ipython().system('wget https://careers.edicomgroup.com/wp-content/uploads/2021/03/DeepLearning-2.jpg -O img.jpg')


# In[131]:


# Leer los pixeles de una imagen
import matplotlib.image as mpimg
img = mpimg.imread('img.jpg')


# In[132]:


print(img)


# La función plt.imshow para visualizar la imagen.

# In[130]:


plt.imshow(img)
plt.axis(False);

