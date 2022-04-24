#!/usr/bin/env python
# coding: utf-8

# # Generando contenido

# Vamos a usar Google Colaboratory para mantenernos sincronizados y aprovechar la portabilidad que ofrece. 
# 
# La notebook debe ser autosuficiente, sirviendo como material para exposición, con ejercicios prácticos orientados al dominio al que se apunta, complementado por una notebook de ejercicios y 
# soluciones. 

# ## Estilo de las clases
# 
# - Partes separadas con títulos grandes y subsecciones jerárquicas con #
# - Explicaciones en texto plano (markdown)
# - Comentarios solo para especificar parámetros, argumentos especificos en ejemplos u otras cuestiones técnicas. 
# - Usar HTML para hipervínculos.
# - Indentación, negrita o indentacion con formato codigo son preferibles cuando se hable de terminos de software como "booleano", *keywords* de Python
# - Respetar las indicaciones de [PEP 8](https://www.python.org/dev/peps/pep-0008/)
#  como manual de estilo.
#   
# Las clases se componen de una o dos (como mucho) notebooks. Cada notebook incluye ejercicios a ser completados. Salvando que sean casos demasiado fáciles (como las primeras clases de intro a Python) se pide que haya una notebook sin ejercicios completados y una con los ejercicios completados, para ayudar al docente. El sufijo -solucion indica en el nombre si incluye la solución o no. Además se debe incluir una carpeta ejercicio/ donde se incluyen ejercicios para realizar fuera de la clase. También debe incluirse la solución.
# 
# Ejemplo:
# 
# ---

# ## Operaciones con variables

# ## Variables  
# 
# ### Booleanos
# 
# Las variables de tipo _bool_ aceptan ciertos operadores lógicos o relacionales: 
# - **&**, **and** : simbolizan la operación conocida de "y", ^, o intersección...
# - ...
# 
# Aparecen en distintos contextos blabla... como las sentencias condicionales o *if*s...
# 
# ```python
# if (10 > 5) & ('palabras' in ['palabras', 'algo', 'cosas']) and True:
#     print('Verdadero!')
# ```

# In[ ]:


# Declaramos un bool con valor verdadero, o sea True o 1
esta_soleado = 1
hay_cuarentena = 1

if esta_soleado & hay_cuarentena:
    print('Uhh qué lástima!')


# ---
# Los ejercicios:
#  - Deben formularse en infinitivo
#  - Pueden tener secciones con títulos
#  - Las consignas deben estar escritas en Markdown con texto plano (no en comentarios, o todo con ##
#  - Deben estar todos juntos al final de la notebook, o en una distinta, y las soluciones en otra ipynb

# ## Operaciones numéricas
# 
# Calcular la raiz cuadrada de 5 y redondear a 3 decimales

# In[ ]:


round(5 ** (1/2), 3)


# In[ ]:





# ## Principales convenciones de PEP8
# 

# In[ ]:


# Recommended naming convention for variables, functions and class methods
under_score_naming_convention = 'default' 


# In[ ]:


# Recommended
class Foo:
  def _private_method(self):
      return 'private'

  def public_method(self):
      return 'public'


# In[ ]:


# Recommended
total = (first_variable
         + second_variable
         - third_variable)


# Indentation following line breaks

# In[ ]:


# Recommended
def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one


# Otros:
# - https://google.github.io/styleguide/pyguide.html
# - https://refactoring.guru/
# - Black para formatting
# - pylint para detectar conflictos
# - isort para ordenar imports
