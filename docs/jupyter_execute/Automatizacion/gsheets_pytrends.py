#!/usr/bin/env python
# coding: utf-8

# <div align="center"><a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Automatizacion/gsheets_pytrends.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg'/> </a> <br> Recordá abrir en una nueva pestaña</div>

# ## Automatización:
# 
# En esta clase veremos:
# 
# - Repaso Python
# - Interactuando con Google Sheets
# - Manipulación de strings 
# - Diccionario
# - Función Enviar Mail
# - Pytrends

# ## Preparación

# Para operar sobre Google Sheets desde Python, tenemos que contar con un archivo de autenticación y compartir el archivo a manipular con el servicio o "bot" creado. Desde Colab, vamos a poder autenticar a nuestro usuario directamente:

# In[ ]:


import gspread

# Colab
from google.colab import auth
from oauth2client.client import GoogleCredentials
#auth.authenticate_user()
#gc = gspread.authorize(GoogleCredentials.get_application_default())

# Local
get_ipython().system('pip install gspread --upgrade')
gc = gspread.service_account(filename='alumnos.json')


# In[ ]:


sheet_name = 'Alumnos'
sh = gc.open(sheet_name)
data = sh.sheet1.get_all_records()


# In[ ]:


print(type(data))
print(type(data[0]))


# In[ ]:


data


# In[ ]:


for d in data:
    print(d['Mail'].split('@')[0])


# ### Ejercicio:
# - ¿Qué estructura de datos es?
# - Los nombres donde aparece el apellido primero, darlos vuelta a la forma "Nombre Apellido"
# 

# Pseudocódigo:
#   
# 
# ```
#  para cada elemento:
#      si el nombre está al revés:
#         separar el nombre por la coma
#         invertirlo
#         unirlo
# ```

# In[ ]:


for d in data:
    if ',' in d['Nombre']:
        d['Nombre'] = ' '.join(d['Nombre'].split(',')[::-1]).strip()
data


# ### Ejercicio:
# 
# Definir la llave "Primer nombre" con el primer nombre en cada entrada
# 
# Pseudocódigo
# 
# ```
# para cada elemento:
#    separar el string
#    guardar la primer palabra en el dict con el key "primer nombre"
# ```
# 
# 

# In[ ]:


for d in data:
    d['Primer Nombre'] = d['Nombre'].split()[0]
data


# ### Ejercicio:
# 
# Guardar una lista con los dominios únicos de los mails
# 
# Pseudocódigo
# 
# ```
# para cada elemento:
#    tomar el mail
#    extraer el dominio
#    si no está en la lista
#       guardarlo
# ```
# 
# 

# In[ ]:


dominios = []

for d in data:
    dominio = d['Mail'].split('@')[1].split('.')[0]
    if dominio not in dominios:
        dominios.append(dominio)

dominios


# ### Bonus:
# 
# - Usar regular expressions

# In[ ]:


import re

dominios = []

for d in data:
    dominio = re.findall('@(\w+)\.', d['Mail'])[0]
    if dominio not in dominios:
        dominios.append(dominio)

dominios


# ## Bonus:
# 
# - En vez de una lista, hacer un diccionario con la frecuencia de cada dominio

# In[ ]:


import re

dominios = {}

for d in data:
    dominio = re.findall('@(\w+)\.', d['Mail'])[0]
    if dominio not in dominios:
        dominios[dominio] = 1
    else:
        dominios[dominio] += 1

dominios


# ### Mandando mails

# In[ ]:


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()

# Contenido
msg['From']="ejemplo.cuenta.246@gmail.com"
msg['To']="mg@ihum.ai"
msg['Subject']= "Probando mandar mails!"
msg.attach(MIMEText('Este es un mail enviado con Python', 'plain'))

# No se queden en los detalles aquí
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Usuario y contraseña
server.login("ejemplo.cuenta.246@gmail.com", "Ejemplo246")

# enviar
server.send_message(msg)
server.quit();


# ## Ejercicio: 
# - Hacer una función con el código anterior para mandar mails

# In[ ]:


def mandar_mail(usuario, contra, receptor, asunto, contenido):
    msg = MIMEMultipart()

    # Contenido
    msg['From']= usuario
    msg['To']= receptor
    msg['Subject']= asunto
    msg.attach(MIMEText(contenido, 'plain'))

    # No se queden en los detalles aquí
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Usuario y contraseña
    server.login(usuario, contra)

    # enviar
    server.send_message(msg)
    server.quit();


# ## Ejercicio
# 
# Enviando mail
# 
# - Hacer un búcle que rellene la plantilla para cada diccionario
# - Definir un string como plantilla para rellenar con "Primer Nombre" y "Tema"
# - Si el mail es el tuyo... enviar el mail con la plantilla. Si no, hacer print
# - Mostrar "Enviando mail a..." con el mail a quien se envió

# In[ ]:


mi_nombre = 'Matías Grinberg'
plantilla = '¡Hola! {nombre}. Tu tema es {tema}'

for d in data:
    texto = plantilla.format(nombre=d['Primer Nombre'], tema=d['Tema'])

    if d['Nombre'] == mi_nombre:
        mandar_mail("ejemplo.cuenta.246@gmail.com", "Ejemplo246", d['Mail'], "Tema", texto)
        print(f'Enviando Mail a {d["Mail"]}')
    else:
        print(texto)


# ## Bonus
# 
# Usar la función .update_cell() del objeto sh para anotar "OK" en una nueva columna llamada "Mail Enviado", donde corresponda

# In[ ]:


enviado_idx = sheet.find('Enviado').col

mi_nombre = 'Matías Grinberg'
plantilla = '¡Hola! {nombre}. Tu tema es {tema}'

for d in data:

    texto = plantilla.format(nombre=d['Primer Nombre'], tema=d['Tema'])

    if d['Nombre'] == mi_nombre:
        mandar_mail("ejemplo.cuenta.246@gmail.com", "Ejemplo246", d['Mail'], "Tema", texto)
        print(f'Enviando Mail a {d["Mail"]}')
        sh.update_cell(row_idx, enviado_idx, 'OK')
    else:
        print(texto)


# # Bonus
# 
# Usar la siguiente función para conseguir las  tendencias de Google para el tema de cada persona

# In[ ]:


get_ipython().system('pip install pytrends')


# In[ ]:


import pandas as pd                        
from pytrends.request import TrendReq

def get_trends(query):
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=[query])
    df = pytrend.interest_by_region()
    return df.sort_values(query, ascending=False)[query].to_dict()


# In[ ]:


query = 'Python'
tendencias = get_trends(query)


# In[ ]:


tendencias


# In[ ]:


mi_nombre = 'Matías Grinberg'
plantilla = '¡Hola! {nombre}. Tu búsqueda de <b>"{tema}"</b> trajo los siguientes resultados: \n {resultados} \n ¡Saludos! MatiBot'

for d in data:
    tendencias = get_trends(d['Tema'])  
    texto = plantilla.format(nombre=d['Primer Nombre'], tema=d['Tema'], resultados=tendencias)

    if d['Nombre'] == mi_nombre:
        mandar_mail("ejemplo.cuenta.246@gmail.com", "Ejemplo246", d['Mail'], "Tema", texto)
        print(f'Enviando Mail a {d["Mail"]}')
    else:
        print(texto)


# ¡Eso es todo por hoy!
