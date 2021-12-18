 ### Elección del sistema de integración continua (CI)

Existen un gran número de sistemas de integración continua que podrían servir para el proyecto, entre los candidatos posibles a ser el SCI usado están:

* Travis
* Github Actions
* Circle CI
* Semaphore CI
* Jenkins

Los **requisitos** para un buen sistema de integración continua bajo mi propio juicio son los siguientes:

* Sencillez en la configuración.
* Una fácil configuración para el checks API.
* Esto va por Travis y algún otro sistema más, que no requiere tarjeta de crédito.


Teniendo en cuenta los requisitos mencionados, vamos a realizar un filtro para ver los sistemas que cumplen. Se harán dos elecciones, una para el CI que pasará los tests y otra para el que testeará la aplicación con distintas versiones del lenguaje Python.

1. Por estetica y facilidad de uso **Travis** sería el elegido. Permite ver el resultado de la integración continua en Github (**checks API**) de manera muy sencilla. Sin embargo, por pedir tarjeta de crédito, no será el usado en este proyecto. **Github Actions** tampocó será el indicado ya que fue usado en el objetivo anterior y he decidido buscar otro nuevo.  Entre los candidatos restantes para ser el sistema de CI tenemos a Jenkins, que es el más popular actualmente, sin embargo, no es sólo un sistema de integración continua sino que además es un sistema de entrega/implementación continua, por lo que se ha descartado como opción. Por último, tenemos a **Semaphore CI** y **CircleCI**, de estos dos Circle es el más aceptado por la comunidad según estuve viendo, en cuanto a la popularidad de uso el resultado es el mismo, en rankings como el de [slant](https://www.slant.co/topics/799/~best-continuous-integration-tools) y [cprimestudios](https://cprimestudios.com/blog/top-cicd-tools-2021-most-complete-guide-33-best-picks-devops) CircleCI se encuentra en la 3ª posición y SemaphoreCI en la 16ª y en el que CircleCI está en la 5ª posición y SemaphoreCI en la 10ª, respectivamente, así que la diferencia es notable.

Tras esta comparación, he decidido usar como primer sistema de integración continua **CircleCI** ya que es sencillo de usar, no pide tarjeta de crédito, permite registro con la cuenta de GitHub, es fácilmente configurable, permitiendo incluir [checks API](https://circleci.com/docs/2.0/enable-checks/), de forma que se puedan ver los resultados de la integración continua en Github. Permite crear y editar el archivo de configuración de la integración continua, llamado **config.yml** desde su propia interfaz web, corrigiendo errores sintácticos y permitiendo hacer commits del archivo directamente a la rama del objetivo en la que nos encontremos.

2. Cegundo sistema de CI se usará Github Actions de Github, entre otras cosas porque al buscar un poco de información sobre el uso de la matriz de compilaciones **matrix** se presenta como una configuración sencilla, pudiendo encontrar una documentación clara y concisa (dentro de lo que cabe) respecto al tema de matrices en este [enlace](https://docs.github.com/es/actions/learn-github-actions/workflow-syntax-for-github-actions#jobsjob_idstrategymatrix). 

Al ser de GitHub, el sistema tiene como ventaja que no necesita de conifiguración adicional para ver el resultado de los workflows.

 ### Configuración del sistema de integración continua (CI)


#### Ejecutar tests automáticamente

Un sistema de integración continua tiene como objetivo principal asegurarse de que el código pasa todos los tests  antes de ser desplegado o como en este caso, antes de incorporarlo a la rama princiap. Así que, configuraremos nuestro repo para que los test se ejeuten automáticamente.


Para que el que el CircleCI funcione es necesario un archivo **config.yml** que es el archivo de configuración base, se tiene que ubicar en el directorio **.circleci**. A continuación se explica el contenido del archivo:


* **version: 2.1**: La versión de CircleCI incluida por defecto por el generador automático de configuraciones de CircleCI.

* Se define el trabajo que pasa los tests
**ejecutar-tests**
    * **executor**: Define la tecnología o el entorno subyacente en el que ejecutar un trabajo. Existen cuatro tipos: ***docker, machine, macos o windows***.
    Dado que tenemos ya un contenedor Docker con una imagen Alpine que es muy ligera y los módulos minimos necesarios para ejecutar el proyecto usaremos una **machine** así además nuestro entorno de ejecución (donde se ejecute la tarea) tendrá acceso completo al proceso de Docker.

        * **image: ubuntu-2004:202111-01**: La imagen de la máquina elegida para ejecutar Docker no es especialmente importante en este caso, ya que únicamente ejecutaría el contenedor
        que ya tenemos para pasar los tests. En este caso se ha elegido la imagen que [recomienda](https://circleci.com/docs/2.0/executor-intro/) el propio CircleCI.

    * **Steps**:
        * checkout: comprueba el código fuente del repositorio, para más información, consultar [la documentación oficial de CircleCI](https://circleci.com/docs/2.0/configuration-reference/#checkout).

        * command: docker run -t -v `pwd`:/app/test gomares/more-mangas: ejecuta los tests. 

* Finalmente, se indica el trabajo que se quiere ejcutar, en este caso, el único que tenemos: **ejecutar-tests**.

CircleCI por defecto pasará los tests automáticamente cada vez que se haga push o pull request al repositorio.

#### Versiones del lenguaje permitidas

 Es necesario decidir en qué funciones desarrollaremos nuestra aplicación, ya que no con todas las versiones serán compatibles fragmentos de código o algunos operadores. Comprobando las [dependencias requeridas](https://github.com/gomares/more-mangas/blob/Objetivo-6/pyproject.toml) por el proyecto y las [necesidades futuras](https://github.com/gomares/more-mangas/blob/Objetivo-6/docs/objetivo-5.md), podemos afirmar que las versiones soportadas serían las iguales o superiores a la versión 3.8 de python, al menos por el momento. Con esto en cuenta se testeará la aplicación desde la versión 3.8 hasta la 3.10, todas las que pertenecen a la matrix.

 Una breve explicación de algunos términos presentes en el fichero **"versions.yml"** es la siguiente:

* **strategy**: Indica que se creará una compilation matrix.
    * **matrix**: declaración de la compilation matrix, se ejecutará el job por cada elemento que contenga esta matriz en **python-versions**.

* Usamos una acción de GH Action llamada **"setup-python"** para establecer la versión de python que usará en cada iteración (3.8, 3.9 o 3.10).

* Se testea la aplicación.
