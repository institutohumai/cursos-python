#!/usr/bin/env python
# coding: utf-8

# - Scrapear una lista de nombres
# - Generar strings aleatorios
# - Armar una archivo txt con la siguiente estructura:

# In[ ]:


import pandas as pd
import numpy as np
import string
from numpy.random import choice

data = pd.read_html('https://buenosaires.gob.ar/areas/registrocivil/nombres/busqueda/imprimir.php')[0]['Nombres']

texto = ''
for i in range(1000):
    nombre, apellido = data['Nombre'].sample(2).values
    cuit = ''.join([str(n) for n in np.random.randint(0, 9, 10)])
    mail = nombre[0].lower() + apellido[0].lower() + str(choice(range(1800, 2023))) + '@' + ''.join(choice(list(string.ascii_lowercase), 4)) + choice(['.com', '.com.ar', '.org', '.ai'])
    id_ = ''.join(choice(list(string.ascii_lowercase)+list(string.ascii_uppercase)+list(range(9)), 12))
    s = f"""Datos del Empleador: {nombre} {apellido}\nCUIT: {cuit} \nContacto: {mail} \nN-ID: {id_}\n"""
    texto += s

fp = 'datos_empleados.txt'
with open(fp, 'w') as out:
    out.write(texto)

from google.colab import files
files.download(fp)

