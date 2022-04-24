#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Introduccion/2_Listas_Y_Funciones/listas-funciones.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>
# 
# 
# ## Listas, Funciones, Errores
# 

# - [Control de flujo](#Control-de-flujo)
# - [Tuplas](#Tuplas)
# - [Errores](#Errores)
# - [List Comprehension](#List-Comprehension)
# - [Funciones](#Funciones)

# ### Pequeño Repaso

# In[1]:


for i in range(1, 10):
    if i % 2 == 0:
        print(f"El número {i} es par")


# ## Control de flujo
# 
# Contamos con 3 _keywords_ que modifican el orden de ejecución **dentro de un bucle**
# 
# - **continue**: interrumpe el flujo del bucle y retoma la ejecución en la siguiente iteración
# - **break**: termina el bucle
# - **pass**: no tiene efecto, se usa para evitar error cuando lo exige la sintáxis
# 

# Vamos a simular una base de datos de usuarios empleando un diccionario. Este diccionario tiene como llave un id representando por un entero. Como valor tiene un diccionario con nombre, apellido y dni.

# In[2]:


base = {
    1: {"nombre":"Fernanda",
        "apellido":"Fernandez",
        "dni":333333331},
    2: {"nombre":"Gonzalo",
        "apellido":"Gonzalez",
        "dni":333333332},
    3: {"nombre":"Rodrigo",
        "apellido":"Rodriguez",
        "dni":333333333}
    }


# Supongamos que en una página web tenemos un formulario en el cual las personas que acceden completan con su dni y queremos saber el nombre y apellido si contamos con el mismo en la base, y si no lo tenemos sólo queremos saber cuál es el dni. 

# In[3]:


dnis = [333333331, 333333336, 333333339, 333333332, None, 333333333]


# In[4]:


n_encontrados = 0

for dni in dnis: # itero por todos los dnis

    if type(dni) == int: # si el tipo es entero
        dni_encontrado = False # inicializo una variable con valor False, ya van a ver para qué :-)
        
        # Ahora viene la parte complicada, ¿cómo sé si ese dni ya está en mi base?
        # 1- Recordemos que base es un diccionario y como tal tiene el método items(), pruébenlo afuera de esta celda
        # me devuelve una tupla, con la llave en el primer elemento y el valor en el segundo
        
        # itero por todos los elementos
        for i in base.items(): 
            valor = i[1] # guardo el valor en una variable
            if dni == valor["dni"]: # si el dni es el mismo que estoy buscando...
                dni_encontrado = True
                nombre_completo = valor["nombre"] + " " + valor["apellido"]
                n_encontrados += 1 # esto equivale a encontrados = encontrados + 1, agrega uno
                break # freno la búsqueda, ésto evita que siga buscando

        if dni_encontrado: # entra acá si es True
            print(f"{nombre_completo.title()} ingreso a nuestra web")

        elif not dni_encontrado: # noten el not
            print(f'El dni {dni} no se encuentra en la base...')
            continue # sigo con la búsqueda, NO paso a la siguiente línea
            
        print(f"Hasta el momento se encontraron {n_encontrados} casos")
    
    else:
        pass # si dni no es un entero entonces no hacemos nada, suponemos que hubo algún tipo de error


# ## Tuplas 

# Una **tupla** es una secuencia **inmutable** de longitud fija. Las tuplas generalmente se utilizan para representar secuencias de elementos que tienen longitud fija.

# In[5]:


registro = ('Argentina', 112000, 'Bariloche')


# Podemos acceder a un elemento por un índice como con una lista

# In[6]:


registro[0] 


# #### Unpacking
# 
# Con una tupla, o una lista podemos separar una secuencia en variables de la siguiente manera

# In[7]:


pais, poblacion, ciudad = registro

print("País:", pais)
print("Población:", poblacion)
print("Ciudad:", ciudad)


# In[8]:


registros = [registro, ('Brasil', 477000, 'Florianópolis')]
registros[1]


# Pero como las tuplas son **inmutables** no se pueden modificar

# In[9]:


# Una lista sí se puede modificar
lista = [1, 2, 3]

lista[0] = 4

lista


# En cambio una tupla no se puede modificar o, como dice el cartel de error, no permite asignación:

# In[10]:


print(registro)
registro[0] = 'Chile'


# In[11]:


# tampoco se puede borrar ninguno de sus elementos
del registro[0]


# ## Tipos de errores
# 
# En el ejemplo de arriba vimos una pantalla de error. El **traceback** o **stack trace** nos muestra el camino del error: veremos más adelante que cuando tenemos funciones anidadas, vemos aquí como el error se propaga. 
# 
# Las cosas a las que en principio les debemos prestar atención son:
# 
#    1. El nombre del error, en este caso **TypeError**
#    2. La explicación dada en el último renglón: "'tuple' object doesn't support item deletion"
#    3. La flecha que nos indica la línea en la que ocurrió el error

# Existen distintos tipos de errores en Python, pueden consultar la lista de todas las excepciones básicas acá:
# https://docs.python.org/3/library/exceptions.html#bltin-exceptions
# 
# Sin embargo, las excepciones más frecuentes son:
# 
# **AttributeError**: cuando tratamos de llamar a una referencia que no existe.
# 
# **NameError**: cuando se llama a una variable u otro nombre que no está definido en el ambiente en que estamos trabajando.
# 
# **KeyError**: cuando queremos llamar a una llave que no existe, por ejemplo, en un diccionario.
# 
# **SyntaxError**: cuando hay un problema de sintaxis, errores muy comunes al comienzo pueden ser que no se cerró una llave o corchete, que falta alguna coma o dos puntos.
# 
# **TypeError**: cuando el tipo de soporta una determinada operación.
# 
# **IndexError**: cuando el índice al que se quiere acceder no existe, generalmente debido a que se llama a un índice mayor al largo de la lista.

# Veamos algunos ejemplos:

# In[12]:


print(no_definido)


# In[13]:


print(base) # recordamos base


# In[14]:


base['Gertrudis']


# ### Ejercicios

# Prueben y arreglen los siguientes errores de código:
# 
# 
# 1. ¿Qué está pasando en este código?

# In[15]:


if 10 > 5
    print('Qué está pasando?')


# 2. ¿Y en este? Traten de arreglarlo 

# In[16]:


a = 5
b = "3"
a + b == 8


# 3. ¿Y continuación?

# In[17]:


a = ["the beatles", "the rolling stones", "queen", "led zepellin"]

a[4]


# 4- ¿Y acá? ¿qué pasó?

# In[18]:


a.appended(["cream"])


# ## Manejo de errores

# Para anticipar y manejar los errores, podemos usar la clausula **try** y **except**

# In[19]:


a = '20'
b = 5

try:
    print(a+b)
except:
    print(int(a)+int(b)) # convierto a int ambas variables


# Si queremos ver qué excepción ocurrió, podemos usar la siguiente sintáxis:

# In[20]:


try:
    print(a+b)
except Exception as e:
    print(f"El error fue {e}")


# También podemos especificar qué hacer para distintos tipos de error:

# In[21]:


lista_tuplas = [('3', 8), 
                (5, 0), 
                (3, ), 
                (4, 6)]

for t in lista_tuplas:
    print(f"la tupla es {t}")
    
    try:
        print("intento dividir...")
        print(t[0] / t[1])
        print("éxito!")
    except IndexError:
        print('El largo está mal')
    except TypeError:
        print('Error en el tipo de datos')
    except ZeroDivisionError:
        print("No se puede dividir por cero")


# # Listas por comprensión (List Comprehension)

# Las **listas por comprensión** son una funcionalidad muy flexible de Python que permite crear listas de un modo más "descriptivo", basandose en la notación de definición de conjuntos.

# Supongamos que necesitamos obtener una lista con los elementos de una lista original elevados al cuadrado.
# 
# Sin listas por comprensión haríamos...

# In[22]:


lista = [1,2,3,4,5]

cuadrados = []

for x in lista:
    cuadrados.append(x**2)
    
cuadrados


# En cambio, con listas por comprensión usamos esta expresión:

# In[23]:


cuadrados = [x**2 for x in lista]


# En las listas por comprensión también podemos incluir condicionales en una sola línea, vean la siguiente expresión:

# In[24]:


x = 10
print(x if x > 15 else 0)


# In[25]:


x = 16
print(x if x > 15 else 0)


# Ahora vamos a generar una lista por comprensión sólo con los números donde el cuadrado sea menor a 15

# In[26]:


cuadrados = [x**2 for x in lista if x**2 < 15]
cuadrados


# La sintáxis para **filtrar** con condicionales es
# 
# > [ (elemento) ( for x in (iterable) ) ( if condicion ) ]
# 
# Donde "elemento" es lo que vayamos a guardar en la lista. Incluyendo un **else**:
# 
# > [ (elemento) (if condicion else otro_elemento) ( for x in (iterable) ) ]
# 
# Pueden hacerse loops anidados:
# 
# > [i for i in range(x) for j in range(y)]

# Otra forma de pensar la sintaxis es a partir de teoría de conjuntos. Por ejemplo:
# Un conjunto S definido por todos los números X / 4 que pertenecen a los Naturales y cumplen que su cuadrado es menor a 20
# 
# $$S=\{\,\frac{x}{4}\mid x \in \mathbb{N},\ x^2<60\,\}$$

# Con un loop for:

# In[27]:


S = []

for x in range(1000):
    if x ** 2 < 60:
        S.append(x/4)
S


# Con listas por comprensión:

# In[28]:


S = [x/4 for x in range(1000) if x**2 < 60]
S


# In[29]:


for x in range(3):
    for y in 'abc':
        print(x,y)


# In[30]:


[(x, y) for x in range(3) for y in 'abc']


# O comprensiones anidadas:
# 
# > [ [i for i in range(x) ] for j in range(y) ]

# In[31]:


[[l*n for l in 'abc'] for n in range(3)]


# Además, el elemento que se genera puede ser de otro tipo, en este caso una tupla:

# In[32]:


animales = ['mantarraya', 'pandas', 'narval', 'unicornio']

[(a, len(a)) for a in animales]


# ### Ejercicios

# 1- Dado el siguiente grupo de palabras, crear otra lista que contenga sólo la primera letra de cada una

# In[33]:


lista = ['a','ante','bajo','cabe','con']


# 2- Dada la siguiente frase, crear una lista con el largo de cada palabra.
# Tip: Antes de aplicar listas por comprensión pueden usar la función split que vimos la clase pasada y la función replace para remover la puntuación.

# In[34]:


frase = 'Cambiar el mundo, amigo Sancho, no es ni utopía ni locura, es justicia'


# # I/O
# 
# Ahora veremos como abrir archivos usando Python base. Para hacerlo usaremos la sentencia **with** para definir un **contexto** del siguiente modo:
# 
#     with open('corpus.txt', 'r') as inp:
#         string_contenido = inp.read()
#         
# Lo que significa: con el archivo "corpus.txt" abierto en **modo** lectura ("r" de read) con el **alias** _inp_, definimos la variable contenido usando el método **.read()** para leer el archivo. Algunas aclaraciones:
# 
# - El método .read() es propio del objeto de input, que **en esta ocasión** llamamos _inp_. Otro método útil es **.readlines()** que nos permite iterar por renglones.
# - La ruta al archivo puede ser **relativa** como en este caso, donde el archivo se encontraría en la misma carpeta que la notebook. También se puede dar el path completo, como podría ser "C:/Usuarios/Matías/Documentos/corpus.txt"

# Existen varios modos de abrir un archivo, incluyendo:
# 
#     - r: read, lectura
#     - w: write, escritura
#     - a: append, agregar al final del archivo
#    
# Por ejemplo, para escribir en un archivo, haríamos:
# 
#     with open(outpath, 'w') as f:
#         f.write(string)

# In[35]:


with open('nuevo.txt', 'w') as f:
    f.write('ejemplo de escritura')


# In[36]:


with open('nuevo.txt', 'r') as f:
    contenido = f.read()

print(contenido)


# En Python se puede pedir un input del usuario de la siguiente manera:

# In[37]:


while True:
    usuario_dijo = input('Ingrese un numero')

    try:
        num = int(usuario_dijo)
        break
    except:
        print('No anduvo, intente de nuevo')

print(f'Su numero fue {num}! :D')


# # Funciones
# 
# Las funciones nos permiten estandarizar y reutilizar un proceso en múltiples ocasiones.
# 
# Como patrón de diseño, las funciones tienen que ser lo más atómicas posibles, es decir, resolver un problema lo más pequeño posible y bien definido.
# 
# Los nombres también son importantes, el nombre de la función tiene que reflejar lo mejor posible lo que hace. 
# 
# 
# Las funciones se definen de la siguiente manera:
# 
#     def nombre_de_funcion(argumentos):
#         """docstring opcional"""
#         resultado = procedimiento(argumentos)
#         return resultado
#         
# Las variables definidias en el contexto de una función son locales, es decir, sólo viven dentro de esa función. Por otra parte, si desde una función se llama a una variable que no está definida en la función tratará de buscarla afuera. En general, es buena práctica usar sólo variables definidas dentro de la función o argumentos.
# 
# Los argumentos son variables que le pasamos a la función para que *haga algo*.
# 
# Las funciones emplean dos términos reservados:
# 
# - def: que indica el comienzo de la definición de la función
# 
# - return: establece la variable o variables que devuelve la función
# 
# En este punto vale la pena mencionar que en Python los nombres (de variables, funciones, etc.) se almacenan y ordenan en NameSpaces. En este punto, la información definida dentro de la función no es compartida con el exterior de la función (salvo algunas excepciones que no vienen al caso), por lo tanto, para compartirla, la función debe enviar desde el NameSpace local (el de la función) al NameSpace global (donde está el resto del programa). Para ello, el término return indica qué se devolverá al ambiente global. Para que efectivamente esa/s variable/s que la función devuelve se guarden una variable en el ambiente global debemos asignar el resultado a una variable. Esto va a quedar más claro con el código.
# 
# Por último, vale la pena mencionar que *print* sólo nos muestra el contenido de una variable pero no envía la información desde la función hacia afuera.

# In[38]:


def promedio(lista):
    return sum(lista) / len(lista)


# In[39]:


resultado = promedio([0,1,2,3]) # asigno el resultado
print(resultado)


# In[40]:


def suma(a,b):
    """Esta función recibe dos numeros y devuelve la suma"""
    return a+b


# In[41]:


r = suma(3,5) # asigno el resultado
print(r)


# In[42]:


def rango(lista):
    return max(lista) - min(lista)


# In[43]:


lista = [89, -24, 9, 2]
rango(lista)


# ### Ejercicios: 
# 
# 1- Escribir una función que reciba una lista con números y devuelva la suma de todos los pares
# 
# 2- Escribir una función que tome una lista con distintos elementos (de cualquier tipo) y devuelva una lista sólo con los últimos tres números que aparecen.

# En las funciones existen argumentos se pueden pasar por posición o por su nombre. Algunos de los argumentos tienen un valor por default.

# In[44]:


def unir_lista(lista, conector=' '):
    """Esta funcion recibe dos argumentos, una lista y un conector
    y devuelve la lista unida usando el conector."""
    
    unida = conector.join([str(e) for e in lista])
    
    return unida


# In[45]:


unir_lista(['unir',3,'cosas'])


# In[46]:


unir_lista(['probando', 'unir', 'lista', 123], conector = ',')


# Lo que no podemos hacer es pasar el argumento nombrado antes de el o los posicionales

# In[47]:


unir_lista(conector = ',',['probando', 'unir', 'lista', 123])


# Cuando uso los argumentos por su nombre, puedo pasarlos en cualquier orden

# In[48]:


unir_lista(conector = ',',lista = ['probando', 'unir', 'lista', 123])


# Existen distintos tipos de argumentos, principalmente los llamados "args" y "kwargs", o argumentos y "keyword arguments" es decir argumentos nombrados. 

# También podemos tener un numero variable de argumentos, usando el symbolo *, por conveción al parámetro se le llama 'args'

# Internamente, los elementos de *args se tratan como una tupla

# In[8]:


def suma_todos(*args):
    print(type(args))
    return sum(args)


# In[9]:


suma_todos(9,1,4,2)


# En cambio los elementos de **kwargs se tratan como un diccionario

# In[10]:


def consulta(**kwargs):
    print(type(kwargs))
    texto = f"Su consulta es {kwargs['fecha']} a las {kwargs['hora']}"
    return texto


# In[11]:


consulta(fecha='hoy',hora='4PM')


# Finalmente, podemos juntar todo lo visto en una misma función, es decir, tener argumentos sin nombre sin valor default, argumentos con valores default, args y kwargs. Esto es especialmente útil cuando necesitamos enviar args o kwargs a otras funciones usadas dentro de una función.

# In[12]:


valor_consulta = {"consulta":10, "arreglos_caries":20, "flúor":15}


# In[13]:


costos = list(valor_consulta.values())
costos


# In[14]:


def emitir_factura(nombre, dni, tipo="DNI", *args, **kwargs):
    factura = ""
    factura += f"Gracias por su visita Nombre:{nombre} \n"
    factura += f"{tipo} {dni} \n"
    costo = suma_todos(*args) # hago unpacking de args
    factura += f"El costo es {costo} \n"
    factura += consulta(**kwargs) # hago unpacking de kwargs
    return factura


# In[18]:


factura = emitir_factura("Obi Wan", 370310455, "DNI", *costos, fecha="hoy", hora="5PM")


# In[19]:


print(factura)


# In[ ]:




