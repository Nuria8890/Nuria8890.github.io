# Disposición y alineación de elementos

```html
<!--HTML-->
<section>
    <div class="static">
      <span>Static</span>
    </div>

    <div class="relative">
      <span>Relative</span>
    </div>

    <div class="fixed">
      <span>Fixed</span>
    </div>

    <div class="absolute">
      <span>Absolute</span>
    </div>

    <div class="sticky">
      <span>Sticky</span>
    </div>
  </section>
```

```css
/*CSS*/
section {
  width: 100%;
  height: 100%;
  background-color: rgb(165, 159, 159);
}

div {
  width: 130px;
  height: 50px;
  font-size: 30px;
  border: 3px solid black;
}
```
- Static: es el que viene por defecto.

```css
.static {
  background-color: rgb(66, 66, 221);
}
```

- Relative: nos permite posicionarle en relación a la posición que tendría si fuera static. // Movemos el div con respecto a los demás.

```css
.relative {
  background-color: rgb(234, 60, 60);
	position: relative;
	left: 80px; /*De la izquierda se separa 80px*/
	z-index: 10; /*Visualmente está en primer plano*/
}
```

- Fixed: independientemente del scroll que hagamos, siempre se va a mantener fijo.

```css
.fixed{
  background-color: yellow;
	position: fixed;
	bottom: 0px; /*colocado abajo del todo de la página*/
	left: 0px; /*colocado a la izquierda del todo de la página*/
}
```

- Absolute: permite posicionarlo igual que el fixed pero en relación a su elemento padre. Normalmente se mete el div de clase absolute dentro del div de clase relative (elemento padre). Un recuadro (absolute) dentro de otro (relative). // El div se pone encima y "desaparece" el de al lado.

```css
.absolute{
  background-color: rgb(20, 189, 20);
	position: absolute;
	top: 0px; /*colocado arriba del todo de la página*/
	right: 200px; /*colocado a 200px de distancia de la derecha de la página*/
}
```

- Sticky: Es una mezcla entre el relative y el fixed. Se usa normalmente para los menús, al hacer scroll siempre está visible.

```css
.sticky{
  background-color: rgb(255, 166, 0);
	position: sticky;
}
```


![ejemplo de disposición y alineación de elementos](./img/image-15.png)

### [Flex Box](https://codepen.io/enxaneta/full/adLPwv)
Esta propiedad es un modo de diseño que permite colocar los elementos de una página para que se comporten de forma predecible cuando el diseño de la página debe acomodarse a diferentes tamaños de pantalla y diferentes dispositivos.

- **display: block;** los elementos ocupan el 100% del width de su contenedor y se colocan unos debajo de otros. Se puede agregar margin en las cuatro posiciones. (Los elementos que por defecto tienen display block son: "¿Tendría sentido meter este elemento dentro de un párrafo?". Si la respuesta es no, es muy probable que sea un elemento en block.)

- **display: inline;** los elementos utilizan el width que ocupa su contenido, y si queda espacio, la siguiente etiqueta con display inline la pondrá después, en línea, no debajo. No se le puede agregar margin ni arriba ni abajo, ni se puede manipular el width y el height de los elementos. (Los elementos que por defecto tienen display inline son:  "¿Tendría sentido meter este elemento dentro de un párrafo?". Si la respuesta es sí, es muy probable que sea un elemento en línea.)

- **display: inline-block;** es una fusión del display inline y el display block. *De inline*: utiliza el width que ocupa su contenido. *De block*: se puede agregar margin en las cuatro posiciones.

- **display: none;** oculta el elemento, no lo muestra.

- **display: flex;** afecta a la caja contenedora (donde se activa el modo flex) y a las cajas contenidas (las hijas directas). Se pueden usar varios recursos: 

  - **flex-direction: ___;** **row** (coloca los items en fila de izquierda a derecha), **row-reverse** (en fila en sentido inverso) , **column** (coloca los items en columna de arriba a abajo), **column-reverse** (en columna en sentido inverso). Cuando lo pongo en column, *el eje principal y el eje secundario se intercambian* (el X pasa a ser el secundario y el Y empieza a ser el principal).

  - **flex-wrap: ___;** **wrap** (según se va haciendo pequeña la pantalla, los items cambian de posición y se van reordenando poniéndose unos debajo de los otros), **wrap-reverse** (se reordenan en sentido inverso, de abajo a arriba).

  - **flex-flow: column wrap;** combina flex direction y flex-wrap.

  - **justify-content: ___;** indica cómo quiero justificar el contenido con relación al eje principal (X), es decir, en horizontal. **center**(los coloca centrados), **flex-start** (junta todo el espacio libre a la derecha), **space-evenly** (mismo espacio entre todos los elementos y a los extremos), **space-between** (el primer elemento se alinea al inicio del contenedor, el último elemento se alinea al final, y los elementos intermedios se distribuyen uniformemente, dejando el mismo espacio entre ellos), **space-around** (hay un espacio igual al rededor de cada uno de los elementos), **flex-end** (junta todo el espacio libre a la izquierda).

  - **align-items: ___;** indica cómo colocar el contenido con relación al eje secundario (Y), es decir, en vertical. **center** (centrado), **strech** (los elementos se estiran al 100% de su contenedor padre), **flex-start** (junta todo el espacio libre abajo), **baseline** (los elementos se organizan en la línea de base), **flex-end** (junta todo el espacio libre arriba).

  - **align-self: ___;** permite a una caja hija cambiar la alineación especificada en la caja contenedora. Tiene los mismos valores que align-items.

  - **gap: *10px 20px*;** espacio entre cajas hijas.(*row-gap: 10px; ó column-gap: 10px;* permiten especificar de forma aislada la separación entre filas y entre columnas.)

  - **order: *5*;** por defecto las cajas hija se colocan en orden de llegada; si queremos adelantar o atrasar cajas lo podemos especificar.

  - **flex-grow: *2*;** cuando la pantalla crece, el div al que le haya puesto el flex-grow, se va haciendo más grande que el resto para, entre todos los div, ocupar el 100% del ancho de la pantalla. Un ejemplo: si tuviéramos las cajas 1 y 2 con flex-grow=1 y la 3 con flex-grow=2, y no tuvieran tamaño fijo, acabaríamos con una caja 3 de doble tamaño que las otras: [-1-] [-2-] [--3--]

  - **flex-shrink: *2*;** similar a flex-grow, pero en lugar de agrandar la caja hija, la reduce.

  - **flex-basis: *200px*;** define el tamaño por defecto de un elemento antes de distribuir el espacio. Puede usarse **auto** para que el tamaño del elemento se base en su contenido.

  - **flex: *3 1 auto*;** combina *flex-grow*, *flex-shrink* y *flex-basis*. Se recomienda usar esta propiedad, porque da valores con sentido a las que no.

  - **align-content: ___;** permite ajustar cómo quedan las filas o columnas en conjunto dentro de la caja contenedora, cuando hay espacio de sobra. **flex-start**, **center**, **stretch** (las líneas del contenedor se estiran para ocupar todo el espacio disponible en el eje transversal (eje contrario del principal)).

```html
<!-- HTML -->
<section>
    <div class="div-1">
      <span>DIV 1</span>
    </div>
    <div class="div-2">
      <span>DIV 2</span>
    </div>
    <div class="div-3">
      <span>DIV 3</span>
    </div>
    <div class="div-4">
      <span>DIV 4</span>
    </div>
    <div class="div-5">
      <span>DIV 5</span>
    </div>
  </section>
```

```css
/* CSS */

section {
  background-color: grey;
  display: flex;
  justify-content: center;
  gap: 0.7rem;
  align-items: center;
  flex-wrap: wrap;
}

div {
  width: 300px;
  height: 100px;
}
.div-1 {
  background-color: red;
}
.div-2 {
  background-color: yellow;
}
.div-3 {
  background-color: green;
}
.div-4 {
  background-color: orange;
}
.div-5 {
  background-color: aqua;
}
```

![ejemplo de flex box](./img/image-16.png)

#### Guía para un buen flexbox

- ¿Dónde debemos aplicar los estilos?
  - Los *estilos de la caja contenedora* (dirección, distribución...) los aplicamos en la propia caja contenedora.

  - Los *estilos comunes a todas las hijas* los aplicamos a una clase común para todas las hijas, por ejemplo: .item.

  - Si *una de las hijas* tiene una *disposición o tamaño diferente* a la de las demás, se le aplica estilos solo a esa caja con una clase propia, por ejemplo: .item-x.

- Procedimiento normal
  1. Aplicar *box-sizing* y *border* o *background-color* tanto a la caja contenedora como a las hijas para visualizar cómo se comportan (después se pueden borrar estos estilos).

  2. En la caja contenedora:
    - Indica: *display: flex*.

    - Elige *dirección del eje principal*: filas (row) o columnas (column). Hay que tener muy muy claro cuál queremos que sea el eje principal y cuál el secundario.

    - Indica la *dirección del eje principal*: flex-direction: row | column. No hay que confundir eje principal con eje horizontal, ni eje secundario con eje vertical.

    - Indica si quieres que los *items salten de fila* (o columna): flex-wrap: wrap, *o se mantengan en una sola*. A lo mejor es necesario añadir muchas hijas para poder ver el salto de línea.

    - Indica *cómo se alinean o distribuyen los elementos en el eje principal*, en el caso de que sobre o falte espacio: justify-content: center. (si no parece que no funciona es porque no sobra espacio y no se puede añadir espacio entre las hijas)

    - Indica *cómo se alinean o distribuyen los elementos en el eje secundario*: align-items: center. (si no parece que no funciona es porque no sobra espacio y no se puede añadir espacio entre las hijas)

  3. En los elementos items:
    - Indica a todos los items el *tamaño* que deben tener: ancho si el eje principal es horizontal o alto si el eje principal es vertical.

- Procedimiento avanzado
  1. Si queremos indicar un *ancho variable* en función del espacio sobrante o el espacio faltante, usamos: flex-grow, flex-shrink.

  2. Si queremos indicar un *ancho inicial* antes de repartir el espacio sobrante o faltante, usamos: flex-basis.

  3. Si queremos usar un *ancho fijo* usamos: width.

  4. Para indicar *en un elemento un tamaño especial* que debe tener: flex-grow, flex-shrink y flex-basis.

  5. Si queremos *cambiar el orden de las hijas* le aplicamos order a una de ellas, teniendo en cuenta que los órdenes menores de 0 se moverán a la izquierda y mayores de 0 se moverán a la derecha.

### Grid
**display: grid;**

**grid-template-columns:** Formas de colocar los items en tres columnas:\
    - **auto auto auto;\
    - repeat(3, auto);\
    - 20px 3rem 25vw;\
    - 1fr 1fr 3fr;**

**grid-template-rows: 220px 5rem 100px;** Le damos un tamaño a las filas

**grid-template-areas: 'head head head' 'main main aside' 'footer footer footer';**

**grid-column: 2 / span 2;** Quiero que este item empieze en el espacio 2 y ocupe 2 columnas

**grid-area: 2 / 2 / 4 / 3;** Quiero que este item ocupe desde la fila inicio 2 hasta la columna inicio 1, y desde la fila fin 4 hasta la columna fin 3.

```html
<!-- HTML -->
  <section>
    <div class="div-1">
      <span>DIV 1</span>
    </div>
    <div class="div-2">
      <span>DIV 2</span>
    </div>
    <div class="div-3">
      <span>DIV 3</span>
    </div>
```

```css
/* CSS */
section {
  background-color: grey;
  display: grid;
  grid-template-columns: auto auto auto;
  grid-template-rows: 220px 5rem 100px;
  grid-template-areas: 'head head head' 'main main aside' 'footer footer footer';
}

.div-1 {
  background-color: red;
  grid-column: 2 / span 2;
}
.div-2 {
  background-color: yellow;
  grid-area: 2 / 2 / 4 / 3;
}
.div-3 {
  background-color: green;
}
```

![ejemplo de grid](./img/image-17.png)