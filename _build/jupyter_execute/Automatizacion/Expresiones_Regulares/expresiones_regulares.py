#!/usr/bin/env python
# coding: utf-8

# <div align="center"><a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Automatizacion/expresiones_regulares.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg'/> </a> <br> Recordá abrir en una nueva pestaña </div>

# ## Expresiones Regulares

# También conocido popularmente como **RegEx**. Son un mini lenguaje de programación diseñado para realizar búsquedas en strings. Son extremadamente útiles para:
# - Extraer datos de distintos tipos de archivos, texto o con otro tipo de codificación.
# - Web scraping: como veremos en las próximas clases, las regex son un buen método para encontrar la información que se necesita en un sitio web.
# - Limpieza de datos: herramienta fundamental en el repertorio del científico de datos para limpiar datos quitando caracteres "ruidosos", o armando nuevos "features" según la presencia o no de cierto texto.

# #### Recursos útiles
# 
# - [Sitio para armar RegEx online](https://regexr.com/)
# - [Alternativa](https://regex101.com/)
# - [CheatSheet](https://www.dataquest.io/wp-content/uploads/2019/03/python-regular-expressions-cheat-sheet.pdf)
# 

# Python utiliza la libreria llamada **re** para todo lo relacionado a regular expressions

# In[ ]:


import re

# a- extraer números de una oración.
texto = "Mi nombre es Juan y mi teléfono es 1564232324"
regla_de_busqueda = "15\d+"
print(texto)
print(re.findall(regla_de_busqueda,texto))


# Las funciones principales de la librería re son:
# - re.findall(pattern, string) para encontrar todos los resultados de una búsqueda
# - re.search(pattern, string) para encontrar el primer resultado que coincida
# - re.sub(pattern, replace, string) para substituir un texto por otro

# 
# <h2><center>Sintaxis para construir regex</center></h2>
# 
# 
# <h3><center>Grupos de captura</center></h3>
# 
# 
# |     |                       |
# |-----|-----------------------|
# | ()  | grupo de captura      |
# |(?:) | grupo de no captura   |
# 
# <h3><center>Tipos de datos</center></h3>
# 
# 
# |     |                      |          |                         |
# |----|-----------------------|----------|-------------------------|
# | \w | caracter alfanumérico | .        | cualquier cosa menos \n |
# | \d | dígito                | \|       | operador "or"           |
# | \s | espacio en blanco     | [m-z3-9] | rangos                  |
# | \n | paso de línea         | \W       | Con mayusc. negamos. Ej: NO alfanumérico|
# 
# <h3><center>Operadores</center></h3>
# 
# |         |                      |
# |---------|----------------------|
# | \|      | operador "or"        |
# | \\      | Escapar, o interpretar literalmente |
# | []      | conjunto             |
# |[m-z3-9] | rangos               |
# 
# 
# <h3><center>Cuantificadores</center></h3>
# 
# |      |                                              |
# |------|----------------------------------------------|
# | +    | Uno o más del elemento anterior              |
# | *    | Cero o más del elemento anterior             |
# | {4,} | Cuatro o más del elemento anterior           |
# | ?    | Cambia el operador anterior de lazy a greedy |

# #### ¿Cómo se usa? Veamos ejemplos

# In[68]:


# En realidad los telefonos no son cualquier seguidilla de numeros
# suelen tener entre 6 y 8 numeros despues del 15
texto = "Mi nombre es María y mi teléfono es 1564232324"
regla_de_busqueda = "15\d{6,8}"
re.findall(regla_de_busqueda,texto)


# In[67]:


# En realidad los telefonos no arrancan siempre con 15
# capaz empiezan con 11 si son de buenos aires por ejemplo
texto = "Mi nombre es Carlos y mi teléfono es 1164232324"
regla_de_busqueda = "(?:15|11)\d{6,8}"
re.findall(regla_de_busqueda,texto)


# In[69]:


# En realidad los telefonos pueden tener un guión o espacio a parte de números
texto = "Mi nombre es asfasfeaf33 y mi teléfono es 11 6423-2324"
regla_de_busqueda = "(?:15|11)[0-9\s-]{6,10}"
re.findall(regla_de_busqueda,texto)


# In[70]:


# b- Como extraer el mes de un texto
texto = "REPORTE DE PERFOMANCE - MES DE JUNIO"
regla_de_busqueda = "(MES DE (?:JULIO|AGOSTO|JUNIO))"
re.findall(regla_de_busqueda,texto)


# In[71]:


# ¿Cómo hago que pare de buscar el operador * ?
text = "me llamo pedro. me gusta el rock."
regla_de_busqueda_no_greedy = "(.*?)\."
regla_de_busqueda_greedy = "(.*)\."
print(re.findall(regla_de_busqueda_no_greedy,text))
print(re.findall(regla_de_busqueda_greedy,text))


# In[60]:


import re

comentario_de_mercadolibre = 'hola soy @mariadominguez, me interesa el producto, te dejo mi celu 1565525233, saludos'

def encontrar_telefonos(texto):
    regla_de_busqueda = r'(15[0-9]{8})'
    return re.findall(regla_de_busqueda, texto)

def encontrar_usuarios(texto):
    regla_de_busqueda = r'@([a-zA-Z]+)'
    return re.findall(regla_de_busqueda, texto)

print(encontrar_telefonos(comentario_de_mercadolibre))
print(encontrar_usuarios(comentario_de_mercadolibre))


# #### Ejercicio

# Usa regex para hacer una función que busque todos los emails en un texto

# In[63]:


# Resolución 

texto = "Hola te paso mi mail python@hotmail.com, saludos. Si no te funciona mandame a este otro, pedro_2010@yahoo.com"
encontrar_emails(texto)


# Ejercicio
# 
# Vamos a usar como ejemplo el [DSM](https://en.wikipedia.org/wiki/Diagnostic_and_Statistical_Manual_of_Mental_Disorders), el libro de psiquiatría más importante en el mundo, en formato txt. El mismo se descargó en PDF y convirtió a texto usando [textract](https://textract.readthedocs.io/en/stable/), una cómoda librería de Python.
# 
# De este texto:
# 
# 1. Extraer los nombres de los médicos que aparecen.
# 
# Extracto de ejemplo:
# 
# ```
# Allan Burstein, M.D.
# David M. Clark, Ph.D.
# Lee Anna Clark, Ph.D.
# Deborah S. Cowley, M.D.
# ```
# 
# Es decir, en **cada renglón** sigue el patrón "[nombres], M.D.".
# 
# Tip: recuerden cómo se representa el paso de línea (o "newline")!

# In[17]:


# Descargamos el texto
get_ipython().system('wget -nc https://unket.s3.sa-east-1.amazonaws.com/data/DSM.txt')


# In[18]:


import re

with open('DSM.txt', 'r') as inp:
    texto = inp.read()


# In[26]:


# Completar 


# Ahora buscar a las personas con PhDs (observen el extracto anterior)

# In[45]:





# Hacer una RegEx para extraer nombres de condiciones mentales, ejemplo:
# 
# Ejemplo
# 
# ```
# Clinical judgment must be used in distinguishing developmentally appropriate
# levels of separation anxiety from the clinically significant concerns about separation
# seen in Separation Anxiety Disorder.
# I Diagnostic criteria for 309.21 Separation Anxiety
# Disorder
# A. Developmentally inappropriate and excessive anxiety concerning sep-
# aration
# ```
# 
# Debería dar "Separation Anxiety". Es decir, el patrón es: "Diagnostic criteria for [números con punto] [nombre de la condicion]"
# 
# Tip: podemos hacer que el patrón contemple mayúsculas y minúsculas (con [A-Z] y [a-z]) o indicar un "flag" para que se ignoren las mayúsculas con
# 
# ```re.findall(patrón, string, flags=re.IGNORECASE)```

# In[46]:





# In[ ]:





# Extraer los nombres de los países de los profesionales que fueron colaboradores internacionales en esta última edición

# Extracto de ejemplo:
# 
# ```
# Michael Gelder, M.D. (England)
# Semyon Gluzman, M.D. (former USSR)
# Judith H. Gold, M.D. (Canada)
# Marcus Grant, Ph.D. (Switzerland)
# Herta A. Guttman, M.D. (Canada)
# Heinz Hafner, M.D. (Germany)
# Robert Hare, Ph.D. (Canada)
# ```
# 
# Pistas: 
# 1. Para que sea más sencillo consideren solo países cuyo nombre sea una sola palabra. 
# 2. También pueden considerar que siempre está **después de M.D. o de PhD.** (recuerden cómo buscar una u otra cosa!).
# 3. Cuidado también con "escapar" los paréntesis literales

# In[62]:


paises = None


# Ahora contemos cuántas veces aparece cada país con la siguiente clase Counter. Simplemente pasen su lista de `paises` como argumento al constructor Counter() y les dará el resultado.

# In[57]:


from collections import Counter

Counter(paises)

