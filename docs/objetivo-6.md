## Elección de servicio de Integración Continua

Se necesitan dos servicios de integración continua para cumplir el hito. Se han valorado ciertos CIs:

* En primer lugar tenemos a **TravisCI**, recomendado por el profesor por ser muy intuitivo y con una interfaz buena para implementar la integración continua a los proyectos fácil y rápido. Intenté probar a usar la versión trial pero además de solo durar un mes me pedía tarjeta de crédito y no se por qué pero al ponerla me aparecía un mensaje de la app del banco diciendo que habían denegado un pago de un euro. Descarté la opción instantáneamente porque no tenía sentido pagar si quería seguir con el proyecto en un futuro aun habiendo acabado la asignatura.

* En segundo lugar descarté **SempahoreCI** por la misma razón que Travis, exigen que pagues pasados [14 días](https://semaphoreci.com/pricing). Además de esto no tiene una comunidad tan grande como otras opciones de pago y que me gustan más como el propio Travis. Es muy parecido a CircleCI , hasta el punto de no encontrar ninguna diferencia importante más allá de las diferencias en los ficheros de configuración.

* Las dos últimas opciones que investigué eran por un lado **Jenkins** y por otro **CircleCI**. Jenkins presentaba unos [problemas](https://circleci.com/migrate-jenkins-to-circleci/) que CircleCI no, es cierto que es más completo por tener otras funcionalidades que conseguimos añadiendo plugins (tiene más de 1200 plugins). No elegí Jenkins debido a que a la hora de mantener el producto es mucho más complicado, no hay soporte para flujos de tabajo de Docker así que si usasemos Jenkins el usuario tendría que instalar mediante plugins estas cosas para que estuvieran disponibles para el entorno, la sintaxis se puede simplificar mucho usando CircleCI (se pueden encontrar páginas con ejemplos de ficheros en las dos plataformas y la sintaxis de CircleCI expresa más en menos). Jenkins puede ejecutar varios jobs a la vez usando multi-threading pero causa problemas relacionados con condiciones de carrera en la base de datos que pueden ser difíciles de depurar, con CircleCI tenemos de facto un servicio que soporta el paralelismo y lo he comprobado yo mismo que ejecuta los tests en las diferentes versiones de Python a la vez. En definitiva, Jenkins a pesar de no ser mal sistema requiere de unos conocimientos más avanzados de este tipo de sistemas ya que hay que saber que plugins añadir y hay que hacer el mantenimiento manualmente y con una sintaxis algo más compleja que la de CircleCI que preseta una curva de aprendizaje mucho menor que la de Jenkins. Por último comentar que la página de CircleCI me parece de las más completas y estéticas, permite [editar tu archivo config.yml](imgs/interfaz-circleci)] y saber sin tener que ejecutar nada si la sintaxis es correcta o no. Hay documentación sobre [trabajos que hacen uso de matriz de versiones](https://circleci.com/blog/circleci-matrix-jobs/), que aunque no ha sido necesaria usarla más que en el workflow de GH Action pero podría requerirlo en algún futuro.


## Estructura del objetivo:

Elegí CircleCI y GH Actions para la realización del objetivo. Por tanto, se han configurado dos tareas relativas a la Integración Continua:

- Ejecución de tests en nuestro contenedor personalizado del objetivo 5: Esto lo hice con GH Actions, se busca localmente el contenedor si no hace un pull al repo y ejecuta en el contenedor los test.


- Ejecución de tests en varias versiones Python con CircleCI: La programé con una imagen estándar de CircleCI y una matriz de versiones. Se ejecutan paralelamente las 3 versiones en busca de fallos en los tests.


### Anexo: Problemas con cimg/python

A la hora de construir la imagen en config.yml CircleCI ofrece imágenes predeterminadas por si queremos usarlas. Existe la ruta circleci/ y la ruta cimg/ , las dos son válidas pero se recomienda usar cimg que es la más reciente que sacaron sin embargo me da un problema con invoke que intenté solucionar pero no pude, busqué información pero no aparece nada, en la consola depurando instalaba todo como [la imagen de circleci](imgs/cicrcleci-image.png) pero aparecía el [problema](imgs/cimg-image.png). Ante esta situación dejé finalmente la imagen de la ruta circleci.

### Justificación sobre las versiones usadas en la matriz:

A la hora de elegir las versiones de Python que usaremos para testear es necesario justificar cuáles tendremos en la matriz. En esta matriz se hallan las versiones 3.7,3.8 y 3.9. La razón de por qué solo tengo estas es debido a que mi ordenador tiene instalada la versión 3.7 luego la desarrollé al principio en esa versión, además de que tan solo estas versiones son las que todavía tienen [mantenimiento](https://endoflife.date/python) (la version 3.6 fue abandonada el 23 de Diciembre de 2021). He instalado el intérprete de Python en la versión 3.10 en mi ordenador ya para ir utilizando la última versión con todo lo nuevo que ofrece ya que si fuera útil para el proyecto no dudaré en dejar que solo funcione para la última versión. Quiero hacer un producto con sintaxis actual y no de hace 5 años. Las ventajas de Python 3.10 las comento en un [anexo del objetivo 5](objetivo-5.md) y quizás me son útiles para diseño de apis y sobre todo una mejor depuración gracias a los nuevos mensajes de errores de esta versión.

La versión 3.10 no aparece en la matriz ya que corro los tests una vez en el contenedor de pruebas que hice en el objetivo 5 con esa versión. Para ejectuar los tests hice un [workflow](../.github/workflows/run_tests_in_test_container.yml) de GH Actions.
