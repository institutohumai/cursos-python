#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/4_Data_Wrangling_Avanzado/ejercicio/solucion_ejercicio.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# # Ejercicio: Informe macroeconómico de Argentina
# 
# La consultora "Nuevos Horizontes" quiere hacer un análisis del mercado argentino para entender como ha evolucionado en los últimos años. Van a analizar dos indicadores macroeconómicos principales: el **IPC: Índice de Precios al Consumidor** (para medir inflación) y el tipo de cambio (**cotización del dólar**).
# 
# ## IPC: Índice de Precios al Consumidor
# 
# Para más información sobre el IPC pueden visitar la siguiente página del INDEC: https://www.indec.gob.ar/indec/web/Nivel4-Tema-3-5-31
# 
# La base de IPC a analizar tiene como base diciembre de 2016, al cual le corresponde el índice 100. Los precios se encuentran con cuatro niveles de apertura: 
# 
# * General: Indice de Precios de toda la canasta de bienes y servicios considerada en el análisis
# 
# * Estacional: Bienes y servicios con comportamiento estacional. Por ejemplo: frutas y verduras
# 
# * Regulados: Bienes y servicios cuyos precios están sujetos a regulación o tienen alto componente impositivo. Por ejemplo: electricidad
# 
# * Núcleo: : Resto de los grupos del IPC
# 
# Su jefa quiere analizar el comportamiento de los cuatro niveles de apertura del indice de precios en los años que componen el dataset. Para eso le pide que obtenga el promedio, mediana e índice máximo anuales para cada nivel de apertura. Luego, de ser posible, graficar la evolución anual del índice medio a nivel general.
# 
# **Pasos sugeridos:**
# 
#     1) Leer los datos del IPC.
# 
#     2) Modificar la tabla para que cumpla con la definición de tidy data: cada variable debe ser una columna (Apertura, Fecha e Indice).
# 
#     3) Convertir la variable de fecha al formato date-time y extraer el año y el mes.
# 
#     *Ayuda*: Vas a tener que utilizar el argumento format en la función to_datetime de pandas. En esta página vas a poder encontrar los códigos de formato o directivas necesarios para convertir las fechas: https://docs.python.org/es/3/library/datetime.html#strftime-and-strptime-behavior
# 
#     4) Calcular el indice promedio, mediano y maximo por año para cada nivel de apertura.
# 
#     5) Graficar.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')

get_ipython().run_line_magic('matplotlib', 'inline')


# **1) Leer los datos del IPC.**

# In[2]:


ipc_df = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/ipc_indec.csv')


# In[3]:


ipc_df.head()


# **2) Modificar la tabla** para que cumpla con la definición de tidy data: cada variable debe ser una columna (Apertura, Fecha e Indice).

# In[4]:


tidy_ipc_df = pd.melt(ipc_df,
                      id_vars="Apertura",  # V
                      var_name="Fecha",
                      value_name="Indice")


# In[5]:


tidy_ipc_df.head()


# **3)** Convertir la **variable de fecha** al formato date-time y extraer el año y el mes
# 

# In[6]:


# Especificamos el formato de nuestra fecha
tidy_ipc_df["Fecha"] = pd.to_datetime(tidy_ipc_df["Fecha"], format="%b-%y")


# In[7]:


tidy_ipc_df.head()


# Creamos el índice temporal a partir de la fecha y extraemos el año y mes. 
# *(Esta operación se puede realizar también sin necesidad de crear el índice temporal)*

# In[8]:


# Creamos el índice temporal
tidy_ipc_df = tidy_ipc_df.set_index("Fecha")

# Extraemos año y mes
tidy_ipc_df['Año'] = tidy_ipc_df.index.year
tidy_ipc_df['Mes'] = tidy_ipc_df.index.month


# In[9]:


tidy_ipc_df.head()


# **4)** Calcular el **indice promedio, mediano y maximo** por año para cada nivel de apertura.

# In[10]:


tidy_ipc_df.groupby(["Apertura", "Año"]).agg(
    {"Indice": ['mean', 'median', 'max']})


# **5) Graficar**

# In[11]:


# Mensual
tidy_ipc_df[tidy_ipc_df.Apertura == 'Nivel general'].Indice.plot(style='-o', linewidth=2, ms=4)


# # Dolar
# La base de cotización de dolar traer los precios de compra y venta oficiales de la divisa en Argentina desde el 01-06-2015 hasta el 03-08-2020 según el portal Ámbito Financiero.
# 
# Para proseguir con el informe se quiere obtener la cotización media diaria (promedio entre compra y venta) y obtener la mediana mensual con su respectivo gráfico. Adicionalmente, se quiere encontrar el top 5 de los días con mayores aumentos porcentuales en el tipo de cambio para la misma ventana de tiempo que se analizó el IPC (desde 01-12-2016 hasta el 30-06-2020)
# 
# **Pasos sugeridos:**
# 
#     1) Leer los datos de la cotización del dolar
# 
#     2) Crear una variable que compute el valor promedio entre compra y venta por día
# 
#     3) Convertir la fecha de un dato tipo string a un objeto datetime (to_datetime). Construir las variables de año y mes. 
# 
#     4) Calcular el promedio mensual y graficar (recordar ordenar en forma ascendente la fecha)
# 
#     5) Ordenar de manera ascendente por fecha, filtrar las fechas señaladas y calcular la variación porcentual diaria en la cotización
# 
#     6) Hallar los 5 días con mayor variación en la cotización.

# **1)** Leer los datos de la cotización del dolar

# In[12]:


dolar_df = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/dolar_oficial_ambito.csv')


# In[13]:


dolar_df.head()


# **2)** Crear una variable que compute el valor **promedio** entre compra y venta por día

# In[14]:


dolar_df["Promedio"] = dolar_df.loc[:, ['compra', 'venta']].mean(axis=1)


# In[15]:


dolar_df.head()


# **3)** Convertir la **fecha** de un dato tipo string a un objeto datetime (to_datetime) y construir las variables de año y mes

# In[16]:


dolar_df['fecha'] = pd.to_datetime(dolar_df['fecha'], dayfirst=True)


# In[17]:


dolar_df.head()


# In[18]:


dolar_df['Año'] = dolar_df.fecha.dt.year
dolar_df['Mes'] = dolar_df.fecha.dt.month


# In[19]:


dolar_df.head()


# **4)** Calcular el promedio mensual y graficar.

# In[20]:


dolar_mensual = dolar_df.groupby(["Año", "Mes"])                        .agg({'Promedio': 'median'})                        .reset_index()


# In[21]:


dolar_mensual.head()


# In[22]:


dolar_mensual.Promedio.plot(style='-o', linewidth=2, ms=4)


# **5)** Ordenar de manera ascendente por fecha, filtrar las fechas señaladas y calcular la variación porcentual diaria en la cotización
# 
# Para calcular la variación porcentual debemos realizar la siguiente cuenta:
# 
# $VariacionPorcentual = \frac{CotizacionHoy - CotizacionAyer}{CotizacionAyer}*100$

# Filtramos entre las fechas indicadas

# In[23]:


dolar_df_filtrado = dolar_df[dolar_df["fecha"].between("2016-12-01","2020-06-30")]


# Ordenamos por fecha de manera ascendente

# In[24]:


dolar_df_filtrado = dolar_df_filtrado.sort_values('fecha')


# Calculamos la diferencia entre la cotización del día de hoy y la del día de ayer

# In[25]:


dolar_df_filtrado['Diferencia_diaria'] = dolar_df_filtrado['Promedio'].diff(periods=1)


# Creamos la variable de la cotización del día anterior

# In[26]:


dolar_df_filtrado['Valor_anterior'] = dolar_df_filtrado['Promedio'].shift(periods=1)


# Calculamos la variación diaria en la cotización del dólar

# In[27]:


dolar_df_filtrado['Variacion_diaria'] = round(
    dolar_df_filtrado['Diferencia_diaria'] / dolar_df_filtrado['Valor_anterior']*100, 2)
# Reemplazamos el valor NA del primer día de la serie con 0
dolar_df_filtrado = dolar_df_filtrado.fillna(0)


# In[28]:


dolar_df_filtrado.head()


# **6)** Hallar los 5 días con mayor variación en la cotización.

# In[29]:


dolar_df_filtrado.sort_values("Variacion_diaria", ascending=False).head(5)


# In[30]:


# Forma alternativa
dolar_df_filtrado.nlargest(5, 'Variacion_diaria')

