#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Introduccion/1_TiposDatos/ejercicio/ejercicios-solucion.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>
# 

# # 1- Cambiar un texto
# 
# Necesitamos mostrar en nuestra web la sinopsis de las películas. El problema es que tenemos los textos separados por pipes ("|") en lugar de saltos de línea. 

# In[1]:


string = 'Sinopsis | Marty McFly, un típico adolescente americano de los años ochenta, ''es accidentalmente enviado de vuelta a 1955 en una "máquina del tiempo" realizada con''un DeLorean inventada por un científico un poco loco. | En este viaje, Marty debe ''asegurarse de que sus padres se encuentren y se enamoren, para que pueda volver a su tiempo. '


# In[2]:


print(string)


# ¿Cómo podríamos hacer para que la función "print" muestre saltos de línea en lugar de pipes?

# In[3]:


string2 = string.replace('|','\n')


# In[4]:


print(string2)


# # 2 - Crear un acrónimo
# 
# Ahora nos piden crear un acrónimo (una palabra compuesta por la primera letra de cada palabra) de cada título. Pero antes de eso es necesario que transformemos los títulos a "title case" porque no todos van a llegar prolijos. Entonces, el acrónimo de "Volver al futuro" debería ser "VAF".
# 

# In[5]:


titulo = 'Volver al futuro'


# In[ ]:


# 1. Transformar el string a "title case"


# In[6]:


titulo = titulo.title()


# In[ ]:


# 2. Crear una lista con todas las palabras del string


# In[8]:


# 3. Recorrer la lista y agregar al acrónimo la primera letra de cada palabra
acronimo = ''
lista_palabras = titulo.split(' ')


# In[9]:


for palabra in lista_palabras:
    acronimo = acronimo + palabra[0]


# In[10]:


print(acronimo)


# In[ ]:




