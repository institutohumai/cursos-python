#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/institutohumai/cursos-python/blob/master/MachineLearning/8_ShapyAnomalias/anomaly-detection-shap-values.ipynb"> <img src='https://colab.research.google.com/assets/colab-badge.svg' /> </a>
# <div align="center"> Recordá abrir en una nueva pestaña </div>

# # Detección de anomalías y explicabilidad de modelos con valores SHAP

# #### Tabla de Contenidos
# 
# 1) Importar dependencias, definir los parámetros y explorar los datos.
# 
# 2) Detección de anomalías: métodos univariados y multivariados.
# 
# 3) Explicabilidad de modelos: desempeño versus parsimonia, técnicas de subrogación, valores SHAP.

# ## 1) Importar dependencias, explorar los datos y definir los parámetros

# Utilizo el _magic command_ `bash` (ver más [aquí](https://ipython.readthedocs.io/en/stable/interactive/magics.html) para crear el archivo de dependencias requeridas e instalarlas.

# In[1]:


get_ipython().run_cell_magic('bash', '', "\necho $'matplotlib \\nnumpy==1.20 \\npandas \\nsklearn \\nxgboost \\nseaborn \\nshap'  > requirements.txt\npip3 install -r requirements.txt")


# Importo las dependencias instaladas.

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import xgboost as xgb
import shap
from IPython import display
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_curve, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

shap.initjs()


# Defino parámetros de semilla y el estilo de los graficos y los valores de punto flotante.

# In[3]:


sns.set_style("ticks")
sns.set_context("paper")

seed = 1234
np.set_printoptions(formatter={'float_kind':'{:f}'.format})


# Cargo el conjunto de datos desde la instancia de Colab. En este caso usaremos el mismo que para la clase de XGBoost, el [Adult de la UCI](https://archive.ics.uci.edu/ml/datasets/Adult). En caso de no estar disponible (por ejemplo, la primera vez que se ejecuta el código) se lo descarga desde el repositorio público de Humai. 

# In[4]:


try:
    data = pd.read_csv("device_failure.csv")
except:
    data = pd.read_csv("https://datasets-humai.s3.amazonaws.com/datasets/adult_train.csv")
    data.to_csv("device_failure.csv", index = False)


# Analizo los datos, comenzando por los primeros registros y siguiendo por la distribución de las variables cuantitativas y la variable objetivo.

# In[5]:


data.head()


# In[6]:


data.describe()


# La variable objetivo `target` define si una persona tenía un ingreso anual superior a los 50 mil dólares estadounidenses al momento de ser relevada la información.

# In[7]:


pd.value_counts(data.target)


# Reemplazamos las categorías de la variable objetivo por valores binarios.

# Normalizamos los datos utilizando la estandarización de `scikit-learn`

# In[8]:


numeric_data = data[["education-num", "capital-gain", "capital-loss", "hours-per-week"]]


# In[9]:


scaler = StandardScaler()
scaled_data = pd.DataFrame(scaler.fit_transform(numeric_data), 
                           columns = numeric_data.columns)


# ## 2) Detección de anomalías
# 
# Para tener una primera aproximación es útil estandarizar el conjunto de datos -las variables cuantitativas- y graficarlas usando un _boxplot_. Así, podemos tener rápidamente una idea de la cardinalidad de las variables y la cantidad de _outliers_ potenciales, a quienes podemos definir como puntos por fuera de los "bigotes" del _boxplot_. Si lo pensamos en términos de desvíos estándar, en este caso los "bigotes" comprenden 3 desvíos para sólo graficar por fuera puntos que están realmente lejos.

# In[10]:


data_boxplot = sns.boxplot(data = scaled_data, orient = "h", palette = "Set2", whis = 3)
plt.title("Distribución de valores estandarizados por variable")
plt.xlabel("Valor")
data_boxplot.figure.set_size_inches(18,5)


# Para analizar los _outliers_ puedo evaluar cuántos puntos se ubican a más de 3 veces el rango intercuartil (IQR) con una técnica conocida como [Tukey's fences](https://en.wikipedia.org/wiki/Outlier#Tukey%27s_fences). Si bien estos puntos son probablemente _outliers_, siempre es importante tener en cuenta el dominio de análisis.

# ### Ejercicio 1: Calcular el IQR para al menos dos variables del conjunto de datos

# Para facilitar el análisis -y no tener que hacerlo nosotros- vamos a utilizar el mismo conjunto de datos pero tomándolo desde su versión previamente categorizada en la librería `shap`.

# In[11]:


numeric_data,y = shap.datasets.adult()


# In[12]:


numeric_data.head()


# ### Isolation Forest
# 
# La técnica de detección de anomalías conocida como Isolation Forest es muy útil para detectar _outliers_ multivariados. Es un método similar al de _Random Forest_ y funciona mediante la selección aleatoria de particiones de variables aleatorias. Dado que los _outliers_ son menos frecuentes que las observaciones normales, el método asume para calcular su _score_ que debieran estar más cerca de la raíz del árbol (dado que residen en regiones dispersas -ralas- del espacio de variables).

# In[13]:


display.Image("https://www.relataly.com/wp-content/uploads/2021/06/image-40.png")


# 
# 
# En términos formales, el valor de la probabilidad de que un registro sea anomalo está dado por la siguiente ecuación:

# ## $s(x_i, N) = 2 ^ \frac{-E(h(x_i))}{c(N)}$

# donde $s$ es el score, $x_i$ es la observación, $E(h(x_i))$ es el promedio de longitud de los caminos y $c(N)$ es la longitud promedio de una búsqueda no exitosa en un árbol binario (BST, por su acrónimo en inglés).

# Dado que la construcción de este modelo es similar a un árbol binario de búsqueda, por estar basada en selecciones de atributos y particiones aleatorias, podemos aproximar el camino promedio de un nodo con la búsqueda no exitosa en un árbol binario. Es por este motivo que tomamos el término $c(N)$ como referencia. 
# 
# Como puede deducirse de la función detallada, mientras más se diferencie el promedio de longitud de los caminos con el de las búsquedas no exitosas más alta va ser la probabilidad de anomalía.

# #### Entrenar un modelo y predecir valores anómalos
# 
# Lo primero que vamos a hacer es analizar los parámetros más relevantes.

# In[14]:


iso_forest = IsolationForest(max_samples = "auto", contamination = "auto", random_state = seed)


# In[15]:


iso_forest.fit(numeric_data)


# In[16]:


outlier_pred = iso_forest.predict(numeric_data)
outlier_pred = [False if x == 1 else True for x in outlier_pred]


# In[17]:


data[outlier_pred].head()


# ### Ejercicio 2: compararlo con la distribución de la variable "Education-Num"

# Los métodos multivariados de detección de anomalías son útiles también para encontrar patrones en la clase minoritaria que nos permitan mejorar la representación de la información.

# ## 3) Explicabilidad de modelos

# Uno de los libros más relevantes para profundizar en el dominio de la interpretabilidad es [Interpretable Machine Learning] (https://christophm.github.io/interpretable-ml-book/) de Christoph Molnar. Allí se enumeran distintos tipos de interpretaciones que se pueden categorizar en 3 grupos: 
# 
# 1) Modelos interpretables
# - Regresión lineal, logística, modelos lineales generalizados, árboles
# 2) Métodos agnósticos de los modelos
# - PDP, ICE, ALE, Feature Importance, modelos surrogados, LIME, SHAP
# 3) Explicaciones basadas en ejemplos
# - Contrafácticas, adversarias

# #### Creación del conjunto para entrenar
# Vamos a cargar el mismo conjunto de datos pero desde la librería `SHAP`

# In[18]:


X,y = shap.datasets.adult()

X_display,y_display = shap.datasets.adult(display=True)


# Dividimos en entrenamiento y validación

# In[19]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=seed)


# #### Entrenamiento de modelo de extreme gradient boosting (XGBoost)
# 
# La técnica de XGBoost fue explicada en clases anteriores. Aquí modelaremos usando un conjunto no optimizado de hiperparámetros, con cien iteraciones y _early stopping_.

# In[20]:


dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)


# In[21]:


params = {
    "eta": 0.01,
    "objective": "binary:logistic",
    "subsample": 0.5,
    "base_score": np.mean(y_train),
    "eval_metric": "logloss"
}


# In[22]:


model_xgboost = xgb.train(params, dtrain, 1000, evals = [(dtest, "test")], verbose_eval=100, early_stopping_rounds=100)


# #### Feature importance
# 
# Antes de evaluar los valores Shapley utilizando la librería `SHAP` analizaremos la métrica de importancia de atributos con la que cuenta XGBoost. Hay tres maneras de evaluarla: peso (weight), ganancia (gain) y cobertura (coverage).
# 
# 1) El peso refiere a la cantidad de veces que un atributo aparece en un árbol.
# 
# 2) La ganancia representa a la ganancia promedio de los cortes que utilizan el atributo. 
# 
# 3) La cobertura refiere a la cobertura -cantidad de registros afectados- promedio de las divisiones que usan el atributo.

# In[23]:


xgb.plot_importance(model_xgboost, importance_type = "gain")
plt.show()


# #### SHAP

# La librería [`SHAP`( SHapley Additive exPlanations)](https://shap.readthedocs.io/en/latest/index.html) utiliza los valores Shapley, provenientes de la teoría de juegos, para explicar el comportamiento de los modelos. 
# En este caso, al contar con un modelo basado en árboles, utilizaremos la función `TreeExplainer()`.

# In[24]:


explainer = shap.TreeExplainer(model_xgboost)
shap_values = explainer.shap_values(dtrain)


# In[25]:


shap.summary_plot(shap_values, X_display, plot_type="bar")


# In[26]:


shap.force_plot(explainer.expected_value, shap_values[0,:], X_display.iloc[0,:])


# Los gráficos de dependencia muestran el efecto de un atributo específico a través de todo el conjunto de datos. Contrastan su valor con el valor SHAP de dicho atributo a través de muchos registros. Si bien son similares a los _Partial Dependency Plots_ (PDP), toman además en cuenta las interacciones entre los atributos, que se evidencia en la dispersión vertical en un determinado valor y en el color de la variable elegida a tal fin.

# In[27]:


for name in X_train[["Relationship", "Capital Gain", "Capital Loss"]].columns:
    shap.dependence_plot(name, shap_values, X_train, display_features=X_display)


# ### Próximos pasos:

# - Las técnicas de detección de anomalías pueden ser utilizadas para detectar patrones en los comportamientos de las clases minoritarias (en este caso, aquellas personas con un ingreso anual mayor a USD50 mil).
# 
# - Se pueden aplicar técnicas de _clustering_ a los valores de Shapley para evaluar el potencial de ingresos, en línea con lo mencionado sobre los patrones que se pueden detectar. Este tipo de _clustering_ supervisado es una alternativa interesante para validar la pertinencia de los valores.
