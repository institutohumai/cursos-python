'''
Módulo que contiene la función truco.
'''
import random

def truco(cantaron_truco = False):
    """ Esta función replica una jugada de truco"""
    respuesta = ["quiero", "quiero retruco", "quiero vale 4", "no quiero"]

    if cantaron_truco is True:
        frase = random.choice(list(respuesta))
    else:
        frase = "truco!"
    print(frase)

if __name__ == "__main__":
    truco(cantaron_truco = True)
