#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/APIs/2_APIs_Series_Tiempo/ejercicios/ejercicios.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# # APIs Series de Tiempo: Ejercicios

# In[1]:


import pandas as pd


# ## Ejercicio 1: API de Series de Tiempo de Argentina 

# * Genera una tabla y grafica la evolucion de los tipos de cambio ARS/USD de todas las entidades financieras (canal electronico, venta, 15hs).

# In[ ]:





# * Genera un reporte automatico en HTML que diga las ultimas temperaturas diarias y el promedio de los ultimos 30 dias, para 3 ciudades de Argentina

# In[ ]:





# * Grafica la relacion entre el nivel de precios (nucleo) y la base monetaria. Podes buscar la base monetaria en [este dataset](https://datos.gob.ar/dataset/sspm-factores-explicacion-base-monetaria/archivo/sspm_331.2) bajo el nombre de "Saldo de la base monetaria" y la serie de nivel de precios [es esta](https://datos.gob.ar/series/api/series/?ids=148.3_INUCLEONAL_DICI_M_19). Algunos scatter a probar:
#     - IPC vs. base monetaria
#     - IPC promedio 6 meses vs. base monetaria promedio 6 meses (Pista: usa rolling() y mean()).
#     - IPC promedio 6 meses (variacion porcentual) vs. base monetaria promedio 6 meses (variacion porcentual) (Pista: agregale pct_change(1) al anterior).
#     - IPC promedio 6 meses (variacion porcentual) vs. base monetaria promedio 6 meses (variacion porcentual) de hace 3 meses -rezago de 3 meses- (Pista: agregale shift(3) a una de las variables).
#     
# Que otras variables se podrian incorporar para explicar o controlar esta relacion? Nivel de actividad? Tipo de cambio? Tasa de interes?

# In[ ]:





# ## Ejercicio 2: API de Quandl

# * Grafica las tasas de interes de los bonos de Estados Unidos, a partir del dataset de FRED disponible en Quandl (Pista: podes arrancar a buscar por aca: https://www.quandl.com/data/FRED-Federal-Reserve-Economic-Data?keyword=10%20years%20treasury)

# In[ ]:





# ## Ejercicio 3: API de Banco Mundial

# * Grafica la evolucion de las emisiones per capita de CO2 para por lo menos 8 paises paises de Sudamérica desde 1960 (o el primer año con datos).

# In[ ]:




