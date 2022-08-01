
def truco(cantaron_truco = False):
    import random
    import requests
    r = ["quiero", "quiero retruco", "quiero vale 4", "no quiero" ]

    if cantaron_truco == True:
         frase = random.choice(list(r))
    else:
        frase = "truco!"
    print(frase)

if __name__ == "__main__":
    truco(cantaron_truco = True)
