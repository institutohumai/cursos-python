#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/AnalisisDeDatos/5_Visualizacion/Visualizacion_Plotly.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# # Visualización con Plotly

# Vamos a dar un recorrido por algunas de las posibilidades de la librería de visualización [Plotly](https://plotly.com/python/). Recordamos que estos son algunos de los ejemplos, en la documentación puede encontrar mucho más!
# Si estan usando Jupyter Lab o Jupyter Notebooks para correr esta notebook, recomendamos antes, instalar Plotly con sus respectivas extensiones como indica [aquí](https://plotly.com/python/getting-started/)
# 
# Podemos hacer distintos tipos de gráficos, nosotros vamos a abordar los siguientes:<br>
# >    - Objeto gráfico 
# >    - Gráficos a partir de diccionarios 
# >    - Plotly express 

# ### Datos
# 
# Vamos a usar un dataset de la Ciudad de Buenos Aires con información acerca de estaciones de subtes.

# In[ ]:


import pandas as pd 
                                
data = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/data_subtes.csv')


# In[ ]:


data.info()


# In[ ]:


data.isna().sum()


# In[4]:


data.head()


# Vemos que el dataset es muy grande, por lo que nos vamos a quedar con una muestra.

# In[ ]:


import random

random.seed(7)
df = data.sample(frac=0.25)


# In[6]:


df.info()


# Ahora sí, vemos que tenemos un dataset sin valores nulos y bien organizado, podemos seguir con los gráficos.
# 

# ### A partir de un diccionario
# 

# In[7]:


import plotly.io as pio

fig = dict({
    "data": [{"type": "bar",
              "x": df['linea'].value_counts().index.tolist(),
              "y": df['linea'].value_counts()
              }],
    "layout": {"title": {"text": "Cantidad de observaciones por linea"}}
})

pio.show(fig)


# Dentro del mismo diccionario podemos personalizar nuestro gráfico de manera más detallada. Vemos como agregarle anotaciones y elegimos un tema de diseño.

# In[8]:


fig = dict({
    "data": [{"type": "bar",
              "x": df['linea'].value_counts().index.tolist(),
              "y": df['linea'].value_counts()
              }],
    "layout": {"title": {"text": "Cantidad de observaciones por linea"},
               "template":"ggplot2",
               'annotations':[dict(text="Es la más concurrida", x=0, y=180000),
                             dict(text="Es la menos concurrida", x=5, y=80000)],
               'xaxis':{'title':'Lineas','color':'grey'},
               'yaxis':{'title':'Frecuencia','color':'grey'}
              }
})

pio.show(fig)


# ### Plotly Express
# 
# Con plotly express podemos gozar de la calidad gráfica de plotly sin la necesidad de un código muy complejo.

# Acomodomamos los formatos de las fechas.

# In[9]:


df['desde'] = pd.to_datetime(df['desde'], format = '%H:%M:%S')
df['hasta'] = pd.to_datetime(df['hasta'], format = '%H:%M:%S')


# In[10]:


df.hasta = df.hasta.apply(lambda x: x.strftime('%H:%M:%S'))
df.desde = df.desde.apply(lambda x: x.strftime('%H:%M:%S'))


# In[11]:


df.fecha = pd.to_datetime(df['fecha'])


# In[12]:


df['dia_semana'] = df['fecha'].apply(lambda x: x.day_name())


# In[13]:


import plotly.express as px

template = 'ggplot2'

fig = px.histogram(df.sort_values(by='desde'),
                 x='desde', y="total",
                 template=template, title='Total de pasajeros por hora',
                  labels={'desde':'Horario','total':'Cantidad de pasajeros'})

fig.update_xaxes(rangeslider_visible=True)
fig.show()


# ### Objeto Grafico

# Esta clase de plotly nos permite una mayor customización de los graficos. 

# In[14]:


import plotly.graph_objects as go


# Ahora vemos los histogramas de 3 días distintos para ver como se comportan, suponemos que los días laborales, el subte se usa más.

# Lunes

# In[15]:


x1 = df.loc[df['dia_semana']=='Monday']['desde']

traza1 = go.Histogram(
    x = x1.sort_values(),
    y = df.loc[df['dia_semana']=='Monday']['total'],
    name = 'Lunes',
    opacity = 0.8,
    xaxis = 'x1',
    yaxis = 'y1',
    marker = go.histogram.Marker(
        color = 'rgb(95, 182, 239)',
    )
)


# Viernes

# In[16]:


x2 = df.loc[df['dia_semana']=='Friday']['desde']

traza2 = go.Histogram(
    x = x2.sort_values(),
    y = df.loc[df['dia_semana']=='Friday']['total'],
    name = 'Viernes',
    opacity = 0.8,
    xaxis = 'x1',
    yaxis = 'y1',
    marker = go.histogram.Marker(
        color = 'rgb(300, 150, 100)',
    )
)


# Sabados

# In[17]:


x3 = df.loc[df['dia_semana']=='Saturday']['desde']

traza3 = go.Histogram(
    x = x3.sort_values(),
    y = df.loc[df['dia_semana']=='Saturday']['total'],
    name = 'Sabados',
    opacity = 0.8,
    xaxis = 'x1',
    yaxis = 'y1',
    marker = go.histogram.Marker(
        color = 'rgb(200, 104, 50)',
    )
)


# Retocamos la estetica del gráfico.

# In[18]:


plantilla = go.Layout(title='Histogramas por día de semana')


# Ahora unimos todas las trazas en una figura de Graphing Objects

# In[19]:


fig = go.Figure(data=[traza1, traza2, traza3], layout=plantilla)

fig.show()


# ### Torta 2D
# 
# Creamos un objeto gráfico a partir de los datos instanciados en una figura de plotly express.

# In[20]:


store = px.sunburst(df,path=['linea', 'estacion'])

traza = go.Sunburst(labels=store['data'][0]['labels'].tolist(),
                            parents=store['data'][0]['parents'].tolist())

fig = go.Figure(data=[traza])

fig.show()


# ### Series de tiempo
# 
# Utilizaremos las series financieras de Apple, Google y Amazon.

# In[21]:


df = pd.read_csv('https://datasets-humai.s3.amazonaws.com/datasets/data_financiera.csv')


# Gráficamos las tres series de tiempo con las siguientes líneas de código.

# In[22]:


columnas = ['AAPL','AMZN', 'GOOGL']

fig = go.Figure([{
    'x': df.Date,
    'y': df[col],
    'name': col
}  for col in columnas])

fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(title='Amazon vs Google vs Apple')
fig.show()


# ### OHLC
# 
# Vamos a utilizar una serie financiera, en especifico la de Apple. 

# In[23]:


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')


# In[24]:


df.head(5)


# Por sus siglas en inglés OHLC es Open High Low Close.

# In[25]:


fig = go.Figure(data=go.Ohlc(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close']))


fig.update_layout(
    title='OHLC de Apple',
    yaxis_title='AAPL',
    shapes = [dict(
        x0='2016-12-09', x1='2016-12-09', y0=0, y1=1, xref='x', yref='paper',   #con esta linea de codigo hacemos la linea vertical
        line_width=2)],
    annotations=[dict(
        x='2016-12-09', y=0.60, xref='x', yref='paper',
        showarrow=True, xanchor='right', text='Apple actualizó el software')]    #con esta linea nos encargamos de la anotación
)


fig.show()


# ## Ejercicio
# 
# Continuando con el ejemplo anterior, realice el gráfico de la OHLC. Investigue la [documentación](https://plotly.com/python/ohlc-charts/) para agregarle ulteriores modificaciones. Además considere agregarle al gráfico la media móvil ('mavg') y su volumén diario ('AAPL.Volume') 

# In[26]:


# Traza 1 
traza1 = go.Ohlc()

# Traza 2 
traza2 = go.Scatter()

# Traza 3 
traza3 = go.Histogram()


# In[27]:


fig = go.Figure(data=[traza1,traza2,traza3])
fig.show()

