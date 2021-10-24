# Proyecto_IV

## Idea General :bulb:

El sector del manga y los webtoons continúa creciendo y llevando sus obras literarias al resto del mundo. Cientos de novelas están siendo transformadas en obras ilustradas por mangakas. Nuestra aplicación contribuirá a que las personas nuevas en ese mundo reciban una buena dosis de entretenimiento y para que las más experimentadas, que no saben que más pueden ver, encuentre joyas ocultas que quizás no sean tan populares.

## Descripción :clipboard:

Se trata de una aplicación para amantes del manga o de los webtoons y para lectores no tan experimentados pero que están interesados en saber más del mundillo. Con esta app podrán recibir las mejores recomendaciones gracias a nuestro algoritmo, el cual se apoyará en un análisis previo de los gustos del usuario y además les ofrecerá información de interés como pueden ser los sitios dónde leer el manga con la mejor calidad y algunas curiosidades sobre la obra.

Para poder explicar cómo funciona el algoritmo primero tenemos que describir dos estructuras:
* La estructura A: Será nuestro vector de perfil, este vector tendrá toda la información relacionada con el comportamiento del usuario, es decir, los mangas que le gustan y los que no le gustan y las calificaciones dadas por ellos.

* La estructura B: Se trata del vector de elemento contiene los detalles de cada manga, como el género, el autor, los capítulos, los volúmenes, etc.

Este algoritmo encuentra el coseno del ángulo entre el vector de perfil y diferentes vectores elementos, es decir, la similitud de coseno. Supongamos A y B siendo vector de perfil y un vector de elemento, la similitud entre estos se puede calcular como:

![Fórmula de similitud escrita en LaTeX](/docs/imgs/similitud.png)

## Documentación :file_folder:

La documentación al completo se puede consultar desde [aquí](docs/)

