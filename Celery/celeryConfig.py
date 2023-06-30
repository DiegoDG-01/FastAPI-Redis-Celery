# enable_utc: Establece el uso de UTC.
enable_utc = True
# task_serializer: Establece el serializador de tareas para usar el formato JSON.
task_serializer = 'json'
# result_serializer: Establece el serializador de resultados para usar el formato JSON.
result_serializer = 'json'
# broker_url: Establece la URL del broker de mensajes.
broker_url = 'redis://localhost:6379/0'
# result_backend: Establece la URL del backend de resultados. (En este caso, el mismo que el broker de mensajes)
result_backend = 'redis://localhost:6379/0'
# Celery intentará reconectarse al broker si la conexión falla al iniciar la aplicación
broker_connection_retry_on_startup = True
# imports: Establece una lista de módulos para importar cuando se inicia la aplicación.
# En este caso, importamos el módulo tasks.py el cual contiene en su archivo previamente definido las tareas que
# queremos ejecutar.
imports = (
    'tasks',
)