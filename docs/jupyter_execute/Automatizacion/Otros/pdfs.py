#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install textract')


# In[81]:


import textract
import os
from shutil import copyfile


# In[82]:


pdf_dir = r"./papers"


# In[85]:


ruta_neuro = 'Neuro'
os.makedirs(ruta_neuro, exist_ok=True)


# In[86]:


ruta_deep = 'Deep'
os.makedirs(ruta_deep, exist_ok=True)


# In[ ]:


ruta_otros = 'Otros'
os.makedirs(ruta_otros, exist_ok=True)


# In[87]:


files = os.listdir(pdf_dir)


# In[105]:


def limpiar(s):
    """Función para limpiar los renglones quitando los caracteres que no queremos considerar"""
    no_valen = '0123456789-:. '
    return ''.join([i for i in s if i not in no_valen])


# In[106]:


def get_title(texto):
    """Función para extraer un título. Sería mejor usar regex! 
    También podríamos mejorar la lógica o usar distintos enfoques"""
    return [t for t in top.split('\n') if len(limpiar(t)) > 25][0]


# In[104]:


files = os.listdir(pdf_dir)

for filename in files:
    full_name = os.path.join(pdf_dir, filename)
    text = textract.process(full_name, language='eng').decode()
    top = text[:1000]
    
    try:
        title = [t for t in top.split('\n') if len(limpiar(t)) > 25][0]
    except:
        title = filename
        
    is_deep = ('deep learning' in text.lower()) or ('statistic' in text.lower())
    is_neuro = ('neuro' in text.lower()) or ('brain' in text.lower())

    print(title)
    if is_neuro:
        print('Neuro')
        copyfile(f"{pdf_dir}/{filename}", f"{ruta_neuro}/{title}.pdf")
    elif is_deep:
        print('Deep')
        copyfile(f"{pdf_dir}/{filename}", f"{ruta_deep}/{title}.pdf")
    else:
        print('Otros')
        copyfile(f"{pdf_dir}/{filename}", f"{ruta_otros}/{title}.pdf")    
        
    print()

