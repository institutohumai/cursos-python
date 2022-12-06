import os
import click
import requests
import pandas as pd
import datetime

def numero_trivia():
    """Programa que arma busca trivias sobre el número que se le indique."""
    # usamos el modulo datetime para obtener el valor del minuto de la ejecucion
    numero = datetime.datetime.now().minute
    
    # el endpoint de la API
    key = f'http://numbersapi.com/{numero}/'
    
    data = requests.get(key)  
    data = data.text
    
    # ahora necesitamos que la funcion devuelva el texto
    return data
    
if __name__ == '__main__':
    
    # aplicamos la logica para construir las carpetas
    path = 'trivia'
    os.makedirs(path, exist_ok=True)
    TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    trivia = numero_trivia()
    
    # armamos el nombre del archivo usando el path con la carpeta que creamos y el timestamp
    FILENAME = f'{path}/trivia_{TIMESTAMP}.txt'
    text_file = open(FILENAME, 'w')
    text_file.write(trivia)
    text_file.close()
    print(f'Creé el archivo {FILENAME}')
    print(f'Trivia: {trivia}')
    
