# Imagen padre desde la que vamos a heredar. Podriamos usar otra?
FROM python:3.10

# Directorio adentro del container en donde vamos a trabajar
# Es como hacer un cd, sino estariamos trabajando en el /
WORKDIR /app

# Contexto: Copia todo el contenido de este directorio adentro del container en la carpeta /app
COPY . /app

# Correr un comando, en este caso para instalar las dependencias en requirements.txt
RUN pip install -r requirements.txt

# Abre el puerto 5000 del container
EXPOSE 5000

# Cuando el container se lance va a ejecutar este comando
CMD ["python", "app.py"]