#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Scraping/2_HTTP_Avanzado/scraping_2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" data-canonical-src="https://colab.research.google.com/assets/colab-badge.svg"></a>

# 
# # Práctica: Scraping Avanzado 2:
# 
# - ChromeDevTools
# - Cookies
# - Crawling
# - Regex, XPath
# 

# ## Pyautogui, Selenium, Requests
# 
# Ahora que vimos `requests` podemos entender que es una manera protocolar de conseguir un recurso en lugar de interactuar a través del sistema operativo con mousse y teclado como con `pyautogui`.
# 
# La web está hecha con la tríada de lenguajes: HTML, JS, y CSS. Javascript modifica el contenido dinámicamente, ejecutando código del lado del cliente. Requests no ejecuta el código javascript, por lo que en ese caso es necesario usar una alternativa que sí lo haga. Desde "alto nivel" hacia "bajo nivel" sería: automatizando la interacción con el navegador desde el sistema operativo (pyautogui), automatizando el navegador (selenium), o encontrando una **API oculta o visible para usar requests.**.
# 
# Cuando una compañia desarrolla un sitio web muchas veces separa lo que se dice el _frontend_, que es la parte visible del sitio y la cual se ejecuta en tu navegador, del _backend_, la parte del sitio que realiza el computo mas pesado y se ejecuta en servidores/computadoras de la compañia.
# 
# Para comunicar el _backend_ con el _frontend_ una forma popular es desarrollar REST APIs, a veces estas son públicas pero a veces están ocultas y las utilizamos sin darnos cuenta cuando interactuamos con un sitio web.
# 
# Ejemplo de un sitio web y su API: http://numbersapi.com/

# # Ejemplos

# #### Modo 1: pyautogui
# 
# Lo queremos evitar, es frágil y _ad hoc_ (**y no anda en Colab!**)

# In[ ]:


get_ipython().system('pip install pyautogui')
import pyautogui
from time import sleep


# In[153]:


import requests as rq
url = 'https://www.lanacion.com.ar/'


# In[ ]:


pyautogui.hotkey('ctrl', 't')
sleep(2)
pyautogui.write(url.split())
sleep(2)
pyautogui.press('enter')


# Modo 2:
# 
# Emulando un navegador con Selenium

# In[ ]:


# Esta celda instala selenium y chromedriver en Colab
get_ipython().system('pip install selenium')
get_ipython().system('apt-get update # to update ubuntu to correctly run apt install')
get_ipython().system('apt install chromium-chromedriver')
get_ipython().system('cp /usr/lib/chromium-browser/chromedriver/usr/bin')
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')


# In[ ]:


url


# In[ ]:


from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox') # necesarios en colab 
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)


# In[ ]:


# *vamos* a un sitio
driver.get(url)


# In[ ]:


# el driver ahora "está" en ese sitio
driver.page_source[:100]


# In[ ]:


# Ejercicio: usar xpath para encontrar los títulos
patron = '' # completar
titulos = [e.text for e in driver.find_elements_by_xpath(patron)]


# In[ ]:


titulos


# Tercer modo: requests
# 

# In[183]:


import requests 
# para pasar del string con el html a un DOM y usar xpath
from lxml import html
# alternativa 
from bs4 import BeautifulSoup


# In[202]:


r = requests.get('https://www.lanacion.com.ar/')


# In[185]:


soup = BeautifulSoup(r.content, 'html.parser')


# Ahora parseo: 
# - BeautifulSoup: funciones importantes son .find(), .find_all(), .get()
# - XPATH: un mini lenguaje para recorrer archivos en formato [XML](https://www.w3schools.com/xml/xpath_intro.asp)

# In[211]:


[e for e in soup.find_all('h2')]


# In[212]:


dom = html.fromstring(r.content)

# con XPATH
[''.join(e.itertext()) for e in dom.xpath('//h2')]


# In[237]:


# Cualquier elemento cuyo atributo "class" contenga "title"
patron = '//*[contains(@class, "title")]'
[''.join(e.itertext()) for e in dom.xpath(patron)]


# Buenas puntas:
# 
# - sitemap
# - robots.txt
# 
# ¿Cómo encuentro el sitemap? Ejemplo de "Google Hacking": uso de operadores en google para mejores búsquedas.
# 
# `inurl:sitemap site:lanacion.com.ar` 

# In[ ]:





# ### ChromeDevTools
# 
# El navegador de Chrome nos ofrece herramientas para analizar elementos de la web. Para eso, vamos a abrir las "Herramientas de Desarrollador" en el menú o con _CTRL + SHIFT + I_.
# 
# Ahí hay dos pestañas que van a ser de nuestro interés:
# 
# En **Elements** vamos a poder inspeccionar el código HTML, para ubicar los datos de nuestro interés. Para identificar la ubicación de uno, podemos posicionarnos con el cursor sobre el sitio, hacer click derecho, y seleccionar "Inspeccionar elemento".
# 
# En la solapa **Network** podemos ver todos los paquetes HTTP que realiza nuestro navegador interactuando con un sitio. Identificando los paquetes de las APIs que traen los datos, podemos _scrapear_ datos más facilmente.
# 
# Posibles estrategias:
# - Tomar una parte de la info que buscamos del sitio y ponerla en el buscador en _Network_
# - Buscar en el HTML dónde se ubica la info que necesitamos
# - Buscar en HTML o con DevTools las llamadas de javascript

# <img src='https://i2.wp.com/abodeqa.com/wp-content/uploads/2019/02/Inspect-Element-Using-Select-Tool.gif'>
# 

# **Ejemplo Bytes:**
# 
# Base de Datos de Comercio Exterior del Instituto Nacional de Estadística de Bolivia
# 
# Vamos a ingresar al siguiente sitio web:
# 
# http://web2.ine.gob.bo:8081/IneComex/BasesComex.aspx
# 
# Pasos:
# 
# - Ingresar al sitio en una nueva pestaña
# - Abrir la pestaña "Network" en las herramientas de desarrollador del navegador
# - Llenar el formulario y descargar la base de datos
# - Observar el paquete HTTP que realizó el pedido

# In[ ]:


get_ipython().system('wget http://web2.ine.gob.bo:8081/IneComex/BD/exp2020.rar')
get_ipython().system('unrar x exp2020.rar ./')


# Podríamos bajarlo directo con Python. Las descargas de distintos archivos de formatos distintos a texto (.txt, .csv, .json...) son iguales, escribiendo a disco en modo "write bytes" ('wb')

# In[238]:


# Ejemplo bytes
url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/HTML_logo.png/250px-HTML_logo.png'
r = requests.get(url)


# In[239]:


with open('imagen.png', 'wb') as out:
  out.write(r.content)


# In[ ]:


# vemos la primera parte de la base de datos
get_ipython().system('head exp2020.txt ')


# In[ ]:


# Lo podemos cargar con pandas para análisis de datos

import pandas as pd
df = pd.read_csv('exp2020.txt', sep='|', encoding="ISO-8859-1")
df.head()


# Ejercicio: 
# 
# - Descargar el archivo con Python
# - Hacer un búcle que descargue exportaciones desde el 2016 al 2020
# 
# Pista: usar un for, f-strings, ```.content``` y ```
# with open(...
# ```

# In[ ]:


# Con un loop podemos cambiar el año y descargar todas

anios = []

for a in range(2016, 2021):
  nombre = f"exp{a}.rar"
  url = f'http://web2.ine.gob.bo:8081/IneComex/BD/{nombre}'

  obj = requests.get(url)

  # guardar el contenido de obj en archivo de nombre 'nombre'

  with open(nombre, 'wb') as out:
    out.write(obj.content)
    
  print('Guardando', nombre)
  sleep(5)


# ## Crawling y Scraping
# 
# Podemos de un sitio inicial tomar todos los links que aparecen, y entrar para extraer la información de cada uno. 
# 
# Ejercicio:
# 
# Extraer todos los links de http://www.sice.oas.org .
# 
# - Usar ChromeDevTools para ver dónde se encuentran los datos 
# - Usar requests y BeautifulSoup
# - Filtrar los links que no sean nulos, contengan "/Trade/" y terminen con .asp
# 
# 
# En una aplicación real, uno tiene que considerar como se diseña la arquitectura del servicio. Se podrían tener procesos "trabajadores" o *Workers* que hacen rastreo de nuevos links (*crawling*) alimentando una cola o (*Queue*), mientras otros que se ocupan de ir tomando de estos links y extraer los datos (*Scraping*).
# 
# [Scrapy](https://scrapy.org/) es una librería que nos ofrece abstracciones para fácilmente produccionalizar (*deploy*) productos escalables de crawling y scraping.

# In[ ]:


from bs4 import BeautifulSoup

def codigo_html(url):
    '''recibe una URL y devuelve el .text de la Response'''
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    return requests.get(url, headers=headers).text


# In[ ]:


url = 'http://www.sice.oas.org/agreements_s.asp'


# In[ ]:


# Extraer los links con BS, Regex o XPATH
soup = BeautifulSoup(..., 'html.parser')


# In[ ]:


# Alternativa con Expresiones Regulares

import re
r = requests.get(url)

patron = ...

# Buscamos todo lo que coincida con nuestro patrón
subs = re.findall(patron, r.text)
subs[:10]


# ## Cookies WTO

# Vamos a buscar nuevos acuerdos comerciales en el sitio de la World Trade Organization:
# 
# https://rtais.wto.org/ 
# 
# Los acuerdos están indexados por ID, por ejemplo:
# 
# https://rtais.wto.org/UI/PublicShowRTAIDCard.aspx?rtaid=1093
# 
# Observen que en la URL hay un parámetro que es una identificación (ID) numérica

# 
# Mientras el usuario navega por un sitio, se acumula información sobre su actividad como pequeños archivos o strings denominados _cookies_, que sirven, por ejemplo, para mantener una sesión iniciada.
# 
# La clase Session de requests permite almacenar cookies

# In[ ]:


from IPython.display import HTML


# In[155]:


import requests 

id = 1093

# Creamos una nueva sesión
s = requests.Session() 


# In[156]:


s.get('https://rtais.wto.org/')


# In[164]:


# Al ingresar primero a este sitio, nos otorgan las cookies
r = rq.get(f'https://rtais.wto.org/UI/PublicShowRTAIDCard.aspx?rtaid={id}')


# In[ ]:


r.content


# Sin esos _cookies_, y los siguientes headers, el sitio no devuelve la información.

# In[167]:


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36',
    'Referer': f'https://rtais.wto.org/UI/PublicShowRTAIDCard.aspx?rtaid={id}'}

# Hacemos un GET pero usando la Sesión que instanciamos
r2 = s.get('https://rtais.wto.org/WEBCONTROL/ExportRTAIDCard.aspx', headers=headers)


# In[ ]:


r2.content[:1000]


# In[174]:


HTML(r2.text)


# In[175]:


with open('data.xls', 'w') as out:
  out.write(r2.text)


# Ejercicio:
# 
# - Extraigan los IDs de https://rtais.wto.org/ y descarguen los .xls para cada uno.
# 
# - Con la librería OS, creen una carpeta con el nombre de la fecha de hoy, y guarden los archivos ahí

# In[ ]:





# 
# Muchas veces las páginas web obtienen sus ingresos a partir del uso de usuarios tradicionales (humanos) pero no de los scrapers (máquinas). Por lo que estos no generan ganancias al sitio y encima pueden causar congestión en los servidores (Pudiendo causar incluso la rotura del sitio similar a lo que pasa con los [ataques DDOS](https://es.wikipedia.org/wiki/Ataque_de_denegaci%C3%B3n_de_servicio)).
# 
# Por esta razón los sitios webs suelen tener una pagina [/robots.txt](https://es.wikipedia.org/wiki/Est%C3%A1ndar_de_exclusi%C3%B3n_de_robots) donde especifican que tipo de scrapeo prefieren evitar.
# 
# Pueden ver, como ejemplos:
# 
# - https://www.google.com/robots.txt
# - https://en.wikipedia.org/robots.txt

# Ejercicio para la casa: 
# 
# Descargar PDFs de https://www.markiteconomics.com/Public/Release/PressReleases
# 

# In[ ]:





# Ejemplo con curl2python: identificamos el paquete, y con la herramienta armamos el paquete de requests:
# 
# Datos de la OECD https://stats.oecd.org/Index.aspx?DataSetCode=ULC_EEQ%20

# In[ ]:





# In[ ]:


response.content[:1000]


# In[ ]:


df = pd.read_csv('./unit_labour_costs_and_labour_productivity_(employment_based).csv')


# In[ ]:


df


# ## Recursos extra:
# 
# ### Scheduling
# 
# Scheduling es configurar una ejecución automáticamente en el tiempo. 
# 
# - [Crontab para Linux o Mac](https://tecadmin.net/crontab-in-linux-with-20-examples-of-cron-schedule/)
# - [Schedule en Windows](https://stackoverflow.com/questions/132971/what-is-the-windows-version-of-cron)
# 
# ### Recursos útiles
# - [Tutorial de Indian Pythonista sobre APIs ocultas](https://www.youtube.com/watch?v=twuhocLtGCg)
# 
# ### Herramientas útiles
# - [curl2python](https://curl.trillworks.com/)
# - [Visualizador de JSONs](http://jsonviewer.stack.hu/)
# 
# 
