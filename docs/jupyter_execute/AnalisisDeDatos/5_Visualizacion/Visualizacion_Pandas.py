#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/5_Visualizacion/Visualizacion_Pandas.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# # Visualización con Pandas y Matplotlib
# 
# Recorrido por las visualizaciones la libreria [Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html).
# 
# 
# Empezamos, importamos las librerias a utilizar.

# In[ ]:


import wbdata
import pandas as pd
import matplotlib.pyplot as plt
import datetime
get_ipython().run_line_magic('matplotlib', 'inline')


# ## World Bank Data API
# 
# Vemos el principal funcionamiento de la API.
# 
# Recorremos la (fuente?) de datos

# In[ ]:


wbdata.get_source()  


# Seleccionamos algunos datos de educacion. [Barro-Lee dataset](http://www.barrolee.com/)

# In[ ]:


wbdata.get_indicator(source=12)  


# ## Graficando con Pandas

# ### Grafico de torta

# In[ ]:


wbdata.get_indicator(source=14)


# In[ ]:


indicadores = {'HD.HCI.LAYS.FE':'educacion_femenina','HD.HCI.LAYS.MA':'educacion_masculina'}

data = wbdata.get_dataframe(indicadores, country=['USA','ARG'])

df = pd.DataFrame(data=data)


# In[ ]:


df.head()


# Hacemos un gráfico de tortas para comparar la educación por género entre Argentina y Estado Unidos de manera relativa.

# In[ ]:


ax1, ax2 = df.plot.pie(subplots=True,figsize=(8,4), colors=['yellow', 'skyblue'],
                      autopct='%.2f')

ax1.set_title('Educación femenina USA vs ARG', color='skyblue')
ax2.set_title('Educación masculina USA vs ARG', color='skyblue')


# ### Serie de tiempo
# 
# Vemos la educacion en la poblacion a lo largo de los años 

# In[ ]:


date_time = datetime.datetime(1950,1,1), datetime.datetime(2010,1,1)


# Porcentaje de no educacion en la población
indicadores = {'BAR.NOED.1519.ZS':'15-19','BAR.NOED.2024.ZS':'20-24', 
              'BAR.NOED.2529.ZS':'25-29', 'BAR.NOED.3034.ZS':'30-34',
              'BAR.NOED.3539.ZS':'35-39' , 'BAR.NOED.4044.ZS':'40-44',
              'BAR.NOED.4549.ZS':'45-49', 'BAR.NOED.5054.ZS':'50-54',
              'BAR.NOED.5559.ZS':'55-59'}

data = wbdata.get_dataframe(indicadores, country = 'ARG', data_date = date_time)
df = pd.DataFrame(data=data)


# In[ ]:


print('Valores nulos:',sum(df.isna().sum()))


# El dataset contiene va desde el año 1950 a 2010 y con ddatos cada cinco años. Como vamos a enfocarnos en la visualizacion dejamos los datos nulos de lado. 

# In[ ]:


df.dropna(inplace=True)
df


# Breve resumen descriptivo

# In[ ]:


df.describe()


# Graficamos el porcentaje de la poblacion no educado de toda la población para distintas categorías de edades.

# In[ ]:


df.iloc[8,].plot(style = '-.', label = '1970', legend=True)
df.iloc[5,].plot(style = ('--'), label = '1990', legend = True)
df.iloc[1,].plot(style = '-', label = '2010', legend = True)
plt.title('Porcentaje de no educación')
plt.ylabel('Porcentaje',color = 'grey')
plt.xlabel('Edad', color = 'grey')
plt.xticks([0,1,2,3,4,5,6,7,8],df.columns.tolist())


# Esta vez lo hacemos sólo para la población femenina.

# In[ ]:


date_time = datetime.datetime(1950,1,1), datetime.datetime(2010,1,1)

# Porcentaje de mujeres sin educacion por rango etario
indicadores = {'BAR.NOED.1519.FE.ZS':'15-19','BAR.NOED.2024.FE.ZS':'20-24', 
              'BAR.NOED.2529.FE.ZS':'25-29', 'BAR.NOED.3034.FE.ZS':'30-34',
              'BAR.NOED.3539.FE.ZS':'35-39' , 'BAR.NOED.4044.FE.ZS':'40-44',
              'BAR.NOED.4549.FE.ZS':'45-49', 'BAR.NOED.5054.FE.ZS':'50-54',
              'BAR.NOED.5559.FE.ZS':'55-59'}

df1 = wbdata.get_dataframe(indicadores, country = 'ARG', data_date=date_time)
df1.dropna(inplace = True)


# Porcentaje no educado de la población femenina.

# In[ ]:


df1.iloc[8,].plot(style = '-.', label = '1970', legend=True)
df1.iloc[5,].plot(style = '-.', label = '1990', legend = True)
df1.iloc[1,].plot(style = '-.', label = '2010', legend = True)
plt.title('Porcentaje de no educación femenino')
plt.ylabel('Porcentaje',color = 'grey')
plt.xlabel('Edad', color = 'grey')
plt.xticks([0,1,2,3,4,5,6,7,8],df.columns.tolist())


# Ahora comparamos la educacion de la población total vs población femenina en los años 1970 y 2010. 

# In[ ]:


# 2010
df.iloc[1,].plot(style = '-.', label = '2010', legend = True)
df1.iloc[1,].plot(style = '-.', label = '2010-F', legend = True) 
# 1970
df.iloc[8,].plot(style = '-.', label = '1970', legend=True)
df1.iloc[8,].plot(style = '-.', label = '1970-F', legend=True)
plt.title('Comparación no educación mujeres y población')
plt.xlabel('Edad', color = 'grey')
plt.ylabel('Porcentaje', color = 'grey')
plt.xticks([0,1,2,3,4,5,6,7,8],df.columns.tolist())


# Vemos que luego de 40 años la brecha se acoto.

# ## Gráfico de barras
# 

# In[ ]:


df.head(5)


# In[ ]:


ax = df.plot(kind='bar',
       title='Gráficos de barras de toda la población')
ax.set_xlabel('Años',color='grey')
ax.set_ylabel('Porcentaje',color='grey')


# Lo hacemos en horizontal y apilamos la población en una barra.

# In[ ]:


ax = df1.plot.barh(stacked=True)
ax.set_title('Graficos de barras apilados')
ax.set_xlabel('Porcentaje',color='grey')
ax.set_ylabel('Años',color='grey')


# ## Histogramas

# Vamos a trabajar con el [Indice de facilidad para hacer negocios](https://es.wikipedia.org/wiki/%C3%8Dndice_de_facilidad_para_hacer_negocios) en distintos países.
# 

# Seleccionamos los paises a utilizar y creamos el dataframe.

# In[ ]:


paises = [i['id'] for i in wbdata.get_country(incomelevel=['LIC','HIC'])]

# Seleccionamos nuestros nuevos datos
indicadores = {"IC.BUS.EASE.XQ": "indice_negocio", "NY.GDP.PCAP.PP.KD": "PIBPC"} 

data = wbdata.get_dataframe(indicadores, country=paises, convert_date=True)   
df = pd.DataFrame(data=data)


# In[ ]:


df.dropna(inplace=True)


# In[ ]:


df.info()


# In[ ]:


df.head()


# In[ ]:


plt.figure()
df['PIBPC'].plot.hist(alpha=0.7,  # Con alpha seteamos la transparencia
                     color='y',
                     bins=9,
                     title='Distribución del PIB per capita')
plt.xlabel('PIB per capita', color='grey')
plt.ylabel('Frecuencia',color='grey')


# ## Box plot

# In[ ]:


df['PIBPC'].plot.box(title='Diagrma de caja PIB')


# Recordamos que dentro de la caja se encuentra el 50% de la población. La línea verde indica la mediana.

# ## Scatter plot

# Hacemos un gráfico de dispersión entre las variables PIB p/ capita e Indice de facilidad p/ hacer negocios.

# In[ ]:


df.plot.scatter(y='PIBPC', x='indice_negocio',
                c='r', 
                s=df['PIBPC']**0.4    # Con s seteamos el tamaño de los puntos
               ) 

plt.gca().invert_xaxis() 
plt.xlabel('Indice de facilidad de hacer negocio')
plt.ylabel('PIB per capita')


# Es intuitivo que en los países con más facilidad para los negocios tienen un PIB per capita más alto. 

# Finalmente vemos una variante al gráfico de dispersión, un gráfico hexagonal. 

# In[ ]:


df.plot.hexbin(y='PIBPC', x='indice_negocio', gridsize=15,
              title='Gráfico de dispersión hexagonal')
plt.gca().invert_xaxis()
plt.xlabel('Indice de facilidad de hacer negocio')
plt.ylabel('PIB per capita')


# ## Ejercicio

# Haga un gráfico para ver la evolución de los inscriptos a las distintas instancias educativas, diferenciando pr género, a lo largo del tiempo. Puede ayudarse con la [documentación](https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html)

# In[ ]:


indicadores = {'SE.PRM.ENRR.FE':'primario-femenino','SE.PRM.ENRR.MA':'primario-masculino',
               'SE.SEC.ENRR.FE':'secundario-femenino','SE.SEC.ENRR.MA':'segundario-masculino',
               'SE.TER.ENRR.FE':'terciario-femenino','SE.TER.ENRR.MA':'terciario-masculino'}

df = wbdata.get_dataframe(indicadores,country='ARG')


# Utilize el período [2000-2017].

# In[ ]:


# df.iloc...


# Una vez que tenga los datos a utilizar realice el gráfico. Pruebe agregarle una leyenda y cambiar el color. Tambíen puede etiquetar los ejes y elegir un título.

# In[ ]:


# df.plot...

