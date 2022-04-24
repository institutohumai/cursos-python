#!/usr/bin/env python
# coding: utf-8

# [![Open In colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/APIs/1_APIs_Geograficas/clase-1.ipynb)

# # APIs geográficas

# In[1]:


import requests
import pandas as pd
import geopandas as gpd
import helpers
import json


# ## Requests

# ### Interfaces de aplicaciones

# ¿Qué es una API? Los sistemas tienen distintos tipos de interfaces que permiten interactuar con ellos.
# 
# * **GUI (Graphical User Interface)**: El usuario clickea e interactúa con distintos objetos para ejecutar acciones y lograr sus objetivos. Las páginas web tienen interfaces gráficas.
# * **API (Application Programming Interface)**: El usuario escribe líneas de código para interactuar con el sistema, ejecutar acciones y lograr sus objetivos.
# 
# Todos los sitios web tienen una interfaz gráfica con la que estamos acostumbrados a interactuar, y también tienen una interfaz de programación más o menos desarrollada, o más o menos expuesta, con la cual tal vez no estemos tan acostumbrados a interactuar.
# 
# Ejemplo: 
# 
# Si van a https://www.mercadolibre.com.ar/ pueden hacer click en un input box, escribir "pelotas", apretar "Enter" y el sistema les devolverá el resultado de una búsqueda. Si lo cambian por "pelotas futbol" y hacen "Enter" de nuevo, cambiará el resultado de la búsqueda. Esta es la **interfaz gráfica del sitio**.
# 
# Sin embargo también podrían cumplir el mismo objetivo sólo escribiendo distintas URLs en el navegador:
# 
# * https://listado.mercadolibre.com.ar/pelotas
# * https://listado.mercadolibre.com.ar/pelotas-futbol
# 
# Esto es más parecido a lo que llamaríamos una **interfaz de programación**.

# ### APIs REST

# En la web, las interfaces de programación de uso más difundido son las APIs REST ([Representational state transfer](https://es.wikipedia.org/wiki/Transferencia_de_Estado_Representacional)) que especifica protocolos y métodos para interactuar con los vastos recursos de internet, escribiendo líneas de código.
# 
# La web utiliza ampliamente el protocolo HTTP para interactuar con sus recursos. Este protocolo indica cómo estructurar un mensaje de texto que describa la petición (**request**) del usuario a un servidor. Hay distintos tipos de peticios que un usuario puede realizar, algunas de ellas son:
# 
# * **GET**: Solicita una representación de un recurso alojado en el servidor.
# * **POST**: Envía datos al servidor para crear un recurso nuevo.
# * **PUT**: Crea o modifica un recurso del servidor.
# * **DELETE**: Elimina un recurso del servidor.
# 
# Existen otros métodos que hoy no nos interesan.

# ### GET request 

# Cada vez que vamos al navegador y escribimos la dirección de una página web, **estamos haciendo un GET request** a un servidor. Esto es una petición para adquirir el código de un recurso que queremos visualizar en el navegador. 
# 
# La URL es la parte más importante de la definición de un GET request (aunque el navegador agrega otras cosas también, que no vemos) y nos permite cambiar la representación deseada de ese mismo recurso de distintas maneras:
# 
# * https://deportes.mercadolibre.com.ar/pelotas-futbol pide al servidor pelotas de fútbol.
# * https://deportes.mercadolibre.com.ar/pelotas-futbol_OrderId_PRICE pide al servidor pelotas de fútbol ordenadas por precio.
# 
# Cuando escribimos una URL en un navegador, la mayoría de las veces hacemos GET requests que devuelven código HTML (es el código que usa el navegador para renderizar una página web) pero las GET requests pueden devolver datos en otros formatos (por ejemplo en JSON y en CSV). 
# 
# **Las APIs REST que definen GET requests capaces de devolver datos en formato JSON y CSV, son particularmente interesantes para enriquecer nuestras capacidades de análisis de datos.**
# 
# Ahora vamos a conocer algunas de ellas.

# ## API Georef 

# La [API Georef](http://apis.datos.gob.ar/georef) o, en su nombre más largo, el **Servicio de Normalización de Datos Geográficos de Argentina** es una API REST desarrollada y mantenida por el Estado Nacional de Argentina para la normalización de datos geográficos, que es capaz de:
# 
# * Georreferenciar una dirección
# * Normalizar nombres de provincias, departamentos y otras entidades
# * Devolver los nombres de provincias, departamentos y otras entidades que contienen a un par de coordenadas (georreferenciación inversa)
# * Sirve de referencia, devolviendo las listas canónicas con nombres y códigos oficiales de estas entidades, en formato CSV, JSON, SHP y otros.
# 
# A continuación, vamos a ver algunos de los usos que tienen los recursos de esta API para potenciar nuestras capacidades de analizar datos.

# ### Referencia 

# La API Georef contiene las listas con nombres y códigos oficiales de Argentina para, entre otras, las siguientes entidades:
# 
# * Provinicias
# * Departamentos
# * Municipios
# * Localidades
# * Calles
# 
# Cada una de ellas se consulta usando un **recurso** de la API.

# #### Librería `requests` y formato JSON

# Si estuviéramos desarrollando una aplicación web que contiene, por ejemplo, un formulario donde el usurio debe elegir el nombre de la provincia donde vive con el objeto de guardar la información en una base de datos, podríamos usar la API Georef para obtener esa lista.
# 
# La librería `requests` en python permite hacer todo tipo de requests APIs REST y es sencilla de utilizar.

# In[3]:


response = requests.get("https://apis.datos.gob.ar/georef/api/provincias")


# In[4]:


# el status code de una request indica si esta fue realizada con éxito o no, y por qué
# el código 200 indica que una request fue realizada exitosamente
response.status_code


# In[ ]:


provincias = response.json()
provincias


# El método `response.json()` de la librería `requests` devuelve una respuesta de formato JSON, en un familiar diccionario de python.

# In[6]:


provincias["provincias"][0]


# Las APIs tienen distintos parámetros que permiten modificar la consulta a un recurso determinado, estos se agregan al final usando un signo de interrogación `?` y separándolos con el caracter _ampersand_ `&`.
# 
# * **Recurso**: apis.datos.gob.ar/georef/api/provincias
# * **Parámetros**: ?orden=nombre&aplanar
# * **URL completa**: apis.datos.gob.ar/georef/api/provincias?orden=nombre&aplanar
# 
# El parámetro "orden" permite elegir un campo por el cual ordenar los resultados. El parámetro "aplanar" devuelve una estructura plana o no anidada de los resultados que a veces es más fácil de utilizar, dependiendo de lo que estemos haciendo.
# 
# Podés consultar los otros parámetros disponibles para el recurso "provincias" en https://datosgobar.github.io/georef-ar-api/open-api/#/Recursos/get_provincias

# **Ejercicio:** crea una lista ordenada alfabéticamente con tuplas que contengan id y nombre de cada provincia, que usarías para armar tu selector de provincias en una página web.

# In[ ]:





# #### `pandas` y formato CSV 

# Si estamos creando una tabla auxiliar o de consulta para obtener los nombres y códigos oficiales de las provincias, es posible que queramos descargarla en CSV o leerla directamente en un dataframe de pandas.

# In[7]:


df = pd.read_csv('https://apis.datos.gob.ar/georef/api/provincias?formato=csv')


# In[8]:


df


# Notá que la respuesta viene "aplanada" por defecto, ya que el CSV es un formato tabular (no anidado).

# **Ejercicio:** crea una tabla con la lista de departamentos de la provincia de Santa Fé. Para esto usa el recurso "departamentos" y el parámetro "provincia" para filtrarlo con los resultados de la provincia de Santa Fé. 
# 
# Puedes usar tanto el id como el nombre de la provincia para filtrar.

# In[ ]:





# #### `geopandas` y el formato SHP (shapefile) 

# La API georef también permite obtener las geometrías de las entidades para, por ejemplo, graficarlas en un mapa. Sólo debe cambiarse el formato por "shp".
# 
# Geopandas puede leer un shapefile directo de la URL, tal como hicimos con el CSV.

# In[9]:


gdf = gpd.read_file('https://apis.datos.gob.ar/georef/api/departamentos?formato=shp&provincia=82')


# In[10]:


gdf.plot()


# In[11]:


len(gdf)


# Por qué faltan departamentos? La API devuelve 10 resultados como máximo por defecto, pero se puede aumentar la cantidad de resultados con el parámetro "max" hasta 5000.

# In[12]:


gdf = gpd.read_file('https://apis.datos.gob.ar/georef/api/departamentos?formato=shp&provincia=82&max=5000')


# In[13]:


gdf.plot(figsize=(10, 10))


# **Ejercicio:** crea un mapa de los departamentos de la provincia de Buenos Aires. Y luego crea otro solamente de aquellos departamentos con nombres de santos.
# 
# Podés usar el parámetro "nombre" para filtrar los nombres de los departamentos que contengan la palabra "san".

# In[ ]:





# ### Normalización

# #### Métodos POST y consultas bulk 

# Los recursos se pueden usar para normalizar nombres de unidades territoriales mal escritos, corrigiendo con el nombre oficial y agregando el código oficial. Esto facilita enormemente la cruza de datos.

# In[14]:


requests.get("https://apis.datos.gob.ar/georef/api/provincias?nombre=sant fe").json()


# Sin embargo, los datasets a normalizar generalmente tendrán muchas filas y el método GET en este caso no nos llevará muy lejos.. Consumiremos rápidamente la cuota de la API y no conseguiremos el objetivo.
# 
# Para esto podemos usar la versión "bulk" del recurso, y realizar una request POST.
# 
# Imaginemos que tenemos un dataset con varias filas a normalizar.

# In[15]:


bioetanol = pd.read_csv('http://datos.minem.gob.ar/dataset/5ce77ad1-c729-42cd-a8b5-2407de005e5b/resource/0df1eeda-854b-44b0-8ea6-1a537f167fa4/download/bioetanol.csv')


# In[16]:


bioetanol


# Los métodos POST se usan cuando una request debe enviarle datos al servidor para cumplir su cometido. Generalmente las POST requests generan cambios en el servidor (por ejemplo, agregan un comentario a una nota periodística) pero también se usan cuando la consulta requiere parámetros más complejos o voluminosos.
# 
# El método POST permite enviar un JSON (por ejemplo) aparte de la URL.

# In[17]:


data = {
    'provincias': [
        {
            'nombre': 'JUJUY',
            'max': 1,
            'campos': 'id,nombre'
        },
        {
            'nombre': 'TUCUMAN',
            'max': 1,
            'campos': 'id,nombre'
        },
        {
            'nombre': 'CORDOBA',
            'max': 1,
            'campos': 'id,nombre'
        },
        {
            'nombre': 'SALTA',
            'max': 1,
            'campos': 'id,nombre'
        }
    ]
}


# En este diccionario, cada objeto en la lista de provincias es una consulta individual. Se pueden acumular hasta 1000 consultas en un solo POST request de esta API.
# 
# En todos los casos ponemos 'max' = 1 porque solo queremos el mejor match posible de cada caso, y elegimos que devuelva solo los campos que necesitamos, para agilizar la consulta.

# In[18]:


resultado_provs = requests.post(
    "https://apis.datos.gob.ar/georef/api/provincias",
    json=data
).json()


# In[19]:


resultado_provs


# In[20]:


resultado_provs['resultados'][0]['provincias']


# Para usar este método necesitamos generar el diccionario de una forma más flexible (no lo podemos hacer a mano!).

# In[21]:


provincias_normalizar = list(bioetanol.provincia)


# In[22]:


data = {
    'provincias': [
        {
            'nombre': provincia,
            'max': 1,
            'campos': 'id,nombre'
        }
        for provincia in provincias_normalizar
    ]
}


# In[23]:


resultado_provs = requests.post(
    "https://apis.datos.gob.ar/georef/api/provincias",
    json=data
).json()


# In[ ]:


resultado_provs['resultados'][:10]


# In[25]:


provincias_normalizadas = [
    resultado['provincias'][0]
    for resultado in resultado_provs['resultados']   
]


# In[26]:


provincias_normalizadas[:10]


# In[27]:


df_provincias_normalizadas = pd.DataFrame(provincias_normalizadas)


# In[28]:


df_provincias_normalizadas


# In[29]:


bioetanol['provincia_id'] = df_provincias_normalizadas['id']
bioetanol['provincia_nombre'] = df_provincias_normalizadas['nombre']


# In[30]:


def normalizar_unidades_territoriales(entidades, entidades_tipo):
    
    # genera el JSON con la lista de consultas a realizar
    data = {
        entidades_tipo: [
            {
                'nombre': nombre,
                'max': 1,
                'campos': 'id,nombre'
            }
            for nombre in entidades
        ]
    }
    
    # realiza la consulta
    resultados = requests.post(
        f"https://apis.datos.gob.ar/georef/api/{entidades_tipo}",
        json=data
    ).json()
    
    # parsea la respuesta
    entidades_normalizadas = [
        resultado[entidades_tipo][0]
        for resultado in resultados['resultados']   
    ]
    
    return pd.DataFrame(entidades_normalizadas)


# **Ejercicio:** usá la función para normalizar las localidades del dataset. Qué te parece que puede estar mal en el resultado, en este caso?

# In[ ]:





# Tal vez necesitemos modificar un poco la función para este caso. Como no queremos pasar todo el tiempo con este tema, en el módulo `helpers.py` te dejamos ya armada una funcion para normalizar distintas entidades usando la API Georef.

# In[31]:


localidades_normalizadas = helpers.normalizar_unidades_territoriales(
    bioetanol[['localidad', 'provincia']],
    entidades_tipo='localidades',
    nombre_campo='localidad',
    provincia_campo='provincia',
)


# In[32]:


localidades_normalizadas


# In[33]:


bioetanol['localidad_id'] = df_provincias_normalizadas['id']
bioetanol['localidad_nombre'] = df_provincias_normalizadas['nombre']


# ### Georreferenciación 

# En la API Georef, casi todos los recursos tienen una version GET (mas facil de usar, pero que permite hace pocas consultas) y una version POST (mas dificil de usar, pero que permite hacer mas consultas y mas eficientemente).
# 
# En las proximas dos secciones te vamos a presentar otras funcionalidades de la API Georef con el metodo GET correspondiente, y luego te ofreceremos una funcion ya escrita para hacer consultas masivas.

# La funcion de **georreferenciacion** permite normalizar y descomponer una direccion de Argentina en partes, asi como obtener sus coordenadas.

# In[ ]:


requests.get(
    'https://apis.datos.gob.ar/georef/api/direcciones?direccion=balcarce 50&provincia=02'
).json()


# No es obligatorio especificar una provincia, pero esto mejora mucho la precision del resultado. Tambien se puede especificar departamento u otros tipos de filtros. La API reconoce esquinas y diversas modalidades de especificar una direccion.

# In[35]:


requests.get(
    'https://apis.datos.gob.ar/georef/api/direcciones?direccion=santa fe y pueyrredon&provincia=02'
).json()


# In[36]:


requests.get(
    'https://apis.datos.gob.ar/georef/api/direcciones?direccion=santa fe (esq pueyrredon)&provincia=02'
).json()


# **Ejercicio**: Genera un dataframe con direcciones para georreferenciar, que se pueda usar en la funcion de abajo. 

# In[37]:


# completa con direcciones y la provincia a la que pertenecen
direcciones = pd.DataFrame([
    {'direccion': 'balcarce 50', 'provincia': '02'},
    {'direccion': 'balcarce 50', 'provincia': '02'},
    {'direccion': 'balcarce 50', 'provincia': '02'},
    {'direccion': 'balcarce 50', 'provincia': '02'},
    {'direccion': 'balcarce 50', 'provincia': '02'},
])


# In[38]:


direcciones_georreferenciadas = helpers.georreferenciar_direcciones(
    direcciones[['direccion', 'provincia']],
    nombre_campo='direccion',
    provincia_campo='provincia',
)
direcciones_georreferenciadas


# ### Georreferenciación inversa 

# La funcionalidad de **georreferenciacion inversa** toma un punto de coordenadas y devuelve aquellas unidades territoriales que lo contienen.
# 
# No es esctrictamente una funcion georreferenciacion inversa en realidad, ya que no devuelve una aproximacion de la direccion a la que pertenece ese punto de coordenadas, solo devuelve las unidades territoriales que contienen al punto.
# 
# Esta funcion es muy util cuando ya se tiene un dataset con coordenadas, pero queremos tener tambien las columnas de provincias, departamentos y municipios.

# In[39]:


requests.get(
    'https://apis.datos.gob.ar/georef/api/ubicacion?lat=-34.6037389&lon=-58.3815704'
).json()


# In[40]:


requests.get(
    'https://apis.datos.gob.ar/georef/api/ubicacion?lat=-32.9477132&lon=-60.6304658'
).json()


# In[41]:


requests.get(
    'https://apis.datos.gob.ar/georef/api/ubicacion?lat=-38.0048387&lon=-57.5483175'
).json()


# Por ejemplo, si tenemos las coordenadas de todos los aeropuertos del pais, podemos agregarle facilmente los codigos y nombres oficiales de las provincias, departamentos y municipios que los contienen.

# In[42]:


aeropuertos = pd.read_csv(
    'https://servicios.transporte.gob.ar/gobierno_abierto/descargar.php?t=aeropuertos&d=detalle',
    sep=';'
)


# In[43]:


aeropuertos


# Notemos que el dataset tiene un error! Los nombres de las columnas latitud y longitud, estan invertidos.

# In[44]:


lat = aeropuertos.iloc[0]['latitud']
lon = aeropuertos.iloc[0]['longitud']

requests.get(
    f'https://apis.datos.gob.ar/georef/api/ubicacion?lat={lat}&lon={lon}'
).json()


# In[45]:


lat = aeropuertos.iloc[0]['longitud']
lon = aeropuertos.iloc[0]['latitud']

requests.get(
    f'https://apis.datos.gob.ar/georef/api/ubicacion?lat={lat}&lon={lon}'
).json()


# Alcanza con notar esto para poder especifiar los nombres invertidos en la funcion.

# In[46]:


unidades_territoriales = helpers.ubicar_coordenadas(
    aeropuertos[['latitud', 'longitud']],
    'longitud', 'latitud'
)
unidades_territoriales


# **Ejercicio**: ubica las coordenadas de las estaciones de medicion de recursos hidricos (https://datos.mininterior.gob.ar/dataset/93913deb-d22e-4c0d-bca3-f465e7b2bb94/resource/26d292a4-4d7f-48e1-872a-50a0dca35386/download/estacioneslatlong.csv) en sus unidades territoriales. Tene en cuenta que este dataset **esta codificado en 'latin1'**. Tenes que especificar la codificacion en la llamada pd.read_csv() para que lo lea sin errores.

# In[ ]:





# ##  API Nominatim

# https://nominatim.org/

# Por supuesto, la API Georef del Estado Nacional no es la unica API de georreferenciacion que podes usar, existen muchas otras con distintos alcances y funcionalides.
# 
# La API de Nominativa, utiliza la base de datos de la iniciativa Open Street Map para proveer un servicio abierto de georreferenciacion con alcance global.
# 
# Es importante que si usas esta API regularmente, leas los [terminos y condiciones](https://operations.osmfoundation.org/policies/nominatim/). Entre ellas no permite hacer mas de 1 request por segundo, debe citarse la fuente y no se permite el uso para geocodificacion bulk. Esta API es para usar en forma esporadica, pero no en produccion (salvo que se instale la API en infraestructura propia).
# 
# Podes leer la documentacion de uso de la API, aca: https://nominatim.org/release-docs/develop/api/Overview/

# ### Busqueda de objetos en el espacio 

# Uno de los usos de la API es buscar objetos en el espacio, funciona de manera parecida a como a veces usamos Google Maps. Le podemos decir 'escuelas en berlin', 'hospitales en montevideo' y otras cosas parecidas, y devolvera una lista de resultados de lo que encuentre.

# In[ ]:


# hospitales en Montevideo
requests.get(
    'https://nominatim.openstreetmap.org/?addressdetails=1&q=hospitales+en+montevideo+uruguay&format=json&limit=3'
).json()


# **Ejercicio:** genera una lista de nombres y direcciones de hospitales en la Ciudad de Buenos Aires, a partir de la API de Nominatim.

# In[ ]:





# ### Georreferenciacion inversa

# El recurso /reverse permite recuperar una direccion, a partir de un par de coordenadas.

# In[48]:


requests.get(
    'https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=-34.6083411208197&lon=-58.37088525365451'
).json()


# **Ejercicio:** usa alguna de las coordenadas de las estaciones de medicion hidricas, para encontrar su direccion con este metodo. Funciona? Que resultados da esta API para esos casos?

# ### Chequea el estado del servicio 

# Si la API no parece funcionar, podes asegurarte consultando si el servicio esta funcionando en este momento o no.

# In[49]:


requests.get(
    'https://nominatim.openstreetmap.org/status.php?format=json'
).json()


# ## API normalización GCBA

# https://usig.buenosaires.gob.ar/apis/

# Si lo que necesitas hacer tiene un alcance acotado al Area Metropolitana de Buenos Aires (AMBA), tambien podes usar la API de normalizacion de direcciones del AMBA del Gobierno de la Ciudad de Buenos Aires. Una ventaja que tiene este servicio, es que tambien lo podes instalar como una libreria de python para no necesitar internet ni tener limite de cuotas (https://github.com/usig/normalizador-amba).

# ### Georreferenciacion 

# In[50]:


requests.get(
    'https://ws.usig.buenosaires.gob.ar/rest/normalizar_y_geocodificar_direcciones?calle=balcarce&altura=50&desambiguar=1'
).json()


# La API de normalizacion de la USIG del GCBA devuelve coordenadas en el sistema de proyeccion Buenos Aires Gauss Krueguer, que es mas preciso para trabajar dentro del espacio geografico de la CABA pero tambien menos facil de usar para otros usos.
# 
# Hay otro recurso de la API que transforma esas coordenadas en EPSG 4326 (el sistema de coordenadas al que estamos mas acostumbrados).

# In[51]:


requests.get(
    'https://ws.usig.buenosaires.gob.ar/rest/convertir_coordenadas?x=108487.447694&y=102343.772587&output=lonlat'
).json()


# ### Datos utiles 

# Otro metodo de las APIs de USIG devuelve datos utiles del contexto de una direccion. Es parecido al de 'ubicacion' de la API Georef, pero tiene otras areas / unidades territoriales que contienen al punto, y son propias del AMBA.

# In[52]:


requests.get(
    'https://ws.usig.buenosaires.gob.ar/datos_utiles?calle=balcarce&altura=50'
).json()


# ## API Transporte GCBA

# https://www.buenosaires.gob.ar/desarrollourbano/transporte/apitransporte

# La API unificada de transporte del GCBA ofrece acceso en tiempo real a las localizaciones de subtes, colectivos, trenes, monopatines y otros muchos datos sobre la movilidad en la Ciudad de Buenos Aires. Es gratuita pero requiere registrarse y usar credenciales para cada consulta.
# 
# Una vez registrado, tenes que guardar tus credenciales en un archivo JSON `api_transporte_creds.json` en el directorio de este notebook, o copiarlas directamente en la URL de la llamada.

# In[53]:


# carga credenciales
with open('api_transporte_creds.json', 'r') as f:
    creds = json.load(f)


# In[54]:


client_id = creds['client_id']
client_secret = creds['client_secret']


# In[ ]:


colectivos_ahora = requests.get(
    f'https://apitransporte.buenosaires.gob.ar/colectivos/vehiclePositionsSimple?client_id={client_id}&client_secret={client_secret}'
).json()
colectivos_ahora[:5]


# In[56]:


gdf = gpd.GeoDataFrame(colectivos_ahora)


# In[57]:


gdf['geometry'] = gpd.points_from_xy(gdf.longitude, gdf.latitude)


# In[58]:


gdf.plot(figsize=(10, 10))


# In[59]:


lineas = gdf.groupby(['route_short_name']).count()


# In[60]:


lineas.sort_values('id', ascending=False).head(20)


# In[61]:


gdf[gdf.route_short_name == '152A'].plot(figsize=(10, 10))

