# Documentación hito 3

## Elección del gestor de tareas:

Las opciones que en un principio me convencieron fueron Pypyr, Doit e Invoke


El proyecto usará Invoke como task runner ya que no solo es simple pero a la vez completo (Pypyr también lo es sin embargo Doit presenta menos funcionalidades) sino que también de las tres opciones es el que más Watchers tiene detrás del proyecto, el que más estrellas y PRs tiene, investigando he visto que es un software muy aceptado por la comunidad y con bastantes años de vida.


## Elección del gestor de dependencias:

A la hora de elegir un gestor de dependencias había varias alternativas como Conda, Poetry, pipenv o hatch.

He elegido Poetry porque su página de documentación no podría estar más completa, su sintaxis es increíblemente sencilla más que pipenv y que hatch. Hatch tiene incluso más aspectos reflejados en el flujo de trabajo del project management (como incrementar versiones, etiquetado de lanzamientos y creación de nuevos "skeleton projects" a partir de plantillas de proyecto) pero con sintaxis más compleja y para está aplicación no necesitaremos tantas funcionalidades.

## Elección de comprobador de sintaxis:

Al principio vi que mucha gente mencionaba Pylint pero investigando me dí cuenta de que este no era un comprobador de sintaxis como tal sino un linter (también leí los errores de la semana-8 de la asignatura) así que se ha optado po Pyflakes que es muy sencillo de usar y tan solo chequea la sintaxis del directorio o del fichero .py de forma pasiva.