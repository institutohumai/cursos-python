import pandas as pd


def normalizar_unidades_territoriales(entidades, entidades_tipo,
                                      chunk_size=1000):
    '''Normaliza unidades territoriales usando la API Georef.'''

    # genera un array vacio para guardar los resultados de cada request
    resultados = []

    # genera un resultado nulo para reemplazar los casos que no funcionen
    resultado_nulo = {
        'id': None,
        'nombre': None,
        f'{entidades_tipo[:-1]}_id': None,
        f'{entidades_tipo[:-1]}_nombre': None,
    }

    for i in range(0, len(entidades), chunk_size):
        start, end = i, i + chunk_size

        # el final no puede ser mayor a la cantidad de entidades
        if end > len(entidades):
            end = len(entidades)

        # genera el JSON con la lista de consultas a realizar
        data = {
            entidades_tipo: [
                {
                    'nombre': nombre,
                    'max': 1,
                    'campos': 'id,nombre'
                }
                for nombre in entidades[start:end]
            ]
        }

        try:
            # realiza la consulta
            resultados.extend(requests.post(
                f"https://apis.datos.gob.ar/georef/api/{entidades_tipo}",
                json=data
            ).json()['resultados'])
        except Exception as e:
            print(f'No se pudo normalizar el bloque {start} a {end}. '
                  'Reemplazando por resultados nulos.')
            resultados.extend([resultado_nulo] * (end - start))

    # parsea la respuesta
    entidades_normalizadas = [
        resultado[entidades_tipo][0]
        for resultado in resultados
    ]

    return pd.DataFrame(entidades_normalizadas)
