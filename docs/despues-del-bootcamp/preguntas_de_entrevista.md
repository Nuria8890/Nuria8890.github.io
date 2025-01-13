# Preguntas de entrevista

## HTML

**1. ¿Qué es una librería (biblioteca) de código?**

Una librería es por ejemplo Bootstrap, que es un conjunto de recursos que han sido realizados por unos desarrolladores para que otros desarrolladores puedan utilizalos y sea más fácil escribir el código, ya que utilizando librerías nos evitamos escribir un determinado código desde cero, y así podremos programar de manera más eficiente y efectiva.

**2. ¿Qué es accesibilidad web? ¿Por qué es importante? ¿Cómo construyes una web accesible?**

La accesibilidad web se refiere a desarrollar sitios web que sean accesibles para todos, sobretodo para personas con capacidades diferentes, como visuales o auditivas. Es importante construir una web accesible que ofrezca una experiencia inclusiva para todos los usuarios.

Para construir una web accesible, por ejemplo, habría que:

- utilizar media queries para que la web se adapte a diferentes dispositivos y tamaños de pantalla
- utilizar HTML semántico, es decir, utilizar las etiquetas adecuadas para estructurar el contenido de la página de manera lógica, por ejemplo `header`, `nav`, `main`, `article`, `footer`...
- y también estructurarlo de manera jerárquica utilizando `h1`, `h2`...
- utilizar también texto alternativo con etiquetas `alt` para imágenes o cualquier elemento visual
- usar etiquetas `label` en los formularios para que al hacer click en el texto nos lleve directamente al campo en el que tenemos que escribir
- usar colores de texto y fondo adecuados para facilitar la lectura, y una fuente de texto legible

**3. ¿Cómo afrontas un desarrollo front-end que de soporte a distintos tipos de navegadores?**

Para que la web tenga soporte en diferentes tipos de navegadores hay que seguir una serie de buenas prácticas, como por ejemplo:

- utilizar HTML semántico, es decir, utilizar las etiquetas adecuadas para estructurar el contenido de la página de manera lógica, por ejemplo `header`, `nav`, `main`, `article`, `footer`...
- y también estructurarlo de manera jerárquica utilizando `h1`, `h2`...
- utilizar media queries para que la web se adapte a diferentes dispositivos y tamaños de pantalla
- utilizar medidas relativas como `%`, `rem`
- utilizar frameworks y librerías que ya sean compatibles en diferentes navegadores (Bootstrap o jQuery)
- utilizar una hoja de estilos CSS de reset para resetear todos los estilos que traen por defecto los navegadores
- utilizar las DevTools en los diferentes navegadores para depurar y probar el rendimiento de cada estilo

**4. Para qué es útil el posicionamiento (position) de elementos en CSS. Da ejemplos de uso en una web.**

El posicionamiento nos permite controlar cómo se van a colocar los elementos en la página web.

Por ejemplo es útil para colocar un menú de encabezado que queremos que al hacer scroll, se quede fijo y permanezca en la parte superior de la página (position `fixed`).

Otro ejemplo es un tooltip que aparece sobre un botón cuando pasamos el ratón por encima (`:hover`), si usamos `position: absolute`, lo podemos posicionar en relación a ese botón.

**5. Cómo afrontas el desarrollo de una página para un dispositivo que no tiene soporte para flexbox.**

Utilizando:

- CSS Grid
- display inline-block
- un diseño más sencillo para no tener que colocar demasiado los elementos...

**6. ¿Qué es DOCTYPE y para que se usa?**

DOCTYPE es una etiqueta que se coloca al principio de un documento HTML y se usa para inidcar al navegador la versión del lenguaje y el tipo de documento que se está utilizando, para que el navegador sepa cómo renderizar ese contenido.

**7. ¿Cuál es la diferencia entre div, section y article?**

Los tres son elementos HTML que se utilizan para estructurar el contenido de una página web, pero son diferentes entre sí:

- `div`: es un contenedor genérico que no tiene ningún contenido semántico.

- `section`: se utiliza para agrupar contenido que está relacionado o forma parte de un mismo tema.

- `article`: se usa para representar contenido independiente, que tiene sentido por sí mismo.

**8. Lista todas las etiquetas de HTML que conozcas.**

header, main, footer, h1-h6, p, br, hr, strong, em, a, img, video, audio, ul, ol, li, table, form, input, lable, textarea, button, select, div, spam, section, article, aside, link, script...

**9. ¿Por qué es útil una herramienta de automatización de tareas? ¿Has usado alguna? ¿Para qué?**

Una herramienta de automatizacion de tareas es por ejemplo `Vite`, es útil porque ayudan a ser más eficientes, nos ahorran tener que realizar tareas repetitivas y ayudan a reducir los errores, y todo esto permite que el desarrollador esté concentrado en cosas más importantes.

Lo he utilizado para:

- convertir Sass en CSS y que ese código sea legible para el ordenador
- generar un único html (cuando se tiene el código dividido en partials)
- optimizar los ficheros CSS y JavaScript antes de subir la web a producción.

## CSS

**1. ¿Qué es la cascada de CSS y cómo funciona?**

La cascada es la forma en la que se aplican los estilos CSS a los elementos HTML, es decir, el navegador lee el código CSS y va aplicando los estilos de arriba a abajo.

Existen una serie de reglas de combinación de estilos, en función de su **origen** (estilos del navegador, en línea u hojas de estilo), **especificidad** (estilos en línea, selectores de id, de clase, de tipo) y **orden** (se aplica la última regla definida).

**2. ¿Has usado alguna vez un sistema de grid? ¿Prefieres usarlo o no?**

He utilizado CSS Grid, display inline-block y Flexbox.

Prefiero utilizar flexbox o la ibrería de bootstrap.

**3. ¿Conoces algún preprocesador de CSS? ¿Cuáles son las ventajas/inconvenientes de usarlo?**

Conozco **Sass**.

Ventajas:

- permite escribir los estilos de manera más eficiente, organizada y legible
- se pueden anidar los estilos y se pueden utilizar variables
- permite dividir el código en varios archivos e importarlos en un archivo principal

Inconvenientes:

- necesitan de una herramienta de compliación, como por ejemplo node.js, y en proyectos muy grandes puede que el tiempo de carga sea mayor
- a la hora de debuggear, puede ser más dificil de depurar el código, porque el código final no siempre refleja la estructura real del código fuente.

**4. ¿Has usado o implementado alguna vez media queries o realizado layous específicos para móvil?**

Sí, siempre que realizo cualquier maquetación de un proyecto, la hago responsive para que se adapte a todos los dipositivos y diferentes tamaños de pantallas, y siempre utilizo la estrategia mobile first, ya que se priorizan los dispositivos con menor capacidad de pantalla, conexión y batería.

**5. ¿Puedes explicar la diferencia entre desarrollar un sitio web responsive frente a usar una estrategia mobile-first?**

Al utilizar la estrategia mobile first se priorizan los dispositivos con menor capacidad de pantalla, conexión y batería.

Normalmente cuando se desarrolla un sitio web responsive se utiliza esta estrategia, ya que es más sencillo añadir estilos y características que quitarlos.

**6. ¿Qué es y cómo funciona la especificidad de selectores CSS?**

La especificidad es una regla que determina qué estilos de CSS debe aplicar el navegador a los elementos HTML.

El navegador primero lee los estilos en línea, luego los selectores de id, después los de clase, y por último las etiquetas.

**7. Describe qué es z-index y para qué usarlo.**

z-indez es una propiedad de CSS que coloca los elementos en el eje Z, se suele usar junto con la propiedad `position` (relative, absolute, fixed o sticky)

**8. Describe qué son pseudo-elementos y discute para qué puedes usarlos.**
Los pseudo-elementos permiten aplicar estilos a partes específicas de un elemento HTML, por ejemplo:

- para resaltar la primera linea de un párrafo `p::first-line{font-weight:bold}`
- o la primera letra `p::first-letter{font-weight:bold}`
- o cuando un usuario selecciona un texto, resaltarlo de una manera específica `::selection{background-color:yellow}`

**9. Cuál es la diferencia entre una transición y una animación en CSS. Da ejemplos de uso.**

Ambas permiten crear efectos visuales dinámicos en los elementos de una página web, pero

- las transiciones hacen que ese efecto visual ocurra de manera suave y gradual (`transition: background-color 0.3s ease`) cuando sucede un evento, por ejemplo un `:hover`

- las animaciones no necesitan que ocurra ningún evento para que se active ese efecto visual, y se definen mediante `@keyframes` para especificar los estados intermedios de la animación (cuántas veces se repite la animación, a qué velocidad, hacia que eje se mueve, cuánta distancia...)

10. **Qué es un sistema de diseño y por qué es útil.**

Un sistema de diseño son una serie de reglas que se definen para que la interfaz de usuario tenga coherencia.

Por ejemplo, definir:

- la paleta de colores, la tipografía que se va a utilizar, los iconos...
- qué elementos se van a reutilizar (botones, modales, menús...)

Es útil porque:

- facilita el trabajo de los diseñadores y desarrolladores al existir componentes reutilizables
- mejora la comunicación entre ambos equipos
- hace que todos los elementos de la web se vean y se comporten de manera similar, lo que facilita una buena navegación y experiencia al usuario.
- facilita el mantenimiento y actualización de la web, ya que no hay que actualizar cada elemento de forma individual.

## JavaScript

**1. ¿Qué es una librería (biblioteca) de código? ¿Has usado alguna en JS?**

Una librería de código es por ejemplo jQuery, que es un conjunto de recursos que han sido realizados por unos desarrolladores para que otros desarrolladores puedan utilizalos y sea más fácil escribir el código, ya que utilizando librerías nos evitamos escribir un determinado código desde cero, y así podremos programar de manera más eficiente y efectiva.

**2. ¿Qué es un API? ¿Por qué es importante para el desarrollo front-end?**
Una API es una Interfaz de Programación de Aplicaciones, y permite que el navegador pueda comunicarse con el servidor.

Es importante para el desarrollo front-end porque:

- gracias a las APIs, las aplicaciones se comunican con un servidor y es posible obtener, enviar, modificar o eliminar datos que están alojados en una base de datos.

**3. ¿Qué es debugging de aplicaciones? ¿Cómo lo haces?**

El debuggin es la depuración del código, sirve para corregir errores.

Normalmente utilizo console.log, y si no encuentro el error utilizo `debugger` en las DevTools para ir viendo el comportamiento del código.

Si estoy utilizando React, uso una extensión que se llama React DEvTools.

**4. ¿Qué es el DOM y por qué es importante saber manipularlo para un desarrollador front-end?**

El DOM es una representación en forma de árbol de la estructura de un documento HTML, que permite ser modificado por lenguajes de programación como JS, o también a través de las DevTools.

Es importante saber manipularlo porque:

- nos permite interactuar de forma dinámica con la página web a través de eventos como clicks, desplazamientos con el ratón, entradas del teclado...
- podemos modificar el contenido de la página sin necesidad de recargarla
- puede ayudarnos a optimizar el rendimiento de la aplicación minimizando el número de cambios en el DOM, así mejoramos la velocidad.

**5. What is the difference between == and ===?**

**6. What are the differences between variables created using let, var or const?**

**7. What are callbacks? What for and how to use them.**

**8. What is "use strict";? what are the advantages and disadvantages to using it?**

**9. Explain what is localStorage and why is it useful.**

**10. Explain the concept of hoisting**

**11. Can you give an example for destructuring an object or an array?**

**12. Explain the difference between ES6 spread operator and rest operator**

**13. What is an endpoint nad how it is useful?**

**14. ES6 Template Literals offer a lot of flexibility in generating strings, can you give an example?**

**15. Explain what is it HTTP and requests types and response codes.**

**16. Explain Ajax in as much detail as possible.**

**17. What are Promises and why are they useful?**

**18. Explain how this works in JavaScript**

**19. Explain "destructuring" and why is it useful**

**20. Explain the difference between spread operator and rest operator**

**21. What are classes? And instances?**

**22. What is classes inheritance and why is it useful**

**23. What are JS module and how are they useful**

## React

1. Qué son componentes web y por qué son útiles para crear interfaces web

2. Qué son las props de React y para qué sirven

3. ¿Para qué sirve el estado de un componente web de React?

4. ¿Por qué es útil tener distintas rutas en una app de front-end? ¿Cómo lo haces en una SPA React?

5. ¿Cómo puedo pasar información de un componente React a otro que está más arriba en la jerarquía?

6. Qué son los métodos del ciclo de vida de un componente de React y para qué sirven

## GIT

1. ¿Por qué razones puede surgir un conflicto en un sistema de control de versiones? ¿Cómo lo solucionas?

2. ¿Conoces alguna herramienta para el control de versiones? ¿Cuál es el flujo de trabajo para usarla en un equipo?

3. ¿Cuál es la diferencia entre git y GitHub?

4. ¿Qué significan las siglas HTTP?
