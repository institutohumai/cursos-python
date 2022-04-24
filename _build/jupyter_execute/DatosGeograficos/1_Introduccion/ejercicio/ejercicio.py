#!/usr/bin/env python
# coding: utf-8

# <h1 id="tocheading">Tabla de contenidos</h1>
# <div id="toc"></div>

# I. Tabla de contenidos
# 
#     I. Ejercicios
#     II. Leemos y cargamos geometrías
#     III. Pasamos todo a GKBA
#     IV. Calculamos centroide y distancias
#     V. Graficamos y comparamos
#     VI. Barrio con mayor distancia a hospitales

# ## Ejercicios
# 
# Cuando uno realiza análisis urbanos es común intentar resumir la heterogeneidad de condiciones en pocas métricas, para poder entender cómo se fragmenta las ciudades con zonas de mayor o menor calidad de servicios, condiciones de vida, facilidad en circulación o conectividad, etc.
# 
# En este caso vamos a tratar de generar indicadores de accesibilidad por barrios para analizar:
# 
# - El acceso a la salud pública
# 
# - El acceso a los servicios de bomberos
# 
# 1- Para ello, se propone calcular las siguientes métricas:
# 
#     a- Obtener el centroide para cada barrio.
# 
#     b- Medir la distancia de cada centroide a cada estación de bomberos (u hospital).
#     
#     c_1- Generamos la métrica "Distancia a hospitales":  entendiendo que a veces los hospitales pueden saturarse o tienen mayor diversidad de especializaciones (por ejemplo, hay hospitales especializados en niños o en problemas psiquiátricos) calculamos la distancia promedio a los 3 más cercanos. 
#     c_2 - Generamos la métrica "Distancia a bomberos": en el caso de los bomberos se decide sólo tomar la distancia al más cercano.
# 
# Para que la métrica sea más interpretable debemos calcular la distancia en metros o kilómetros.
# 
# 2- Luego analicemos los resultados. Para ello se propone:
# 
#     a- comparar un histograma de la distribución de la distancia a bomberos y a hospitales por barrios. Deberían encontrar que la distribución a los hospitales presenta "una cola más larga". Es decir, hay barrios que están relativamente más lejos.
# 
#     b- Finalmente, se pide que encuentren el barrio con mayor distancia a los hospitales y generen un mapa donde muestren en distintos colores:
#     
#     - Barrios
#     
#     - Hospitales
#     
#     - El barrio con mayor distancia

# ## Leemos y cargamos geometrías

# In[ ]:





# ## Pasamos todo a GKBA

# In[ ]:





# ## Calculamos centroide y distancias

# In[ ]:





# ## Graficamos y comparamos

# In[ ]:





# ## Barrio con mayor distancia a hospitales

# In[ ]:




