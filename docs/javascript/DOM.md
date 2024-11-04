## DOM

El DOM es la propia página web, el conjunto de html, css y js.

# Crear, añadir y eliminar elementos

Partiendo de este html:

```html
<div id="container" class="container">
  <ul class="items">
    <li class="item item--1">Item 1</li>
    <li class="item item--2">Item 2</li>
    <li class="item item--3">Item 3</li>
  </ul>
</div>
```

- **.parentelement**: selecciona el padre del elemento

```javascript
const item1 = document.querySelector(".item--1");
console.log(item1); // Devuelve una representación del elemento como HTML
console.dir(item1); // Devuelve una representación del elemento como objeto

const mother = item1.parentElement;

console.log(
  `La madre de nuestro elemento es un <${mother.nodeName.toLowerCase()}> y tiene la clase .${
    mother.className
  }`
);
// Devuelve "La madre de nuestro elemento es un <ul> y tiene la clase .items"
```

## Crear elementos

- **.createElement()** y añadirle contenido con **.createTextNode()**

```javascript
// Creamos un elemento nuevo, un <li>
const newItem = document.createElement("li");
console.log(newItem); // Devuelve "<li></li>"

// Ahora creamos algo de contenido
const newContent = document.createTextNode("Item nuevo");

// Y se lo añadimos a nuestro <li>
newItem.appendChild(newContent);
console.log(newItem); // Devuelve "<li>Item nuevo</li>"
```

## Añadir elementos

- **.appendChild()**

```javascript
const newItem = document.createElement("li");
const newContent = document.createTextNode("Item nuevo");
newItem.appendChild(newContent);

const items = document.querySelector(".items");
items.appendChild(newItem);
```

## Borrar elementos

- **.remove()**: elimina el elemento en sí
- **.removeChild()**: elimina el elemento hijo

RESUMEN:
Crear y eliminar elementos:

_Crea_ nuevos elementos con **document.createElement()**.

_Añade_ elementos al DOM con **parentElement.appendChild()**.

_Elimina_ elementos con **parentElement.removeChild()**.

_Navega_ por el DOM usando propiedades como e**lement.parentNode**, **element.childNodes**

## Modificar elementos

- **.getAttribute()**: se utiliza para obtener el valor de un atributo específico de un elemento.

```html
<a class="miEnlace" href="https://www.ejemplo.com">Enlace a Ejemplo</a>
```

```javascript
const enlace = document.querySelector(".miEnlace");
const url = enlace.getAttribute("href");
console.log(url); // Imprimirá "https://www.ejemplo.com"
```

- **.hasAttribute()**: sirve para verificar si existe un atributo expecífico en un elemento.

```html
<img class="miImagen" src="imagen.jpg" alt="Descripción de la imagen" />
```

```javascript
const imagen = document.querySelector(".miImagen");
const tieneAlt = imagen.hasAttribute("alt");
console.log(tieneAlt); // Imprimirá true
```

- **.setAttribute()**: sirve para agregar o modificar el valor de un atributo en un elemento.

CAMBIAR VALOR DE ATRIBUTO EXISTENTE

```html
<img class="miImagen" src="imagen1.jpg" alt="Imagen 1" />
```

```javascript
const imagen = document.querySelector(".miImagen");
imagen.setAttribute("src", "imagen2.jpg");
```

AGREGAR ATRIBUTO

```javascript
const enlace = document.createElement("a");
enlace.setAttribute("href", "https://www.ejemplo.com");
enlace.textContent = "Visitar Ejemplo";
```

## Ocultar y mostrar elementos basados en datos `data`

Los elementos con data-visible="false" se ocultarán inicialmente:

```html
<ul>
  <li data-visible="true">Elemento 1</li>
  <li data-visible="false">Elemento 2</li>
  <li data-visible="true">Elemento 3</li>
</ul>
```

```javascript
// Obtener todos los elementos de la lista
let elementos = document.querySelectorAll("li");

// Iterar a través de los elementos y mostrar u ocultar según el atributo data-visible
elementos.forEach(function (elemento) {
  let isVisible = elemento.dataset.visible === "true";
  if (!isVisible) {
    elemento.style.display = "none";
  }
});
```
