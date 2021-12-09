# Documentación hito 4

## Elección del gestor de tests: pytest

Las posibles opciones eran Robot(el más popular), PyTest, UnitTest y DocTest. Robot a pesar de ser muy completo tenía demasiadas funcionalidades que no se le darán uso en este proyecto y DocTest presenta una sintaxis muy fea que no me acaba de convencer. Entre UnitTest y PyTest elegí PyTest debido a que tiene una mayor popularidad y está muy depurado.

El software elegido para realizar los tests, será la librería PyTest. Tiene una sintaxis muy sencilla (no como DocTest por ejemplo) y se invoca de manera sencilla también, presenta buena documentación por lo que he estado viendo y es muy popular entre desarrolladores de Python, este es un aspecto a tener en cuenta ya que si tenemos dudas que necesitasemos resolver es la comunidad quien nos ayudará.

## Elección de la biblioteca de aserciones:

Las posibles opciones eran Grappa, Asssertpy y Verify. Verify decidí descartarlo puesto que la última actualización era de 2017 y no parecía haber demasiado trabajo en el proyecto por parte de los propios desarrolladores. Grappa presentaba dos grandes inconvenientes: Era demasiado verboso para mi gusto y la sintaxis era distinta de las expresiones regulares usadas en Python. Por tanto, el elegido no es otro que Assertpy

Las aserciones nos servirán para nuestros tests, nosotros usaremos Assertpy. Esta [biblioteca](https://github.com/assertpy/assertpy) es la recomendada por Pytest. Permite importar funciones para comprobar lo que necesitamos para pasar los tests.