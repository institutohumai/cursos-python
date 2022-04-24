#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Introduccion/2_Listas_Y_Funciones/ejercicio/adicionales.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# # Ejercicios Adicionales II
# 
# Estos ejercicios tienen un nivel de dificultad un poco mas elevado. Cada ejercicio tiene una función de test para chequear si lo que hicieron esta bien. 

# In[ ]:


get_ipython().system('wget https://datasets-humai.s3.amazonaws.com/datasets/test_intro_clase2.zip')
get_ipython().system('unzip test_intro_clase2.zip')


# In[ ]:


from test import *


# ### Juego de espías (Fácil)
# El espía Ramsay debe codificar los mensajes que le mandan otros espías sobre la cantidad de tropas que tiene el enemigo en distintos cuarteles. Para esto, otro espía le manda una tira de números con un pequeño truco. Esta tira de números estan separados por `-`, pero para que no sea tan fácil saber que esta informando, la cantidad de tropas esta levemente escondida y también esta escondido el número del cuartel. El cuartel estará escondido en el último lugar de la tira y para obtener la cantidad de tropas aproximadas se deben sumar todos los números que son divisibles por el número del cuartel de la tira. Crear una función que reciba el string de la tira de números y devuelva la cantidad de tropas que hay en el cuartel enemigo como una tupla. Adicionalmente, podria imprimir un mensaje con la información requerida.
# 
# Ej:
# ```Python
# INPUT:
# tira_numeros = '29-32-1-5-65-12345-0-12-2'
# OUTPUT: 
# (2, 44)
#     "En el cuartel número 2 hay 44 soldados"
# ```

# In[ ]:


# Corre para ver si tu código esta bien
def informe_espia(tira_numeros):
    # Hacer la magia
    
    return (cuartel,informe)


# In[ ]:


test1(informe_espia)


# ***
# ### Codificador César (Intermedio)
# Una de las formas mas antiguas de crear un código encriptado es lo que se conoce como el encriptado César <https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar>. En este tipo de encriptado lo que se hace es "girar" el abecedario una determinada cantidad de pasos según una clave numérica (ver ejemplo). Crear una función que lea un string dentro de un txt en la misma ruta que esta notebook, tome una clave y devuelva el string encriptado con la clave César en minúsculas(asumir que el texto esta en castellano).
# 
# Ej: Clave = 2
# 
# | Letra   | Letra encriptada |
# | ------------- |:-------------:| 
# | A | C | 
# | B | D |
# | C | E |
# | ... | ... |
# | Y | A |
# | Z | B |
# 
# ```Python
# INPUT:
# 'mi_archivo.txt' ("Hola estudiante"), clave = 1
# OUTPUT:
# "Jqnc guvwfkcovg"
# ```
# 
# *AYUDA*
# 
# El método `mi_lista.index(elemento)` búsca el `elemento` en la lista `mi_lista` y devuelve la posición del elemento si lo encontró. Si no lo encontró devuelve un `ValueError`.

# In[ ]:


def codificador_cesar(mensaje_path, clave):
    # Un ayudin
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    # Ahora hagan su magia (ojo con las mayúsculas)

    return cifrado


# In[ ]:


# Corre para ver si tu código esta bien
test2(codificador_cesar)


# **OPCIONALES** 
# 
# - Hacer que la función guarde la salida como un archivo de texto.
# - Podemos encriptar respetando mayúsculas. Adaptar la función para que lo haga. Se puede usar la funcion test2_mayusculas para probarla. Sugerencia: Mirar el método `isupper()` para los strings.
# - Adaptar la función anterior pero para desencriptar, una función que cree una lista con todas las posibles rotaciones del texto.

# ***
# ### La calesita (Rompecoco) 
# El señor Jacinto es dueño de una antigua calesita con animalitos que no funciona hace varios años y quiere volver a ponerla en funcionamiento. Para eso va a probarla prendiendola y viendo cuanto rota segun la cantidad de movimientos. 
# 
# Crear una función que reciba una lista de strings (con la primera en mayúscula) con los animales que componen la calesita, una cantidad de ciclos(n_ciclos) y devuelva la misma lista pero rotada hacia la derecha esa cantidad de movimientos, donde un movimiento es cambiar todos los animales una posición hacia la derecha:
# 
# Ej:
# ``` Python
# INPUT:
# ['Unicornio','Oso','Jirafa', 'Pato'. 'Elefante'], movimiento = 1
# OUTPUT:
# ['Elefante', 'Unicornio', 'Oso', 'Jirafa', 'Pato']
# ```

# In[ ]:


def probar_calesita(calesita, n_movimientos):
    # Proba la calesita
    
    return calesita_girada


# In[ ]:


# Corre para ver si tu código esta bien
test3(probar_calesita)


# Cuando prueba la calesita se da cuenta que es muy lenta. Debe sacar uno de los animales para que pueda funcionar correctamente. Para eso los manda a pesar y le dicen cual es el que hay que sacar para que funcione perfectamente.
# 
# Modificar la función anterior para que reciba un string, que es un animal en MAYÚSCULAS (animal_quitar) para sacar y pruebe la función nuevamente.
# 
# Ej:
# ```Python
# INPUT:
# ['Unicornio','Oso','Jirafa', 'Pato'. 'Elefante'], animal_quitar = 'JIRAFA', movimientos = 1
# OUTPUT:
# ['Elefante', 'Unicornio', 'Oso', 'Pato']
# ```

# In[ ]:


def probar_calesita_arreglada(calesita, n_mov, animal_quitar):
    # Arregla la calesita
    
    return calesita_arreglada


# In[ ]:


# Corre para ver si tu código esta bien
test4(probar_calesita_arreglada)

