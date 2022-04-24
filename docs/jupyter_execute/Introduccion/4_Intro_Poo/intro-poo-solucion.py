#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Introduccion/4_Intro_Poo/intro-poo-solucion.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# <h1 id="tocheading">Programación orientada a objetos</h1>
# 
#     I. Terminologia de clases y objetos
#     II. Creando la primera clase
#         I. Herencia
#         II. Protección de acceso
#     III. Métodos Especiales
#     IV. Métodos Estáticos
#     V. Duck typing y monkey patching
#         I. Duck typing
#         II. Monkey Patching

# En el paradigma de programación orientada a objetos los programas se estructuran organizando el código en entidades llamadas objetos. Estos nos permiten encapsular data, funciones y variables dentro de una misma clase. Veamos de qué se trata.

# ## Terminologia de clases y objetos

# 1. Una **clase** es un prototipo de objeto, que engloba atributos que poseen todos los objetos de esa clase. Los atributos pueden ser datos como variables de clase y de instancia, y métodos (funciones). Se acceden con un punto.
# 
# 2. Una **instancia** es un objeto en particular que pertenece a una clase.
# 
# 3. Una variable de clase o **class variable**  es un atributo compartido por todas las instancias de la clase. Se definen dentro de una clase pero fuera de un método. 
# 
# 4. La **herencia** es la transferencia de atributos de una clase a otra clase
# 
# 5. Un **método** es una función contenida dentro de un objeto.
# 
# 6. Un **objeto** es una instancia única de una estructura definida por su clase. Posee de atributos variables de clase, de instancia y métodos.
# 
# 

# ## Creando la primera clase

# In[1]:


import math


# In[2]:


#La sintáxis es:

class Ejemplo:
    pass

# Instancio la clase
x = Ejemplo()

print(type(x))


# Por convención, las clases se nombran empleando "upper camel case". Es decir, con mayúscula para cada término que sea parte del nombre. 

# Una librería famosa en Python por sus clases es "requests". Esta ĺibrería se usa para acceder a información web por HTTP. Algunas de sus clases son:
# 
# - Session
# - Request
# - ConnectionError
# - ConnectTimeout
# 
# Las últimas dos clases son para especificar errores, noten que se repiten las mayúsculas.

# Podemos pensar a una clase como un molde, el cual usamos para generar objetos o instancias que tienen ciertos atributos o métodos (funciones) que deseamos mantener.
# 
# Aquellos atributos y métodos que queremos que los objetos conserven son definidos como parte del constructor. El constructor en Python es el método reservado **\_\_init\_\_()**. Este método se llama cuando se instancia la clase y en ese momento se inicializan los atributos de la clase, para lo cual podemos pasar parámetros.
# 
# Además, vamos a emplear el término reservado **self** para indicar aquellos atributos y métodos que van a ser propios de los objetos. Veámoslo con un ejemplo.

# In[3]:


class Persona():
    def __init__(self, nombre, apellido, edad, contacto):
        # Este método puede tomar parámetros que asignamos a los atributos, que luego podemos acceder
        self.edad = edad # este es un atributo
        self.contacto = contacto # este es otro atributo
        self.nombre = nombre
        self.apellido = apellido
        
    def nombre_completo(self):
        # este método toma el nombre completo y lo separa en nombre y apellido 
        nombre_completo = ', '.join([self.apellido,self.nombre])
        return nombre_completo

    def saludar(self):
        print(f'Hola mi nombre es {self.nombre_completo()}',
              f'y te dejo mi mail por si necesitás algo: {self.contacto}')


# In[4]:


instancia_ejemplo = Persona('Matías Andrés','Ripley', 24, 'mati@rip.com')
instancia_ejemplo.saludar()


# Ahora veamos una clase menú que administra los platos y los precios

# In[5]:


class Menu():
    def __init__(self, items):
        self.items = items
    
    def precio(self, lista_items):
        precio = 0
        for nombre_item in lista_items:
            precio = precio + self.items[nombre_item]
        return precio
    
    def tamaño(self):
        return len(self.items)
            


# In[6]:


mi_menu = Menu({'latte':25, 'medialuna':15})


# ¿Cuánto salen un latte y dos madialunas? ¿Cuántos ítems tenemos?

# In[7]:


mi_menu.precio(['latte','medialuna','medialuna'])


# In[8]:


mi_menu.tamaño()


# Ejercicio: Vamos a mejorar la clase anterior... En lugar de que el método precio reciba una lista de strings, hagamos que reciba una lista de diccionarios cada uno con dos claves nombre y cantidad que querríamos ordenar ¿Cuántos cuestan 10 lattes y 30 medialunas?

# In[9]:


class Menu():
    def __init__(self, items):
        self.items = items
    
    def precio(self, lista_items):
        precio = 0
        for pedido in lista_items:
            # Leemos el diccionario
            nombre = pedido['nombre']
            cantidad = pedido['cantidad']
            # Buscamos el precio en los ítems del menú
            precio_unidad = self.items[nombre]        
            # Agregamos el total de cada ítem
            precio = precio + precio_unidad * cantidad
        return precio
    
    def tamaño(self):
        return len(self.items)
            


# In[10]:


mi_menu = Menu({'latte':25, 'medialuna':15})


# In[11]:


mi_menu.precio([{'nombre':'latte','cantidad':10},
        {'nombre':'medialuna','cantidad':30}])


# Los atributos también son conocidos como variables de instancia, en contraposición a las variables de clase. Las variables de instancia toman un valor específico a una instancia en particular (por eso se emplea el término **self**), por su parte, las variables de clase tienen un valor común para todas las instancias de una clase. Por convención las variables de clase se definen antes del constructor y no llevan **self** en su definición pero sí cuando se la quiere llamar.

# In[12]:


class Curso:
    max_alumnos = 35 # definimos variable de clase

    def __init__(self, nombre, duracion, alumnos = None, costo=10):
        self.nombre = nombre
        self.duracion = duracion
        if alumnos is None:
            self.alumnos = []
        else:
            self.alumnos = alumnos
        self.costo = costo # costo tiene un valor por default
        """¿Por qué ese if? Las variables por default sólo se evalúan a la hora de ejecutar la sentencia def. 
        En nuestro caso necesitamos que self.alumnos sea una lista y las listas son objetos mutables. 
        Esto quiere decir que podemos modificarla sin volver a asignarla. Si en vez de 'alumnos = None' usáramos
        alumnos = [], entonces con cada nueva instancia del objeto estaríamos compartiendo los alumnos.
        Para evitar eso, en general la forma pythónica de hacerlo es usando None por default y asignando el valor
        deseado dentro de la función y no en el 'def' """

    def inscribir_alumno(self, nombre):
        self.alumnos.append(nombre) # para poder llamar a alumnos tengo que usar self.
        print(f'Se agregó al alumno/a {nombre}')

    def tomar_lista(self):
        for a in self.alumnos:
            print(f'Alumno: {a}')

    def resumen(self):
        print(f'Curso {self.nombre}, {self.duracion} clases pensadas para {len(self.alumnos)} alumnos\n'
              f'Por el muy módico precio de {self.costo} rupias.',
              # llamo variable de clase:
              f'La ocupación actual es del {round(len(self.alumnos)/self.max_alumnos,2)*100}%') 


# In[13]:


curso_python = Curso('Python', 6)


# In[14]:


curso_python.alumnos


# In[15]:


# Llamamos metodos de la instancia
curso_python.inscribir_alumno('Diotimia')
curso_python.inscribir_alumno('Aritófanes')


# In[16]:


curso_python.tomar_lista()


# In[17]:


curso_python.resumen()


# In[18]:


curso_ml = Curso('Machine Learning', 8)


# In[19]:


curso_ml.alumnos # vean que el curso está vacío!


# In[20]:


curso_ml = Curso('Machine Learning', 8)
curso_ml.inscribir_alumno('Agatón')
curso_ml.inscribir_alumno('Erixímaco')
curso_ml.inscribir_alumno('Sócrates')


# In[21]:


curso_ml.resumen()


# In[22]:


curso_ml.alumnos


# Ejercicios:
# 
# 1- Defina una clase Punto que tome como parámetros x e y (las coordenadas) y constante que se puede instanciar correctamente.
# 
# 2- En Python existen los llamados métodos mágicos (magic methods) o dunder (Double Underscores). Estos métodos se caracterizan, justamente, por comenzar y terminar con "\_\_". Uno de los más comunes es el que permite darle estilo a la función **print**. Para que nuestro objeto entonces tenga un lindo print tenemos que definir una función "\_\_str\_\_" que sólo toma "self" como parámetro y que torne un string. Eso que retorna es el string que queremos que muestra cuando hagamos "print" del objeto. Dicho ésto, te invitamos a que lo intentes de la siguiente manera:
# 
# a. Definí una función "\_\_str\_\_" que sólo toma self como parámetro.
# 
# b. La función debe retornar el string que querés mostrar, recordá que podés usar los valores de "x" y de "y"

# In[23]:


class Punto:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"


# In[24]:


punto = Punto(1.0, 2.0)
print(punto)


# ### Herencia
# La herencia se emplea cuando queremos que una clase tome los atributos y características de otra clase.
# En este caso, la clase derivada (Alumno) **hereda** atributos y métodos de la clase base (Persona).
# Para acceder a los métodos de la clase previa vamos a emplear el método reservado **super()**. Con este método podemos invocar el constructor y así acceder a los atributos de esa clase.

# In[25]:


# Clase derivada
class Alumno(Persona):
    def __init__(self, curso: Curso, *args): 
        """ 
        Alumno pertence a un Curso (una instancia de la clase Curso) y, además, tiene otros atributos que pasaremos
        a la clase previa
        """
        self.curso = curso
        super().__init__(*args) # inicializamos la clase 'madre'. La llamamos usando super() y ejecutamos el constructor
        # Nótese también que desempacamos args

    def saludar(self): # Sobrecarga de métodos, ver abajo
        super().saludar() # ejecutamos el método de Persona .saludar() y agregamos más cosas a este método
        print('Estoy cursando:')
        self.curso.resumen()

    def estudiar(self, dato): # También podemos definir nuevos métodos
        self.conocimiento = dato


# La clase Persona cuenta con un método saludar() y para Alumno también definimos un método saludar(). Cuando instanciemos un Alumno y ejecutemos el método saludar() lo que va a ejecutarse es el método saludar() de Alumno, no de Persona. Esto no quita que el método saludar() de Alumno llame al de Persona. Además, vale la pena mencionar que los dos tienen los mismos parámetros (ninguno en este caso). Este patrón de diseño es lo que se llama sobrecarga de métodos o overriding.

# In[26]:


scott = Alumno(curso_python, 'Scott', 'Henderson', 49, 'sh@mail.com')
scott.saludar()


# In[27]:


scott.estudiar('Se puede heredar de otra clase y extender sus métodos')


# In[28]:


scott.conocimiento


# Ejercicio:
# 
# 1- Listar cuáles son los atributos y los métodos de scott y especificar cuáles provienen de Persona y cuáles están definidos por ser Alumno.

# In[ ]:





# ### Protección de acceso
# 
# Podemos cambiar el acceso (publico, no publico, protejido) de los métodos y variables.

# Dos formas distintas de encapsulamiento:
# 
# - `_nopublico`
# - `__protegido`
# 
# Los atributos o método no públicos pueden ser accedidos desde el objeto y llevan el prefijo "\_". La utilidad de este es indicarle al usuario que es una variable o método privado, de uso interno en el código de la clase y que no está pensando que sea usado desde afuera, por el usuario. 
# 
# Por otra parte, en el caso de usar como prefijo "\_\_" (doble "\_") directamente vamos a ocultar la variable o método de la lista de sugerencias para el usuario y tampoco va a poder invocarlo desde el objeto. Por este motivo, decimos que el atributo o método está protegido.

# In[29]:


class Auto():

    def __init__(self, color, marca, velocidad_maxima):
        self.color = color
        self.marca = marca
        self.__velocidad_maxima = 200
        self.velocidad = 0
        self.__contador = 0 # kilometros recorridos
    
    def avanzar(self, horas=1, velocidad=10):
        if self._chequear_velocidad(velocidad):
            self.velocidad = velocidad
            print(f'avanzando durante {horas} horas')
            self.__contador += horas*self.velocidad
        else:
            print(f"Tu auto no puede llegar a tanta velocidad, el máximo es {self.__velocidad_maxima}")
    
    def _chequear_velocidad(self, velocidad):
        es_valida = False
        if velocidad < self.__velocidad_maxima:
            es_valida = True
            if self.velocidad < velocidad:
                print("Vas a acelerar!")
            else:
                print("Vas a desaceler!")
        else:
            print("Tu motor no permite ir tan rápido")
            es_valida = False
        return es_valida
    
    def status(self):
        print(f"Vas a una velocidad de {self.velocidad} y llevás {self.__contador} km. recorridos")


# In[30]:


superauto = Auto('rojo','Ferraudi', 200)


# In[31]:


# Atributo no publ
superauto.avanzar(10)


# In[32]:


superauto.status()


# In[33]:


# No se puede acceder a un atributo protegido
superauto.__contador 


# In[35]:


# Pero sí se puede acceder a un método no público:
superauto._chequear_velocidad(10)


# Ejercicio:
# 
# A continuación se define una clase Linea. Esta clase toma como parámetros dos objetos Punto() (instancias de la clase que definieron antes). 
# 
# 1- Agregar un método 'largo' que permita calcular el largo de la línea. Para ello vale la pena recordar que ésta se puede calcular como la hipotenusa del triángulo rectángulo que se forma con los dos puntos.

# \\[ a = \sqrt{b^2 + c^2} \\]

# <img src="https://static1.abc.es/media/ciencia/2019/10/31/TeoremadePitagorasABC-kW8F-U3032581527206JG-620x450@abc.jpg" width=250/>

# 2- Agregar un método 'pendiente' que permita calcular la pendiente de la línea. Recordar que ésta se puede calcular como el cociente entre las diferencias de 'y' y de 'x'. 
# 
# La fórmula es :
# \\[ m = (y_2 - y_1)/(x_2 - x_1) \\]

# In[36]:


class Linea(object):
    def __init__(self, p1: Punto, p2: Punto):
        self.p1 = Punto(x0,y0)
        self.p2 = Punto(x1,y1)

    def __str__(self):
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        linea = "((%f,%f),(%f,%f))" % (x0, y0, x1, y1)
        return linea
    
    def largo(self):
        dist_x = self.p2.x - self.p1.x
        dist_y = self.p2.y - self.p1.y
        dist_x_squared = dist_x ** 2
        dist_y_squared = dist_y ** 2
        largo = (dist_x_squared + dist_y_squared) ** 0.5
        return largo
    
    def pendiente(self):
        dist_y = self.p2.y - self.p1.y
        dist_x = self.p2.x - self.p1.x
        pendiente = dist_y/dist_x
        return pendiente


# In[37]:


x0,y0 = 7,5
x1,y1 = 4,1


# In[38]:


p1 = Punto(x0,y0)
p2 = Punto(x1,y1)
linea = Linea(p1,p2)


# In[39]:


linea.pendiente()


# In[40]:


linea.largo()


# ## Métodos Especiales
# 
# Las clases en Python cuentan con múltiples métodos especiales, los cuales se encuentran entre dobles guiones bajos __<metodo>__().
# 
# Los métodos especiales más utilizados son <strong> \_\_init\_\_(), \_\_str\_\_() y \_\_del\_\_() </strong>.
# 
# \_\_init\_\_ sirve para inicializar la clase y \_\_del\_\_ sirve para eliminar completamente el objeto del compilador.
# 
# Veamos un ejemplo de uso de \_\_str\_\_. Una vez que definimos este método, responde a la sintaxis reservada de Python str().

# In[41]:


# Clase derivada
class Alumno(Persona):
    def __init__(self, curso: Curso, *args): 
        """ 
        Alumno pertence a un Curso (una instancia de la clase Curso) y, además, tiene otros atributos que pasaremos
        a la clase previa
        """
        self.curso = curso
        super().__init__(*args) # inicializamos la clase 'madre'. La llamamos usando super() y ejecutamos el constructor
        # Nótese también que desempacamos args

    def saludar(self): # Sobrecarga de métodos, ver abajo
        super().saludar() # ejecutamos el método de Persona .saludar() y agregamos más cosas a este método
        print('Estoy cursando:')
        self.curso.resumen()

    def estudiar(self, dato): # También podemos definir nuevos métodos
        self.conocimiento = dato
        
    def __str__(self):
        #Devuelve un string representativo del alumno
        return f'Alumno {self.nombre_completo()}'
    


# In[42]:


un_alumno = Alumno(curso_python, 'Scott', 'Henderson', 49, 'sh@mail.com')


# In[43]:


str(un_alumno)


# ## Métodos Estáticos
# 
# ¿Qué pasa si no queremos instanciar los objetos a la hora de usarlos? En algunos diseños, tiene sentido utilizar las clases como simples repositorios de métodos. Por ejemplo, si necesito resolver varias operaciones geométricas puedo crear una clase Geometria que contenga todos los métodos necesarios.
# 
# Para crear este tipo de métodos en una clase utilizamos el decorador @staticmethod. 
# 
# 

# In[44]:


class Geomtria():
    """Resuelve operaciones geométricas"""
    
    @staticmethod
    def pendiente(x1,y1,x2,y2):
        return ((y2 - y1)/(x2-x1))
    
    @staticmethod
    def area_circulo(radio):
        return math.pi * (radio**2)


# In[45]:


Geomtria.area_circulo(3)


# ## Duck typing y monkey patching
# 
# Dos características de la programación orientada a objetos con Python son el duck tiping y el monkey patching. Este tipo de flexibilidad es el que le permitió a Python crecer tanto en su adopción porque reducen la cantidad de palabras que es necesario escribir para desarrollar código, lo cual ahorra tiempo y también disminuyen la complejidad.
# 
# ### Duck typing
# 
# 

# In[46]:


class ElHobbit:
    
    def __init__(self,nombre):
        self.nombre = nombre
    
    def __len__(self):
        return 95022
    
    def saludar(self):
        return f'Hola soy {self.nombre}'

el_hobbit = ElHobbit('Frodo')


# In[47]:


len(el_hobbit)


# In[48]:


mi_str = "Hello World"
mi_list = [34, 54, 65, 78]
mi_dict = {"a": 123, "b": 456, "c": 789}


# <i> “If it walks like a duck, and it quacks like a duck, then it must be a duck.”</i>
# 
# Duck typing significa que a diferencia de otros lenguajes, las funciones especiales no están definidas para una lista específica de clases y tipos, si no que se pueden usar para cualquier objeto que las implemente. Esto no es así para la mayoría de los lenguajes.   

# In[49]:


len(mi_str)
len(mi_list)
len(mi_dict)
len(el_hobbit)


# In[50]:


mi_int = 7
mi_float = 42.3


# In[51]:


len(mi_int)
len(mi_float)


# ### Monkey Patching
# 
# Guerrilla, gorilla, ¿monkey?... Este término viene de uno anterior, "guerrilla patching", que hace referencia a emparchar el código rápido y cuando es necesario. 
# 
# Se refiere a la posibilidad en Python de sobreescribir clases después de haberlas instanciado y por qué no también la funcionalidad de los módulos. 

# In[52]:


el_hobbit.saludar()


# In[53]:


def saludo_largo(self):
    return f'Hola mi nombre es {self.nombre}'


# In[54]:


ElHobbit.saludar = saludo_largo


# In[55]:


el_hobbit.saludar()


# Esto es especialmente útil cuando queremos sobre-escribir ligeramente módulos hechos por terceros (¡o por nosotros mismos en otro momento!) 

# In[56]:


import math


# In[57]:


math.pi


# In[58]:


math.pi = 2


# In[59]:


math.pi


# Los cambios se sobre-escriben si REINICIAMOS EL KERNEL y volvemos a importar el módulo

# In[60]:


import math
math.pi

