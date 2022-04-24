#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/4_Data_Wrangling_Avanzado/ejercicio/ejercicio.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# # Ejercicio Pandas IV: Informe macroeconómico de Argentina
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

# In[ ]:


ipc_df = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/ipc_indec.csv')


# **2) Modificar la tabla** para que cumpla con la definición de tidy data: cada variable debe ser una columna (Apertura, Fecha e Indice).

# In[ ]:





# **3)** Convertir la **variable de fecha** al formato date-time y extraer el año y el mes
# 

# In[ ]:





# **4)** Calcular el **indice promedio, mediano y maximo** por año para cada nivel de apertura.

# In[ ]:





# **5) Graficar**

# In[ ]:





# ### Dolar
# 
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

# In[ ]:


dolar_df = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/dolar_oficial_ambito.csv')


# **2)** Crear una variable que compute el valor **promedio** entre compra y venta por día

# In[ ]:





# **3)** Convertir la **fecha** de un dato tipo string a un objeto datetime (to_datetime) y construir las variables de año y mes

# In[ ]:





# **4)** Calcular el promedio mensual y graficar.

# In[ ]:





# **5)** Ordenar de manera ascendente por fecha, filtrar las fechas señaladas y calcular la variación porcentual diaria en la cotización
# 
# Para calcular la variación porcentual debemos realizar la siguiente cuenta:
# 
# $VariacionPorcentual = \frac{CotizacionHoy - CotizacionAyer}{CotizacionAyer}*100$

# In[ ]:





# **6)** Hallar los 5 días con mayor variación en la cotización.

# In[ ]:




