FROM python:3.10

WORKDIR /code

COPY . /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# COPY ./app /code/app

CMD ["python", "batch-data.py"]