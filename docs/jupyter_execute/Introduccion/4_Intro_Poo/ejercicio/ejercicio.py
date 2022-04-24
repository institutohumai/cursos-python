#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Introduccion/4_Intro_Poo/ejercicio/ejercicio.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# # Ejercicios POO IV
# 
# ## Programación orientada a objetos
# 
# En este ejercicio vamos a programar un carrito de compras.
# 
# Para esto vamos a escribir dos clases: Carrito e Item.
# 
# El ítem va a tener como propiedades un nombre, un precio y una url de la imágen que lo representa. Por default, la url se inicializa en blanco.
# 
# El Carrito tiene como propiedad una lista de diccionarios, la variable _lineas. 
# 
# Los carritos se inicializan vacíos y luego se agregan líneas utilizando el método agregar_línea(). Cada línea es un diccionario con dos claves: "ítem" que contiene un objeto de tipo ítem y "cantidad" según la cantidad que queremos agregar al carrito.
# 
# Por último los carritos tienen un método get_total() que devuelve la suma de los precios de los ítems, multiplicados por las cantidades que hay en cada línea.

# In[ ]:


# Clase Item


# In[ ]:


# Crear los ítems banana de $49.5 y yoghurt de $32.5


# In[ ]:


# Crear la clase Carrito


# Ahora vamos a instanciar el carrito y agregarle una "línea" con dos bananas y otra con tres yoghures.

# In[ ]:


# Instancias el carrito


# In[ ]:


# Agregar bananas


# In[ ]:


# Agregar yoghures


# In[ ]:


# Obtener el total


# In[ ]:




