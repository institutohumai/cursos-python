'''
Módulo que contiene la función dados_locos.
'''
import random
def dados_locos():
    '''
    Devuelve un string con el tipo de dado y cantidad de veces que debe ser arrojado.
    '''
    tirada_dados = {'blanco':1, 'rojo':2, 'verde':3, 'amarillo':4}
    dado = random.choice(list(tirada_dados.keys()))
    veces = random.choice(list(tirada_dados.values()))
    if veces==1:
        frase = f'Tira el dado {dado} un total de {veces} vez'
    else:
        frase = f'Tira el dado {dado} un total de {veces} veces'
    print(frase)

if __name__ == "__main__":
    dados_locos()
