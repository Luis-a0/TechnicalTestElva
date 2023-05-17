# TechnicalTestElva

## Pasos para su la ejecución del proyecto.
Para la ejecución del proyecto se requiere de un token para acceder a la API de Google Maps y esta debe de guardarse en un archivo .env bajo la clave *key*.

Posteriormente, se requiere que instale las dependencias listadas en el archivo *requirements.txt*.

Finalmente, podrá probar la aplicación ejecutando el archivo *app.py*
```sh
pip install requirements.txt
python app.py
```

## Decisiones tomadas durante el desarrollo del reto.
- En primera instancia se analizó el problema planteado y se dividió en 4 funciones a implementar.
- Dichas funciones tenían que cumplir con las tareas de:
    - Conectarse a la API de Google Maps.
    - Obtener las coordenadas de una locación basándonos en una dirección.
    - Obtener el nombre de un vecindario con base en un par de coordenadas.
    - Obtener el nombre de un vecindario próximo al vecindario encontrado en primera instancia.
- Posteriormente, se agregó una función que permitiera la modificación del número de una dirección.

