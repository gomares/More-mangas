# Documentación hito 4

## Requisitos para la elección del gestor de tests:

* Tiempo en el mercado.
* Frecuencia de actualizaciones.
* Sintaxis y funcionalidades.
* Documentación.
* Popularidad.


## Elección del gestor de tests: pytest

Las posibles opciones eran Robot, PyTest y DocTest. 

Robot lleva en el mercado desde 2005 que tuvo su primera release, es muy popular y tiene muy buena documentación. Sin embargo, muchas de sus funcionalidades no van a ser usadas para la aplicación y la instalación no es sencilla ya que aunque se puede usar pip requiere tener instaladas otras librerías como Jython y IronPython, además su sintaxis es más compleja que la de los otros candidatos.

DocTest salió por primera vez en 2016 con su versión 1.0.0, es muy popular, su documentación aunque para mi gusto no es tan buena como la de Robot o la de PyTest. No se actualiza tanto como los otros candidatos por lo que he visto, su versión actual es la 3.10.0 y llevan año sin sacar nada.

PyTest salió en 2008 por lo tanto lleva más de diez años en el mercado, a diferencia de Robot no requiere instalar ningún módulo adicional, es una herramienta muy conocida y fácil de usar incluso para personas sin conocimientos avanzados de Python, rápido generando informes y ofrece pruebas simples y no tan complejas como DocTest o Robot Framework pero que nos bastan para la aplicación. Su versión última es la 6.2.5 que salió a finales de agosto de este año y ya hay una pre-release de la version 7.0.0 así que la frecuencia de las updates es bastante alta.


El software elegido para realizar los tests, será la librería PyTest. Tiene una sintaxis muy sencilla y se invoca facilmente también, presenta buena documentación por lo que he estado viendo y es muy popular entre desarrolladores de Python, este es un aspecto a tener en cuenta ya que si tenemos dudas que necesitasemos resolver es la comunidad quien nos ayudará.

## Requisitos para la elección de la biblioteca de aserciones:

* Tiempo en el mercado.
* Frecuencia de actualizaciones.
* Tipos de aserciones posibles y sintaxis.
* Documentación.
* Popularidad.


## Elección de la biblioteca de aserciones:

Grappa lleva solamente tres años de vida y en novimebre entraron en la versión 1.0.1, es la menos popular de las opciones y no tiene muchas actualizaciones así que decidí descartarla instantáneamente.

Algo parecido sucede con Verify y es que a pesar de llevar desde el 2015 solo van por la version 1.1.1 y esa actualización es de 2017. El pryecto parece muerto. Encima la sintaxis era distinta de las expresiones regulares usadas en Python complicando más su uso.

UnitTest tenía el problema de que no podían crearse tests en funciones fuera de las clases y tampoco me gusta el kit de funciones que tiene, por ejemplo, con AssertEqual teníamos los dos obejtos a comparar y no hacía falta poner el "==" pero sinceramente a la hora de leer código veo antes el símbolo que tener que leer una función mil veces para saber si era AssertTrue, AssertFalse, etc.

Elegí Assertpy porque lleva un tiempo considerable en el mercado (desde 2015), es la recomendada por PyTest, se actualiza con frecuencia y además tiene sintaxis que me gusta más que la de UnitTest y permite crear funciones fuera de la clase. Lo cual ofrece más flexibilidad para probar código en otras partes.

Las aserciones nos servirán para nuestros tests, nosotros usaremos Assertpy. Esta [biblioteca](https://github.com/assertpy/assertpy) es la recomendada por Pytest. Permite importar funciones para comprobar lo que necesitamos para pasar los tests.