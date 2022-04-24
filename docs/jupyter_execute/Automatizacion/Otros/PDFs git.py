#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as rq
import re

def get_pdfs(url, path):
    content = rq.get(url).text
    pattern = r'\/(.+?pdf)'
    #cambio para descargar
    urls = [r'https://github.com/' + re.sub(r'/blob/', r'/raw/', url_) for url_ in re.findall(pattern, content)]
    for url_ in urls:
        pdf = rq.get(url_).content
        autor = url_.split('/')[3]
        nombrePdf = url_.split('/')[-1]
        file = '{} {}'.format(autor, nombrePdf)
        print(file)
        with open(file, 'wb') as out:
            out.write(pdf)
    return None


# In[2]:


import os
os.chdir(r'D:\Matias\PDFs Ciencia\Estadística y Data Science')


# In[3]:


get_pdfs(url = r'https://github.com/jdwittenauer/ipython-notebooks/tree/master/exercises/ML', path = r'D:\Matias\PDFs Ciencia')

