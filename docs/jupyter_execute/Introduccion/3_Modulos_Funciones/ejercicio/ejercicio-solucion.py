#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Introduccion/3_Modulos_Funciones/ejercicio/ejercicio-solucion.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# ## Factoriales
# 
# El factorial de un número natural es la multiplicación de todos los números anteriores hasta llegar a 1. Por ejemplo el factorial de 5 es igual a $5*4*3*2*1$, es decir, 120.
# 
# Igual que con la serie Fibonacci, hay dos formas de resolver este problema: una con un loop for y la otra utilizando funciones recursivas.  Recuerden que cada función recursiva tiene que tener una condición terminal.
# En el caso de Fibonacci, la condición terminal es que fibo(1) = 1. 
# 
# En el caso de factorial, la condición terminal será factorial(1) = 1 
# 
# Escriban ahora las dos versiones posibles de la función factorial(x). 

# In[1]:


# Solución recursiva. 

def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)


# In[6]:


# Solución iterativa. 

def factorial(x):
    resultado = 1
    for i in range(1, x+1):
        resultado = resultado * (i)
    return resultado


# Ahora construyan un módulo que se llame "operaciones" con cualquiera de las dos versiones de la función y luego invoquen a la función factorial del módulo.

# In[10]:


# Escriban el archivo operaciones.py
with open('operaciones.py', 'w') as out:
    out.write("""def factorial(x):
    resultado = 1
    for i in range(1, x+1):
        resultado = resultado * (i)
    return resultado""")


# In[11]:


# Importen operaciones
import operaciones


# In[12]:


# Invoquen con cualquier valor a operaciones.factorial()
operaciones.factorial(4)


# In[ ]:




