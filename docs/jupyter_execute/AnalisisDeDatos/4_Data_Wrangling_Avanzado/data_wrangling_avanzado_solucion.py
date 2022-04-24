#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/4_Data_Wrangling_Avanzado/data_wrangling_avanzado_solucion.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# # Data Wrangling Avanzado
# 

# ## Tabla de Contenidos
# 
# I. Data Wrangling Avanzado
# 
#     I. Tabla de Contenidos
# 
# II. Table of Contents
# 
#     I. Introducción
#     II. Pandas y Cadenas de caracteres
#         I. count
#         II. Ejercicio
#         III. contains
#         IV. lower, upper y title
#         V. split
# 
# III. ¿Cómo organizar la información? OLAP, OLTP y Tidy data
# 
#     I. OLTP y OLAP
#     II. Tidy data
#         I. Tuberculosis
#             I. Tabla 1
#             II. Tablas 2.a y 2.b
#             III. Tabla 3
#             IV. Tabla 4
#             V. Tabla 5
#     III. Melt
#         I. Ejercicios
#         II. Ejercicios
# 
# IV. Series de Tiempo
# 
#     I. Datetime y metodos de manipulacion de series de tiempo
#     II. Ventanas y Medias moviles
#     III. Shift y Diff

# ## Introducción
# 
# En esta clase vamos a ver cómo hacer manejo avanzado de datos a partir, tanto en cadenas de caracteres como en series de tiempo. El primer dataset que vamos a utilizar es del portal de datos abiertos de España.

# In[1]:


# !pip install seaborn
# !pip install numpy==1.18.5


# In[2]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/parodesprov.csv')


# In[4]:


df.head()


# Generalmente cuando en un dataset encontramos campos de texto es recomendable analizar si la carga se hizo con un buen criterio y no hay errores en la carga. Vamos a prestar atención a los campos Texto y PAD_1_COD_PROV.

# In[5]:


df["Texto"].head()


# Noten que el primer valor incluye un "-" como separador

# Vamos a comenzar eliminando las filas que tienen null el campo Texto, para facilitar el análisis posterior.

# In[6]:


df = df[~df["Texto"].isnull()]


# ## Pandas y Cadenas de caracteres
# 
# Cuando una pd.Series es de tipo object Pandas permite acceder a métodos para operar sobre strings llamando al método **.str**.

# ### count
# 
# El método **.str.count()** permite contar cuántas ocurrencias de un patrón hay en una Series. Para ello se puede pasar una regex. Las regex o expresiones regulares son una cadena de caracteres que define una búsqueda de un patrón. En esta clase no vamos a ahondar en regex pero sí podemos mencionar que:
# - Si pasamos un carácter en particular nos va a matchear cuántas veces aparece.
# - El carácter . funcion como comodín, con lo cual cualquier caracter va a matchear.

# Entonces, si queremos saber cuántas veces aparece el símbolo "-" en cada término podemos hacer:

# In[7]:


df["Texto"].str.count("-").head()


# Ahora, nos llama la atención que el símbolo "-" aparece en la primera fila, ¿será algo común?

# In[8]:


df["Texto"].str.count("-").value_counts()


# ### Ejercicio
# 
# 1- Ver los casos que tiene 2 "-" en el nombre.

# In[9]:


df["Texto"][df["Texto"].str.count("-") == 2]


# 2- Graficar un histograma con la cantidad de caracteres en la columna Texto usando contains. Tip: pueden usar el método .hist.

# In[10]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[11]:


df["Texto"].str.count(".").hist(bins=20)


# 3- Mostrar que el resultado obtenido en el ejercicio anterior equivale a aplicar **.str.len()**. Para ello usen el método **pd.Series.equals()** y comparen el método usado en el ejercicio anterior con aplicar .str.len()

# In[12]:


df["Texto"].str.count(".").equals(df["Texto"].str.len())


# ### contains

# Digamos que queremos encontrar nombres de ciudades vascas. Para ello sabemos que "herri" en Euskera significa lugar, con lo que esperamos encontrar "erri" en una gran cantidad de ciudades. Vamos a filtrar trayendo solamente las ciudades que incluyen "erri" dentro de su nombre con el método **.str.contains**.

# In[13]:


df[df["Texto"].str.contains("erri",case=False)].head() # case es para considerar mayúsculas y minúsculas o no


# In[14]:


df[df["Texto"].str.contains("erri",case=False)].shape 


# ### lower, upper y title

# Supongamos que queremos estar seguros que las nombres están estandarizados... podemos elegir pasar todo a minúscula o a mayúscula de la siguiente manera:

# In[15]:


df["Texto"].str.lower().head()


# In[16]:


df["Texto"].str.upper().head()


# También podemos aplicar mayúscula a la primera letra y al resto minúscula, con **.str.title**. Este método toma en consideración espacios o símbolos no alfabéticos. Es decir, va a comenzar con mayúscula los términos después de un espacio, "-" o "/". Por ejemplo

# In[17]:


df["Texto"][df["Texto"].str.count("-") == 2].str.title()


# ### split

# En el ejemplo anterior encontramos el uso de "/". En este caso se refiere a que el nombre de la ciudad (Oroz-Betelu/Orotz-Betelu) tiene dos nombres oficiales, uno en español y otro en vasco.
# 
# Supongamos que queremos estandarizar el problema y quedarnos sólo con el nombre que aparece primero, ¿cómo podemos hacerlo?

# Primero veamos algunos ejemplos otros ejemplos de nombres con "/":

# In[18]:


df["Texto"][df["Texto"].str.count("/") > 0].unique()[:10]


# Nota: en un primer momento uno podría pensar que en este dataset el primer elemento debería ser siempre el nombre en, por ejemplo, español y el segundo en vasco... Sin embargo, no es así :-S
# 
# Vamos a usar **.str.split()**, vale la pena mencionar que el método devuelve una lista con un elemento por cada separación que pudo realizar. Para ello recibe como parámetro un string que es un patrón que va a usar, justamente, para dividir la cadena de caracteres. Comúnmente sólo vamos a pasarle un elemento por el cual splitear.

# In[19]:


df["Texto"].str.split() # por default split separa por espacios en blanco


# Noten en el ejemplo anterior que si devuelve una lista con un solo elemento es que no matcheó y, por lo tanto, no dividió el string.

# Yendo a nuestro problema, separamos por el caracter '/'. Notar como se transforman los nombres compuestos
# MUCHO CUIDADO! Nuestros strings ahora son listas!! :o

# In[20]:


df["Texto"].str.split("/").head()


# Entonces, nos quedamos con la primera versión del nombre al separar por "/"

# In[21]:


texto_para_split = df["Texto"][df["Texto"].str.count("/") > 0] # guardo en una variable casos con /

texto_para_split.str.split("/").apply(lambda x: x[0]) # para indexar las listas tengo que usar apply


# Por otra parte, si quisiéramos guardar cada nombre en una columna separada podemos hacerlo usando la opción expand:

# In[22]:


texto_para_split.str.split("/", expand=True)


# Podemos asignar el resultado de expand de la siguiente manera:

# In[23]:


df[["nombre_1", "nombre_2"]] = df["Texto"].str.split("/", expand=True) # usamos el df original y expandimos


# In[24]:


df[["nombre_1", "nombre_2"]].head() # vemos que hay nulls que nombre_2 porque tienen un solo nombre


# In[25]:


df.loc[~df["nombre_2"].isnull(), ["nombre_1", "nombre_2"]].head() # noten el filtro booleano


# # ¿Cómo organizar la información? OLAP, OLTP y Tidy data
# 
# Existen diversas formas de organizar la información. En general, qué vamos a hacer con la información es clave para entender cómo organizarla. Veamos algunos conceptos habituales a la hora de trabajar con datos.

# ## OLTP y OLAP

# La sigla OLTP viene de Online transaction processing y se refiere a transacciones que ocurren en tiempo real. Un ejemplo típico son los ATMs (automated teller machine), más conocidos como "cajeros automáticos". 
# 
# En este aspecto transacción tiene dos acepciones y ambas son válidas: por un lado, se procesan transacciones en término de bases de datos (que vamos a ver a continuación), por otro lado, se suele aplicar a transacciones económicas en donde se intercambian entidades económicas. 
# 
# Sistemas OLTP son la mayoría de los sistemas tradicionales que conocemos, especialmente los sistemas bancarios. Estos son sistemas transaccionales (en la primera acepción de arriba) porque intentan cumplir 4 objetivos (**ACID**):
# 
# - Las transacciones son operaciones **atómicas**: se hacen por completo o no se hacen. Imagínense una transferencia bancaria, ésto requiere debitar en una cuenta y acreditar en otra. Si la operación no fuera atómica y fallara podríamos quedarnos en un estado inesperado en el cual se debite de la primera y no se acredite en la segunda. Para evitar ésto, la atomicidad garantiza que si la operación falla en alguna parte del proceso revertimos completamos la operación y no impactamos ningún cambio (hacemos *rollback*).
# 
# - Toda transacción debe mantener la **consistencia** de la base de datos, es decir, debe respetar una serie de restricciones. Por ejemplo, podemos pensar que para que una tarjeta de crédito sea de extensión de una cuenta esa cuenta debe existir previamente. Otro ejemplo, puede ser que no pueden existir dos cuentas bancarias diferentes con el mismo número.
# 
# - Además, los sistemas transaccionales (especialmente los sistemas OLTP) requieren garantizar el **aislamiento** de las operaciones. Es común que estos sistemas necesiten resolver miles de operaciones concurrentes (es decir, que suceden en simultáneo), el aislamiento consiste en que esas operaciones dejen en la base de datos el mismo estado que si las operaciones fueran secuenciales (es decir, una por vez). Incluso, si una de esas falla, no debería alterar el resultado.
# 
# 
# Para ésto, se implementan diferentes algoritmos a fin de asegurar que no se generen errores ni competencias entre usuarios que estan intentando acceder a los mismos registros a la vez.

# OLAP (Online Analytical Processing) por otra parte se refiere a todos los sistemas utilizados para analisis y reportes de negocios (Business Intelligence), en los cuales se realizan diferentes operaciones de agregacion sobre los datos, a fin de proveer a los usuarios con informacion relevante. 
# 
# Las herramientas OLAP permiten realizar análisis multidimensionales, tomando en consideración distintas dimensiones y métricas. En este sentido, está lo que se conoce como "cubo OLAP". El cubo OLAP es un array multidimensional que permite analizar la información vista desde distintos ángulos. Por ejemplo, podemos querer ver un reporte financiero por producto, por ciudad, por tiempo, etc. Cada uno de estos términos es una dimensión del análisis.
# 
# Estos sistemas generalmente requieren procesos de carga y transformaciones masivas que pueden durar horas o días, y permiten presentan la información de un modo tal que el análisis es en tiempo real, no así la información que usa. 

# ## Tidy data

# **Tidy data** es un trabajo escrito por Hadley Wickham (de la empresa RStudio) que se ha difundido mucho, especialmente en la comunidad de R, sobre buenas prácticas a la hora de estructurar información tabular. Pueden consultar el trabajo acá: https://vita.had.co.nz/papers/tidy-data.pdf
# 
# La información tabular consta de **filas** y **columnas**. Las columnas siempre tienen una etiqueta y las filas sólo a veces.
# 
# Los *datasets* constan de **valores**, éstos pueden ser numéricos o no numéricos . En el caso en que sea un valor numérico representa una cantidad, si no es numérico es una cualidad. Además, los valores miden o caracterizan un determinado atributo (altura, peso, temperatura, etc.). Este atributo se conoce como **variable**. Por último, esa variable se corresponde con una determinada unidad observada. Generalmente llamamos a eso simplemente **observación** (por ejemplo, la persona a la que se le midió la altura).
# 
# Dicho ésto, Wickham define un dataset *tidy* u ordenado como aquel que cumple la tercera forma normal de bases de datos, pero con un lenguaje más cercano al campo del análisis de datos y pensando en información contenida en una tabla, y no en una base de datos con muchas tablas. Las condiciones son:
# 
# - Cada variable forma una columna.
# - Cada observación forma una fila.
# - Cada tipo de unidad observacional forma una tabla.
# 
# Además, describe 5 de los errores más comunes a la hora de ordenar la información:
# 
# - Los nombres de columna en vez de ser nombres de variables son valores
# - Muchas variables se guardan en una sola columna.
# - Las variables se guardan tanto en columnas como en filas.
# - Distintos tipos de unidades observacionales se guardan en una misma tabla.
# - Una única unidad observacional se almacena en distintas tablas.4

# ### Tuberculosis
# 
# A continuación vamos a ver un dataset de tuberculosis representado de distintas maneras... 

# #### Tabla 1
# 
# En esta primera representación de la información vemos que una misma columna (type) contiene dos variables (cases y population)

# |country|year|type|count|
# | --- | --- | --- | --- |
# |Afghanistan|1999|cases|745|
# |Afghanistan|1999|population|19987071|
# |Afghanistan|2000|cases|2666|
# |Afghanistan|2000|population|20595360|
# |Brazil|1999|cases|37737|
# |Brazil|1999|population|172006362|

# #### Tablas 2.a y 2.b
# En este caso separamos la tabla en dos tablas. Una donde vemosla población y otra donde vemos la cantidad de casos... ¿Cuál es el problema acá?
# 
# Si bien ésto puede parecer correcto noten que la unidad observacional en realidad es un país en un año determinado... Con lo cual, lo que estamos haciendo acá es tener la misma unidad observacional en dos tablas. Además, los valores de la variable year están como nombres de columnas...

# 
# |country|1999|2000|
# | --- | --- | --- |
# |Afghanistan|745|2666|
# |Brazil|37737|80488|
# |China|212258|213766|

# |country|1999|2000|
# | --- | --- | --- |
# |Afghanistan|19987071|20595360|
# |Brazil|172006362|174504898|
# |China|1272915272|1280428583|

# #### Tabla 3
# 
# En este caso, perdimos las variables cases y population y calculamos un ratio. Si bien ésto cumple con ser "ordenado" estamos perdiendo las variables originales.

# |country|year|rate|
# | --- | --- | --- |
# |Afghanistan|1999|745/19987071|
# |Afghanistan|2000|2666/20595360|
# |Brazil|1999|37737/172006362|
# |Brazil|2000|80488/174504898|
# |China|1999|212258/1272915272|
# |China|2000|213766/1280428583|

# #### Tabla 4
#  
# En la tabla 4 vemos que la variable *year*, *cases* y *population* se juntaron, con lo cual los valores de *year* pasan a formar parte de los nombres de las columnas.

# |country|cases_1999|cases_2000|population_1999|population_2000|
# | --- | --- | --- | --- | --- |
# |Afghanistan|745|19987071|2666|20595360|
# |Brazil|37737|172006362|80488|174504898|
# |China|212258|1272915272|213766|1280428583|

# #### Tabla 5
# 
# Finalmente, la tabla *tidy* es:

# |country|year|cases|population|
# | --- | --- | --- | --- |
# |Afghanistan|1999|745|19987071|
# |Afghanistan|2000|2666|20595360|
# |Brazil|1999|37737|172006362|
# |Brazil|2000|80488|174504898|
# |China|1999|212258|1272915272|
# |China|2000|213766|1280428583|

# ## Melt
# 
# Una de los métodos más útiles de Pandas para pasar de un formato *wide* o *ancho* como el de la tabla 4 a uno *largo* como el de la tabla 5 es **.melt**.
# 
# Para aplicar este método vamos a obtener un dataset de Billboard sobre las canciones mas escuchadas del 2000.
# 
# Vamos a agregar la opcion de encoding para solucionar un problema con los caracteres usados.

# In[26]:


billboard = pd.read_csv('https://raw.githubusercontent.com/hadley/tidy-data/master/data/billboard.csv', warn_bad_lines=False, error_bad_lines=False, encoding='iso-8859-1')


# ### Ejercicios

# 1- Analicen el dataset, vean cuáles son las variables, qué es la observación. ¿Es necesario separarlo en dos tablas? Nota: lo que se está midiendo en las columnas x1st.week a x76th.week es la posición en el ranking de las 100 canciones más escuchadas en esa semana. Es decir, x1st.week es la posición en el ranking durante la primera semana que esa canción fue top 100.

# No es necesario separarlo en dos tablas porque el tipo de unidad observacional es el mismo, siempre es una canción en una semana determinada desde que entró al ranking top 100.

# 2- ¿Por qué creen que hay tantas columnas con valores nulos?

# Porque las canciones pueden salir del ranking top 100 antes de la semana 76.

# 3- ¿Cómo podríamos hacer este dataset más ordenado? (no miren la continuación de la notebook :-S)

# Creando una columna semana que indique el número de semana y una columna ranking que nos diga la posición en el ranking en esa semana.

# Veamos primero como luce el dataset

# In[27]:


billboard.head()


# Lo que querríamos es poder mantener todas las columnas excepto las columnas que incluyen "week" en el nombre. Para poder tener un formato "tidy" u "ordenado" deberíamos tener, por un lado, una columna week que indique el número de la semana (y preferentemente que sea un entero), y por otro lado una columna ranking con el valor del ranking en esa semana. 
# 
# Para lograr ésto, vamos a usar la función **.melt**. Esta función recibe el DataFrame y vamos a usar el parámetro id_vars para pasarle la lista de columnas que van a ser constantes, es decir, que no van a variar. Con las demás columnas .melt va a:
# 
# 1- tomar los nombres de columnas no incluídas en id_vars y convertirlos en una columna
# 
# 2- va a tomar los valores de esas columnas y convertirlos en una segunda columna.

# In[123]:


pd.melt(billboard,
        id_vars=["year", "artist.inverted", "track", "time", "genre", "date.entered", "date.peaked"]).head()


# Ahora, querríamos que variable se llame week y value se llame ranking, para eso hacemos...

# In[148]:


billboard_2 = pd.melt(billboard, 
                      id_vars=["year", "artist.inverted", "track", "time", "genre", "date.entered", "date.peaked"], 
                      var_name="week", 
                      value_name="ranking")


# In[149]:


billboard_2.head()


# ### Ejercicios

# 1- Quédense sólo con la parte numérica de week sin usar regex, y conviertan a número los valores de la columna.

# In[150]:


billboard_2["week"] = billboard_2["week"].str[1:-7].astype(int)


# 2- Conviertan los valores de la columna ranking a entero. Tip: prueben usar pd.isna() para saber si un valor es nulo o no.

# In[153]:


billboard_2["ranking"] = billboard_2["ranking"].apply(lambda x: int(x) if not pd.isna(x) else x)


# 3- Vean cuántas filas totales hay y eliminen las filas con nulos, ahora vuelvan a ver cuántas filas quedan.

# In[156]:


billboard_2.shape


# In[157]:


billboard_2 = billboard_2.dropna()


# In[158]:


billboard_2.shape


# # Series de Tiempo

# Las series de tiempo representan uno de los problemas mas interesantes en la ciencia de datos ya que refiere a eventos continuos y ordenados los cuales pueden ser independientes o tener alguna correlacion entre si. En este modulo veremos los metodos mas utilizados para manipular series de tiempo en pandas

# ## Datetime y metodos de manipulacion de series de tiempo
# 
# Para esta seccion vamos a utilizar el dataset de consumo energetico de Alemania.

# In[92]:


df_energia = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')


# Primeramente vamos a evaluar el dataset

# In[93]:


df_energia.columns = ['Fecha', 'Consumo', 'Eolica', 'Solar', 'Suma']
df_energia.tail(10)


# Las columnas son las siguientes:
#     - Date — La fecha (yyyy-mm-dd)
#     - Consumo — Electricidad Consumida en GWh
#     - Eolica — Produccion de energia eolica en GWh
#     - Solar — Produccion de energia solar en GWh
#     - Suma — Suma de las dos anteriores GWh

# Antes de comenzar a explorar el dataset, veamos algunas funciones de pandas para crear fechas. El metodo to_datetime nos permite transformar un string en cierto formato a un objeto del tipo Timestamp, el cual consiste de una fecha y una hora. Podemos ver que acepta varios formatos

# In[94]:


pd.to_datetime('2018-01-15 3:45pm')


# In[95]:


pd.to_datetime('7/8/1952')


# Vamos a convertir el dtype de nuestra columna Fecha de object a  datetime64

# In[96]:


df_energia.info()


# In[97]:


df_energia["Fecha"] = pd.to_datetime(df_energia["Fecha"])


# In[98]:


df_energia.info()


# Convertir la columna *Fecha* en datetime nos permite filtrar usando la información temporal...

# In[99]:


df_energia.head()


# Podemos traernos los casos posteriores a 2009, por default a partir del 1ero de enero...

# In[100]:


df_energia[df_energia["Fecha"] > "2009"].head()


# Con el método **.between** podemos filtrar por un rango de fechas... 

# In[101]:


df_energia[df_energia["Fecha"].between("2008", "2010")].head()


# En vez de filtrar usando años podemos pasar la fecha completa (siempre tengan presente el formato de la fecha)...

# In[102]:


df_energia[df_energia["Fecha"].between("2008-01-01", "2010-01-22")].head()


# Y como si fuera poco también podemos filtrar sólo usando el año y el mes, sin especificar el día...

# In[103]:


df_energia[df_energia["Fecha"].between("2008-01", "2010-02")].head()


# In[104]:


df_energia[df_energia["Fecha"].between("2008-01", "2010-02")].tail()


# Ahora, vamos a convertir nuestra columna Fecha en un índice temporal... Esto va a crear un nuevo tipo de objeto llamado DatetimeIndex

# In[105]:


df_energia = df_energia.set_index("Fecha")


# In[106]:


df_energia.tail(10)


# In[107]:


df_energia.index


# Primeramente vamos a agregar columnas que nos proporcionen mas informacion sobre las fechas

# In[108]:


df_energia['Anio'] = df_energia.index.year
df_energia['Mes'] = df_energia.index.month
df_energia['Dia'] = df_energia.index.day_name()
df_energia.sample(5, random_state=0)


# Como creamos el indice por las fechas, podemos localizar cualquier dia que querramos ahora

# In[109]:


df_energia.loc['2017-08-10']


# Incluso podemos buscar rangos de fechas

# In[110]:


df_energia.loc['2014-01-20':'2014-01-22']


# O buscar por algun mes en particular

# In[111]:


df_energia.loc['2016-05']


# Ahora veamos como se ve nuestra data de consumo de energia

# In[112]:


#! pip install seaborn
import matplotlib.pyplot as plt
import seaborn as sns
df_energia['Consumo'].plot(linewidth=0.5);


# ## Ventanas y Medias moviles
# 
# Las ventanas moviles se refiere a aplicar alguna operacion de agregacion, por ejemplo el promedio sobre un conjunto de datos ordenados a la vez, por ejemplo el promedio de los ultimos 6 dias sobre cada conjunto ordenado de 6 dias en el dataset. Veamos un ejemplo para entenderlo mejor

# In[113]:


opsd_7d = df_energia["Consumo"].rolling(6).mean()
opsd_7d.head(10)


# Podemos observar como las primeras 5 mediciones son Nan, ya que utiliza los primeros 5 valores para calcular a partir del 6to dia la media. El valor en el 7mo dia va a ser calculado con los datos del 2do al 6to dia, y asi sucesivamente.

# Este tipo de metodos son particularmente utiles en analisis financiero.

# ## Shift y Diff
# 
# La operacion de Shift, como su nombre lo dice traducido al castellano, desplazar los datos una cantidad N de periodos. Veamoslo con el ejemplo del consumo, suponiendo que quiero crear otra columna con el consumo total del periodo anterior para poder compararlo con el actual

# In[114]:


df_energia['ConsumoAyer'] = df_energia['Suma'].shift(periods=1)


# Veamos como quedo ahora el dataset

# In[115]:


df_energia.tail(10)


# Podemos observar como la columna 'ConsumoAyer' es el valor de la columna 'Suma' exactamente del periodo anterior. Esto se puede realizar con tantos periodos como uno desee, pero hay que tener cuidado porque al inicio de nuestro dataset van a quedar valores Nan por la cantidad de periodos que elijamos. Hay que evaluar con que valor completamos esos valores.

# Por ultimo supongamos que deseamos hacer la diferencia fila a fila del valor de ayer con el valor de hoy para el consumo total. Aqui nos conviene utilizar el metodo diff.

# In[116]:


df_energia['Diferencia'] = df_energia['Suma'].diff(1)


# In[117]:


df_energia.tail(10)

