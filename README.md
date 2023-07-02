# FastAPI, Redis y Celery

En este repositorio encontrarás un notebook que explica cómo utilizar FastAPI, Redis y Celery juntos en un ejemplo sencillo.

Si quieres saber un poco mas de estas herramientas y este mini proyecto puedes visitar mi [web](https://diegodg.com.mx/2023/06/28/fastapi-celery-y-redis-los-tres-mosqueteros/) 🤓.

## Requisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- Python 3.8+
- FastAPI
- Redis
- Celery

## Estructura del repositorio

El repositorio se organiza de la siguiente manera:

```
.
├── Blog.ipynb
├── Celery
│   ├── app.py
│   └── celeryConfig.py
├── requirements.txt
├── tasks.py
└── README.md
```

- `Blog.ipynb`: Es el notebook preparado para iniciar FastAPI e importar los archivos necesarios.
- `Celery/app.py`: El archivo donde inicializamos celery.
- `Celery/celeryConfig.py`: Es el archivo principal de configuración de celery
- `requirements.txt`: Lista de dependencias de Python necesarias para ejecutar el ejemplo.
- `tasks.py`:  Nuestro archivo que contiene las funciones que podremos usar con celery
- `README.md`: Este archivo, que proporciona una descripción general del repositorio.

## Ejecutando el ejemplo

Sigue estos pasos para ejecutar el ejemplo:

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual y activa el entorno.
3. Instala las dependencias ejecutando `pip install -r requirements.txt`.
4. Inicia el servidor de FastAPI accediendo y ejecutando el notebook.
5. Inicia el trabajador de Celery ejecutando `celery -A app.celery_tasks worker --loglevel=info`.
6. Accede la siguiente dirección 127.0.0.1:8000/docs.
7. Pruebas las funciones dentro del panel que nos proporciona FastAPI

¡Y eso es todo! Si sigues estos pasos, deberías poder ejecutar el ejemplo de FastAPI, Redis y Celery correctamente.

## Contribuir

Si deseas contribuir a este proyecto, siéntete libre de enviar pull requests. ¡Tus contribuciones son bienvenidas!

## Licencia

Este repositorio se distribuye bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más información.


