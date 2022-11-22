import click
import requests

@click.command()
@click.option('--numero', type=int, default=1, help='El numero a buscar.')
def numero_trivia(numero):
    """Programa que arma busca trivias sobre el número que se le indique."""
    # el endpoint de la API
    key = f'http://numbersapi.com/{numero}/'
    
    data = requests.get(key)  
    data = data.text
    
    click.echo(data)
    
if __name__ == '__main__':
    numero_trivia()
