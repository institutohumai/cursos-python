#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Introduccion/2_Listas_Y_Funciones/ejercicio/ejercicio.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>
# 

# # Ejercicios II

# ## El contador de palabras
# 
# Una revista científica quiere publicar los abstracts de los trabajos que aprobó recientemente pero primero tiene que asegurarse de que ninguno de los abstracts tenga más de 200 palabras. 
# 
# Para interactuar con los archivos que tenemos en nuestro "file system" vamos a utilizar el módulo os. No se preocupen por entender todos los detalles ahora, vamos a ir profundizando en la utilización de módulos. 

# In[ ]:


get_ipython().system('wget https://datasets-humai.s3.amazonaws.com/datasets/publicaciones.zip')


# In[ ]:


get_ipython().system('unzip publicaciones.zip')


# In[ ]:


import os


# In[ ]:


archivos_directorio = os.listdir('publicaciones')


# In[ ]:


print(archivos_directorio)


# La función listdir nos devuelve una lista con todos los archivos que están en la carpeta publicaciones. Noten que solamente nos devuelve los nombres de los archivos, no la ruta completa que necesitamos para acceder a los mismos desde la ubicación en el filesystem donde se encuentra esta notebook.
# 
# Las rutas hasta los archivos cambian con el sistema operativo, por eso si están en Windows, la forma de acceder al archivo Yukon Delta Salmon Management.txt es ejercicios\\Yukon Delta Salmon Management.txt mientras que si están en Linux o Unix la forma de acceder es ejercicios/Yukon Delta Salmon Management.txt .  Para evitar problemas y que el código sea ejecutable desde cualquier sistema operativo, el módulo os tiene la función os.join.
# 
# Entonces para crear las rutas vamos a usar la función os.path.join y para esto es ideal una lista por comprensión

# In[ ]:


rutas_archivos = [os.path.join('publicaciones',archivo) for archivo in archivos_directorio]


# In[ ]:


rutas_archivos


# Ahora vamos a unir estas dos listas del mismo tamaño en una lista de tuplas utilizando la función "zip" de Python nativo. Como el zip de Python devuelve un objeto iterable, vamos a convertirlo en lista para trabajar mejor

# In[ ]:


tuplas_archivos = list(zip(rutas_archivos,archivos_directorio))


# In[ ]:


for tupla in tuplas_archivos:
    print(tupla)


# Ahora sí, vamos a pedirles que creen una función que reciba una tupla con la ruta y el nombre del archivo. Necesitamos que esta función cuente las palabras que hay en el txt que se encuentra en esa ruta y luego imprima el nombre del archivo y la cantidad. 
# Después vamos a escribir un for loop que recorra la lista tuplas_archivos y devuelve una tupla con el nombre del archivo y la cantidad de palabras. Desde el loop for vamos a imprimir esa tupla.
# 

# In[ ]:


# 1. Escribir la función 


# In[ ]:


# 2. Recorrer en un loop tuplas_archivos invocando a la función


# Entonces ¿Cuáles superan las 250 palabras? Si quieren ir una milla extra modifiquen la función para que devuelva True si supera y False si no supera en lugar de devolver la cantidad. 

# In[ ]:


# 3. Modifiquen la función


# In[ ]:


#4. Vuelvan a llamarla


# In[ ]:




