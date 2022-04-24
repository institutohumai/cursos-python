#!/usr/bin/env python
# coding: utf-8

# ## Descargar letras de canciones
# 
# Utilizando beautiful soup descargar todas las canciones de [Spinetta](https://es.wikipedia.org/wiki/Luis_Alberto_Spinetta) que hay en [letras.com](https://www.letras.com/spinetta/)

# In[ ]:


from bs4 import BeautifulSoup
import requests
import os

letras_url = "https://www.letras.com"

def descargar_cancion(url_path, destination_path):
    url = f"{letras_url}{url_path}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    letra = ""

    for div in soup.findAll("div", {"class": "cnt-letra p402_premium"}):
        for p in div.findAll("p"):
            text = str(p)
            for space in ["</br>","<br>","<br/>","<p>","</p>"]:
                text = text.replace(space,"\n")
            letra += text

    with open(destination_path,'w') as f:
        f.write(letra)

def descargar_letras(artista):

    url = f"{letras_url}/{artista}/mais_tocadas.html"
    page = requests.get(url)

    if not os.path.exists(artista):
      os.mkdir(artista)

    soup = BeautifulSoup(page.content, 'html.parser')

    i = 0
    for a in soup.findAll("a", {"class": "song-name"}):
        descargar_cancion(a["href"], f"{artista}/{i:03d}.txt")
        i += 1
        
artista = "luis-alberto-spinetta"
descargar_letras(artista)

