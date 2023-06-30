# Importamos sleep y randint para simular un proceso pueda tardar entre 1 y 5 segundos
from time import sleep
from random import randint

# Importamos la variable "app" nuestro archivo celery y le asignamos el nombre de celery_app
from Celery.app import app as celery_app

# @celery_app: Es un decorador que nos permite registrar una función como tarea.
# Al aplicar este decorador a una función, estás indicando a Celery que esa función debe tratarse como
# una tarea asincrónica que se puede ejecutar en segundo plano.
# name: Es el nombre de la tarea. Si no se especifica, se utiliza el nombre de la función.
@celery_app.task(name='add')
def add(x, y):
    sleep(randint(1, 5))
    print(x + y)


@celery_app.task(name='mul')
def mul(x, y):
    sleep(randint(1, 5))
    print(x * y)