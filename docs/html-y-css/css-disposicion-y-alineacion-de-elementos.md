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

- **display: block;** utiliza el 100% del widrh de su contenedor. Se puede agregar margin en las cuatro posiciones.

- **display: inline;** utiliza el width que ocupa su contenido, y si queda espacio, la siguiente etiqueta con display inline la pondrá después, no debajo. No se le puede agregar margin ni arriba ni abajo, ni se puede manipular el widht y el height de los elementos.

- **display: inline-block** es una fusión del display inline y el display block. *De inline*: utiliza el width que ocupa su contenido. *De block*: se puede agregar margin en las cuatro posiciones.

- **display: flex;** hace qus sus hijos sean flexibles. Se pueden usar varios recursos: 

  - **justify-content: center;** indica cómo quiero justificar el contenido con relación al eje principal (X), es decir, en horizontal, en este caso los coloca centrados. *space-evenly* (mismo espacio entre todos los elementos y a los extremos).

  - **align-items: center;** indica cómo colocar el contenido con relación al eje secundario (Y), es decir, en vertical, en este caso centrado. *strech* (los elementos se estiran al 100% de su contenedor padre). *baseline* (los elementos se encogen al tamaño de su contenido).

  - **flex-direction: column;** coloca los items en fila de izquierda a derecha (row), o en columna (column) de arriba a abajo. cuando lo pongo en column, el eje principal y el eje secundario se intercambian (el X pasa a ser el secundario y el Y empieza a ser el principal).

  - **flex-wrap: wrap;** según se va haciendo pequeña la pantalla, los items cambian de posición y se van reordenando poniéndose unos debajo de los otros.

  - **flex-grow: 1;** cuando la pantalla crece, el div al que le haya puesto el flex.grow, se va haciendo más grande que el resto para, entre todos los div, ocupar el 100% del ancho de la pantalla.

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