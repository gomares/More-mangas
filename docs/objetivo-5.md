## Contenedor: Docker - Python 1.30 Alpine

Para la construcción del archivo update_docker.yml se ha seguido la [documentación oficial de GitHub](https://docs.github.com/es/actions/publishing-packages/publishing-docker-images).

Para la elección de la imagen de python usada en el Dockerfile se han seguido las buenas práctica de la [documentación oficial de Docker](https://docs.docker.com/language/python/build-images/), también he investigado acerca de las posibles imágenes que instalar.


La imagen a usar debe ser una imagen ligera que facilite el despliegue posterior de la aplicación. Por lo tanto, la imagen completa de python fue descartada, siendo demasiado pesada. En ese caso, -slim y -alpine eran dos fuertes candidatas. Slim al principio no daba problemas pero había instaladas bibliotecas y programas que NO eran necesarias para el proyecto, por tanto probé con -alpine.


Al intentar construir la imagen daban MUCHOS errores, sin embargo no desfacellí y empecé a instalar dependecias necesaria, entre ellas estaba "gcc" y la librería "libffi". También tenía problemas al manejar apk ya que daba erorres de permisos:

```console
#10 0.227 ERROR: Unable to lock database: Permission denied
#10 0.227 ERROR: Failed to open apk database: Permission denied
```


Después de resolver todos los errores la imagen funciona a las mil maravillas y  además la relación de tamaño respecto a la versión slim es de 3 a 1, bastante notable:

```console
abrahamg@MacBook-Pro-de-Abraham Proyecto_IV % docker images                        
REPOSITORY                            TAG                  IMAGE ID       CREATED          SIZE
python                                3.10.1-alpine3.15    eb5bc7d10d52   1 days ago       45.4MB
python                                3.10-slim-bullseye   9328aba7e797   1 days ago       123MB
```


Los puntos negativos que veo a usar Alpine son, por un lado, que puede dar errores díficiles de depurar a veces aunque en este caso he podido resolverlos todos y, por otro lado, que el tiempo de construcción es mayor que el de la imagen slim, con Alpine tarda alrededor de 30 segundos y con sim tan solo 10 segundos.


### Anexo sobre el DockerFile:

En la construcción del docker usamos la siguiente orden: 
```shell
poetry config virtualenvs.create false
```

Debido a que con el uso de docker ya tenemos un entorno virtual, no es necesario crear el de poetry. Tras investigar acerca de la creación de Dockerfiles que incluyan poetry, he llegado a la conclusión de que no es necesario el entorno virtual de poetry.
La alternativa sería editar la variable de entorno $PATH global, no la perteneciente al entorno virtual de docker.

### Sobre la versión de Python:

He instalado la 3.10 porque investigué primeramente sobre las versiones que había disponibles de Python y vi que el mantenimiento en la 3.8 y 3.9 acabaría unos años antes que la 3.10 y empecé a ver las [características que se incluían en el nuevo python 3.10](https://www.analyticsvidhya.com/blog/2021/08/differences-between-python-3-10-and-python-3-9-which-you-need-to-know/) y encontré especialmente útiles para el proyecto las siguientes:

* Using a Structural Pattern for Matching (Para diseño de apis y gestión de errores)
* Improved Syntax Error Messages - Esta es de mis favoritas, se agradece cualquier ayuda por pequeá que sea a la hora de depurar un programa hecho en un lenguaje de alto nivel.