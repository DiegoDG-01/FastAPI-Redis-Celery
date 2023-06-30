# Importamos celery
from celery import Celery

# Creamos la instancia de celery y le asignamos el nombre de la app
app = Celery('tasks_celery')
# Le asignamos la configuracion para celery
# Celery.celeryConfig hace referencia al archivo celeryConfig.py que se encuentra en la carpeta Celery
# Celery/celeryConfig.py
# Porque poner Celery.celeryConfig y no solo celeryConfig?
# Cuando importamos app.py desde Blog.ipynb, estamos al mismo nivel que se encuentra Blog.ipynb
# Por lo tanto, si ponemos celeryConfig, no va a encontrar el archivo.
app.config_from_object('Celery.celeryConfig')