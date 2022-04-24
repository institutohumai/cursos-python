#!/usr/bin/env python
# coding: utf-8

# <div align="center"><a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Automatizacion/Automatización_2/clase_automatizacion_2_gsheets_cron_mails.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg'/> </a> <br> Recordá abrir en una nueva pestaña </div>

# # Automatización II: outputs, envío de mail, volcado a GSheets, scheduling
# 
# ### Hoja de ruta
# 
# -   Ejemplo scrapeo sencillo con *Pandas*.					
# -   Uso de la API de *Google Sheets*.							
# -   Carga de datos en *Google Data Studio* y creación de un gráfico sencillo.
# -   Ejemplo envío automático de mail con *smtplib*.				 	
# -   Scheduling: cron para Mac y linux, GUI en Windows.					

# ## Scrapping con Pandas
# 
# 
# 
# Vamos a utilizar la librería de pandas para obtener las tablas que contiene una página. 
# 
# Documentación: https://pandas.pydata.org/docs/reference/api/pandas.read_html.html

# In[ ]:


import pandas as pd
import numpy as np

pd.set_option('display.float_format', lambda x: '%.7f' % x)


# In[ ]:


# Datos de criptomonedas
url = "https://coinmarketcap.com/new/"


# Ahora con *pandas.read_html()* es posible conseguir una lista con las tablas que contiene una *url*.

# In[ ]:


listadoTablas = pd.read_html(url)


# In[ ]:


listadoTablas[0].info()


# Seleccionamos la tabla de las criptomonedas recientemente añadidas.

# In[ ]:


df = listadoTablas[0].copy()
df.drop(['#','Unnamed: 10', 'Unnamed: 0'], axis=1, inplace=True) # Eliminamos columna valores nulos.
df.columns = ['Name', 'Price', 'PctChnge_1h', 'PctChnge_24h', 'FullDiluted_MarketCap', 'Volume', 'Blockchain', 'Added_HoursAgo']
df.replace('--', '0', inplace=True) # Imputamos valores nulos como 0 
df.replace('\.\.\.', '', regex=True, inplace=True) #Para liberarnos de los tres puntos. OJO: No devuelve el valor real, sino que le sacamos ceros. 
df.fillna('', inplace=True)
df.head(20)


# In[ ]:


# Convertimos a los tipos deseados

df['Price'] = df['Price'].replace( '[\$,)]','', regex=True ).astype(float)
df['FullDiluted_MarketCap'] = df['FullDiluted_MarketCap'].replace( '[\$,)]','', regex=True )
df['Volume'] = df['Volume'  ].replace( '[\$,)]','', regex=True ).astype(float)
df['PctChnge_1h'] = df['PctChnge_1h'].replace( '[\%,)]','', regex=True ).astype(float)/100
df['PctChnge_24h'] = df['PctChnge_24h'].replace( '[\%,)]','', regex=True ).astype(float)/100
df['Added_HoursAgo'] = df['Added_HoursAgo'].apply(lambda x: x[0])


# In[ ]:


df.head()


# ## **Vinculación con Google Drive**
# 
# Para poder escribir/leer un archivo que se encuentra en *Google Drive*, será necesario primero, contar con un archivo de *autenticación* a su vez que compartir el archivo pertinente con el servicio creado desde Python.

# #### Generación de archivo de autenticación. (Conexión local)
# 
# Para ello entraremos en el siguiente [link](https://console.cloud.google.com/apis/) ingresando con la cuenta de google que querramos vincular. Una vez dentro de la plataforma de Google Cloud, crearemos un proyecto. Una vez dentro del proyecto entraremos en la sección **API y servicios** y daremos click en la opción **habilitar API y servicio**.
# 
#   <img src="https://unket.s3.sa-east-1.amazonaws.com/static/gcp1.png" alt="drawing" width="500"/>

# Allí dentro seleccionaremos el tipo de API que estemos necesitando. En este caso la de Google Drive y Google Sheets. Una vez habilitada la API dentro de nuestro proyecto, iremos a la sección de **credenciales**, y dentro de la misma daremos click a **crear credenciales**. Seleccionamos la opción de *Cuenta de servicio*. Una vez que la *Cuenta de servicio* haya sido generada, será posible acceder a sus configuraciones y generar una clave en formato json dentro de la misma.
# 
# <img src="https://unket.s3.sa-east-1.amazonaws.com/static/gcp2.png" alt="drawing" width="500" height="300"/> <img src="https://unket.s3.sa-east-1.amazonaws.com/static/clave2.png" alt="drawing" width="500"/>
# 
# Más información sobre como crear un proyecto y habilitar una API [aquí](https://developers.google.com/workspace/guides/create-project)

# In[ ]:


# Esta funcion incluye todo lo que hicios antes, para poder actualizar nuestro DataFrame
def coinmarketcap_scraper():
  """Scraper de la pagina https://coinmarketcap.com/new/
  Obtiene los datos, los limpia y los devuelve como un DataFrame de Pandas.
  """
  url = "https://coinmarketcap.com/new/"
  
  # Scrapeamos la tabla con Pandas
  listadoTablas = pd.read_html(url)
  
  # creamos DataFrame
  df = listadoTablas[0].copy()

  # Limpieza de datos
  df.drop(['#','Unnamed: 10', 'Unnamed: 0'], axis=1, inplace=True) # Eliminamos columna valores nulos.
  df.columns = ['Name', 'Price', 'PctChnge_1h', 'PctChnge_24h', 'FullDiluted_MarketCap', 'Volume', 'Blockchain', 'Added_HoursAgo']
  df.replace('--', '0', inplace=True) # Imputamos valores nulos como 0 
  df.replace('\.\.\.', '', regex=True, inplace=True) #Para liberarnos de los tres puntos. OJO: No devuelve el valor real, sino que le sacamos ceros. 
  df.fillna('', inplace=True)
  df.head(20)

  # Convertimos a los tipos deseados
  df['Price'] = df['Price'].replace( '[\$,)]','', regex=True ).astype(float)
  df['FullDiluted_MarketCap'] = df['FullDiluted_MarketCap'].replace( '[\$,)]','', regex=True ).astype(float)
  df['Volume'] = df['Volume'].replace( '[\$,)]','', regex=True ).astype(float)
  df['PctChnge_1h'] = df['PctChnge_1h'].replace( '[\%,)]','', regex=True ).astype(float)/100
  df['PctChnge_24h'] = df['PctChnge_24h'].replace( '[\%,)]','', regex=True ).astype(float)/100
  df['Added_HoursAgo'] = df['Added_HoursAgo'].apply(lambda x: x[0])

  return df


# ### Usando gspread para interactuar con las hojas de cálculo de Google
# 
# Documentación: https://docs.gspread.org/en/v5.3.0/
# 

# In[ ]:


# Instalamos y hacemos un upgrade de gspread porque la funcion que necesitamos esta a partir de la version 3.6
get_ipython().system('pip install gspread --upgrade')


# Importamos la libreria gspread y chequeamos la version 

# In[ ]:


import gspread
print(f'Version de gspread:{gspread.__version__}')


# #### Interactuamos con Google Sheets.
# 
# Creamos una nueva hoja de calculo con su debido título y la compartimos con la cuenta desde la cual querramos acceder.

# **Autenticación local**
# * Documentación: https://docs.gspread.org/en/latest/oauth2.html

# In[ ]:


# Paso 1: Accedemos a nuestra cuenta y creamos la hoja de calculo

gc = gspread.service_account(filename='/content/credenciales_gsheets.json')

nombre = 'humai2'
hoja_de_calculo = gc.create(nombre)

# Para hacer visible el archivo es necesario compartirlo
tu_mail = 'mi_mail@mail.com'
hoja_de_calculo.share(tu_mail, perm_type='user', role='writer')


# In[ ]:


# Paso 2: Compartir la hoja con el 'client_email' que viene en el json
# Para eso simplemente abrimos nuestra hoja, vamos a 'Compartir' y ahi agregamos el mail que encontramos 
#en el json como si fuera un usuario mas


# In[ ]:


# Paso 3: Abrimos accedemos al documento 
# Abrimos el documento
hoja_de_calculo = gc.open("humai2")

# Agarramos la primera de las hojas 
worksheet = hoja_de_calculo.sheet1

# Actualizo la hoja
worksheet.update([df.columns.values.tolist()] + df.values.tolist())


# In[ ]:


# Paso 4: Obtenemos los valores desde nuestra hoja de calculo

nuestra_hoja = worksheet.get_all_values()

# Cargamos con Pandas
df_aux = pd.DataFrame(nuestra_hoja)
df_aux.columns = df_aux.iloc[0,:]
df_aux = df_aux.iloc[1:,:]
df_aux.head()


# In[ ]:



# actualizamos el df
df = coinmarketcap_scraper()
df


# **Otorgar acceso desde Google Colab**
# 
# * En caso de acceder desde Google Colab resulta más sencillo autenticarse dado que lo hace automaticamente con la cuenta linkeada.
# 
# * Una vez que ya tenemos nuestro objeto ```gc``` podemos trabajar usando los mismos métodos que en el caso local.

# In[ ]:


# Autenticarse con Colab
import gspread
from google.auth import default
creds, _ = default()
gc = gspread.authorize(creds)


# ## **Interacción con Google Data Studio**
# 
# <img src='https://www.mdmarketingdigital.com/blog/wp-content/uploads/2019/06/Data-Studio-Stats-1200x700.png' width=500>
# 
# 
# 
# [Google Data Studio](https://datastudio.google.com/) es una herramienta en línea para convertir datos en paneles e informes  personalizables

# ## **Envio automatico de e-mails**
# 
# En esta sección haremos un ejemplo de como enviar mails desde Python 
# 
# ### **Protocolo SMTP**
# El protocolo para transferencia simple de correo (en inglés: Simple Mail Transfer Protocol o SMTP) es un protocolo de red utilizado para el intercambio de mensajes de correo electrónico entre computadoras u otros dispositivos (PDA, teléfonos móviles, impresoras, etcétera).
# 
# ### Usando Python
# 
# Para poder usar Python desde gmail tendremos que habilitar el uso de "aplicaciones poco seguras". 
# 
# <img src='https://docs.rocketbot.co/wp-content/uploads/2020/01/c3.png' >
# <img src='https://docs.rocketbot.co/wp-content/uploads/2020/01/c4-768x244.png' >
# <center>
# Fuente: https://docs.rocketbot.co/?p=1567
# </center>
# 
# * Si tienen problemas mirar aca: https://stackoverflow.com/questions/26852128/smtpauthenticationerror-when-sending-mail-using-gmail-and-python
# 
# 

# In[ ]:


import smtplib
from email.message import EmailMessage

msg = EmailMessage()

# Contenido
msg['From']="curso_de_automatizacion_de_humai@gmail.com"
msg['To']="mi_mail@mail.com"
msg['Subject']= "Probando mandar mails!"
cuerpo_del_mail = 'Este es un mail enviado con Python en la clase! =D'
msg.set_content(cuerpo_del_mail)

# No se queden en los detalles aquí, pero pueden leer más sobre el protocolo SMTP acá: https://es.wikipedia.org/wiki/Protocolo_para_transferencia_simple_de_correo 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Usuario y contraseña
usuario = 'mi_usuario'

server.login(usuario, password)

# enviar
server.send_message(msg)
server.quit();


# ### Enviar más de un mail
# 
# Podría existir el caso de uso donde querramos enviar más de un mail. Por ejemplo a todes nuestres alumnes con la nota de su parcial.

# In[ ]:


import smtplib
from email.message import EmailMessage
import time

notas  = [10, 8 , 7]
alumnes = ['Lupe', 'Juan', 'Sofia']
mails = ['Juan@mail.com', 'Sofia@mail.com', 'Lupe@mail.com']

# Usuario y contraseña
usuario = 'mi_usuario'


with smtplib.SMTP('smtp.gmail.com', 587) as server:
  for i in range(len(notas)):
    # Contenido
    msg = EmailMessage()

    msg['From']="curso_de_automatizacion_de_humai@gmail.com"
    msg['To']="tu_mail@mail.com" # Obviamente habria que ir variando los mails, aca no lo voya hacer pero seria poner mails[i]
    msg['Subject']= "Probando mandar mails!"
    cuerpo_del_mail = f'Hola {alumnes[i]}, tu nota en el parcial fue de {notas[i]}.\n\nSaludos!'
    msg.set_content(cuerpo_del_mail)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(usuario, password)
    # server.starttls()

    # enviar
    server.send_message(msg)
    time.sleep(3)
    print(f'mail enviado a {alumnes[i]}')


# ### Enviar archivos adjuntos
# 
# Podemos agregar archivos adjuntos como por ejemplo imágenes o PDFs.

# In[ ]:


# Enviar archivos adjuntos

import smtplib
# El módulo imghdr determina el tipo de imagen contenida en un archivo.
import imghdr
from email.message import EmailMessage

msg = EmailMessage()

# Contenido
msg['From']="curso_de_automatizacion_de_humai@gmail.com"
msg['To']="mi_mail@gmail.com"
msg['Subject']= "Probando mandar mails!"
cuerpo_del_mail = 'Te estoy enviando una imagen con Python! =D'
msg.set_content(cuerpo_del_mail)

path_imagen = '/content/humai_logo.png' 

with open(path_imagen, 'rb') as f:
    image_data = f.read()
    # Para saber el tipo de archivo
    image_type = imghdr.what(f.name)
    image_name = f.name

msg.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

# No se queden en los detalles aquí, pero pueden leer más sobre el protocolo SMTP acá: https://es.wikipedia.org/wiki/Protocolo_para_transferencia_simple_de_correo 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Usuario y contraseña
usuario = 'mi_usuario'


server.login(usuario, password)

# enviar
server.send_message(msg)
print('Mail enviado')
server.quit();


# ## Scheduling con CRON
# 
# En el sistema operativo Unix, cron es un administrador regular de procesos en segundo plano (demonio) que ejecuta procesos o guiones a intervalos regulares (por ejemplo, cada minuto, día, semana o mes). Los procesos que deben ejecutarse y la hora a la que deben hacerlo se especifican en el archivo crontab. 
# 
# <img src="https://i.ibb.co/ZWCbc2m/crontab.png" alt="crontab" border="0">
# 
# 
# Cron se puede definir como el equivalente a Tareas Programadas de Windows.
# 
# <img src='https://www.solvetic.com/uploads/monthly_01_2017/tutorials-9832-0-90051600-1484655732.png'> <br>
# Fuente: https://www.solvetic.com/tutoriales/article/3441-como-abrir-y-configurar-programador-tareas-windows-10/
# 
# 
# 
# 

# ### Comandos básicos de Cron
# 
# En la terminal: <br>
# **`crontab -l`** -> Permite ver la lista de las tareas programadas <br>
# **`crontab -e`** -> Permite ver editar las tareas programadas
# 
# <font color='red'><h3>ATENCION! </h3></font>
# 
# **`crontab -r`** -> Permite borrar las tareas programadas  <br>
# Es importante que lo uses cuando quieras que tu tarea deje de ser ejecutada, sino va a quedar funcionando indefinidamente 

# In[ ]:


# ┌───────────── Minutos (0 - 59)
# │ ┌───────────── Hora (0 - 23)
# │ │ ┌───────────── Dia del mes (1 - 31)
# │ │ │ ┌───────────── Mes (1 - 12) o jan,feb,mar,apr,may,jun,jul... (meses en inglés)
# │ │ │ │ ┌─────────────  día de la semana (0-6) (domingo=0 o 7) o sun,mon,tue,wed,thu,fri,sat (días en inglés) 
# │ │ │ │ │                                       
# │ │ │ │ │
# │ │ │ │ │
# * * * * *  comando_a_ejecutar


# Algunos ejemplos:
# 
# Todos los dias a las 12 y media del mediodia corre esto
# 
# `30 12 * * * python /ruta/a/mi/archivo/script.py`
# 
# El 10 de cada mes corre esto a las 3 de la tarde
# 
# ` * 3 10 * * python /ruta/a/mi/archivo/script.py`
# 
# Consideraciones
# * Dependiendo del intérprete de Python que tengan instalado pueden tener que poner algo distinto a la palabra python. Ejemplo:
# ` * * * * * python3 /ruta/a/mi/archivo/script.py`
# 
# * Otra forma es que cron se posicione en la ruta del archivo y luego solo lo corra. Ejemplo:
# `* * * * * cd /ruta/a/mi/archivo && python script.py`
# 

# In[ ]:


def escribir_archivo():
	with open('prueba.txt', 'a+') as f:
		f.write('Esribiendo archivo desde Cron\n')
		
if __name__ == '__main__':
	escribir_archivo()


# ### Recursos
# 
# * Google Data Studio
#   * https://datastudio.google.com/gallery les recomendamos ver la galeria para inspirarse y ver todo lo que se puede hacer con esta herramienta
# 
# 
# * cron: 
#   * [Video de Corey Schafer](https://www.youtube.com/watch?v=QZJ1drMQz1A&t=12s&ab_channel=CoreySchafer) , aunque esta en ingles se los super recomiendo
#   * https://crontab.guru/ Ayuda a escribir los comandos de cron
# 
# 
