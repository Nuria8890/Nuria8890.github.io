# Sass (Syntactically Awesome StyleSheets)

Con el adalab starter kit SIEMPRE hay que usar la ruta completa para llamar a los archivos, esté donde esté.


Para utilizar scss:
1. Crear style.scss y escribir el código de estilos en sass.
2. En la terminal escribir: `sass style.scss style.css`
3. Se van a crear dos archivos `.css`.
4. En `.html` linkar `style.css`.


Un **preprocesador** de CSS es un lenguaje parecido al CSS pero que nos permite tener acceso a funcionalidades que no tiene el CSS y, tras el procesado, generar un CSS válido.

## Variables

```scss
$headerHeight: 100px;
$fontText: 'Roboto', arial, sans-serif;
$pathImages: '../images/';

body {
  font: 16px $fontText;
}
.header {
  background: url($pathImages + 'imagen.png') left top no-repeat;
  height: $headerHeight;
}
```

## Anidado o nesting


```scss
// Todos los párrafos que estén dentro de un elemento con clase .content van a ser de color azul y, si llevan enlace, este se mostrará en rojo:

.content {
  p {
    color: blue;
    a {
      color: red;
    }
  }
}
```

Genera el siguiente css:

```css
.content p {
  color: blue;
}
.content p a {
  color: red;
}
```

### &

```scss
// Enlaces rojos y el hover en azúl
// Enlaces del footer naranjas y el hover en verde

a {
  color: red;
  &:hover {
    color: blue;
  }
  .footer & {
    color: orange;
    &:hover {
      color: green;
    }
  }
}
```

Genera el siguiente css

```css
a {
  color: red;
}
a:hover {
  color: blue;
}
.footer a {
  color: orange;
}
.footer a:hover {
  color: green;
}
```

## Media queries en Sass

```scss
.wrapper {
  margin: 0 25px;
  @media (min-width: 768px) {
    margin: 0 40px;
  }
  @media (min-width: 1280px) {
    margin: 0 auto;
    max-width: 1200px;
  }
}
```

Genera el siguiente css

```css
.wrapper {
  margin: 0 25px;
}
@media all and (min-width: 768px) {
  .wrapper {
    margin: 0 40px;
  }
}
@media all and (min-width: 1280px) {
  .wrapper {
    margin: 0 auto;
    max-width: 1200px;
  }
}
```