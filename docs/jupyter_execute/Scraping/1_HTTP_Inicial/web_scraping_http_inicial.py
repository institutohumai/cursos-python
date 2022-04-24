#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Scraping/1_HTTP_Inicial/web_scraping_http_inicial.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" data-canonical-src="https://colab.research.google.com/assets/colab-badge.svg"></a>

# # Web Scraping: Extrayendo datos de Internet

# ## **¿Qué es el web scraping?**  🤔
# 
# *La práctica de **recopilar datos** a través de cualquier medio que no sea un programa que interactúa con una API o un humano que usa un navegador web. **Normalmente mediante un programa automatizado** que consulta un servidor web, solicita datos (generalmente en forma de HTML y otros archivos que componen las páginas web) y luego analiza esos datos para extraer la información necesaria.*
# 
# <br>
# 
# <center>
# <img src="https://images-na.ssl-images-amazon.com/images/I/517z2NUzcEL._SX198_BO1,204,203,200_QL40_ML2_.jpg">
# </center>
# 
# <br>
# 
# *Por otro lado, el **web crawling o indexación** se utiliza para indexar la información de la página mediante bots también conocidos como crawlers (lo que hacen los motores de búsqueda). Se trata de ver una página como un todo e indexarla. Cuando un bot rastrea un sitio web, **recorre todas las páginas y todos los enlaces**, hasta la última línea del sitio web, en busca de **CUALQUIER información**.*

# ## **Antes de empezar** ⚠️
# 
# 1. *Aspectos éticos y legales del web scraping*
#   * El web scraping es una forma automática de guardar información que se presenta en nuestro navegador muy utilizada tanto en la industria como en la academia, sus aspectos legales dependerán de cada sitio y de cada estado. Respecto a la ética es importante que nos detengamos a pensar si estamos o no generando algun perjuicio. En ambos casos el debate está abierto y hay mucha bibliografía al respecto como por ejemplo [este trabajo](https://www.researchgate.net/profile/Vlad-Krotov/publication/324907302_Legality_and_Ethics_of_Web_Scraping/links/5aea622345851588dd8287dc/Legality-and-Ethics-of-Web-Scraping.pdf)
# 
# 2. *No reinventar la rueda*
#   * Emprender un proyecto de web scraping a veces es rapido y sencillo, pero normalmente requiere tiempo y esfuerzo. Siempre es aconsejable asegurarse de que valga la pena y antes iniciar hacerse algunas preguntas:<br>
#     - ¿La informacion que necesito ya se encuentra disponible? (ej: APIs)
#     - ¿Vale la pena automatizarlo o es algo que lleva poco trabajo a mano?
# 
# 
# 
# 

# ## **Conceptos básicos sobre la web** 
# 
# #### HTML, CSS y JavaScript son los tres lenguajes principales con los que está hecho la parte de la web que vemos (*front-end*).
# 
# <center>
# <img src="https://www.nicepng.com/png/detail/142-1423886_html5-css3-js-html-css-javascript.png" width="400">
# 
# <img src="https://geekflare.com/wp-content/uploads/2019/12/css-gif.gif" width="243">
# 
# 
# </center>
# 
# <br>
# <br>
# 
# | ESTRUCTURA  | ESTILO | FUNCIONALIDAD|
# |-----|----------------| ---------- |
# |HTML| CSS | JAVASCRIPT|
# 
# <font color="gray">
# Fuente de las imágenes: <br>
# https://geekflare.com/es/css-formatting-optimization-tools/ <br>
# https://www.nicepng.com/ourpic/u2q8i1o0e6q8r5t4_html5-css3-js-html-css-javascript/
# </font>
# 
# 

# ## Introducción a HTML

# El lenguaje principal de la internet es HTML, cuando nosotros vemos algo así:
# 
# ![](https://github.com/institutohumai/cursos-python/blob/master/Scraping/1_HTTP_Inicial/multimedia/hello-world.jpeg?raw=1)
# 
# Eso se genera a partir de una código que luce así
# 
# ```html
# <html>
#   <header>
#     <title>Web Scraping - Instituto Humai</title>
#   </header>
#   <body>
#     <h1>¡Hola!</h1>
#     <p>Esto es un sitio web</p>
#   </body>
# </html>
# ```
# 
# **_Nota_**: Para saber más sobre HTML podés consultar [acá](https://www.w3schools.com/TAGS/default.ASP) la lista de etiquetas de este lenguaje.

# 
# ```html
#   <head>
#     <title>Mi primer pagina</title>
#   </head>
#   <body>
#     <h1 id='titulo'>Hola</h1>
#     <h2 style='color:red;'>Subtitulo en rojo</h2>
#     <p>Primer parrafo</p>
#     <hr>
#     <img src="https://i.pinimg.com/564x/8f/14/25/8f142555ef5006abd82d8c5c7f9f8570.jpg" alt="gato" width=400>
#   </body>
# ```
# <center>
# <img src="https://i.ibb.co/9pqvGSv/HTML-gatito.png"  width=800> <br>
# <h3>Probar el código: <a>https://codepen.io/GEJ1/pen/GRmVNPb</a></h3>
# </center>
# 

# ## DOM (Document Object Model)
# 
# 
# Interfaz independiente del lenguaje que trata un documento XML o HTML como una estructura de tipo **árbol**
# <figure>
# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/DOM-model.svg/330px-DOM-model.svg.png" width="500">
# 
# ```html
# <html>
#   <head>
#     <title>My title</title>
#   </head>
#   <body>
#     <h1>A heading</h1>
#     <a href>Link text</a>
#   </body>
# </html>
# ```
# </figure>
# 
# <font color="gray"> Fuente: https://en.wikipedia.org/wiki/Document_Object_Model
# <br>Autor: Birger Eriksson
# </font>
# 

# ## ¿Cómo consigo el código HTML?
# 
# Ahora que sabemos cuál es el componente principal de los sitios webs podemos intentar programar a nuestra computadora para leer HTML y extraer información útil.
# 
# Para conseguir el código de un sitio web podemos presionar `ctrl+u` en el navegador.
# 
# Para hacer lo mismo desde Python podemos hacer lo siguiente:

# In[ ]:


#Importamos la libreria necesaria
import requests

un_sitio_web = "https://es.wikipedia.org/wiki/HTML"

# esto descarga la información del sitio web
# Es similar a lo que hace un navegador web antes de mostrar el contenido de forma amigable para un humano
resultado = requests.get(un_sitio_web)

# accedemos al código a través del atributo "text" del resultado
codigo_html = resultado.text
print(codigo_html[:1000])


# ### ¿Qué acabamos de hacer?
# 
# Veamos algunos detalles más sobre cómo descargar el contenido de un sitio web (O cómo se le suele decir en la jerga de la programación _realizar un request_). Como dijimos, en python se puede utilizar la función get de la libreria requests para hacer esto, veamos con mayor profundidad cómo se utiliza.

# In[ ]:


# httpbin es una pagina para testear pedidos HTTP, en particular la siguiente URL nos devuelve nuestro header.
url = 'http://httpbin.org/headers' 
resp = requests.get(url)

print('------------------------------')
print('Respuesta sin headers')
print(resp.text)

print('------------------------------')
print('Respuesta con headers')
nuestros_headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
resp_con_headers = requests.get(url, headers = nuestros_headers)
print(resp_con_headers.text)


# A parte de la _url_, muchas veces se especifican los _headers_, estos son objetos que proveen datos sobre nuestro _request_, por ejemplo en el campo user-agent brindamos detalles sobre quienes somos (Nuestro sistema operativo, navegador web y demás). En este caso, como no estamos usando un navegador sino que hacemos el _request_ desde Python normalmente se omite este campo, o en caso de ser obligatorio se puede inventar, ya que algunos sitios nos van a ignorar a menos que especifiquemos este campo.
# 
# Pueden ver más en esta [Lista de Headers](https://en.wikipedia.org/wiki/List_of_HTTP_header_fields)
# 
# - Consultas
#     - ¿Por qué los sitios te podrían bloquear/ignorar?
#     - ¿De donde saco un user-agent?
# 

# ### Protocolo HTTP

# La web utiliza ampliamente el protocolo HTTP (de _Hypertext Transfer Protocol_) para interactuar con sus recursos. Este protocolo indica cómo estructurar un mensaje de texto que describa la petición (**request**) del usuario a un servidor. Hay distintos tipos de peticios que un usuario puede realizar, algunas de ellas son:
# 
# * **GET**: Solicita una representación de un recurso alojado en el servidor.
# * **POST**: Envía datos al servidor para crear un recurso nuevo.
# * **PUT**: Crea o modifica un recurso del servidor.
# * **DELETE**: Elimina un recurso del servidor.
# 
# Existen otros métodos que no nos van a ser relevantes por ahora.
# 
# Cada vez que vamos al navegador y escribimos la dirección de una página web, **estamos haciendo un GET request** a un servidor. 
# Esto es una petición para adquirir el código de un recurso que queremos visualizar en el navegador. 

# Como vimos antes la función `get` retorna un objeto, el cual llamamos _resp_, este es un elemento de la clase **_Response_** y tiene distintos atributos a los que podemos acceder.
# 
# El objeto **_Response_** de requests tiene los siguientes elementos principales:
# 
# - **.text**: devuelve el contenido como string.
# - **.content**: devuelve el contenido en bytes.
# - **.json()**: el contenido en formato JSON, si es posible.
# - **.status_code**: el código de respuesta.
# 
# 
# El código de status (*status code*) nos informa del estado de nuestra *request*
# 
# Códigos posibles:
# 
# - 1xx Mensaje de información
# - 2xx Éxito
# - 3xx Redirigir a otra URL
# - 4xx Error del cliente
# - 5xx Error del servidor
# 
# <center>
# <img alt="http-status-codes" src="https://miro.medium.com/max/1400/1*w_iicbG7L3xEQTArjHUS6g.jpeg" width="500"> <br>
# <font color='gray'>Fuente: https://www.youtube.com/watch?v=LtNSd_4txVc
# </font>
# </center>
# 
# 

# In[ ]:


#Vemos el código de estado
# 200 es que esta todo bien, 5xx o 4xx es que esta todo mal (Por ejemplo el clasico 404)
resp.status_code


# In[ ]:


#Vemos los headers que enviamos
resp.request.headers


# El atributo que nos interesa particularmente es resp.text, que guardan el contenido de la página.
# 
# Como vamos a descargar el codigo de un sitio frecuentemente armamos una funcion para no reescribir lo mismo muchas veces

# In[ ]:


def codigo_html(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }
    resp = requests.get(url, headers = headers)
    return resp.text


# In[ ]:


# Tambien podemos scrapear otro tipo de a que no sea texto
import requests

# defino la URL
image_url = 'https://www.octoparse.com/media/7179/find-data.jpg'

# Hago una peticion y guardo la respuesta
image_response = requests.get(image_url)

# Accedemos al contenido de la imagen en bytes
image_response_content = image_response.content

print(f'Este es el contenido en bytes: \n {image_response_content[:100]}')


# In[ ]:


# Importamos librerias para manejar imagenes (no tienen nada que ver con el scrapeo)
from PIL import Image
from io import BytesIO

# Mostramos la imagen
image_from_url = Image.open(BytesIO(image_response_content))
print('Esta imagen la bajamos de internet usando Python! \n ')
image_from_url


# ### Documentación
# La función get y la clase Response fueron desarrolladas por lxs programadores que crearon la librería requests. Si quieren saber mas sobre algún detalle siempre es recomendable buscar en la [documentación oficial de la librería](https://docs.python-requests.org/en/latest/).

# ## ¿Cómo extraigo datos útiles del código HTML?
# 
# - Veamos un ejemplo inspeccionando con chrome un sitio web:
# 1. Nos posicionamos sobre el elemento que nos interesa.
# 2. Presionamos click derecho -> *inspeccionar elemento* para abrir las *herramientas de desarrollo* (o presionando `CTRL + SHIFT + I`)
# 4. Esto nos da acceso al codigo de HTML correspondiente al elemento de la pagina que nos interesa.
# 
# 
# <img src="https://i.ibb.co/1RSNcs5/inspect.png" alt="inspect" width="1100">
# 
# <hr>
# <br>
# <br>
# 
# En **Elements** vamos a poder inspeccionar el código HTML, para ubicar los datos de nuestro interés. Para identificar la ubicación de uno, podemos posicionarnos con el cursor sobre el sitio, hacer click derecho, y seleccionar "Inspeccionar elemento".
# 
# En la solapa **Network** podemos ver todos los paquetes HTTP que realiza nuestro navegador interactuando con un sitio. Identificando los paquetes de las APIs que traen los datos, podemos _scrapear_ datos más facilmente. **[Esto lo verán en la clase de APIs]**
# 
# <br>
# <br>
# 
# <img src='https://i2.wp.com/abodeqa.com/wp-content/uploads/2019/02/Inspect-Element-Using-Select-Tool.gif'>
# 
# 

# ### **Método 1: Expresiones regulares**

# RegEx para los amigos. Son un mini lenguaje de programación diseñado para realizar búsquedas en strings.

# Las funciones principales de la librería re son:
# - re.findall(pattern, string) para encontrar todos los resultados de una búsqueda
# - re.search(pattern, string) para encontrar el primer resultado que coincida
# - re.sub(pattern, replace, string) para substituir un texto por otro
# 
# Recursos útiles
# 
# - [Testeo de regex online](https://regex101.com/)
# - [CheatSheet](https://www.dataquest.io/wp-content/uploads/2019/03/python-regular-expressions-cheat-sheet.pdf)

# #### Aplicandolo a la web
# ##### Ejemplo 1: Usamos regex para extraer los títulos del diario La Prensa.
# 
# 
# ```html
# <h2 class="entry__title"><a href="http://www.laprensa.com.ar/491843-Dilemas-de-la-batalla-cultural-I.note.aspx" target="_self" onclick="javascript:if(typeof(_gaq)!='undefined'){_gaq.push(['_trackEvent', 'Notas', 'Cultura', 'Dilemas de la batalla cultural (I)'])};">Dilemas de la batalla cultural (I)</a></h2>
# ```
# 

# In[ ]:


#Usamos el navegador para identificar la estructura de los datos que queremos extraer y creamos el patrón de búsqueda
regla_de_busqueda = r'_self">(.+)</a></h2>'


# In[ ]:


#Usamos findall para encontrar todas las coincidencias
import re
import requests
titles = [m for m in re.findall(regla_de_busqueda, codigo_html("http://www.laprensa.com.ar/"))]


# In[ ]:


print(titles)


# ####  <font color='red'> Ejercicio </font>
# 
# ####  Modifiquen la regla de búsqueda para que descargue los links a las notas en vez del título

# In[1]:


# Resolución


# ### **Método 2: BeautifulSoup**
# * Esta librería provee un *parser* de html, o sea un programa que entiende el código, permitiendonos hacer consultas más sofisticadas de forma simple, por ejemplo "buscame todos los titulos h2 del sitio".
# 
# 
# * Se usa para extraer los datos de archivos HTML. Crea un árbol de análisis a partir del código fuente de la página que se puede utilizar para extraer datos de forma jerárquica y más legible.
# 
# <center>
# <img alt="" width="700" role="presentation" src="https://miro.medium.com/max/700/0*ETFzXPCNHkPpqNv_.png"> <br>
# 
# <font color="gray">
# Fuente: https://medium.com/milooproject/python-simple-crawling-using-beautifulsoup-8247657c2de5
# <font>
# </center>

# ## Generalidades

# In[ ]:


from bs4 import BeautifulSoup
from IPython.display import HTML
import requests

# Vamos a jugar un poco con la pagina de Exactas
url_base = 'https://exactas.uba.ar/'
endpoint_calendario = 'calendario-academico/'
html_obtenido = requests.get(url_base + endpoint_calendario)
soup = BeautifulSoup(html_obtenido.text, "html.parser")
# print(soup)
# print(type(soup))
# print(soup.prettify())

## Tambien podemos mostrar renderizar el html aca en Colab :D
# HTML(html_obtenido.text)


# In[ ]:


# Si queremos quedarnos con un tag

# El método "find" busca el primer elemento de la pagina con ese tag
primer_h3 = soup.find('h3')
print(primer_h3)

# equivalente a:
# print(soup.h3.text)


# In[ ]:


# El método "find_all" busca TODOS los elementos de la pagina con ese tag y devuelve una lista que los contiene (en realidad devuelve un objeto de la clase "bs4.element.ResultSet")
h3_todos = soup.find_all('h3')
print(h3_todos)

# Si usamos el parametro limit = 1, emulamos al metodo find:
# h3_uno_solo = soup.find_all('h3',limit=1)
# print(h3_uno_solo)


# In[ ]:


# podemos iterar sobre el objeto
for fecha in h3_todos[:-1]:
  # Extraemos el texto que se encuentra dentro del tag
  print(fecha.text)


# In[ ]:


# Busco por clase, escribo class_ porque "class" es una palabra reservada en Python
eventos_proximos = soup.find('aside', class_ = 'widget_my_calendar_upcoming_widget')
for evento in eventos_proximos:
  print(evento.text)


# In[ ]:


# Todos los links. Esto podría ser útil para seguir scrapeando todo el sitio haciendo requests en ellos
a_todos = soup.find_all('a', href=True)
for a in a_todos:
  print(f"{a.text}: {a['href']}")


# In[ ]:


# Podemos tambien scrapear un tabla y traernos los feriados
tabla_feriados = soup.find_all('td')

# Con 'attr' podemos acceder a cualquier atributo de a etiqueta usando un diccionario
dias = soup.find_all('td', attrs={'style':'width: 74px;'}) 
fechas = soup.find_all('td', attrs={'style':'width: 127px;'}) 
eventos = soup.find_all('td', attrs={'style':'width: 438px;'}) 
# print(tabla_feriados)

for pos in range(len(dias)):
  print(f" Dia: {dias[pos].text.strip()} | fecha: {fechas[pos].text.strip()} | evento: {eventos[pos].text.strip()} ")


# In[ ]:


# Obtener la última actualización

# Para exprresiones regulares
import re
# Para manejo de fechas
from datetime import datetime

def calendario_ultima_actualizacion():
  ultima_actualizacion = soup.select('#post-256') 
  ultima_actualizacion= ultima_actualizacion[0].text
  # Expresion que busca algo del estilo x/x/xxxx (donde x es un número)
  match = re.search(r'\d/\d/\d{4}', ultima_actualizacion)
  fecha = match.group()
  fecha_datetime = datetime.strptime(fecha, '%d/%m/%Y').date()
  return fecha_datetime

fecha_datetime = calendario_ultima_actualizacion()
print(f"Última actualización: {fecha_datetime.day}/{fecha_datetime.month}/{fecha_datetime.year} ")

# Ahora podemos crear un programa que nos avise si se actualiza el calendario

def avisame_si_actualizaron(fecha_previa):
  # Esto esta solo para cortar el while
  contador_anti_explosion = 0
  fecha_datetime = calendario_ultima_actualizacion()
  fecha_previa = f'{fecha_previa.day}/{fecha_previa.month}/{fecha_previa.year}'

  while True:
    fecha_actual = f'{fecha_datetime.day}/{fecha_datetime.month}/{fecha_datetime.year}'

    if fecha_actual == fecha_previa and contador_anti_explosion < 5:
      url_base = 'https://exactas.uba.ar/'
      endpoint_calendario = 'calendario-academico/'
      html_obtenido = requests.get(url_base + endpoint_calendario)
      soup = BeautifulSoup(html_obtenido.text, "html.parser")
      fecha_datetime = calendario_ultima_actualizacion()
      print('igual')
      contador_anti_explosion += 1

    else:
      print('Actualizaron!! \n')
      from google.colab import output
      print(f'Se actualizo el: {fecha_datetime.day}/{fecha_datetime.month}/{fecha_datetime.year}')
      # Para que ladre un perro avisandonos 
      output.eval_js('new Audio("https://assets.mixkit.co/sfx/preview/mixkit-dog-barking-twice-1.mp3").play()')
      break

fecha_previa = calendario_ultima_actualizacion()

# Corremos la funcion
avisame_si_actualizaron(fecha_previa)


# <font color='red'>Ejercicio</font>
# 
# * Generar diccionario cuyas claves sean los nombres de las carreras de grado vigentes en Exactas y sus valores el link asociado a cada una de ellas. https://exactas.uba.ar/ensenanza/carreras-de-grado/
# 
# **¡A trabajar!**
# 
# <img src="https://img.icons8.com/ios/452/spade.png" width="80" height="auto"/>
# 

# In[2]:


# Resolución


# #### Ejemplo 2: Cortazar

# In[ ]:


# Creo carpeta donde voy a guardar los cuentos
get_ipython().system('mkdir -p multimedia/cortazar/')

import re
codigo_html_crudo = codigo_html('http://ciudadseva.com/autor/julio-cortazar/cuentos/')

regla_para_url_de_un_cuento = r'(https://ciudadseva.com/texto/.+/)'

for url_de_un_cuento in re.findall(regla_para_url_de_un_cuento, codigo_html_crudo):
    codigo_html_interpretado = BeautifulSoup(codigo_html(url_de_un_cuento), 'html.parser')
    elem = codigo_html_interpretado.find("div", { "class" : "text-justify" })
    cuento = elem.text
    
    # Asi podemos guardar los resultados
    nombre_del_archivo = url_de_un_cuento.split('/')[-2]
    with open (f"multimedia/cortazar/{nombre_del_archivo}.txt", 'w') as out:
        print(f'Guardando {nombre_del_archivo}')
        out.write(cuento)


# ## Práctica: Mercadolibre

# <font color='red'> Ejercicio </font>
# 
# Descargá y calculá el promedio de los precios que aparecen en la primer página de mercado libre al buscar gibson

# In[ ]:


# Resolución

import requests
import re

def precios_gibson():
    url = "https://listado.mercadolibre.com.ar/gibson"
    soup = BeautifulSoup(codigo_html(url), 'html.parser')
    prices = []
    # COMPLETAR

    return prices


# ## Usando cookies 🍪
# 
# Las [*cookies*](https://es.wikipedia.org/wiki/Cookie_(inform%C3%A1tica)) son bloques de datos creados por un servidor con información enviada por un sitio web y almacenada en el navegador del usuario, de manera que el sitio web puede consultar la actividad previa del navegador. 
# 
# Sus principales funciones son:
# 
# * Recordar accesos para saber si ya se ha visitado la página (ejemplo: cuando nos *loggeamos* se guardan cookies).
# 
# * Conocer información sobre los hábitos de navegación.
# 
# También hay otro tipo de información que se guarda en algunas páginas que son las *sessions*, básicamente es un dato similar a una cookie pero que se guarda en el servidor en lugar de hacerlo en el cliente (nuestro navegador).
# 
# Para algunos proyectos de *web scraping* puede ser útil interactuar con ellas.

# In[ ]:


import requests
from IPython.display import HTML

response = requests.get('https://www.kaggle.com/')

# Obtenemos el atributo cookies
cookies = response.cookies
print(type(cookies))
print([cookies])


# In[ ]:


# iteramos sobre las cookies en el cookie jar
for cookie in cookies:
  print('domain: ' ,cookie.domain)
  print('name: ', cookie.name)
  print('value: ', cookie.value)
  print('------------------------')


# Podemos enviar cookies junto con nuestro request. Esto puede ser util para ciertos sitios que usan la ausencia de cookies como criterio para bloquear el acceso.

# In[ ]:


url = 'https://www.kaggle.com/'

mis_cookies = {
    'name':'mi nombre',
    'password':'superSeguro1234'
    }
print(mis_cookies)

# Mando mis propias cookies
respuesta = requests.get(url, cookies=mis_cookies)

respuesta


# ## ¿Entonces me puedo descargar todo internet?
# 
# En la próximas clases veremos algunas limitaciones de este método y sus alternativas. Mas allá de eso es importante ponerse de vez en cuando en el lugar del sitio del cual estamos descargando datos.
# 
# 
# Muchas veces las páginas web obtienen sus ingresos a partir del uso de usuarios tradicionales (humanos) pero no de los scrapers (máquinas). Por lo que estos no generan ganancias al sitio y encima pueden causar congestión en los servidores (Pudiendo causar incluso la rotura del sitio similar a lo que pasa con los [ataques DDOS](https://es.wikipedia.org/wiki/Ataque_de_denegaci%C3%B3n_de_servicio)).
# 
# Por esta razón los sitios webs suelen tener una pagina [/robots.txt](https://es.wikipedia.org/wiki/Est%C3%A1ndar_de_exclusi%C3%B3n_de_robots) donde especifican que tipo de scrapeo prefieren evitar para poder mantener su sitio funcionando correctamente sin problemas.
# 
# Pueden ver, como ejemplos:
# 
# - https://www.google.com/robots.txt
# - https://en.wikipedia.org/robots.txt
