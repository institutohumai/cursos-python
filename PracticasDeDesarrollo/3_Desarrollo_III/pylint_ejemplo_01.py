def dados_locos():
    import random
    import csv
    d = {'blanco':1, 'rojo':2, 'verde':3, 'amarillo':4}
    dado = random.choice(list(d.keys()))
    veces = random.choice(list(d.values()))
    if veces==1:
         frase = f'Tira el dado {dado} un total de {veces} vez'
    else:
        frase = f'Tira el dado {dado} un total de {veces} veces'
    print(frase)

if __name__ == "__main__":
    dados_locos()
