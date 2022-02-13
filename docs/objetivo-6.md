
# Elección de servicios de Integración Continua

Se necesitan dos servicios de integración continua para cumplir el hito. Para valorar los posibles candidatos primero vamos a establecer una serie de requisitos para realizar un primer filtro, estos requisitos son los siguientes:

## Requisitos:

- Debe tener una integración fácil o al menos la posibilidad de integrarse con GitHub ya que aquí es donde estamos desarrollando nuestro proyecto.
- La plataforma debe ser alojada por un tercero (cloud-based) ya que no tenemos la infraestructura necesaria para el hosteo.
- Buscamos un CI que no requiera de plugins ni instalaciones por tanto.
- Curva de aprendizaje no muy alta debido al limitado tiempo que tenemos para poner en práctica lo investigado/aprendido.
- Debido al tiempo, necesitamos un CI con una buena documentación y si es posible un buen soporte para responder a las dudas que pudiéramos tener.
- Que tenga al menos una versión de prueba gratuita.
- Que tenga una disponibilidad alta. El software estará en la nube y por esto mismo no podemos estar con problemas continuamente.

Basándonos en estos criterios hemos descartado directamente CircleCI y Jenkins. Este último por usar [plugins](https://plugins.jenkins.io/) y no tener una versión del software hospedado en la nube (se tiene que instalar en el ordenador de uno) y CircleCI porque aunque es gratuito, toda la clase lo ha usado dejando de ser original y de nuestros criterios podemos decir que tiene algunos [problemas de disponibilidad](imgs/status-circleci.png) frecuentemente. GithHub Actions tampoco lo voy a tener en cuenta porque, aunque es del propio GitHub, la mayoría de estudiantes lo usaron junto a CircleCI.


##Análisis de los candidatos

Se han valorado ciertos CIs, todos los candidatos tendrán una breve descripción, un análisis y por último, una conclusión.

### TravisCI

#### Descripción

Travis CI es un servicio de integración continua alojado que se utiliza para crear y probar proyectos de software alojados en GitHub y Bitbucket.

Fue (según wikipedia) el primer servicio de CI que brindó servicios a proyectos de código abierto de forma gratuita. Tiene una versión de prueba de 30 días y dos versiones de pago (Core y Enterprise). La versión Enterprise proporciona implementaciones personalizadas de una versión propietaria en el propio hardware del cliente aunque no nos van a hacer ninguna falta.


#### Análisis

- Ofrece integración con GitHub por medio de OAuthApp, para saber más sobre la configuración consultar [aquí](https://docs.travis-ci.com/user/tutorial/).
- La prueba gratuita y la versión Core no necesitan hostearse en nuestro hardware. Tenemos 10.000 créditos con la versión de prueba que al cambio son más de 1000 minutos de ejecución.
- No requiere plugins adicionales ni instalaciones.
- Por lo que he visto en su [documentación](https://docs.travis-ci.com/user/docker/) el uso de Dockers y también los [test en diferentes versiones](https://docs.travis-ci.com/user/multi-os/) es bastante fácil y explícito.
- La documentación tiene muchos ejemplos y tienen soporte con un foro para ayudarse entre usuarios del software.
- Tiene una versión de prueba de 30 días aunque te requisan un euro para probarla (espero que me lo devuelvan intacto).
- La [disponibilidad](https://www.traviscistatus.com/) en los últimos 90 días es del 100%. Esto ya es mejor que con CircleCI.


#### Conclusión

Tiene la nota máxima ya que cumple con todo. Un software que aunque es de pago pasado el mes, merece la pena probar.

### SemaphoreCI

#### Descripción

Es una herramienta de integración continua que cuenta con versión gratuita pero en el apartado de [los precios](https://semaphoreci.com/pricing) no son tan transparentes como en otras páginas. Me gusta su eslogan "For every $1 invested in Semaphore, engineers gain $41 in reclaimed productivity".

#### Análisis

- Integración con Github y BitBucket.
- Tiene una versión en la nube y otra para que las empresas hosteen sus propios servidores para que hagan pruebas pero es necesario contactar con Semaphore y no se puede pagar de primeras.
- No requiere instalaciones ni tiene plugins la versión de prueba. 
- Muy parecido a CircleCI así que no habría mucho problema en cambiarse de uno a otro si se tiene experiencia previa. 
- Cuenta con una [documentación](https://docs.semaphoreci.com/) que a mi personalmente no me parece estética ni se resaltan los apartados importantes (todo en letra muy pequeña y no de un color llamativo). Cuenta con un apartado de preguntas y respuestas frecuentes aunque no muy elaborado.
- Versión de prueba de solo 14 días, ofrecen 13.000 créditos que son 1.300 minutos, es equivalente 10$.
- Tiene una disponibilidad alta pese a no ser al [100%](https://status.semaphoreci.com/).

#### Conclusión

Tiene la nota máxima porque cumple con los requisitos que hemos establecido. Sin embargo, no me ha gustado ni la documentación ni el hecho de que la versión de prueba no sea de un mes ni siquiera. Su disponibilidad tampoco es la mejor de los candidatos de la lista.

### Buddy

#### Descripción

Buddy es un software CI/CD basado en web para desarrolladores de Git que se puede usar para crear, probar e implementar sitios web y aplicaciones con código de GitHub, Bitbucket y GitLab. Emplea contenedores Docker con lenguajes y marcos preinstalados para compilaciones. Lo descubrí por un anuncio de Google pero es muy popular en Estados Unidos y nada más meterme entendí el por qué.

#### Análisis

- Tiene integración con GitHub y más.
- Tiene una versión web y hosteada en la nube.
- No requiere nada, es MUY fácil empezar a construir tus primeros pipelines que vienen a ser los trabajos que queremos realizar automáticamente.
- Como ya dije antes, es extremadamente fácil crear [pipelines](imgs/pipeline-crecion-buddy.png) ya que se va generando automáticamente pero tiene un pero muy grande. Las configuraciones más interesantes y avanzadas requieren conocerse muy bien [los apartados de configuración](imgs/configuracion-buddy.png) y para esto sí que falta documetnación bajo mi punto d evista, tanto que tuve que pedir ayuda al soporte.
- La documentación solo sirve para ejemplos muy básicos. El soporte técnico debo decir que es muy rápido, cuando les pedí ayuda me respondieron [en menos de un día](imgs/chat-buddy.png) aunque seguí con alguna que otra duda sin resolver.
- Es gratis.
- Según su [página oficial](https://status.buddy.works/) no ha sufrido problemas en los últimos 7 días, me parece muy poco la ventana de tiempo que ponen aquí, que menos que reportar el estado del último mes.

#### Conclusión

Este software tras haberlo probado es cierto que es muy sencillo de usar y en 15 minutos tienes generadas unos ficheros que contienen las instrucciones que uno pone por la web pero precisamente por esto no me gusta, para configuraciones avanzadas puede llegar a ser muy largo y complicado el fichero generado y además requiere aprender mucho sobre las opciones que ofrece la interfaz web. La documentación en casos avanzados no sirve de nada. Otro problema fue el hecho de que cuando ejecutaba un pipeline diera fallo o fuera un éxito no aparecía en el PR como con CircleCI así que no lo voy a usar.

### AppVeyor

#### Descripción

AppVeyor es otra herramienta que ofrece CI/CD. Fue creada en 2011 por una empresa privada canadiense y tienen como [clientes](https://www.appveyor.com/) a empresas tan conocidas como Netflix, Google, Microsoft, Slack o el propio GitHub.

#### Análisis

- Cuenta con la típica integración con GitHub, te registras con tu cuenta y mediante OAuth App le das ciertos permisos sobre los repositorios públicos que quieras.
- En la versión gratuita llamada "Open-source" no hace falta hosteo por parte del usuario.
- Tiene una versión para instalar en tu propio hardware pero no nos hará falta para el proyecto y existe la que queremos, la cloud-based.
- Es otro CI que funciona a través de un .yml y por lo que veo en los ejemplos no es complicado encomparación con, por ejemplo, los ficheros que genera automáticamente Buddy y no sabes ni qué hacen (hay muchas cosas implícitas en las configuraciones que se hacen en la web, sobre todo para un inexperto).
- La [documentación](https://www.appveyor.com/docs/) de este me ha sorprendido, no es la más bonita pero contiene todo tipo de ejemplos incluyendo otros servicios como FTP,SFTP,SSDT y Amazon S3. Estos dos últimos no los había visto en los CI anteriores.
- Presenta una versión totalmente gratuita con la que puedes gestionar un número ilimitado de proyectos públicos y la única limitación esta en que solo puedes tener un trabajo a la vez.
- En los últimos 7 días no ha habido incidencias ni problemas reportados según este [boletín](https://status.appveyor.com/). Parece estable por lo que he leído en páginas extra oficiales.

#### Conclusión

Le he dado la puntuación máxima porque no solo cumple los requisitos sino que además lo hace con méritos como el de tener 100% de disponibilidad, la documentación más completa que he visto junto con Travis e incluso más variada , una versión gratuita sin prácticamente limitaciones (no hay créditos) y se puede entender lo básico en cuestión de minutos.

### GitLab

#### Descripción

GitLab es una suite que permite gestionar, administrar, crear y conectar los repositorios con diferentes aplicaciones y hacer todo tipo de integraciones con ellas. Es una plataforma en la cual se pueden realizar distintas etapas del desarrollo del producto. Nosotros nos centraremos en la aplicación de CI/CD que ofrece.

#### Análisis

- GitLab presenta integración con sus propios repositorios pero también con GitHub y existen facilidades para migrar un repo desde GH a GitLab.
- GitLab ofrece versión del software CI/CD sin requerir hardware nuestro.
- No tiene instalación ninguna.
- En mi opinión no cumple con este requisito porque aunque tiene mucha documentación e incluso vídeos, GitLab ofrece muchas posibilidades pero es que además no es de la ssintaxis más fáciles que he estado viendo. 
- Buena [documentación](https://docs.gitlab.com/ee/ci/) que incluye hasta vídeos.
- Versión gratuita de 30 días.
- Tienen una página de monitorización de incidentes en tiempo real oficial y un [Twitter](https://twitter.com/gitlabstatus) para notificar de problemas, al ser una plataforma usada por +100.000 empresas debe de estar habiendo problemas porque revisando el Twitter encuentro que cada semana o dos algún servicio se viene abajo. No me inspira confianza en este sentido.

#### Conclusión

Es una plataforma super popular pero por el tema de problemas con los servicios que han tenido recientemente y la curva de aprendizaje que tiene pienso que hay mejores opciones si uno está dispuesto a pagar y si no vamos a utilizar todas las otras aplicaciones que ofrece GitLab renta más otro software. Otro punto muy negativo es el tiempo que tarda en testear, los cambios pueden tardar hasta 180s en reflejarse según ponía la página.

### Conclusión final

Tras experimentar con los candidatos CI puedo decir que los que más me han gustado para dejarlos como sistemas finales han sido TravisCI y AppVeyor. Travis simplemente me ha encantado y no puedo ponerle pegas importantes más que es de pago y el euro que te retienen en la versión gratuita, se puede decir mucho en muy pocas líneas de código y tiene de las mejores documentaciones de nuestros candidatos. AppVeyor a pesar de no ser tan famosa como otros me parece que su versión gratuita "Open Source" es de las mejores ya que apenas tiene limitaciones, no hay créditos, una documentación bastante decente y en los ficheros veremos una sintaxis parecida a la de CircleCI. 

También he de decir que al intentar otros candidatos como Buddy acabé muy cansado de ciertas dificultades que me encontré en el camino pero todos los problemas los explicaré en el apartado de problemas que tengo mñas abajo.

## Justificación sobre las versiones testeadas:

A la hora de elegir las versiones de Python que usaremos para testear es necesario justificar cuáles tendremos en la matriz. En esta matriz se hallan las versiones 3.7,3.8 y 3.9. La razón de por qué solo tengo estas es debido a que mi proyecto se comenzó a desarrollar con el intérprete de Python de la versión 3.7  y aunque podría funcionar en la versión 3.6 no he querido incluir versiones antiguas que no tienen [mantenimiento](https://endoflife.date/python) (la version 3.6 fue abandonada el 23 de Diciembre de 2021). He instalado el intérprete de Python en la versión 3.10 en mi ordenador ya para ir utilizando la última versión con todo lo nuevo que ofrece ya que si fuera útil para el proyecto no dudaré en dejar que solo funcione para la última versión. Quiero hacer un producto con sintaxis actual y no de hace 5 años. Las ventajas de Python 3.10 las comento en un [anexo del objetivo 5](objetivo-5.md) y quizás me son útiles para diseño de apis y sobre todo una mejor depuración gracias a los nuevos mensajes de errores de esta versión.

La versión 3.10 no aparece en la matriz ya que corro los tests una vez en el contenedor de pruebas que hice en el objetivo 5 con esa versión. Para ejectuar los tests hice un [workflow](../.github/workflows/run_tests_in_test_container.yml) de GH Actions.

## Estructura del objetivo:

Elegí TravisCI y AppVeyor para la realización del objetivo. Por tanto, se han configurado dos tareas relativas a la Integración Continua:

- Ejecución de tests en nuestro contenedor personalizado del objetivo 5: Esto lo hice con AppVeyor, se busca localmente el contenedor si no hace un pull al repo y ejecuta en el contenedor los test. La interfaz de AppVeyor nos dará [este output](imgs/output-exito-appveyor.png) a la build realizada(así lo llaman).


- Ejecución de tests en varias versiones Python con Travis CI: La programé con TravisCI. Se ejecutan las 3 versiones en busca de fallos en los tests. Este es el [resultado](imgs/output-exito-travis.png) ¿He mencionado ya que me gusta mucho su interfaz y todo salió a la primera?



## Problemas 

#### Problemas con Buddy

Con Buddy empecé creando un [pipeline](pipelines-buddy.png) de ejecutar el contenedor Docker con sus tests pero a la hora de ejecutarlo me dió un [error](imgs/output-fallo-buddy.png). Contacté entonces con el soporte quien dió una respuesta muy rápida, desgraciadamente he perdido la conversación porque se borró del chat de la web que es temporal al parecer. La respuesta que me dieron era que tenía que tocar en el apartado del [caché](imgs/cache-buddy.png) algunos parámetros, sinceramente me pareció un rollazo muy grande y lo dejé porque ese mismo día descubrí que los fichero generados eran muy largos y no sentía que aprendía cómo funcionaba Buddy, una pena. En Go por lo que he estado viendo funciona a las mil maravillas siguiendo un tutorial que hay en la página.

#### Problemas con SemaphoreCI

El primer problema que tuve con SemaphoreCI se dió antes de lo que pensaba. En el registro no entiendo por qué me dió un [error](imgs/semaphore-error-registro.png), ante el error escribí un correo a abuseprevention@semaphoreci.com y tuve que esperar unos días a la respuesta (así que el soporte no me ha convencido, al menos para este tipo de incidencias). A pesar de todo, programé un fichero yml gracias al [tutorial](https://docs.semaphoreci.com/ci-cd-environment/working-with-docker/) que encontré en su documentción aunque no lo vaya a usar como sistema CI final.


#### Problemas con AppVeyor

A la hora de hacer el script en AppVeyor tuve que aprender que este primero realiza una build del proyecto y para eso usa MSBuild, propio de Windows. En nuestro proyecto noera necesario usar esto ya que solo queríamos ejecutar unos tests de un contenedor público, así que deshabilite la opción de builds para que no me diera [error](imgs/output-fallo-appveyor.png) y deje directamente el script que hacía los tests. Por lo demás todo fue bien y se actualizó muy rapido

#### Problemas con cimg/python probando CircleCI

A la hora de construir la imagen en config.yml CircleCI ofrece imágenes predeterminadas por si queremos usarlas. Existe la ruta circleci/ y la ruta cimg/ , las dos son válidas pero se recomienda usar cimg que es la más reciente que sacaron sin embargo me da un problema con invoke que intenté solucionar pero no pude, busqué información pero no aparece nada, en la consola depurando instalaba todo como [la imagen de circleci](imgs/cicrcleci-image.png) pero aparecía el [problema](imgs/cimg-image.png). Ante esta situación dejé finalmente la imagen de la ruta circleci.ienso que hay mejores opciones si uno está dispuesto a pagar y si no vamos a utilizar todas las otras aplicaciones que ofrece GitLab renta más otro software.
