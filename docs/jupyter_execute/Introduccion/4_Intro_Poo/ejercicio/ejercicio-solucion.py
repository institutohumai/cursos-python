#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Introduccion/4_Intro_Poo/ejercicio/ejercicio-solucion.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

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

# In[1]:


# Clase Item

class Item():
    def __init__(self, nombre, precio, url_imagen=''): 
        """ 
        Todas las propiedades del ítem son obligatorias menos url_imagen
        En el ítem todas las propiedades son "públicas". Esto va a ser útil para acceder al precio desde el carrito.
        """
        self.nombre = nombre
        self.precio = precio
        self.url_imagen = url_imagen


# In[2]:


# Crear los ítems banana de $49.5 y yoghurt de $32.5

banana = Item("banana",49.5)
yoghurt = Item("yoghurt",32.5)


# In[3]:


# Crear la clase Carrito

class Carrito():
    def __init__(self): 
        """ 
        El Carrito siempre se inicializa con una lista de Ítems.
        En el carrito la única propiedad es privada. 
        """
        self._lineas = []
        
    def get_total(self):
        total = 0
        for linea in self._lineas:
            total = total + (linea['cantidad'] * linea['item'].precio)
        return total
            
    def agregar_item(self,linea):
        self._lineas.append(linea)


# Ahora vamos a instanciar el carrito y agregarle una "línea" con dos bananas y otra con tres yoghures.

# In[4]:


# Instancias el carrito
carrito = Carrito()


# In[5]:


# Agregar bananas
carrito.agregar_item({'item':banana,'cantidad':2})


# In[6]:


# Agregar yoghures
carrito.agregar_item({'item':yoghurt,'cantidad':3})


# In[7]:


# Obtener el total
carrito.get_total()


# In[ ]:




