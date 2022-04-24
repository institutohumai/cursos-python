#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Introduccion/6_Poo_Proyecto/poo-proyecto.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# # Aplicación de POO: PACMAN

# En esta guía vamos a empezar a diseñar una versión básica del tradicional juego PACMAN, organizando el código a partir de algunos conceptos de POO.

# Qué elementos van a ser clases? Pensemos en cómo es el juego...
# En primer lugar, existe un juego, que surje de la interacción entre el PACMAN, los FANTASMAS, el MAPA... Antes de pensar cómo modelar el juego pensemos en el mapa.

# ¿Cómo describirían un mapa?

# Una versión simple de un mapa podría considerar:
# - Ser como una matriz, lo cual lo podríamos hacer con una lista de listas
# - Ser accesible en sus posiciones, ya que vamos a querer posicionar a los fantasmas, a pacman y posiblemente otros objetos
# - Ser printeable/printable
# - Poder preguntarle si una posición existe en el mapa, o qué hay en una determinada posición

# Escribamos primero la clase "Mapa". 

# In[ ]:


import random
import sys


# In[ ]:


class Mapa:
    def __init__(self, n_rows, n_cols):
        # primero guardo la cantidad de filas y la cantidad de columnas
        self.n_rows = n_rows
        self.n_cols = n_cols
        # luego, genero un mapa vacío. Nota: ésto se puede hacer mejor usando setters, dejémoslo para otra oportunidad
        self._map = [[CeldaVacia() for i in range(self.n_cols)] for x in range(self.n_rows)]
    
    def __getitem__(self, row):
        # esta es una función mágica, nos va a permitir acceder de una forma muy pythonezca
        return self._map[row] # pueden adivinar qué nos va a devolver?
    
    def __str__(self):
        # esta es otra función mágica, nos va a dar un print muy canchero, y luego la vamos a modificar más
        str_map = ""
        for row in self._map:
            for col_idx in range(len(row)):
                str_map += str(row[col_idx])
                if col_idx == len(row) - 1:
                    str_map += "\n"
                
        return str_map


# Y ahora vamos a generar el primer objeto que puede pertenecer a un mapa: una celda vacía. Queremos que esta celda vacía se muestre desde una clase que no es la original, usamos el método <code> __repr__ </code> en lugar de <code> __str__ </code>

# In[ ]:


class CeldaVacia:
    def __repr__(self):
        return " . "


# Primero, veamos para qué sirve...

# In[ ]:


# instanciamos un mapa de 5 filas por 3 columnas
mapa = Mapa(5,3)


# In[ ]:


mapa[4]


# In[ ]:


print(mapa)


# In[ ]:


mapa.n_cols


# ¿Qué va a pasar a continuación...?

# In[ ]:


mapa[4][4]


# ¿Qué más podemos imprimir dentro del mapa? A continuación vamos a crear las clases Pacman y Fantasma

# In[ ]:


class Fantasma:
    def __repr__(self):
        return " G "


# In[ ]:


class Pacman:
    def __repr__(self):
        return " P "


# Ahora que ya creamos estos elementos, necesitamos crear métodos en el mapa que nos permitan agregarlos y también consultar para cada posición del mapa qué elemento la está ocupando.

# In[ ]:


class Mapa:
    def __init__(self, n_filas:int, n_columnas:int):
        # primero guardo la cantidad de filas y la cantidad de columnas
        self.n_filas = n_filas
        self.n_columnas = n_columnas
        # luego, genero un mapa vacío. Nota: ésto se puede hacer mejor usando setters, dejémoslo para otra oportunidad
        self._elementos = [[CeldaVacia() for i in range(self.n_columnas)] for x in range(self.n_filas)]
    
   
    def __str__(self):
        str_map = ""
        for row in self._elementos:
            for col_idx in range(len(row)):
                element = row[col_idx]
                str_map += str(element)
                if col_idx == len(row) - 1:
                    str_map += "\n"
                
        return str_map

    def modificar_elemento(self, elemento, pos_x, pos_y):
        # método para modificar el tablero
        self._elementos[pos_x][pos_y] = elemento

    def get_elemento(self, x, y):
      # método para tomar un elemento
      return self._elementos[x][y]


# Creamos un nuevo mapa

# In[ ]:


mapa = Mapa(7,8)


# In[ ]:


print(mapa)


# Y vamos a agregar a Pacman en la posición (2,2)

# In[ ]:


mapa.modificar_elemento(Pacman(),2,2)


# In[ ]:


print(mapa)


# Ahora vamos a crear la clase Juego. A la hora de inicializar el juego, creamos un mapa con los personajes ubicados en sus posiciones iniciales. 
# 
# Ejercicio: Creen una clase "Juego" que tenga entre sus propiedades un mapa de 9x9 donde vamos a colocar un Pacman en la posición (2,3) y fantasmas en las posiciones (4,4) y (5,7).

# In[ ]:





# ### Poblando el tablero e inicializando el juego
# 
# Ahora vamos a crear una clase Juego que se inicialice con un mapa de 7X8 y los personajes en distintas posiciones. También vamos a inicializar el score en 0 y crear un método start() que permita tomar el input del usuario y nos muestre el tablero.

# In[ ]:


class Juego:
    
    def __init__(self):
        # cuando instanciamos el juego creamos personajes. Por ahora las posiciones son fijas pero se podrían hacer al azar
        mapa_inicial = Mapa(7,8)
        mapa_inicial.modificar_elemento(Pacman(),4,3)
        mapa_inicial.modificar_elemento(Fantasma(),1,3)
        mapa_inicial.modificar_elemento(Fantasma(),0,0)
        self.mapa = mapa_inicial
        self.puntaje = 0

    def start(self):
        fin = False
        while not fin:
            print(f"score:{self.puntaje}")
            print(self.mapa)
            input_movimiento = input()


# In[ ]:


juego = Juego()
juego.start()


# ### Validar el input
# 
# Por ahora el juego nos permite ingresar cualquier valor, no reacciona a ese input y tenemos que terminar el juego manualmente. 
# 
# Agreguemos, entonces un poco de funcionalidad a la clase Juego. Ahora vamos a validar que el input sea alguna de las teclas "a","w","s" o "d" que permiten mover a Pacman. Para eso vamos a crear un método privado en la clase \_input\_valido que valida si la tecla es correcta

# In[ ]:


class Juego:
    
    def __init__(self):
        # cuando instanciamos el juego creamos personajes. Por ahora las posiciones son fijas pero se podrían hacer al azar
        mapa_inicial = Mapa(7,8)
        mapa_inicial.modificar_elemento(Pacman(),4,3)
        mapa_inicial.modificar_elemento(Fantasma(),1,3)
        mapa_inicial.modificar_elemento(Fantasma(),0,0)
        self.mapa = mapa_inicial
        self.puntaje = 0

    def start(self):
        # Loop con la lógica del juego
        fin = False
        while not fin:
            print(f"score:{self.puntaje}")
            print(self.mapa)
            input_movimiento = input()
            if not self._input_valido(input_movimiento):
                print("El input tiene que ser a, w, s o d")
                
    def _input_valido(self, move_input):
        # Valida si el input es correcto
        if move_input in ["a","w","s","d"]:
            return True
        else:
            return False


# In[ ]:


juego = Juego()
juego.start()


# ### Mover a Pacman
# 
# Ahora queremos reaccionar al input del usuario. Para esto vamos a invocar al método \_modificar\_elemento.
# * Para poder mover a Pacman tenemos que consultar su posición. Esto lo hacemos con el método _get_posicion_pacman.
# * Una vez que tenemos la posición vamos a calcular la nueva posición en función del movimiento del usuario. Noten que éste puede ser un método estático porque no modifica ni consulta ninguna de las propiedades de la clase Juego.
# * Finalmente actualizamos el mapa del juego. 

# In[ ]:


class Juego:
    
    def __init__(self):
        # cuando instanciamos el juego creamos personajes. Por ahora las posiciones son fijas pero se podrían hacer al azar
        mapa_inicial = Mapa(7,8)
        mapa_inicial.modificar_elemento(Pacman(),4,3)
        mapa_inicial.modificar_elemento(Fantasma(),1,3)
        mapa_inicial.modificar_elemento(Fantasma(),0,0)
        self.mapa = mapa_inicial
        self.puntaje = 0

    def start(self):
        # Loop con la lógica del juego
        fin = False
        while not fin:
            print(f"score:{self.puntaje}")
            print(self.mapa)
            input_movimiento = input()
            if not self._input_valido(input_movimiento):
                print("El input tiene que ser a, w, s o d")
            else:
                self._actualizar_mapa(input_movimiento)
                
    def _input_valido(self, input_movimiento):
        # Valida si el input es correcto
        if input_movimiento in ["a","w","s","d"]:
            return True
        else:
            return False
        
    def _actualizar_mapa(self, input_movimiento):
        # Actualiza la posición del pacman
        pacman_x,pacman_y = self._get_posicion_pacman()
        nueva_x, nueva_y = self._avanzar_posicion(pacman_x,pacman_y,input_movimiento)
        self.mapa.modificar_elemento(CeldaVacia(), pacman_x, pacman_y)
        self.mapa.modificar_elemento(Pacman(), nueva_x, nueva_y)
        return 0
    
    def _get_posicion_pacman(self):
        # Iteramos por todos los elementos del mapa del juego hasta encontrar a Pacman
        for fila in range(self.mapa.n_filas):
            for columna in range(self.mapa.n_columnas):
                elemento = self.mapa.get_elemento(fila,columna)
                if isinstance(elemento,Pacman):
                    # Hay un único elemento de la clase Pacman. Los demás son Fantasma o CeldaVacia
                    return fila, columna
                
    @staticmethod
    def _avanzar_posicion(x,y,move):
        if move == "a":
            y = y - 1
        elif move == "w":
            x = x - 1
        elif move == "s":
            x = x + 1
        elif move == "d":
            y = y + 1
        else:
            raise NotImplementedError(f"{move}")
        return x,y


# Ahora movamos un poco a Pacman por el mapa del juego.

# In[ ]:


juego = Juego()
juego.start()


# ### Validar los movimientos de Pacman
# 
# Ahora nos queda agregar un poco más de funcionalidad:
# 
# * Validar que se pierde cuando Pacman coincide en el casillero con un Fantasma
# * Aumentar el score en cada jugada
# * Evitar que los Pacman se salga de los límites del mapa.
# 
# Como el resultado de mover a Pacman puede ser tanto chocarse con la pared, como coincidir con un fantasma y perder, como moverse exitosamente, vamos a ampliar la funcionalidad del método \_actualizar\_mapa. 
# 
# Ahora este método devuelve un status, de acuerdo al resultado de la movida y vamos a renombrarlo como \_actualizar\_mapa\_y\_devolver\_status. Noten lo importante que es que los métodos tengan nombres detallados que señalen todo lo que hacen. De esa forma el código es más legible y eso mejora la experiencia de trabajar colaborando con otros.
# 
# No tengan miedo de usar nombres largos para los métodos. Poner buenos nombres para las variables y funciones hace que el código cuente una historia que otros también puedan leer.

# In[ ]:


class Juego:
    
    def __init__(self):
        # cuando instanciamos el juego creamos personajes. Por ahora las posiciones son fijas pero se podrían hacer al azar
        mapa_inicial = Mapa(7,8)
        mapa_inicial.modificar_elemento(Pacman(),4,3)
        mapa_inicial.modificar_elemento(Fantasma(),1,3)
        mapa_inicial.modificar_elemento(Fantasma(),0,0)
        self.mapa = mapa_inicial
        self.puntaje = 0

    def start(self):
        # Loop con la lógica del juego
        fin = False
        while not fin:
            print(f"score:{self.puntaje}")
            print(self.mapa)
            input_movimiento = input()
            if not self._input_valido(input_movimiento):
                print("El input tiene que ser a, w, s o d")
            else:
                status = self._actualizar_mapa_y_devolver_status(input_movimiento)
                if status == 1:
                    print("Cuidado con la pared")
                if status == 2:
                    print("Perdiste")
                    return
                elif status == 0:
                    self.puntaje += 1

                
    def _input_valido(self, input_movimiento):
        # Valida si el input es correcto
        if input_movimiento in ["a","w","s","d"]:
            return True
        else:
            return False
        
    def _actualizar_mapa_y_devolver_status(self, input_movimiento):
        # Actualiza la posición del pacman
        pacman_x,pacman_y = self._get_posicion_pacman()
        nueva_x, nueva_y = self._avanzar_posicion(pacman_x,pacman_y,input_movimiento)
        print(nueva_x, nueva_y)
        if self._choca_la_pared(nueva_x, nueva_y):
            return 1
        elif isinstance(self.mapa.get_elemento(nueva_x, nueva_y),Fantasma):
            return 2
        else:
            self.mapa.modificar_elemento(CeldaVacia(), pacman_x, pacman_y)
            self.mapa.modificar_elemento(Pacman(), nueva_x, nueva_y)
        return 0
    
    def _get_posicion_pacman(self):
        # Iteramos por todos los elementos del mapa del juego hasta encontrar a Pacman
        for fila in range(self.mapa.n_filas):
            for columna in range(self.mapa.n_columnas):
                elemento = self.mapa.get_elemento(fila,columna)
                if isinstance(elemento,Pacman):
                    # Hay un único elemento de la clase Pacman. Los demás son Fantasma o CeldaVacia
                    return fila, columna
                
    def _choca_la_pared(self, x, y):
        if x >= 0 and x < self.mapa.n_filas and y >= 0 and y < self.mapa.n_columnas:
            return False
        return True
        
                
    @staticmethod
    def _avanzar_posicion(x,y,move):
        if move == "a":
            y = y - 1
        elif move == "w":
            x = x - 1
        elif move == "s":
            x = x + 1
        elif move == "d":
            y = y + 1
        else:
            raise NotImplementedError(f"{move}")
        return x,y


# In[ ]:


juego = Juego()
juego.start()


# ### Agregar el movimiento de los fantasmas
# 
# Ahora vamos a agregar movimiento al azar para los fantasmas al principio de la jugada. Estos pueden moverse en cuatro posibles direcciones. Para decidir adónde irán, vamos a ordenar estas cuatro posiciones al azar y elegir la primera que sea "válida", es decir, que no se choca contra una pared ni trata de ocupar un casillero ya ocupado.
# 
# Noten cómo reutilizamos los métodos que habíamos usado para mover a Pacman "\_choca\_la\_pared" y "\_avanzar\_posicion" vuelven a usarse para mover a los fantasmas

# In[ ]:


class Juego:
    
    def __init__(self):
        # cuando instanciamos el juego creamos personajes. Por ahora las posiciones son fijas pero se podrían hacer al azar
        mapa_inicial = Mapa(7,8)
        mapa_inicial.modificar_elemento(Pacman(),4,3)
        mapa_inicial.modificar_elemento(Fantasma(),1,3)
        mapa_inicial.modificar_elemento(Fantasma(),0,0)
        self.mapa = mapa_inicial
        self.puntaje = 0

    def start(self):
        # Loop con la lógica del juego
        fin = False
        while not fin:
            print(f"score:{self.puntaje}")
            print(self.mapa)
            status = self._mover_fantasmas_y_devolver_status()
            if status == 1:
                print("Perdiste")
                return
            input_movimiento = input()
            if not self._input_valido(input_movimiento):
                print("El input tiene que ser a, w, s o d")
            else:
                status = self._actualizar_mapa_y_devolver_status(input_movimiento)
                if status == 1:
                    print("Cuidado con la pared")
                if status == 2:
                    print("Perdiste")
                    return
                elif status == 0:
                    self.puntaje += 1

                
    def _input_valido(self, input_movimiento):
        # Valida si el input es correcto
        if input_movimiento in ["a","w","s","d"]:
            return True
        else:
            return False
        
    def _actualizar_mapa_y_devolver_status(self, input_movimiento):
        # Actualiza la posición del pacman
        pacman_x,pacman_y = self._get_posicion_pacman()
        nueva_x, nueva_y = self._avanzar_posicion(pacman_x,pacman_y,input_movimiento)
        if self._choca_la_pared(nueva_x, nueva_y):
            return 1
        elif isinstance(self.mapa.get_elemento(nueva_x, nueva_y),Fantasma):
            return 2
        else:
            self.mapa.modificar_elemento(CeldaVacia(), pacman_x, pacman_y)
            self.mapa.modificar_elemento(Pacman(), nueva_x, nueva_y)
        return 0
    
    def _get_posicion_pacman(self):
        # Iteramos por todos los elementos del mapa del juego hasta encontrar a Pacman
        for fila in range(self.mapa.n_filas):
            for columna in range(self.mapa.n_columnas):
                elemento = self.mapa.get_elemento(fila,columna)
                if isinstance(elemento,Pacman):
                    # Hay un único elemento de la clase Pacman. Los demás son Fantasma o CeldaVacia
                    return fila, columna
                
    def _choca_la_pared(self,x, y):
        if x >= 0 and x < self.mapa.n_filas and y >= 0 and y < self.mapa.n_columnas:
            return False
        return True
        
                
    @staticmethod
    def _avanzar_posicion(x,y,move):
        if move == "a":
            y = y - 1
        elif move == "w":
            x = x - 1
        elif move == "s":
            x = x + 1
        elif move == "d":
            y = y + 1
        else:
            raise NotImplementedError(f"{move}")
        return x,y
    
    def _mover_fantasmas_y_devolver_status(self):
        posiciones_fantasmas = self._get_posiciones_fantasmas()
        for posicion_fantasma in posiciones_fantasmas:
            nueva_x, nueva_y = self._nueva_posicion_fantasma(posicion_fantasma)
            if isinstance(self.mapa.get_elemento(nueva_x, nueva_y), Pacman):
                return 1
            else:
                self.mapa.modificar_elemento(Fantasma(),nueva_x, nueva_y)
                self.mapa.modificar_elemento(CeldaVacia(),posicion_fantasma[0], posicion_fantasma[1])
        return 0
    
    def _nueva_posicion_fantasma(self,posicion_fantasma):
        posibles_direcciones = ["a","w","s","d"]
        random.shuffle(posibles_direcciones)
        # El método shuffle modifica la lista "inplace" y cambia el orden original por un orden aleatorio 
        for direccion in posibles_direcciones:
            nueva_x, nueva_y = self._avanzar_posicion(posicion_fantasma[0], posicion_fantasma[1], direccion)
            if not self._choca_la_pared(nueva_x, nueva_y) and                 not isinstance(self.mapa.get_elemento(nueva_x, nueva_y), Fantasma):
                return nueva_x, nueva_y

    def _get_posiciones_fantasmas(self):
        posiciones_fantasmas = []
        for fila in range(self.mapa.n_filas):
            for columna in range(self.mapa.n_columnas):
                elemento = self.mapa.get_elemento(fila,columna)
                if isinstance(elemento,Fantasma):
                    posiciones_fantasmas.append((fila,columna))
        return posiciones_fantasmas
          
           
        


# In[ ]:


juego = Juego()


# In[ ]:


juego.start()


# ## Fantasmas perseguidores
# 
# Ahora sería bueno que los fantasmas sean inteligentes. Es decir que persigan a Pacman por el tablero en vez de moverse aleatoriamente. 
# 
# Para eso vamos a programarles el siguiente comportamiento: van a acercarse a Pacman en la dirección en la cual se encuentran más lejos. Lo bueno de este comportamiento es que nunca los va a hacer chocarse contra una pared así que podemos borrar ese control.
# 
# Imaginen esta posición en el tablero.
# 
# |        |        |        |        |        |
# |--------|--------|--------|--------|--------|
# | .      | .      | .      | G(0,4) | .      |
# | .      | .      | .      | .      | .      |
# | P(3,0) | .      | .      | .      | .      |
# | .      | .      | .      | .      | .      |
# 
# Para acercarse a Pacman el fantasma se debería mover hacia la izquierda porque la distancia más grande se encuentra en el eje y. Cuando la diferencia más grande está en el eje x, el fantasma se debería mover para arriba o para abajo. El signo de la diferencia es el que determina concretamente para dónde se mueve el fantasma. En caso de empate, cualquiera de las direcciones es lo mismo.
# 
# Ejercicio
# Agranden el tamaño del tablero a 10x10 y modifiquen el método <code> _mover_fantasmas_y_devolver_status </code> para que los fantasmas sean perseguidores. 
# 

# In[ ]:





# In[ ]:


juego = Juego()
juego.start()


# In[ ]:




