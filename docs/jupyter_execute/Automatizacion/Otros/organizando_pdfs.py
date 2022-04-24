#!/usr/bin/env python
# coding: utf-8

# <div align="center"><a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Automatizacion/organizando_pdfs.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg'/> </a> <br> Recordá abrir en una nueva pestaña </div>

# # Ejercicio: Organizando PDFs
# 
# Supongamos que tenemos una carpeta con muchos artículos científicos bajados de ArXiv como [este](https://arxiv.org/abs/hep-th/9711200) de Maldacena, el renombrado físico argentino. En esta notebook vamos a usar [textract](https://textract.readthedocs.io/en/stable/) para leer textos de PDFs y así:
# 
# - Reemplazar el título de algo como "9711200.pdf" al título del trabajo
# - Categorizar los trabajos
# - Crear carpetas por categoría
# - Mover los artículos a cada una de las carpetas

# In[1]:


# instalamos la librería que vamos a utilizar
get_ipython().system('pip install textract')


# In[81]:


import textract
import os
from shutil import copyfile


# In[110]:


# descargamos los papers ejemplo
get_ipython().system('wget https://unket.s3.sa-east-1.amazonaws.com/data/papers.zip')
# si ejecutan localmente o no tienen unzip en la terminal, descomprimir a mano
get_ipython().system('unzip papers.zip')


# In[111]:


# la ruta a la carpeta con los trabajos
pdf_dir = r"./papers"


# In[112]:


# listamos todos los archivos de esa carpeta
files = os.listdir(pdf_dir)


# Creamos un directorio para cada una de las 3 categorías, "Neuro", "Deep" (para Deep Learning) y "Otros".

# In[113]:


ruta_neuro = 'Neuro'
os.makedirs(ruta_neuro, exist_ok=True)


# In[114]:


ruta_deep = 'Deep'
os.makedirs(ruta_deep, exist_ok=True)


# In[115]:


ruta_otros = 'Otros'
os.makedirs(ruta_otros, exist_ok=True)


# Vamos a necesitar una función para extraer el título. Como no queremos usar regex todavía (se ve próximamente), vamos a usar también esta siguiente función para limpiar un renglón para ver si tiene el largo suficiente para ser un título. 

# In[269]:


def limpiar(string):
    """Función para limpiar los renglones quitando los caracteres que no queremos considerar"""
    
    # \w+ significa "1 o más de un caracter alfanumérico". Ver más en la clase 
    # de regex
    
    # versión sin regex:
    # no_valen = '0123456789-:\.'
    # return ''.join([i for i in string if i not in no_valen])
    
    return ''.join(re.findall('\w+', string))


# In[270]:


def get_title(texto, largo_min=20):
    """Función para extraer un título. Podríamos mejorar la lógica o usar distintos enfoques"""  
    renglones = [t for t in texto.split('\n') if len(limpiar(t)) > largo_min]
    if len(renglones) > 0:
        return renglones[0]
    else:
        return None


# Ahora, recorremos cada archivo y para cada uno vamos a:
# - Leer el texto con textract
# - Extraer el título
# - Estimar la categoría
# - Mover y renombrarlo

# In[273]:


for filename in files:
    # ruta completa al archivo
    full_name = os.path.join(pdf_dir, filename)
    # de pdf a texto
    text = textract.process(full_name, language='eng').decode()
    # asumimos que el título está en los primeros 1000 caracteres
    top = text[:1000]
    
    # vamos a intentar extraer el titulo con nuestra función
    # si no encontramos un sub-string que cumpla con las condiciones, 
    # mantenemos el nombre original
    title = get_title(top)
    if title == None:
        title = filename.replace('.pdf', '')
        
    # para categorizar los textos, vamos a usar esta lógica sencilla:
    # nos fijamos si contiene alguno de los siguientes términos clave
    is_deep = ('deep learning' in text.lower()) or ('statistic' in text.lower())
    is_neuro = ('neuro' in text.lower()) or ('brain' in text.lower())
    
    # para cada texto, lo vamos a mover a su carpeta y vamos a mostrar su categoría
    print(title)
    if is_neuro:
        print('Neuro')
        copyfile(f"{pdf_dir}/{filename}", f"{ruta_neuro}/{title}.pdf")
    elif is_deep:
        print('Deep')
        copyfile(f"{pdf_dir}/{filename}", f"{ruta_deep}/{title}.pdf")
    else:
        print('Otros')
        copyfile(f"{pdf_dir}/{filename}", f"{ruta_otros}/{title}.pdf")    
    print()

