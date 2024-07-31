# *APUNTES DE HTML Y CSS*
**Alt+Z** Cuando un párrafo es muy largo, al hacer Alt+Z el código se adapta al tamaño de la ventana.

**Ctrl+/** Para poner un comentario. El usuario no los ve y sirven para ver a simple vista la estructura de la página. `<!--HTML-->` `/*CSS*/`

**!** Para crear la estructura inicial de cada html

**Ctrl+d** Para seleccionar varios nombres de etiquetas y poder modificarlos todos a la vez.

**div.padre** Crea esto:

```html
<div class=”padre”></div>
```

**div#hijo** Crea esto:

```html
<div id=”hijo”></div>
```

**li`*`3** Crea esto:

```html
<li></li>
<li></li>
<li></li>
```

# Elementos / Etiquetas
[Apuntes de etiquetas](./html-y-css/html-etiquetas.md)

# Atributos
Describen información adicional del elemento. Se escriben entre comillas en la apertura, antes del > y se separan de su valor con un =.

< h1 `class="titulo-principal"` > Este es el título </ h1 >

**id**: pone un identificador a cada elemento. Es único. Sirve para crear un enlace interno o dar un formato con CSS

**style**: para personalizar un elemento, darle un estilo (formato) determinado.

**lang**: idioma.

**src**: especifica la imagen que queremos insertar. Source, fuente, desde donde se coge la imagen.

**alt**: breve descripción de la imagen que se ha insertado (por si la página no carga).

**href**: es el enlace en sí.

```html
<link href="style.css">

<a href="https://www.unapaginaweb.com" target="_blank" rel="noopener noreferer"> Esto es un enlace a una página web </a>
```
# Listas
- Ordenada: Order list.

```html
<ol>
  <li>Azul</li>
  <li>Verde</li>
  <li>Rojo</li>
</ol>
```

1. Azul
2. Verde
3. Rojo

- Desordenada: Unorder list.

```html
<ul>
  <li>Azul</li>
  <li>Verde</li>
  <li>Rojo</li>
</ul>
```
- Azul
- Verde
- Rojo

# Formularios
[Apuntes de formularios](./html-y-css/html-formularios.md)

# CSS
[Apuntes de CSS](./html-y-css/css.md)