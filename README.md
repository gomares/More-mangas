# More Mangas!

## Idea General :bulb:

El sector del manga y los webtoons continúa creciendo y llevando sus obras literarias al resto del mundo. Cientos de novelas están siendo transformadas en obras ilustradas por mangakas. Nuestra aplicación contribuirá a que las personas nuevas en ese mundo reciban una buena dosis de entretenimiento y para que las más experimentadas, que no saben que más pueden ver, encuentre joyas ocultas que quizás no sean tan populares.

## Descripción :clipboard:

Se trata de una aplicación para amantes del manga o de los webtoons y para lectores no tan experimentados pero que están interesados en saber más del mundillo. Con esta app podrán recibir las mejores recomendaciones gracias a nuestro algoritmo, el cual se apoyará en un análisis previo de los gustos del usuario y además les ofrecerá información de interés como pueden ser los sitios dónde leer el manga con la mejor calidad y algunas curiosidades sobre la obra.

Nuestro algoritmo primeramente tratará con los mangas que tengan una mejor media de puntuación de los usuarios, tendrá en cuenta que el género sea el que el usuario está buscando preferiblemente y también tendrá como parámetro la cantidad de usuarios "siguiendo" el manga, es decir, que estén leyéndolo en estos momentos. Esta decisión se justifica debido a que los mangas salen semanalmente por lo general y si no están acabados muchos usuarios podrían no evaluarlos. Con todos estos parámetros hará una ponderación y los 10 que salgan con un mejor resultado serán los que se muestren en la lista de recomendaciones para el usuario.

## Guía de instalación y uso

Para ejecutar More Mangas! tendremos que descargarnos los archivos fuente del repositorio ya sea directamente desde GitHub o habiendo clonado el repositorio.

Una vez tenemos los archivos del repositorio descargados o clonados nos tendremos que situar en la carpeta raíz de la aplicación y abriremos la terminal.

Lo primero será instalar invoke.

```shell
pip install invoke
```

Para más información sobre el funcionamiento y la instalación de Invoke tenemos la [documentación oficial](https://docs.pyinvoke.org/en/stable/).

Necesitaremos instalar poetry, el cual se puede instalar de varias formas igualmente válidas, consulte cómo [aquí](https://python-poetry.org/docs/) 

Para comprobar si tenemos Poetry ya instalado bastará con ver la versión instalada:

```shell
poetry --version
```

Lo siguiente que necesitamos es instalar las dependencias de la aplicación con el comando:

```shell
poetry install
```

Para abrir el entorno virtual de poetry necesitamos escribir en el terminal:

```shell
poetry shell
```

Para ver la lista de tareas definidas usamos:

```shell
invoke --list
```

Para comprobar con los tests que funciona correctamente debemos ejecutar:

```shell
invoke test
```

Pra comprobar la sintaxis de todos los archivos que componen el módulo ejecutamos:

```shell
invoke check
```

Para saber la justificación de elegir invoke, consultar la documentación del objetivo 3.



## Documentación :file_folder:

La documentación al completo se puede consultar desde [aquí](docs/)

