#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/Scraping/2_HTTP_Avanzado/scraping_extra_tips.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" data-canonical-src="https://colab.research.google.com/assets/colab-badge.svg"></a>

# # Tips para scrapear mejor
# 
# - Scrapear multiples cosas al mismo tiempo: https://python-docs-es.readthedocs.io/es/3.8/library/multiprocessing.html

# In[6]:


from multiprocessing import Pool

from requests import get

def bajar_datos(url):
    return get(url).text

# En este ejemplo intento bajar varios datos del sitio web numbersapi.com

urls = [f"http://numbersapi.com/{number}" for number in [1,2,3,4,5,6,7,8]]
print(urls)


# In[7]:


# De esta manera voy bajando los dato de a uno

for url in urls:
    resultado = bajar_datos(url)
    print(resultado)


# In[8]:


# De esta manera hago todo al mismo tiempo, en paralelo

with Pool(5) as p:
    print(p.map(bajar_datos, urls))


# Una alternativa es multithreading: 

# 
# - Evitar que te bloqueen
#     - Rotacion de ip y useragent
#         - rotacion de userAgent: https://pypi.org/project/fake-useragent/
#         - smartproxy y https://github.com/mattes/rotating-proxy
#         
#     - A veces las cuentas premium las banean/bloquean menos, ya que son la fuente de dinero del sitio y son "intocables" (Ejemplo: Spotify)
# 
# - Crear cuentas sin límites
#     - Registración con teléfono
#         - Teléfonos descartables (proovl y twilio)
#         - Reutilizar un mismo teléfono: +54/+549/11/15/011
# 
#     - Registración con email
#         - Emails descartables
#         - Reutilizar un mismo mail: pedroperez@gmail.com/pedro.perez@gmail.com/...
# 
# - [Resolver captchas](https://addons.mozilla.org/en-US/firefox/addon/recaptcha-solver/)
# 
# - [Acceder a sitios viejos](http://web.archive.org/)
# 
# 
