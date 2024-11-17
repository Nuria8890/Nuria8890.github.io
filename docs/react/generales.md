# REACT

**Apuntes de React de un chico de Platzi**

https://github.com/aleroses/Platzi/blob/master/DW/3-avanzado/1.react.js/Platzi/reactjs.md

**Librería**: conjunto de utilidades de programación, que podemos decidir si utilizar o no.
**Framework**: es un marco de trabajo, un sistema de pautas o reglas concretas. React es un framework. Es una herramienta que nos proporciona una forma de trabajar con unas reglas claras y estrictas de cómo programar.

**Crear un comentario**

```javascript
{
  /* <CreateTodoButton/> */
}
```

**Ctrl+espacio**
Al hacer doble click en un componente (seleccionarlo), si se pulsa ctrl+espacio, sale un aviso de que hay un archivo que se llama igual, y si clickas en el aviso, importa el componente.

## ¿Qué es un componente de React.js?

Es una identidad, finalidad o funcionalidad propia y que se pueden reutilizar (input de formulario, elementos del menú...), es como si fueran funciones de JS.

Si en un proyecto de React nos encontramos una función donde su nombre empieza con una letra mayúscula, 99% es un componente.

```javascript
function App() {} // componente de React.js
```

## Crear un nuevo proyecto de React:

1. UNA ÚNICA VEZ EN CADA ORDENADOR: `npm install -g create-vite`.
2. Ejecuta `create-vite my-react-app --template react`.
3. Abre VS Code en la carpeta creada.
4. Ejecuta `npm install node-sass` y `npm install sass`. si sale este error `Cannot find module 'sass'` hay que volver a ejecutar el punto 4.
5. Ejecuta `npm run dev` para arrancar el proyecto.
6. Ejecuta `npm install prop-types`.
7. Ejecuta `npm run build` para crear una versión de producción.

## Ficheros

- **public/vite.svg**: es el favicon que aparece en la pestaña del navegador.

- **index.html**: HTML principal y único.

  - `<div id="root"></div>` contenedor donde se meten los componentes creados en React. Todo lo que esté dentro, lo gestiona React, lo que está fuera lo gestiono yo a mano con JS y CSS (normalmente no se pone nada fuera).

- **src/styles/App.css**: es un partial de estilos del componente **App.jsx**

- **src/component/App.jsx**: componente principal de la web

  - Aquí se crea el HTML y el JS.
  - `import reactLogo from './assets/react.svg';` y `import viteLogo from '/vite.svg'`: importa una imagen para luego ser utilizada en el HTML de más abajo.
  - `function App() {...}`: retorna el HTML que queremos mostrar en nuestra web.
  - No debemos cambiarlo de nombre ni de carpeta.

- **src/index.css**: los estilos principales de la página. Se importan en el fichero **src/main.jsx**.

- **src/main.jsx**: fichero principal en el que se arranca el proyecto. Desde aquí se le indica a React qué componentes quiero que renderice y dónde.

## Diferenciar html de jsx

Lo que está dentro del **componente de React.js** es jsx. Lo diferenciamos de html porque, por ejemplo, en jsx ponemos className, en lugar de solo class.

Más adelante, esto se convertiá en html.

```javascript
function App() {
  return (
    <div className="App">
      <TodoItem />
      <TodoItem />
      <TodoItem />

      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edita el archivo <code>src/App.js</code> y guarda para recargar.
        </p>
        <a
          className="App-link"
          href="https://platzi.com/reactjs"
          target="_blank"
          rel="noopener noreferrer"
        >
          Aprendamos React
        </a>
      </header>
    </div>
  );
}
```

## ¿Qué es un elemento de React.js?

Un elemento es una "etiqueta de html". En el ejemplo sería <span>

```javascript
function TodoItem() {
  return (
    <li>
      <span>V</span>
      <p>Llorar con la Llorona</p>
      <span>X</span>
    </li>
  );
}
```

## Props

Las props (propierties) es la información que un componente padre le pasa a su hijo para personalizarlo. Es decir, sirve para comunicar dos componentes.

Permiten cambiar valores para que sean dinámicos.

### Recibir propiedades

el hijo las recibe así:

```javascript
import "../styles/layout/Button.scss";
import PropTypes from "prop-types";

function Button(props) {
  return (
    <>
      <button className="btn">{props.textButton}</button>
    </>
  );
}

export default Button;

Button.propTypes = {
  textButton: PropTypes.string.isRequired,
};
```

Es importante ejecutar `npm install prop-types` en la consola para que el hijo "exija" al padre sus props y que la consola nos avise si el padre no le está pasando todas las props que el hijo necesita o si se las está pasando mal.

### Enviar propiedades

El padre las envía así:

```javascript
<Button textButton={"Ir a Adalab"} href={"http://www.adalab.es"} />
/>
```

## Lifting y children

El lifting en React significa subir datos desde un componente hija a una madre por el árbol de componentes. Para ello usamos funciones. Si una hija quiere pasar datos a su madre, puede ejecutar una función de su madre con argumentos.

La madre pasa a la hija por props una función sin ejecutar, y la hija la ejecuta cuando la usuaria realice un evento determinado.

- **Sin parámetros**: la hija avisa a la madre de que ha pasado algo (click en enviar, resetear formulario, cerrar un menú...)
- **Con parámetros**: la hija avisa a la madre de que ha pasado algo y con qué datos ha ocurrido (se cambia el valor del email y el nuevo valor es pepita@adalab.es)

## Local Storage

Guarda el historial.

En la consola:

- localStorage.setItem('key', 'value'): añade un elemento con una clave y un valor al almacenamiento local.
- localStorage.getItem('key'): recupera el valor de la clave especificada en el almacenamiento local.
- localStorage.removeItem('key'): elimina el elemento del almacenamiento local según la clave especificada.
- localStorage.clear(): elimina todo el almacenamiento local.

- localStorage solo puede guardar strings, así que cada vez que queramos guardar algo en localStorage hay que utilizar la siguiente función:
  - JSON.stringify(): convierte JavaScript en strings.
- Para poder leer algo que hemos guardado en localStorage hay que utilizar la siguiente función:
  - JSON.parse(): convierte un string en array.

Ejemplo en consola:

```javascript
const defaultTodos = [
  { text: "Cortar cebolla", completed: true },
  { text: "Curso React.js", completed: false },
  { text: "Saltar a la comba", completed: false },
  { text: "Piscina", completed: true },
];

JSON.stringify(defaultTodos); // '[{"text":"Cortar cebolla","completed":true},{"text":"Curso React.js","completed":false},{"text":"Saltar a la comba","completed":false},{"text":"Piscina","completed":true}]'

const stringifyedTodos = JSON.stringify(defaultTodos);

stringifyedTodos; // '[{"text":"Cortar cebolla","completed":true},{"text":"Curso React.js","completed":false},{"text":"Saltar a la comba","completed":false},{"text":"Piscina","completed":true}]'

JSON.parse(stringifyedTodos);

// (4) [{…}, {…}, {…}, {…}]
// 0
// :
// {text: 'Cortar cebolla', completed: true}
// 1
// :
// {text: 'Curso React.js', completed: false}
// 2
// :
// {text: 'Saltar a la comba', completed: false}
// 3
// :
// {text: 'Piscina', completed: true}
// length
// :
// 4
// [[Prototype]]
// :
// Array(0)
```

## Custom Hooks

Separar la lógica de un componente cuando es demasiado compleja o "enguarrina" el código y no deja que se lea facilmente.

## React Context

**Prop Drilling**: es un paso del desarrollo que ocurre cuando necesitamos obtener datos que están en varias capas en el árbol de componentes React.

Este se ve siempre cuando pasamos props entre hijos, luego ese a otros hijos y así sucesivamente... la solución es usar context:

**Context**: es un elemento que podemos crear en React para establecer una comunicación directa entre un componente en un nivel muy alto y uno en un nivel mucho más bajo.

Por ende, context permite acceder a los valores de forma directa.
