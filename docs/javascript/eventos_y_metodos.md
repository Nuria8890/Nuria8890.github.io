# Eventos

Nuestra web es interactiva de verdad cuando escuchamos eventos y reaccionamos a ellos `addEventListener()`.

Para utilizar la información que el navegador nos devuelve sobre los eventos:
- `event.currentTarget`: contiene el elemento sobre el que pusimos el addEventListener. Es decir, al que asociamos el evento. Es muy útil cuando queremos que se ejecute el mismo código para varios elementos.

- `event.target`: elemento sobre el que sucede el evento.

- `event.preventDefault()`: método para prevenir el comportamiento por defecto de un evento sobre un elemento.

- `event bubbling` para que los eventos pasen de unos elementos a otros de manera ascendente.

- `event delegation` parar poner listeners a elementos padres para controlar eventos en hijos.

- `classList.toggle` para quitar o añadir una clase de CSS.

- `inputNameElement.value` nos devuelve el valor de un input.

## Eventos de ratón
- `click`: botón izquierdo del ratón
- `mouseover`: pasar el ratón sobre un elemento
- `mouseout`: sacar el ratón de un elemento

## Eventos de teclado
- `keydown`: pulsar una tecla
- `keyup`: soltar una tecla

## Sobre elementos
- `focus`: poner el foco (seleccionar) sobre un elemento, por ejemplo un input
- `blur`: quitar el foco de un elemento
- `change`: al cambiar el contenido de un input (hay que quitar el foco para que se considere un cambio) o de un select 

## Formularios
- `submit`: pulsar el botón submit del formulario
- `reset`: pulsar el botón reset del formulario

## De la ventana
- `resize`: se ha cambiado el tamaño de la ventana
- `scroll`: se ha hecho scroll en la ventana o un 

# Metodos
- `classList.contains()`: para comprobar si un elemento contiene una clase. Devolverá un booleano.
- `setAttribute(atributo, valor)`: sirve para añadir atributos a etiquetas de html.