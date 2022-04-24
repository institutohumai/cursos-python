#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Introduccion/1_TiposDatos/tipos-datos.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>
# 

# # Introducción a la programación con Python

# <h1 id="tocheading">Tabla de Contenidos</h1>
# <div id="toc"></div>

# I. Introducción a la programación con Python
# 
# II. Tabla de Contenidos
# 
#     I. Python
# 
# III. IDEs
# 
#         I. VS Code
#         II. Pycharm
#         III. Spyder
# 
# IV. Hola Jupyter!
# 
# V. Declarando variables
# 
#     I. Numéricos
#     II. Operaciones numéricas - Divisiones
#     III. Booleanos
#         I. Operaciones lógicas
# 
# VI. Ejercicios
# 
#     I. Strings
#             I. Ejercicios
#     II. Listas
#         I. Indexing y slicing en listas
#         II. Otras operaciones y métodos
#     III. Diccionarios
#     IV. Condicionales
#     V. Bucles o Loops
#         I. For loop
#         II. While loop
#     VI. Recursos y tips
#     VII. Tips en la práctica

# ## Python
# 
# - Elegante, sencillo
# - Comunidad y accesibilidad
# - Desarrollos de estado del arte
# - Flexibilidad "full stack"
# - Multi-paradigma
# 

# # IDEs

# ### VS Code

# <img src='https://datasets-humai.s3.amazonaws.com/images/IDE.png'></img>

# ### Pycharm

# <img src='https://datasets-humai.s3.amazonaws.com/images/Pycharm.png'></img>

# ### Spyder

# <img src='https://datasets-humai.s3.amazonaws.com/images/spyder.png'></img>

# # Hola Jupyter!
# 
# En esta _notebook_ conoceremos el entorno Jupyter (o Google Colaboratory, una versión online gratuita), interfaz incluida en la instalación de Python ampliamente usada para Data Science llamada <a href="https://www.anaconda.com/products/individual"/> Anaconda </a>. Para seguir el curso offline, luego de descargar e instalar Anaconda, si usan Windows deberán buscar el programa en su computadora y ejecutar Jupyter.
# 
# Si están en una distribución de linux o Mac pueden ejecutar en la terminal:
# 
# > jupyter notebook
# 
# Cada una de estas _celdas_ funciona como un bloque donde podemos escribir texto plano, Latex, HTML, además de ejecutar código Python, R, bash y otros. 
# 
# $$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$$

# # Declarando variables <a name="section-2"></a>

# Existen distintos tipos de variables:
# - int: entero
# - float: punto flotante
# - string: cadena de caracteres
# - bool: booleano, 0, 1, True o False
# 
# Y estructuras de datos, como:
#   - list: lista de elementos (de cualquier tipo, incluida otra lista)
#   - dict: "diccionario", conjunto de pares llave:valor
#   
# Veamos un primer ejemplo

# In[ ]:


primera_variable = 'Hola mundo!'

print(primera_variable)


# Declaramos una variable llamada *primera_variable* asignándole el valor de "Hola mundo!". La **función print** toma entre paréntesis esa variable y muestra el valor en pantalla. 

# En Jupyter la última línea de una celda se imprime al ejecutar...

# In[ ]:


primera_variable


# ## Numéricos

# Declaramos dos variables de tipo numérico:

# In[ ]:


x = 5
y = 17


# Podemos hacer las operaciones numéricas usuales:

# In[ ]:


print(x+y) # suma
print(x*2) # multiplicacion
print(x**(1/2)) # elevado a 


# ## Operaciones numéricas - Divisiones

# Devuelve la división:

# In[ ]:


print(y / x)


# Devuelve la parte entera de la división:

# In[ ]:


print(y // x) 


# Devuelve el resto:

# In[ ]:


print(y % x)


# Otros ejemplos:

# In[ ]:


un_string = 'variable de ejemplo'
un_bool = True


# La **función** _type_ recibe de **argumento** una **variable** y **devuelve** su tipo

# In[ ]:


type(x), type(y)


# Intentemos la siguiente suma...

# In[ ]:


5 + "10"


# ¿Qué paso?

# Si **convertimos** el string "10" a tipo int

# In[ ]:


5 + int('10')


# Cada tipo de variable responde a ciertos **métodos**. Veamos las operaciones lógicas, que utilizan **booleanos**

# ## Booleanos

# ### Operaciones lógicas

# In[ ]:


print(10 >= 9)


# In[ ]:


print("palabra" == "palabra")
print("otras palabras" != "otras palabras") 


# In[ ]:


print("test" in "testing")

a = 'testing'

print('test' in a)


# Los operadores disponibles son: 
# 
#     Relacionales:
#     - >= , <=, <, > : Mayor o igual, menor o igual, mayor o menor
#     - != , == : Distinto, Igual
#     - in : Contenido por 
#     Lógicos:
#     - not o ~ : Negación
#     - and o & : Ambas verdaderas
#     - or o | : Una u otra es verdadera
#     
# Como booleanos, se pueden utilizar tanto 0 y 1 como True y False.

# # Ejercicios <a name="section-3"></a>
# 
# 
# 1- Definan a = 5, b = 7 y c = 8
# 
# Prueben las siguientes operaciones booleanas:
# 
# 2- a > b
# 
# 3- a < b
# 
# 4- a + b < c
# 
# 5- (a + b > c) | (a + b < c) --> a + b o es mayor a c o es menor
# 
# 6- (a + b > c) & (a + b < c) --> a + b es mayor a c y es menor a c

# ## Strings <a name="section-4"></a>

# In[ ]:


"dos strings se pueden " + "sumar"


# Podemos acceder a ellos mediante **índices**. Los mismos funcionan para cualquier **iterable**, que es un objeto con muchos elementos que son accesibles secuencialmente. Podemos usar los índices para acceder a una posición determinada, pasándola entre corchetes [posición]. Es IMPORTANTE mencionar que en Python la primera posición tiene el índice 0 (y no 1).

# In[ ]:


texto = "programación en python"


# In[ ]:


texto[0]


# También podemos usar los índices para traer más de un elemento al mismo tiempo, usando el **slicing**. El slicing lleva tres parámetros: comienzo (start), final (stop) e intervalo o paso (step).
# 
# - El parámetro comienzo (start) indica la primera posición incluida en la selección, por default es 0.
# 
# - El parámetro final (stop) es la primera posición que NO va a estar incluída, por default se incluyen todos los elementos. 
# 
# - El parámetro intervalo o paso (step), es optativo e indica el tamaño del paso entre seleccionar un elemento y el siguiente, por default el paso es 1. El paso también puede ser negativo, en este caso contamos desde el final hacia el comienzo, esto es muy útil para dar vuelta los strings...
# 
#     
#     [comienzo : final : intervalo] (en inglés es [start : stop : step] )
#     
#     
# El intervalo que se recibe es semi-abierto (indice_primero, indice_segundo], es decir se incluye el primero y no el segundo valor. Se admiten números negativos, que contabilizan desde el final.

# In[ ]:


texto[:]


# In[ ]:


texto[:1]


# In[ ]:


texto[1:4]


# In[ ]:


texto[::-1]


# Ejercicio 
# 
# 1- Dado ese string devuelvan únicamente la palabra python usando slicing

# In[ ]:


texto


# In[ ]:


texto[16:23]


# In[ ]:


texto[16:23]


# In[ ]:


texto[-6:]


# In[ ]:


texto[-6:23:1]


# Veamos algunos otros métodos de los strings

# In[ ]:


texto.upper()


# In[ ]:


texto.title()


# In[ ]:


texto.split() # Devuelve una lista, de ésto vamos a hablar a continuación


# Otras formas de combinar variables y texto...

# Rellenamos un string con **.format(query, modales)**:

# In[ ]:


tema = 'data science'
modales = 'por favor'

'Dame información de {0} si esta disponible, {1}'.format(tema, modales)


# In[ ]:


#Otra manera
print(f'Dame información de {tema.upper()} si esta disponible, {modales}')


# Otros métodos a mencionar son:

# In[ ]:


"1000".isdigit()


# In[ ]:


texto.replace(' ', '...')


# In[ ]:


"   quitando espacios  ".strip()


# In[ ]:


texto = "Me gusta el 37" # Piso el contenido de la variable para hacer otras pruebas
texto.isalpha()


# In[ ]:


texto = "Me" # Piso el contenido de la variable
texto.isalpha()


# #### Ejercicios <a name="section-5"></a>
# 
# 1- Concatenar los string "hola" y "qué tal", separando ambos strings con un espacio (Tip: un espacio es: " ")
# 
# 2- Guardar el resultado anterior en una variable y pasar el texto a mayúsculas.

# In[ ]:


# Ejercicio 1


# In[ ]:


# Ejercicio 2


# ## Listas <a name="section-6"></a>
# 
# Las listas son un conjunto de elementos ordenados. Estos elementos pueden ser de cualquier tipo, incluyendo otras listas. Veamos algunas operaciones con ellas.

# In[ ]:


amigos = ['Mateo', 'Nico', 'Claudia', 'Ernestina', 'Paola']


# ### Indexing y slicing en listas

# De la misma forma que con los strings en el contexto de la listas generalmente hablamos de **indexación** o acceso por índice a la acción de encontrar un valor según su posición en la lista. 
# 
# Importantísimo (sí, ¡una vez más!): En Python el primer elemento se indexa con el valor 0. Es decir, si queremos el primer valor de una lista tenemos que llamar a la posición 0.

# In[ ]:


amigos[0]


# Además, el último elemento se indexa como -1, el siguiente -2 y así sucesivamente. Entonces para acceder al último elemento:

# In[ ]:


amigos[-1]


# Además, podemos acceder a varios elementos en simultáneo, usando el **slicing** de la misma manera que con strings.
# 
# El slicing aplicado a una lista nos devuelve una **lista**.
# 
# Veamos algunos ejemplos:

# In[ ]:


amigos[:] # arranco en 0 hasta el final, con el paso default (1)


# In[ ]:


amigos[:1] # arranco en 0 y el primero sin incluir es el 1, con el paso default (1)


# In[ ]:


amigos[:-1] # excluímos el último elemento


# In[ ]:


amigos[::2] # salteamos un elemento a la vez


# Ejercicios:
# 
# 1- ¿Es el resultado de amigos[:1] igual al de acceder directamente a la primera posición? 
# 
# 2- Recorrer la lista de elementos de atrás para adelante.
# 
# 3- Seleccionar del 3er elemento al 4to elemento.

# ### Otras operaciones y métodos

# Agregar un nuevo elemento:

# In[ ]:


amigos.append('Chicharito')
print(amigos)

amigos = amigos + ['Chicharito']

x = 10

x = x + 3

x


# Sumamos otra lista:

# In[ ]:


amigos = amigos + ['Pipi', 'Toto']
print(amigos) 


# Unir una lista con un separador dado:

# In[ ]:


ejemplo = ['valor1', 'valor2', 'valor3']
';'.join(ejemplo)


# El ejercicio 1 se podría haber resuelto usando .join así:

# In[ ]:


" ".join(["hola", "qué tal"])


# Borrado por valor:

# In[ ]:


amigos.remove('Mateo')
print(amigos)


# Borrado por índice:

# In[ ]:


del amigos[0]
print(amigos)


# Devuelve un elemento y lo borra de la lista:

# In[ ]:


valor = amigos.pop(0)


# In[ ]:


edades = [30, 40, 38, 30, 37]


# Cantidad de apariciones:

# In[ ]:


print(edades.count(30))


# Largo de la lista:

# In[ ]:


print(len(edades))


# Ordenar la lista:

# In[ ]:


sorted(edades)


# Sumar el total:

# In[ ]:


print(sum(edades))


# Mínimo:

# In[ ]:


print(min(edades))


# Máximo:

# In[ ]:


print(max(edades))


# Ejercicio: <a name="section-7"></a>
# 
# 1- Calcular el promedio de edad de la lista "edades"
# 

# In[ ]:


# Ejercicio 1


# ## Diccionarios <a name="section-8"></a>
# 
# Los diccionarios consisten en estructuras que contienen pares de una **llave** y un **valor**. Los elementos NO están ordenados, con lo cual no se puede acceder por posición ni slicing.
# 
# Veamos un ejemplo

# In[ ]:


dnis = {'Herrera':32676585, 'Guzmán':9564787, 
        'Pérez':5676898, 'Hernández':40565999, 
        'Abraham':28375814,
       "soy_una_llave":"soy_un_valor"} 


# Sin embargo, sí podemos acceder a un elemento por su llave. Accedemos al valor de "Abraham"

# In[ ]:


dnis['Abraham'] # noten que se usa la misma notación que con las listas


# ¿Qué pasa si tratamos un diccionario como una lista?

# In[ ]:


dnis[0]


# Tenemos un error, tratemos de interpretarlo: KeyError se refierre a que no existe una llave (Key) a la que se trató de acceder. En este caso la llave que se trató de acceder es 0.

# Podemos ver todas las llaves:

# In[ ]:


dnis.keys()


# Traer todos los pares de elementos:

# In[ ]:


dnis.items()


# Y utilizar los mismos métodos para borrar y extrar como en las listas:

# In[ ]:


dnis.pop('Herrera')


# Los diccionarios tienen longitud, de la misma forma que las listas y string

# In[ ]:


len(dnis)


# ## Condicionales <a name="section-9"></a>
# 
# El condicional tiene la siguiente sintáxis:
# 
#     if CONDICIÓN:
#         código1
#     elif CONDICIÓN2:
#         código2
#     else:
#         código3
#         
# Donde la condición es un operador que devuelve un objeto de tipo booleano. La **indentación** del código define qué parte se incluye como condicional.
# 
# El término "elif" viene de "else if". La condición sólo se evaluará si la condición del "if" no se cumple. 

# In[ ]:


precio_dolar = 62

if precio_dolar >= 90:
    print("El dólar se fue por las nubes")
elif (precio_dolar < 90) and (precio_dolar >= 70):
    print("El dolar subió")
else: 
    print("El dólar es menor a 70")

print(precio_dolar)


# ## Bucles o Loops
# 
# Los bucles son un tipo de sentencia donde se realiza el código contenido repetidamente. Existen dos tipos. En el bucle **for**, se **itera** o recorre un conjunto de elementos actuando por cada uno de ellos. En el bucle **while** se itera hasta que se cumple una condiciónn de corte.

# ### For loop

# In[ ]:


for n in [1,2,'3']:
    print(f'EL tipo es {n*2} {type(n*2)}')


# In[ ]:


lista = [1,2,3,4,5]

for n in lista:
    print(n * 2)


# También agreguemos la función **range** a nuestro repertorio. La función range consta de tres parámetros importante: start, stop, step. Si pasamos un sólo parámetro, estamos pasando el "stop" y tomamos 0 como valor default de "start". Del mismo modo que cuando vimos listas, el stop no está incluído y el step por default es 1.
# 
# Veamos cómo funciona:

# In[ ]:


for n in range(5):
    print(n)


# Si pasamos dos parámetros, estamos pasando el start y el stop, el primer valor es el "start" y el segundo el "stop".

# In[ ]:


for n in range(0,5):
    print(n)


# Noten que el valor de start se incluye y el de stop no:

# In[ ]:


for n in range(1, 6): # esto nos da el mismo resultado que un par de celdas más arriba
    print(n * 2)


# Por último, el tercer parámetro es el step...

# Ejercicios combinando lo visto hasta el momento:
# 
# 1- Imprimir los valores de 1 a 50, salteando de a un valor por vez...
# 
# 2- Dada la siguiente lista: medios = ["cheques", "bonos", "acciones", 1000, "transferencia"]. Acceder al 2do elemento, y luego al 3er elemento (de ese 2do elemento) y responder qué devulve.
# 
# 3- De manera similar, ahora accedan al 4to elemento, y luego al 3er elemento de éste, ¿qué ocurre?
# 
# 4- Agreguen una lista vacía al final de esa lista.
# 
# 5- Recorran *medios* (iteren) y si el tipo del elemento es string, hagan un print de su primer elemento, si es int (entero) pásenlo a string y hagan un print de su primer elemento y si no es nada de eso hagan un print que diga "Es otro tipo". Tip1: para pasar un elemento a tipo string pueden usar la función str(variable), donde variable es el elemento que quieren transformar. Tip2: para arrancar este ejercicio pueden copiar lo siguiente:

# In[ ]:


for medio in medios:
    pass # pass no hace nada, sólo pasa sin ejecutar nada... Reemplácenlo y completen con las condiciones.


# ### While loop

# Los bucles **while** se definen con una condición, y el código contenido se ejecuta mientras la misma evalue como True. Es importante definir correctamente cuándo la condición pasa de True a False, si no lo hacemos podemos dejar corriendo un programa infinitamente sin que corte. Si eso llega a suceder tienen un botón de stop arriba en la notebook.

# In[ ]:


contador = 0

while contador < 20:
    contador += 1 # esto equivale a count = count + 1
    print(contador)


# ---
# 
# ## Recursos y tips
# 
# 
# - [Google!](https://google.com)
# - [StackOverflow](https://stackoverflow.com)
# - [Google Colab](https://colab.research.google.com)
# - [Slicing](https://python-reference.readthedocs.io/en/latest/docs/brackets/slicing.html)
# --- 
# 
# ## Tips en la práctica
# 
# - Ver _docstring_ con Shift + TAB o help()
# - Leer Errores
# - Print

# In[ ]:




