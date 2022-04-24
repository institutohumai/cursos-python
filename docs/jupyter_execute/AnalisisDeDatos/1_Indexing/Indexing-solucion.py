#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/1_Indexing/Indexing-solucion.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# In[1]:


# Siempre al principio, importamos las librerías.
import pandas as pd
import numpy as np


# # Tabla de Contenidos
# 
#     I. Análisis de datos con Pandas
#     II. Los objetos fundamentales de Pandas
#         I. Series
#         II. DataFrames
#         III. Índices
#     III. Exploración
#         I. Filtrando un DataFrame (Indexing)
#             I. Boolean Indexing
#                 I. Máscara booleana
#                 II. Máscara booleana con muchas condiciones
#             II. Boolean indexing con query()
#             III. Fancy Indexing
#         II. Funciones de Agregación
#     IV. Otros análisis descriptivos
#         I. Para las variables numéricas
#         II. Para las variables categóricas
#         III. Ordenar por columnas y limitar la cantidad de resultados
#     V. Anexo: volviendo al tema de la vectorización

# # Exploración
# 
# Vamos a analizar datos de una fuente real. Los ingresos de los funcionarios son información pública que se libera anualmente en el <a href='https://data.buenosaires.gob.ar/dataset/sueldo-funcionarios'>portal de datos abiertos</a> de GCBA.  
# 
# En general los 4 primeros pasos para analizar un data set son:
# 1. Leerlo
# 2. Consultar cuáles son las columnas
# 3. Extraer una muestra
# 4. Verificar cuántos registros tiene

# ## 1- Para leer el data set usamos la función de pandas read_csv
# 
# Con esta función podemos leer archivos que estén en una url pública o en una ubicación del disco accesible desde la Jupyter Notebook. 

# In[2]:


df = pd.read_csv('http://cdn.buenosaires.gob.ar/datosabiertos/datasets/sueldo-funcionarios/sueldo_funcionarios_2019.csv')


# ## 2- Consultamos las columnas
# 

# In[3]:


df.columns


# ## 3- Extraemos una muestra

# In[4]:


df.sample(5)


# ## 4- Consultamos la cantidad de filas y de columnas

# In[5]:


# La propiedad shape nos devuelve una tupla (filas,columnas)
df.shape


# # Vectorización con Pandas
# 
# Pandas es una de las librerías de Python más usadas para análisis de datos. El nombre pandas viene de "Panel Data Analysis" y su funcionalidad permite hacer operaciones sobre datos que se encuentran en memoria de manera eficiente. 
# 
# Pandas es útil para trabajar sobre datos tabulares, con dos condiciones importantes:
# 
# I. Los datos se encuentran enteramente en la memoria RAM. Con lo cual, el tamaño de los datos que podemos manipular está limitado por el hardware. Como regla de pulgar, es una buena práctica no ocupar más de 1/3 de la memoria RAM de nuestro dispositivo con el dataset. Así, si estamos trabajando localmente en una notebook con 8GB de memoria RAM no es recomendable procesar datasets de más de 2.33GB.
# 
# II. En pandas, las operaciones sobre filas y columnas son, en general, eficientes porque se hacen de forma "vectorizada". En realidad esta optimización, se hace desde numpy, una librería para realizar operaciones matemáticas que se utilizó a su vez para escribir pandas. 
# 
# Las operaciones vectorizadas son las que se realizan en bloque en vez de caso por caso. Las computadoras de hoy tienen la capacidad de recibir muchas instrucciones juntas y procesar varias de ellas a la vez. Por ejemplo, si nuestro hardware tiene la capacidad de procesar 4 operaciones juntas, el resultado de vectorizar una operación matemática es el siguiente:
# 
# <img src = 'https://datasets-humai.s3.amazonaws.com/images/vectorizacion.png' /> 
# 
# 
# En el primer caso hay que hacer 5 operaciones y en el segundo caso sólo dos.
# 
# Es importante entender, entonces, que Pandas trabaja de esta manera y que por eso es una de las herramientas más elegidas para manipular datos en memoria.
# 

# 
# 
# # Los objetos fundamentales de Pandas
# 
# ## Series
# 
# Las series son "columnas" que de una tabla que están asociadas a un índice y a un nombre. Igual que una lista común de Python es una secuencia de elementos ordenados, pero a diferencia de la lista está asociada a más información.

# In[6]:


# Las series se pueden crear a partir de una lista
serie = pd.Series(['a','b','c'])


# In[7]:


# Propiedades importantes de las series
print('Tipo de objetos que tiene ', serie.dtype)
print('Nombre ', serie.name)
print('Index ',serie.index)
print('Valores ',serie.values)


# ## DataFrames
# 
# Los DataFrames son "tablas", compuestas por varias "columnas" o series que comparten todas un mismo índice. En general los DataFrames se crean a partir de leer tablas de archivos (pueden ser en formato json o csv) pero a veces también se crean a partir de listas de diccionarios o de otras maneras. 
# 
# Los DataFrames tienen un objeto Index que describe los nombres de columnas y otro objeto Index que describen los nombres de las filas.

# In[8]:


# Leemos un dataset público
df = pd.read_csv('http://cdn.buenosaires.gob.ar/datosabiertos/datasets/sueldo-funcionarios/sueldo_funcionarios_2019.csv')


# In[9]:


# Propiedades importantes de los dataframes
print('Columnas ', df.columns)
print('Index ', df.index)
print('Dimensiones ',df.shape)


# In[10]:


# Consultar las primeras filas
df.head()


# Si queremos extraer una serie del DataFrame, podemos hacerlo de la misma forma en que extraemos un valor de un diccionario.
# 
# 

# In[11]:


serie_mes = df['mes']


# In[12]:


type(serie_mes)


# ## Índices
# 
# Los índices acompañan a las series y a los Data Frames. Son conjuntos ordenados e inmutables de elementos

# In[13]:


df.index


# In[14]:


df.columns


# In[15]:


ind = pd.Index([2, 3, 5, 7, 11])
ind


# In[16]:


ind[1] = 0


# Ejercicio: exploren el dataset público que se encuentra en la siguiente url: https://datasets-humai.s3.amazonaws.com/datasets/titanic.csv ¿De qué se trata? ¿Cuántas filas tiene? ¿Cuántas columnas? Al leerlo, pueden almacenarlo en la variable df_titanic. 

# In[17]:


df_titanic = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/titanic.csv',sep='|')


# In[18]:


df_titanic.sample(5)


# In[19]:


df_titanic.shape


# ## Filtrando un DataFrame (Indexing)
# 
# Hay muchas técnicas para filtrar un DataFrame. Podemos querer filtrar por columnas o por filas, por posición o por nombre. También podemos querer filtrar por condiciones que se cumplen o no. Cuando no queremos filtrar sobre una dimensión (filas o columnas) usamos ":" para seleccionar todo.
# 
# 
# <img src='img/indexing.png' style='height:350px' />
# 
# 

# ### Boolean Indexing
# 
# Supongamos que queremos tomar el dataset de funcionarios y quedarnos únicamente con los que pertenecen al Ministerio de Cultura.
# Para eso lo que hacemos es indexar al DataFrame por una condición booleana. Eso implica que debemos crear una serie compuesta por valores True y False para aplicarla como índice a las filas.
# 
# Los operadores que sirven para evaluar condiciones sobre las series son:
# 
# 
# | S  | Descripción   | S  | Descripción   |   |
# |----|---------------|----|---------------|---|
# | >= | Mayor o Igual | <= | Menor o Igual |   |
# | == | Igual         | != | Distinto      |   |
# | >  | Mayor         | <  | Menor         |   |

# #### Máscara booleana
# 
# Veamos lo que pasa cuando le aplicamos a una serie una condición que devuelve un booleano

# In[20]:


df['anio'] != 2019


# In[21]:


mascara_booleana = df['anio'] != 2019


# Nos devuelve una serie de la misma longitud que la original y que contiene sólo valores True o False. 

# In[22]:


type(mascara_booleana)


# In[23]:


mascara_booleana.shape


# In[24]:


mascara_booleana.dtype


# Ahora seleccionemos entonces, los registros que corresponden al Ministerio de Cultura.

# In[25]:


df_min_cul = df.loc[df['reparticion'] == 'Ministerio de Cultura',:]


# In[26]:


# Veamos la cantidad de casos
df_min_cul.shape


# Algo que puede llegar a confundir sobre el Indexing en Pandas es que en algunos casos se puede ser menos explícito a la hora de filtrar. Por ejemplo si ponemos una condición Booleana, pandas asume que el tipo de indexing es loc y que el filtro es sobre las filas y no sobre las columnas:
# 

# In[27]:


df_min_cul = df[df['reparticion'] == 'Ministerio de Cultura']


# In[28]:


df_min_cul.shape


# Probemos con otra condición.
# 
# Ejercicio1: Traer todos los sueldos de la segunda mitad del año...

# In[29]:


# Solución
df_sem2 = df[df['mes'] > 6]


# Ejercicio 2: Volviendo al DataFrame del Titanic ¿Cuántos pasajeros sobrevivieron y cuántos no? ¿Cuántos pagaron una tarifa menor a 25?

# In[30]:


df_titanic = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/titanic.csv',sep='|')


# In[31]:


#Solución 
df_titanic[df_titanic['Survived']==1].shape


# In[32]:


df_titanic[df_titanic['Survived']==0].shape


# In[33]:


df_titanic[df_titanic['Fare'] < 25].shape


# #### Máscara booleana con muchas condiciones
# 
# Ahora tratemos de filtrar el dataset por dos condiciones: por ejemplo tomar los sueldos de abril de la secretaria de innovación. 
# Para eso tenemos que combinar dos máscaras booleanas con una condición.
# 
# | S | Descripcion        | S  | Descripcion |   |
# |---|--------------------|----|-------------|---|
# | & | AND (y)            | \| | OR (o)      |   |
# | ^ | XOR (o exclusivo)  | ~  | NOT (no)    |   |
# 
# 
# 
# Por ejemplo: seleccionemos los casos donde o bien se haya cobrado aguinaldo o bien el salario total haya sido mayor que 240.000, pero no las dos cosas. 
# 

# In[34]:


df[(df['total_salario_bruto_i_+_ii'] > 240000) ^ (df['aguinaldo_ii'] > 0)]


# Ahora veamos los sueldos de febrero de la SECR Ciencia, Tecnologia e Innovacion.

# In[35]:


df[(df['mes'] == 2) & (df['reparticion'] == 'SECR Ciencia, Tecnologia e Innovacion')]


# ### Boolean indexing con query()
# 
# La sintaxis que se utiliza para hacer Boolean indexing es un poco repetitiva. Noten que filtrar (aún en su expresión más corta sin loc ni especificar filas o columnas) implica ESCRIBIR DOS VECES el nombre del dataset. Para crear un shortcut, Pandas ofrece la función .query() 
# 
# 

# In[36]:


df_cult = df.query('reparticion == "Ministerio de Cultura"')


# También se puede hacer query sobre múltiples condiciones.

# In[37]:


df2 = df.query('asignacion_por_cargo_i > 240000 & aguinaldo_ii > 0')


# In[38]:


df2.shape


# Ejercicio: Piensen cómo traducir a la sintaxis de query, estas consultas que ya hicimos:

# In[39]:


# df_sem2 = df[df['mes'] > 6]
# Solución
df_sem2 = df.query('mes > 6')


# In[40]:


# df[(df['mes'] == 2) & (df['reparticion'] == 'SECR Ciencia, Tecnologia e Innovacion')]
# Solución
df.query('(mes == 2) & (reparticion == "SECR Ciencia, Tecnologia e Innovacion")')


# ### Fancy Indexing
# 
# Ahora vamos a quedarnos con un subconjunto de columnas del DataFrame.

# In[41]:


df_view = df.loc[:,['anio','mes']]


# In[42]:


df_view.shape


# Existe una forma menos explícita de hacer esta misma operación. Si pasamos una lista al indexing, pandas asume que el tipo de indexing es loc y que el filtro es sobre las columnas y no las filas:

# In[43]:


df_view = df[['anio','mes']]


# In[44]:


df_view.shape


# Fíjense lo que pasa si tratamos de acceder a filas utilizando una lista de nombres, en este caso [0,1]. 

# In[45]:


# Incorrecto
df_view = df[[3,8]]


# Nos da un error porque cuando pasamos únicamente una lista al indexing, pandas asume que queremos un set de columnas y si los nombres no existen, da error. La forma correcta de hacerlo es pasar una lista de índices y explicitar que vamos a indizar con loc y que seleccionamos todas las columnas.

# In[67]:


# Correcto
df_view = df.loc[[3,8],:]


# In[68]:


df_view


# 

# Ejercicio. Volviendo al ejemplo del titanic...
# 
# 1) ¿Cuántos hombres y mujeres sobrevivieron? 
# 
# 2) ¿Cuántos menores de 18 años había? ¿Cuántos sobrevivieron?
# 
# 3) Seleccionen únicamente las columnas Sex y Survived y almacenenlas en un nuevo DataFrame que se llame df_titanic_subset.
# 

# In[69]:


df_titanic.query('Sex == "male" & Survived==1').shape


# In[70]:


df_titanic.query('Sex == "female" & Survived==1').shape


# In[71]:


df_titanic.query('Age <= 18').shape


# In[72]:


df_titanic.query('Age <= 18 & Survived==1').shape


# In[73]:


df_titanic_subset = df_titanic[['Sex','Survived']]


# In[74]:


df_titanic_subset.head()


# ## Funciones de Agregación
# 
# Utilizando Pandas podemos aplicar funciones a nivel de columna. Algunas funciones predefinidas son la media, el desvío estándar y la sumatoria, el valor máximo y el mínimo.
# 
# Algunas de las funciones de agregación más comunes son:
# 
# <ul>
#     <li>min</li>
#     <li>max</li>
#     <li>count</li>
#     <li>sum</li>
#     <li>prod</li>
#     <li>mean</li>
#     <li>median</li>
#     <li>mode</li>
#     <li>std</li>
#     <li>var</li>
# </ul>
# 
# 
# 

# In[75]:


df['mes'].max()


# In[76]:


df['asignacion_por_cargo_i'].mean()


# In[77]:


df['asignacion_por_cargo_i'].std()


# In[78]:


df['total_salario_bruto_i_+_ii'].sum()


# Podemos combinar los filtros que vimos antes con las funciones de agregación para responder preguntas cómo ¿Cuál fue en gasto en asignaciones de funcionarios para la Secretaría de Medios 2019? ¿Y para la de Justicia y Seguridad?

# In[79]:


df[df['reparticion'] == 'SECR de Medios']['total_salario_bruto_i_+_ii'].sum()


# In[80]:


df[df['reparticion'] == 'SECR Justicia y Seguridad']['total_salario_bruto_i_+_ii'].sum()


# Ahora respondamos algunas preguntas: ¿Quién o quiénes del dataset cobran el salario más alto? ¿Y el más bajo?

# In[81]:


df[df['total_salario_bruto_i_+_ii'] == df['total_salario_bruto_i_+_ii'].max()]


# In[82]:


df[df['total_salario_bruto_i_+_ii'] == df['total_salario_bruto_i_+_ii'].min()]


# # Otros análisis descriptivos
# 
# Pandas viene con algunas funciones built-in para ayudar al análisis descriptivo.
# 
# ## Para las variables numéricas

# In[83]:


df.describe()


# ## Para las variables categóricas
# 

# In[84]:


df['reparticion'].value_counts()


# ### Ejercicio: Volviendo al ejemplo del Titanic:
# 
# 1) ¿Cuál era la edad promedio de los pasajeros de cada clase (Pclass)?
# 
# 2) ¿Cuál fue la tarifa que pagaron en promedio los hombres? ¿Y las mujeres?
# 
# 3) ¿Cuánto pagaron en total los pasajeros de primera clase para subir al Titanic? ¿Y los de tercera?
# 
# 4) ¿Cuántos pasajeros había en cada tipo de clase?

# In[85]:


df_titanic.head()


# In[86]:


df_titanic.query('Pclass == 1')['Age'].mean()


# In[87]:


df_titanic.query('Pclass == 2')['Age'].mean()


# In[88]:


df_titanic.query('Pclass == 3')['Age'].mean()


# In[89]:


df_titanic.query('Sex == "male"')['Fare'].mean()


# In[90]:


df_titanic.query('Sex == "female"')['Fare'].mean()


# In[91]:


df_titanic.query('Pclass == 1')['Fare'].sum()


# In[92]:


df_titanic.query('Pclass == 3')['Fare'].sum()


# In[93]:


df_titanic['Pclass'].value_counts()


# ## Ordenar por columnas y limitar la cantidad de resultados

# Otra forma de resolver el problema de encontrar el mayor y el menos es con el método sort_values. Este método puede recibir un valor único (nombre de columna) o una lista (con varias columnas) y un orden asc o desc. Por default el orden es asc.
# 
# Si combinamos el ordenamiento con el método head() para limitar la cantidad de resultados, podemos encontrar los N primeros. 

# In[94]:


# Recordemos cómo abrir la documentación de un método
get_ipython().run_line_magic('pinfo', 'df.sort_values')


# In[95]:


# Calculamos el máximo
df.sort_values('total_salario_bruto_i_+_ii',ascending=False).head(1)


# In[96]:


# Calculamos el mínimo
df.sort_values('total_salario_bruto_i_+_ii').head(1)


# # Anexo: volviendo al tema de la vectorización
# 
# ¿Por qué es tan importante trabajar con Pandas y no con funciones escritas por nosotros en Python nativo y que procesen los datos dentro de un for loop?
# 
# Por un lado está la comodidad. Hay mucha funcionalidad que ya está desarrollada en Pandas. Existen funciones que resuelven muchos de los problemas clásicos de manipular datos: agrupar, sumarizar, sacar estadísticas, filtrar, etc. Pero además hay una razón de performance. 
# 
# Veamos una demostración de que vectorizar es más eficiente. Vamos a crear dos listas de 1.000.000 de números aleatorios cada una y vamos a tratar de multiplicar elemento por elemento con pandas y sin pandas:
# 
# 

# In[97]:


lista1 = list(np.random.randint(1, 100, 1000000))
lista2 = list(np.random.randint(1, 100, 1000000))


# In[98]:


get_ipython().run_cell_magic('timeit', '', 'for x,y in zip(lista1,lista2):\n    x * y')


# Ahora probemos hacer lo mismo con dos series de Pandas

# In[99]:


serie1 = pd.Series(lista1)
serie2 = pd.Series(lista2)


# In[100]:


get_ipython().run_cell_magic('timeit', '', 'resultado = serie1 * serie2')


# Conclusión: la operación vectorizada es <strong> más de 70 veces más rápida.</strong>

# In[ ]:




