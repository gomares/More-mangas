# Documentación hito 3

## Elección del gestor de tareas:

Las dos opciones principales eran Invoke y Poetry.

El proyecto usará Invoke como task manager debido a su completitud y simplicidad. Aunque Poetry es incluso más simple, tiene la pega de que su enfoque está dirigido más a la gestión de dependencias y no tanto a la de tareas. Invoke es más adecuado por tanto para lanzar tests. Sigue siendo intuitivo su uso y ofrece la posibilidad de ver las tareas a ejecutar al abrir el fichero.

Por todo lo mencionado anteriormente, se ha elegido Invoke pues me parece que se adecua mejor como gestor de tareas.


## Elección del gestor de dependencias:

Como gestor de dependencias se eligió Poetry ya que es más sencillo de usar que Invoke y está orientado a gestionar dependecias.

Su sintaxis y uso son sencillos, además cuenta con una buena documentación en su página oficial.

## Elección de comprobador de sintaxis:

Al principio vi que mucha gente mencionaba Pylint pero investigando me dí cuenta de que este no era un comprobador de sintaxis como tal sino un linter (también leí los errores de la semana-8 de la asignatura) así que se ha optado po Pyflakes que es muy sencillo de usar y tan solo chequea la sintaxis del directorio o del fichero .py de forma pasiva.