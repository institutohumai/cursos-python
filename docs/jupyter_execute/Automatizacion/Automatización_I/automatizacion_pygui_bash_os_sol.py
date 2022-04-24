#!/usr/bin/env python
# coding: utf-8

# <div align="center"><a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Automatizacion/automatizacion_pygui_bash_os_sol.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg'/> </a> <br> Recordá abrir en una nueva pestaña </div>

# ## Automatización:
# 
# En esta clase:
# 
# - Aprenderemos sobre programar desde una carpeta, o **directorio de trabajo**, y las una rutas o _path_ relativos, o absolutos.
# - Veremos como buscar archivos, también listar, borrar, copiar, mover y otras operaciones usuales con el sistema operativo. Librerías os, glob, shutil
# - Lectura de distintos tipos de datos: .sav, .dta, .csv, .zip

# Actualmente cualquier tarea que uno se proponga automatizar, así lo es. Podemos encontrar un espectro de complejidad:
# 
# - Por un lado, con la librería *pyautogui* podemos automatizar movimientos de mouse y teclado. Esto da la posibilidad de automatizar tareas sencillas de una manera directa.
# 
# (El siguiente ejemplo anda solo corriendolo como local!)

# ```python
# # Devuelve las dimensiones de la pantalla
# ancho, alto = pyautogui.size()
# # Devuelve la posición actual
# Xactual, Yactual = pyautogui.position()
# # Mover a coordenadas (pixels)
# pyautogui.moveTo(100, 150) 
# # Clickear
# pyautogui.click() 
# # Tipear con delay
# pyautogui.write('Hello world!', interval=0.25)  
# # Apretar una tecla
# pyautogui.press('esc') 
# pyautogui.hotkey('ctrl', 'c')
# pyautogui.locateOnScreen()
# ```

# ***Nota: Para ejecutar esta sección instalar Anaconda en la computadora local. También el ejemplo de abrir paint funciona sólo en Windows. Esta es la única ocasión de todos nuestros cursos en la que un ejemplo no funcionará en colab y en todos los sistemas operativos.***

# In[6]:


get_ipython().system('pip install pyautogui')


# In[1]:


from time import sleep
import os
import pyautogui as pygui
import numpy as np


# In[2]:


def cuadrado(l):
    pygui.drag(l, 0, duration=1)
    pygui.drag(0, l, duration=1)
    pygui.drag(-l, 0, duration=1)
    pygui.drag(0, -l, duration=1)


# In[3]:


cuadrado(200)


# In[13]:


url = r'https://www.lanacion.com.ar/'


# In[14]:


sleep(2)
pygui.hotkey('ctrl', 't')
sleep(2)
pygui.write(url)
sleep(2)
pygui.press('enter')


# In[11]:


def abrir_paint():
    # Windows
    os.system('start mspaint.exe')
    sleep(1)
    S = pygui.size()
    pygui.moveTo(S[0]//2, S[1]//2)


# In[10]:


def cuadrado_espiral(l, ratio=0.9):
    pygui.move(-l//2, -l//2, duration=0.1)
    for i in range(50):
        l = l*ratio
        pygui.drag(l, 0, duration=0.1)
        l = l*ratio
        pygui.drag(0, l, duration=0.1)
        l = l*ratio
        pygui.drag(-l, 0, duration=0.1)
        l = l*ratio
        pygui.drag(0, -l, duration=0.1)
        if l < 5:
            break


# In[12]:


sleep(2)
abrir_paint()
cuadrado_espiral(600)


# Ocasionalmente hay algunos casos de uso, pero encontramos obstáculos:
# 
# - Frágil ante cambios
# - Método bruto, ad hoc
# - Solo tareas sencillas
# 
# Encontraremos el mismo dilema más adelante en _web scraping_, en un extremo el consumo de APIs y en otro la automatización del navegador.

# ## Bash y OS

# ### Interactuando con el Sistema Operativo

# In[4]:


# Con ! enviamos un comando a la terminal del sistema operativo
get_ipython().system('pwd')


# In[5]:


get_ipython().system('ls')


# Algunos comandos a saber:
# 
# - pwd : "print working directory"
# - ls: listar directorio actual
# - wget: para descargar archivos 

# In[30]:


# http://microdatos.dane.gov.co/index.php/catalog/472/get_microdata
get_ipython().system('wget -O Expo_2021.zip https://unket.s3.sa-east-1.amazonaws.com/data/Expo_2021.zip')


# In[6]:


get_ipython().system('pwd')


# In[7]:


carpeta_actual = os.getcwd()
carpeta_actual


# In[8]:


carpeta_actual.split('\\')[-1]


# Librería OS

# In[9]:


import os


# ```python
# #Devuelve el "current working directory", o directorio actual de trabajo
# os.getcwd() 
# 
# #Es por "change directory", o sea cambiar el directorio actual de trabajo
# os.chdir(path)
# 
# #recorre recursivamente el árbol de directorios, empezando por el path. 
# #en cada iteracion devuelve carpeta, [subcarpetas], [archivos]
# os.walk(path)
# 
# #crea un directorio
# os.makedirs(path)
# 
# #chequea si existe un path
# os.path.exists(path)
# 
# #borra un archivo o carpeta vacia
# os.remove(path)
# 
# #enumera el contenido del path
# os.listdir(path)
# 
# #permite cambiar paths, nombres y extensiones
# os.rename(path, new_path)
# 
# # Devuelve la ruta absoluta de una ruta relativa
# os.path.abspath(path)
# 
# ```

# Cuatro maneras de listar la carpeta actual

# In[17]:


# Con la terminal
get_ipython().system('ls')


# In[18]:


get_ipython().system('dir')


# In[19]:


# Con Python
# ruta relativa

os.listdir('.')


# In[20]:


# Con Python
# ruta absoluta

os.listdir(os.getcwd())


# Tres maneras de ver el directorio actual de trabajo

# In[21]:


os.getcwd()


# In[22]:


get_ipython().system('pwd')


# In[23]:


os.path.abspath('.')


# Ejercicio
# 
# Crear una carpeta nueva con la función ```os.makedirs()```. Recibe simplemente la ruta a la carpeta a crear

# In[24]:


new_dir = 'nueva_carpeta'

os.makedirs(new_dir)


# Ejercicio:
# 
# Cambiar el directorio de trabajo a 'nueva_carpeta' usando os.chdir

# In[25]:


os.chdir(new_dir)


# In[42]:


import zipfile

# Extraemos en la nueva carpeta
with zipfile.ZipFile('../Expo_2021.zip', "r") as zip_ref:
    zip_ref.extractall('.')   


# Buscamos todos los .zip

# In[44]:


for elemento in os.listdir('./Expo_2021/'):  
    if elemento[-4:] == '.zip':
        print(elemento)


# Ahora usando glob

# In[45]:


from glob import glob


# In[70]:


# ruta con todos los archivos
datos_path = './Expo_2021/' 


# In[49]:


zip_files = glob(datos_path + '/*.zip')
zip_files


# Hacemos un búcle para recorrer los archivos .zip y descomprimirlos en carpetas correspondientes

# In[55]:


import zipfile

# Recorremos la lista de zips
for f in zip_files:

    # Definimos el nombre de la nueva carpeta en una variable
    # Es la misma ruta "f" pero sin el ".zip"

    new_dir = f.replace('.zip', '')
    print(new_dir)

    # Extraemos en la nueva carpeta
    with zipfile.ZipFile(f, "r") as zip_ref:
        zip_ref.extractall(new_dir)


# In[57]:


# Vemos que ya estan los .zips, y carpetas correspondientes
os.listdir('Expo_2021')


# La estructura queda así:
# 
# ```
# .
# ├── Expo_2021
# │   ├── Abril
# │   │   ├── Abril.csv
# │   │   ├── Abril.dta
# │   │   └── Abril.sav
# │   ├── Abril2021.zip
# 
# ...
# 
# │   ├── Octubre
# │   │   ├── Octubre.csv
# │   │   ├── Octubre.dta
# │   │   └── Octubre.sav
# │   ├── Octubre2021.zip
# │   ├── Septiembre
# │   │   ├── Septiembre.csv
# │   │   ├── Septiembre.dta
# │   │   └── Septiembre.sav
# │   └── Septiembre2021.zip
# 
# ```

# In[61]:


# Buscamos los archivos del tipo que queremos usando glob
# Podemos cambiar el tipo cambiando la siguiente variable

# tipo = 'dta'
# tipo = 'csv'
tipo = 'sav'


# In[64]:


datos = glob(f'{datos_path}/*/*{tipo}')
datos


# In[71]:


# Chequeamos si la carpeta ya existe, y si no creamos una carpeta para guardar todos archivos los de ese tipo 

if not os.path.exists(datos_path + '/' + tipo + '_2021'):
    os.mkdir(datos_path + tipo + '_2021')


# In[83]:


# Movemos todos los que los archivos de ese tipo a la nueva carpeta
# Podemos chequear si ya está en la carpeta con os.path.exists 

for d in datos:
    # Definimos en una variable cuál va a ser la nueva ruta
    new_path = datos_path + tipo + '_2021/' + d.replace('\\', '/').split('/')[-1]
    if not os.path.exists(new_path):
        os.rename(d, new_path)


# In[85]:


# Listamos los archivos dentro de la nueva carpeta

get_ipython().system('ls {datos_path}/{tipo}_2021')


# ```
# .
# ├── Expo_2021
# │   ├── Abril2021
# │   │   ├── Abril.csv
# │   │   └── Abril.dta
# │   ├── Abril2021.zip
# │   ├── Agosto2021
# │   │   ├── Agosto.csv
# 
# ...
# 
# │   ├── Octubre2021
# │   │   ├── Octubre 2021.csv
# │   │   └── Octubre 2021.dta
# │   ├── Octubre2021.zip
# │   ├── sav_2021
# │   │   ├── Abril.sav
# │   │   ├── Agosto.sav
# │   │   ├── Diciembre.sav
# │   │   ├── Enero.sav
# │   │   ├── Febrero.sav
# │   │   ├── Julio.sav
# │   │   ├── Junio.sav
# │   │   ├── Marzo.sav
# │   │   ├── Mayo.sav
# │   │   ├── Noviembre 2021.sav
# │   │   ├── Octubre 2021.sav
# │   │   └── Septiembre.sav
# │   ├── Septiembre2021
# │   │   ├── Septiembre.csv
# │   │   └── Septiembre.dta
# │   └── Septiembre2021.zip
# ```

# En dos casos puede ser necesario recurrir a otra librería, _shutil_
# 
# Estos casos son:
# 
# - copyfile: para copiar archivos
# - rmtree: para borrar directorios
# 
# ```python
# from shutil import copyfile
# copyfile(src, dst)
# ```
# 
# Usaremos esta 2da función para limpiar los archivos que extrajimos y no necesitamos

# In[92]:


import shutil

for f in zip_files:
    
    # ¡CUIDADO!
    # Estas funciones de borrar y renombrar son potencialmente peligrosas
    # Antes de ejecutarlas con una ruta, pueden hacer un print para asegurarse de qué se haría
    
    # Borramos las carpetas de más, para eso
    # buscamos la ruta absoluta del zip. 
    # Sabemos que carpeta donde se extrajo se llama igual pero sin .zip
    zip_dir = os.path.abspath(f).split('.')[0]
    print('Borrando...', zip_dir)

    shutil.rmtree(zip_dir)

    # Borramos también los .zip
    os.remove(f)


# In[93]:


# Nos queda solo la carpeta con todos los archivos del tipo elegido, ordenados

get_ipython().system('ls {datos_path}')


# Cargamos los datos a un DataFrame

# In[94]:


from glob import glob

rutas_datos = glob(datos_path + '/*/*' + tipo)
rutas_datos


# Leemos 3 tipos de datos:
# - Stata
# - SPSS
# - csv

# In[ ]:


# para stata o SPSS
get_ipython().system('pip install pyreadstat')


# In[98]:


import pandas as pd

datos = []

for r in rutas_datos:

    if tipo == 'dta':
        # En el caso de stata necesitamos instalar la siguiente librería
        import pyreadstat

        df, metadata = pyreadstat.read_dta(r)    

    elif tipo == 'sav':
        df = pd.read_spss(r)

    elif tipo == 'csv':
        df = pd.read_csv(r, delimiter = ';')

    else:
        print('Otro tipo!')

    datos.append(df)

dataframe_total = pd.concat(datos)
dataframe_total.to_csv('todos.csv')


# In[99]:


dataframe_total.sample(3)


# In[100]:


dataframe_total.groupby('COD_PAI4')  .count()['CANTI']     .sort_values()        .iloc[-10:]           .plot.bar();


# # Práctica
# 
# 1) Tomar la siguiente lista de temas  
# 2) Crear una carpeta con su nombre en "title case"  
# 3) Dentro de cada carpeta, guardar los datos de tendencias para el día de hoy  

# In[106]:


temas = ['Python', 'IA', 'Meditación', 'Jazz Rock', 'Sustentabilidad', 'Neurociencias']


# La siguiente celda prepara y define una función _get_trends_ para buscar tendencias de Google. La misma recibe una búsqueda y devuelve un diccionario con los datos de las tendencias.

# In[104]:


get_ipython().system('pip install pytrends')

import pandas as pd                       
from pytrends.request import TrendReq

def get_trends(query):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[query])
    df = pytrend.interest_by_region()
    return df.sort_values(query, ascending=False)[query].to_dict()


# Ahora sí, recorrer la lista de temas y:
# 
# - Buscar las tendencias con la función get_trends
# - Si no existe ya la carpeta para ese tema, crearla
# - Crear un archivo .txt o .csv con los datos buscados dentro de esa carpeta

# In[72]:


# Ejemplo
query = 'Python'
tendencias = get_trends(query)
tendencias


# In[105]:


from datetime import datetime

fecha = datetime.now().strftime('%d-%m-%y')
fecha


# In[107]:


for t in temas:
    if not os.path.exists(fecha):
        os.makedirs(fecha)

    tendencias = get_trends(t)
    ruta = fecha + '/' + f"{t}.txt"

    print(f'Creando {ruta}')
    with open(ruta, 'w') as out:
        out.write(str(tendencias))

