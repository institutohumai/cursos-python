#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/3_Agrupacion_y_Agregacion/agrupacion_agregacion.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# # Agrupación
# 

# ## Tabla de Contenidos
# 
#     I. Agrupación y agregación
#         I. Introducción
#             I. Crear columnas
#     III. Funciones de Agregación simple
#     IV. GroupBy: Trabajando sobre grupos
#         I. Clases que se encargan de la Agregación en Pandas
#         II. DataSetGroupBy
#             I. Lazy Evaluation
#             II. Iterar sobre los grupos
#         III. SeriesGroupBy
#         IV. Agregaciones múltiples
#         V. MultiIndex
#         VI. Ejercicios

# ## Introducción
# 
# En esta clase vamos a ver cómo agrupar datos a partir de una clave para trabajar sobre distintos grupos. 
# El primer dataset que vamos a utilizar es del portal de datos abiertos de España.  Los datos se pueden encontrar <a href='http://opendata.esri.es/datasets/paro-por-municipio-espa%C3%B1a/geoservice'> aquí</a> y la única modificación que se les hizo fue reemplazar el código de provincia por la descripción de la misma

# In[ ]:


#! pip install plotly


# In[ ]:


import pandas as pd
import plotly.express as px


# In[ ]:


df = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/parodesprov.csv')


# In[ ]:


df.sort_values('Codigo').head(6)


# Noten que en este conjunto de datos, al parecer la base está duplicada. Los municipios figuran dos veces, una vez con el código de provincia en NaN y otra vez con el código de provincia informado. Los valores de paro y población son muy cercanos en todos los casos, así que podemos considerarlas cercanas en el tiempo.

# In[ ]:


df = df[df['PAD_1_COD_PROV'].notnull()].copy()


# ## Niveles de Agregación
# 
# Además de los municipios (identificados por la variable Código), tenemos dos niveles de agregación geográfica, la provincia (Cod_Prov) y la comunidad autónoma (Cod_CAA).
# 
# Veamos qué valores toman y cómo se combinan.
# 

# In[ ]:


# ¿Cuántos municipios tiene cada comunidad? ¿Hay alguno que no tenga CCAA asociada?
df['Cod_CCAA'].value_counts(dropna=False)


# In[ ]:


# ¿Cuántas CCAA hay?
len(df['Cod_CCAA'].unique())


# In[ ]:


# ¿Cuántos municipios tiene cada provincia? ¿Hay alguno que no tenga provincia asociada?
df['Cod_Prov'].value_counts(dropna=False)


# In[ ]:


# ¿Cuántas provincias hay?
len(df['Cod_Prov'].unique())


# In[ ]:


# ¿Hay alguna provincia que tenga más de una CCAA asociada?
df[['Cod_CCAA','Cod_Prov']].drop_duplicates().sort_values('Cod_Prov')


# ## Buscando valores nulos
# 
# Ahora queremos filtrar todas las filas del DataFrame que contengan algún valor nulo, para analizar en detalle por qué existe ese valor faltante y si vamos a querer completarlo o descartarlo.
# 
# El método df.isnull() devuelve un DataFrame del mismo tamaño que el original, pero en lugar de los valores devuelve True si había un NaN y False si no lo había. 

# In[ ]:


df.isnull().head(3)


# #### Entendiendo el parámetro axis
# A continuación vamos a reducir el DataFrame de más arriba a una serie, compuesta por Booleans que indican True si hay algún valor nulo en la fila y False si no hay ninguno. La forma de reducir una serie de Booleanos es any() y el parámetro axis = 1 indica que queremos reducir el DataFrame aplicando la función de manera horizontal, probando todos los valores del eje y. 
#  
# 

# In[ ]:


df[df.isnull().any(axis=1)]


# Otro posible método para reucir es all así que una forma equivalente de lograr lo mismo es:

# In[ ]:


df[~(df.notnull().all(axis=1))]


# ¿Qué significará un TotalParoRegistrado nulo? :thinking: ¿Será equivalente a un paro de 0, algo que es posible que se de?

# In[ ]:


df[df['TotalParoRegistrado'] == 0].sample(3)


# Podríamos concluir que no, porque los municipios con paro igual a 0, informan 0. Entonces deberíamos descartar el dato. 
# 
# #### Entendiendo el parámetro inplace
# 
# Noten que la mayor parte de los métodos que trabajan sobre DataFrames devuelven objetos nuevos que si no los almacenamos en una variable se pierden. Cuando queremos que el DataFrame cambie a partir de una determinada acción usamos el parámetro inplace=True. 

# In[ ]:


df.dropna(inplace=True)


# In[ ]:


df[~(df.notnull().all(axis=1))]


# ### Crear columnas
# 
# Contamos con los cambios de población de cada municipio ('PAD_1C02') y también con el área ('Shape__Area'). Con estas columnas podemos formar la densidad.

# In[ ]:


# ¡Operación vectorizada! 
df['Densidad'] = df['PAD_1C02'] / df['Shape__Area']


# También sabemos la cantidad de personas desempleadas y con eso podemos formar la proporción de paro.

# In[ ]:


df['Proporcion_Paro'] =  df['TotalParoRegistrado'] / df['PAD_1C02'] 


# ## Funciones de Agregación simple
# 
# 
# | Nombre             | Versión que descarta NaN | Descripción                            |
# |--------------------|--------------------------|----------------------------------------|
# | serie.sum()        | serie.sum(skipna=True)   | Suma todos los elementos               |
# | serie.prod()       | serie.prod(skipna=True)  | Multiplica                             |
# | serie.mean()       | serie.mean(skipna=True)  | Promedia                               |
# | serie.std()        | serie.std(skipna=True)   | Calcula el desvío estándar             |
# | serie.var()        | serie.var(skipna=True)   | Calcula la varianza                    |
# | serie.min()        | serie.min(skipna=True)   | Calcula el valor mínimo                |
# | serie.max()        | serie.max(skipna=True)   | Calcula el valor máximo                |
# | serie.argmin()     | serie.argmin(skipna=True)| Calcula el índice del valor mínimo     |
# | serie.argmax()     | serie.argmax(skipna=True)| Calcula el índice del valor máximo     |
# | serie.median()     | serie.median(skipna=True)| Calcula la mediana                     |
# | X                  | serie.quantile()         | Calcula los percentiles                |
# | serie.any()        | X                        | Evalúa si algún elemento es TRUE       |
# | serie.all()        | X                        | Evalúa si todos los elementos son TRUE |

# Vamos a comprobar que la población total coincida (aproxiamadamente) con la <a href='https://www.google.com/search?client=firefox-b-e&q=poblacion+espana'>población de España.  <a/>

# In[ ]:


df['PAD_1C02'].sum()


# ¿Cuál es el promedio de proporción de paro en las autonomías de España?

# In[ ]:


df['Proporcion_Paro'].mean()


# Ejercicio: ¿Cuántas autonomías están por encima de la media y cuántas están por debajo?

# In[ ]:





# In[ ]:





# ¿Cuál es la mediana?

# In[ ]:





# Que la mediana sea menor a la media, significa que hay algunos valores llamativamente altos. Veamos un gráfico para ver la distribución de esta variable. 

# In[ ]:


fig = px.histogram(df, x="Proporcion_Paro")
fig.show()


# Y en cuanto al tamaño, ¿cuál es la mediana de tamaño en las autonomías? 

# In[ ]:


mediana_area = df['Shape__Area'].median()


# In[ ]:


mediana_area


# Si dividimos a las autonomías entre "grandes" (con un área mayor que la mediana) y "chicas" (con un área menor), ¿cuál grupo tiene mayor proporción de paro?

# In[ ]:


df.query('Shape__Area > @mediana_area')['Proporcion_Paro'].mean()


# In[ ]:


df.query('Shape__Area < @mediana_area')['Proporcion_Paro'].mean()


# Entonces, mientras que en autonomías más grandes la proporción de paro es 6.5%, en las más chicas es de 5.4%.
# 
# Ejercicio: calculen cómo es esta relación con respecto a la densidad.

# In[ ]:





# ## GroupBy: Trabajando sobre grupos
# 
# Muchas veces necesitamos analizar métricas, pero sobre agrupamientos de los datos. Por ejemplo, las autonomías se agrupan en provincias y podemos querer ver el desempeño de cada provinicia. O en lugar de analizar la densidad separando únicamente por la mediana, podemos querer ver qué pasa en cada percentil. 
# 
# En Pandas las operaciones sobre grupos se pueden ver como una combinación de las operaciones Split Apply Combine.
# 
# <img src='https://datasets-humai.s3.amazonaws.com/images/splitapplycombine.png'></img>
# 
# En algunos casos la operación que aplicamos sobre el dataframe original reduce el tamaño del mismo, por ejemplo cuando devolvemos la media de cada grupo y otras veces no, por ejemplo cuando comparamos cada elemento del grupo contra un benchmark del mismo, por ejemplo si quisiéramos hacer un ranking por juego para grupos de jugadores. 
# 
# ## Clases que se encargan de la Agregación en Pandas
# 
# ## DataSetGroupBy
# 
# Veamos qué devuelve pandas cuando agrupamos un dataset por una columna:

# In[ ]:


df.groupby('PAD_1_COD_PROV')


# In[ ]:


df.groupby('PAD_1_COD_PROV')['Shape__Area']


# En lugar de recibir una lista o numpy array de grupos, recibimos un objeto del tipo DataFrameGroupBy. Ahora veamos cuánto tarda en ejecutarse este método.
# 
# ### Lazy Evaluation

# In[ ]:


get_ipython().run_cell_magic('timeit', '', "df.groupby('PAD_1_COD_PROV')")


# In[ ]:


get_ipython().run_cell_magic('timeit', '', "a = list(df.groupby('PAD_1_COD_PROV'))")


# Hacer únicamente la agrupación por código de provincia lleva 50 microsegundos pero si convertimos el resultado a una lista, forzamos a que efectivamente se separen los grupos y eso tarda 10.9 ms.  
# 
# Este comportamiento se llama "lazy evaluation" y es muy importante en todos los motores de procesamiento de datos. Ejecutar las operaciones computacionalmente pesadas, sólo cuando se necesita permite hacer los procesos más eficientes. 

# In[ ]:


a = list(df.groupby('PAD_1_COD_PROV'))
type(a[0])


# In[ ]:


type(a[0][0])


# In[ ]:


type(a[0][1])


# ### Iterar sobre los grupos
# 
# Podemos recorrer los grupos en un loop for, desempaquetando la tupla que contine el nombre del grupo y el DataFrame correspondiente.
# 
# Veamos a ver cuántas autonomías tiene cada provincia.

# In[ ]:


for (cod_prov, group) in df.groupby('PAD_1_COD_PROV'):
    print("provincia={0}, tamaño={1}".format(cod_prov, group.shape[0]))


# Ejercicio: Calculen la media para cada provincia de la proporción de paro. Midan el tiempo que tarda en ejecutarse esa consulta. 

# In[ ]:





# ## SeriesGroupBy
# 
# Veamos el tipo de objeto que se forma cuando tomamos una serie del DataFrame. 

# In[ ]:


type(df.groupby('PAD_1_COD_PROV')['Proporcion_Paro'])


# Es un objeto de tipo SeriesGroupBy. A estos objetos, podemos aplicarles cualquier función de agregación. 

# In[ ]:


get_ipython().run_cell_magic('time', '', "df.groupby('PAD_1_COD_PROV')['Proporcion_Paro'].mean()")


# Noten que en este caso, la operación sobre el objeto SeriesGroupBy tarda (en este caso, va a depender del hardware) casi 15 veces que el loop for sobre el GroupBy. Esto es gracias a la vectorización que vimos en la clase 1.

# In[ ]:


a = df.groupby('PAD_1_COD_PROV')['Proporcion_Paro'].mean()


# In[ ]:


# El resultado de una función de agregación sobre una SeriesGroupBy, es otra serie
type(a)


# In[ ]:


# El índice de la serie son todas las provincias. 
a.index


# Ahora podemos probar otras funciones de agregación, por ejemplo calculemos el área por provincia:

# In[ ]:


df.groupby('PAD_1_COD_PROV')['Shape__Area'].sum()


# ## Agregaciones múltiples
# 
# Veamos ahora quiero combinar para cada provincia, cuál es el área, cuál es la población, cuál es la media y la mediana de paro y cuántas autonomías la componen. Para esto existe la función aggregate. Aplicada sobre un DataFrameGroupBy recibe como parámetro un diccionario con las nombres de columnas como claves y el tipo de agregación a realizar como valores. Pueden ser valores únicos o listas con varios valores.
# 

# In[ ]:


df.groupby('PAD_1_COD_PROV').aggregate({'Shape__Area':'sum',
                                        'PAD_1C02':'sum',
                                        'Proporcion_Paro':['mean','median','size']}).head()


# ## MultiIndex
# 
# Cuando agregamos por varias columnas distintas, nos queda un MultiIndex en las columnas
# 

# In[ ]:


df_agregado = df.groupby('PAD_1_COD_PROV').aggregate({'Shape__Area':'sum',
                                        'PAD_1C02':'sum',
                                        'Proporcion_Paro':['mean','median','size']})


# In[ ]:


df_agregado.columns


# #### Entendiendo la función pd.qcut
# 
# También podemos agrupar por más de una columna, usando una lista en lugar de un único valor como parámetro del groupby.
# 
# Calculemos los deciles de paro regitrado en los distintos municipios. 
# Para eso vamos a construir una columna que contenga el decil que ocupa el municipio en el ranking de proporción de paro. El decil 1 va a representar las autonomías que mejor se desempeñan y el decil 10 las que peor lo hacen.

# In[ ]:


df['Decil_Paro'] = pd.qcut(df['Proporcion_Paro'], 10, labels=range(1,11))


# Ahora podemos agrupar por provincia y decil para ver cuántos municipios de cada decil hay en cada provincia. 

# In[ ]:


serie_prov_decil = df.groupby(['PAD_1_COD_PROV','Decil_Paro']).size()


# In[ ]:


type(serie_prov_decil)


# In[ ]:


serie_prov_decil.index


# In[ ]:


serie_prov_decil.head(10)


# El objeto MultiIndex puede ser complicado para trabajar. Por eso conviene utilizar el método reset_index() para volver a un DataFrame común.

# In[ ]:


df_prov = serie_prov_decil.reset_index()


# In[ ]:


df_prov.head()


# ## Ejercicios
# 
# Ahora vamos a querer trabajar a nivel de provincia. Calculen la densidad, la proporción de paro y la cantidad de municipios para cada provincia ¿Cuál es la provincia con mayor proporción de paro? ¿Cuál es la que tiene menos?

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




