#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/APIs/2_APIs_Series_Tiempo/ejercicios/ejercicios.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# # Clase 1: ejercicios prácticos resueltos

# In[92]:


get_ipython().system('pip install markdown')
get_ipython().system('pip install arrow')
get_ipython().system('pip install seaborn')
get_ipython().system('pip install requests')


# In[93]:


from IPython.core.display import display, HTML
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import arrow
import markdown
import requests
get_ipython().run_line_magic('matplotlib', 'inline')

matplotlib.style.use('ggplot')
matplotlib.rcParams['figure.figsize'] = [12, 8]


# ## Ejercicio 1: API de Series de Tiempo de Argentina 

# * Genera una tabla y grafica la evolucion de los tipos de cambio ARS/USD de todas las entidades financieras (canal electronico, venta, 15hs).

# In[94]:


BASE_SERIES_API = 'https://apis.datos.gob.ar/series/api/series/?ids={ids}&last=5000&format=csv'

tcs_api = BASE_SERIES_API.format(
    ids=",".join([
        'tc_usd_galicia_ev15',
        'tc_usd_supervielle_ev15',
        'tc_usd_itau_ev15',
        'tc_usd_macro_ev15',
        'tc_usd_piano_ev15',
        'tc_usd_credicoop_ev15',
        'tc_usd_bbva_ev15',
        'tc_usd_bna_ev15',
        'tc_usd_ibcambio_ev15',
        'tc_usd_patagonia_ev15',
        'tc_usd_hsbc_ev15',
        'tc_usd_brubank_ev15',
        'tc_usd_bullmarket_ev15',
        'tc_usd_santander_ev15',
        'tc_usd_hipotecario_ev15',
        'tc_usd_balanz_ev15',
    ])
)

print(tcs_api)

tcs = pd.read_csv(tcs_api)


# In[95]:


tcs['indice_tiempo'] = pd.to_datetime(tcs.indice_tiempo)
tcs = tcs.set_index('indice_tiempo')
tcs


# In[96]:


tcs.plot()


# * Genera un reporte automatico en HTML que diga las ultimas temperaturas diarias y el promedio de los ultimos 30 dias, para 3 ciudades de Argentina

# In[97]:


temperaturas_api = BASE_SERIES_API.format(
    ids=",".join([
        'temp_max_sarc',
        'temp_max_sane',
        'temp_max_saar',
    ])
)

print(temperaturas_api)

temperaturas = pd.read_csv(temperaturas_api)


# In[98]:


temperaturas['indice_tiempo'] = pd.to_datetime(temperaturas.indice_tiempo)
temperaturas = temperaturas.set_index('indice_tiempo')
temperaturas


# In[99]:


# como hay algunos dias sin valores, hay que especificar cual es la 
# cantidad minima de periodos aceptable para hacer el promedio de 30 dias
temperaturas_30d = temperaturas.rolling(30, min_periods=25).mean()
temperaturas_30d


# In[100]:


fecha = arrow.get(temperaturas.index[-1]).format('YYYY-MM-DD')

corrientes_temp = temperaturas.loc[fecha, 'temperatura_maxima_sarc']
santiago_temp = temperaturas.loc[fecha, 'temperatura_maxima_sane']
rosario_temp = temperaturas.loc[fecha, 'temperatura_maxima_saar']

corrientes_temp_30d = temperaturas_30d.loc[fecha, 'temperatura_maxima_sarc']
santiago_temp_30d = temperaturas_30d.loc[fecha, 'temperatura_maxima_sane']
rosario_temp_30d = temperaturas_30d.loc[fecha, 'temperatura_maxima_saar']


# In[101]:


reporte = f"""
=== TEMPERATURAS ===

Temperaturas maximas registradas al dia de {fecha} y 
promedio de maximas de los 30 dias anteriores.

* Corrientes: {corrientes_temp} (promedio 30d: {corrientes_temp_30d:.1f})
* Santiago del Estero: {santiago_temp} (promedio 30d: {santiago_temp_30d:.1f})
* Rosario: {rosario_temp} (promedio 30d: {rosario_temp_30d:.1f})

=====================
"""


# In[102]:


html = markdown.markdown(reporte)
display(HTML(html))


# * Grafica la relacion entre el nivel de precios (nucleo) y la base monetaria. Podes buscar la base monetaria en [este dataset](https://datos.gob.ar/dataset/sspm-factores-explicacion-base-monetaria/archivo/sspm_331.2) bajo el nombre de "Saldo de la base monetaria" y la serie de nivel de precios [es esta](https://datos.gob.ar/series/api/series/?ids=148.3_INUCLEONAL_DICI_M_19). Algunos scatter a probar:
#     - IPC vs. base monetaria
#     - IPC promedio 6 meses vs. base monetaria promedio 6 meses (Pista: usa rolling() y mean()).
#     - IPC promedio 6 meses (variacion porcentual) vs. base monetaria promedio 6 meses (variacion porcentual) (Pista: agregale pct_change(1) al anterior).
#     - IPC promedio 6 meses (variacion porcentual) vs. base monetaria promedio 6 meses (variacion porcentual) de hace 3 meses -rezago de 3 meses- (Pista: agregale shift(3) a una de las variables).
#     
# Que otras variables se podrian incorporar para explicar o controlar esta relacion? Nivel de actividad? Tipo de cambio? Tasa de interes?

# In[103]:


m_ipc_api = BASE_SERIES_API.format(
    ids=",".join([
        '148.3_INUCLEONAL_DICI_M_19',
        '331.2_SALDO_BASERIA__15',
    ])
)

print(m_ipc_api)

m_ipc = pd.read_csv(m_ipc_api)


# In[104]:


m_ipc = m_ipc.set_index('indice_tiempo')


# In[105]:


m_ipc.tail()


# In[106]:


m_ipc.plot.scatter(
    'saldo_base_monetaria', 'ipc_nucleo_nacional'
)


# In[107]:


m_ipc['m_rolling_6'] = m_ipc.saldo_base_monetaria.rolling(6).mean()
m_ipc['ipc_rolling_6'] = m_ipc.ipc_nucleo_nacional.rolling(6).mean()


# In[108]:


m_ipc.plot.scatter(
    'm_rolling_6', 'ipc_rolling_6'
)


# In[109]:


m_ipc['m_roll_6_pct_var'] = m_ipc.saldo_base_monetaria.rolling(6).mean().pct_change(1)
m_ipc['ipc_roll_6_pct_var'] = m_ipc.ipc_nucleo_nacional.rolling(6).mean().pct_change(1)


# In[110]:


ax = m_ipc.plot.scatter(
    'm_roll_6_pct_var', 'ipc_roll_6_pct_var'
)

# para que eje X y eje Y tengan la misma escala
ax.set_aspect('equal')


# In[111]:


m_ipc['ipc_roll_6_pct_var_shift_3'] = m_ipc.ipc_nucleo_nacional.rolling(6).mean().pct_change(1).shift(3)


# In[112]:


# bonus track! con este codigo adicional 
# podes agregar la linea de equivalencia

# creas una nueva serie con los valores de la serie 
# que es indice del grafico (eje Y)
m_ipc['equal_line'] = m_ipc['ipc_roll_6_pct_var']

# creas un dataframe que tiene el mismo indice que el grafico
m_index = m_ipc.set_index('ipc_roll_6_pct_var')


# In[113]:


ax = m_ipc.plot.scatter(
    'm_roll_6_pct_var', 'ipc_roll_6_pct_var_shift_3'
)
ax.set_aspect('equal')

# agrega la linea de equivalencia, donde los valores del eje X
# son iguales a los del eje Y (NO es una linea de tendencia)
m_index.equal_line.plot(ax=ax)


# ### Bonus track: graficar una recta de regresion

# Posiblemente te hayas preguntado haciendo los ejercicios anteriores como se puede graficar una recta de regresion _facilmente_.
# 
# Hay una libreria de graficos llamada `seaborn` que tiene muchos de estos graficos tipicos implementados para hacerlos con facilidad.

# In[114]:


sns.regplot(m_ipc.m_roll_6_pct_var, m_ipc.ipc_roll_6_pct_var_shift_3)


# ## Ejercicio 2: API de Quandl

# * Grafica las tasas de interes de los bonos de Estados Unidos, a partir del dataset de FRED disponible en Quandl (Pista: podes arrancar a buscar por aca: https://www.quandl.com/data/FRED-Federal-Reserve-Economic-Data?keyword=10%20years%20treasury)

# In[115]:


BASE_QUANDL_API = 'https://www.quandl.com/api/v3/datasets/FRED/{serie_id}.csv?start_date=2010-01-01'


# In[116]:


series_ids = ['DGS1', 'DGS2', 'DGS5', 'DGS10', 'DGS30']


# In[117]:


def get_fred_serie(serie_id):
    # extrae la serie de Quandl
    api_call = BASE_QUANDL_API.format(serie_id=serie_id)
    df = pd.read_csv(api_call, index_col='Date').sort_index()
    
    # renombra con el id
    serie = df.Value
    serie.name = serie_id
    
    return serie


# In[118]:


series = list(map(get_fred_serie, series_ids))


# In[119]:


df_t = pd.concat(series, axis=1)
df_t.index = pd.to_datetime(df_t.index)
df_t


# In[120]:


df_t.plot()


# ## Ejercicio 3: API de Banco Mundial

# * Grafica la evolucion de las emisiones per capita de CO2 para por lo menos 8 paises paises de Sudamérica desde 1960 (o el primer año con datos).

# In[121]:


BASE_BM_API = 'http://api.worldbank.org/v2/es/country/{pais}/indicator/{indicador}?format=json&per_page=20000'


# In[122]:


paises = ['arg', 'bra', 'ury', 'chl', 'ven',
          'col', 'bol', 'ecu', 'per', 'pry']
indicadores = ['EN.ATM.CO2E.PC']


# In[123]:


emisiones = requests.get(
    BASE_BM_API.format(
        pais=";".join(paises), 
        indicador=";".join(indicadores)
    )
).json()


# In[124]:


df_emisiones = pd.json_normalize(emisiones[1])


# In[125]:


df_emisiones_series = df_emisiones.pivot_table(
    index='date',
    columns='country.value',
    values='value'
)
df_emisiones_series


# In[126]:


df_emisiones_series.plot()

