#!/usr/bin/env python
# coding: utf-8

# # Data en batch

# In[1]:


import os
import pandas as pd
from sqlalchemy import create_engine


# In[2]:


DATASET_URL = os.environ.get('DATASET_URL', 'https://bank-marketing.s3.amazonaws.com/bank-additional-full.csv')

POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
# POSTGRES_HOST = os.environ.get(DATASET_URL, 'local_pgdb')
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE', 'bank')

SQLALCHEMY_DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DATABASE}'
    
TABLE_NAME = 'clients'


# In[ ]:


print('Leyendo el dataset')


# In[4]:


bank_data_df = pd.read_csv(DATASET_URL, sep=';')


# In[5]:


bank_data_df.info()


# In[6]:


print(bank_data_df.head(10))


# In[7]:


print('Escribiendo en base de datos')
engine = create_engine(SQLALCHEMY_DATABASE_URL)
bank_data_df.to_sql(name=TABLE_NAME, con=engine, if_exists='replace', index=False)


# In[ ]:


# !pip install --upgrade nbconvert
# !jupyter nbconvert --to script batch-data.ipynb

