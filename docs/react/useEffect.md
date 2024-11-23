# useEffect

- Como primer parámetro SIEMPRE recibe una **función sin ejecutar**, esta función puede ser un `fetch` o una escritura en `localStorage`.

- Como segundo parámetro recibe un array (opcional), que sirve para indicar a React cuándo queremos que se ejecute el primer parámetro.
  - Sin array: la función se ejecutará siempre que se renderice el componente App.
  - Array vacío: la función se ejecutará solo la primera vez que se renderice el componente App.
  - Array relleno (con una constante de estado): la función se ejecutará cuando cambie el valor de la constante de estado.

## Fetch

Para realizar un fetch en React hay que crear una carpeta services, y dentro un archivo api.js. Dentro de este fichero se hace el fetch:

```javascript
const callToApi = () => {
  return fetch() // url de la api
    .then((response) => response.json())
    .then((data) => {
      const result = () => {
        // código
      };
      return result;
    });
};

export default callToApi;
```

Este fichero se importa en App.jsx y se usa:

```javascript
import callToApi from "../services/api";
import { useState, useEffect } from "react";

function App() {
  // Estados

  const [variable, setVariable] = useState("");

  useEffect(() => {
    callToApi().then((response) => {
      setVariable(response);
    });
  }, []); // Array vacío porque quiero que llame a la API solo una vez

  return <>{/* código HTML */}</>;
}

export default App;
```

## Local Storage

Para guardar un datos en localStorage hay que crear una carpeta services, y dentro un archivo localStorage.js. Dentro de este fichero se hace un objeto con las 4 acciones del localStorage (recuperar, guardar, eliminar un elemento y limpiar todo el caché):

```javascript
// Comprueba si hay datos en localStorage
const get = (key, defaultValue) => {
  const localStorageData = localStorage.getItem(key);
  if (localStorageData === null) {
    return defaultValue;
  } else {
    return JSON.parse(localStorageData);
  }
};

// Guarda una propiedad y su valor en localStorage
const set = (key, value) => {
  const localStorageData = JSON.stringify(value);
  localStorage.setItem(key, localStorageData);
};

// Borra una propiedad del localStorage
const remove = (key) => {
  localStorage.removeItem(key);
};

// Limpia todo el localStorage
const clear = () => {
  localStorage.clear();
};

// Objeto temporal para exportarlo
const objectToExport = {
  get: get,
  set: set,
  remove: remove,
  clear: clear,
};

// Exporto el objeto para que pueda ser usado desde App
export default objectToExport;
```

Este fichero se importa en App.jsx y se usa:

```javascript
import callToApi from "../services/api";
import { useState, useEffect } from "react";

function App() {
  // Estados

  const [variable, setVariable] = useState(localStorage.get("variable", ""));

  useEffect(() => {
    localStorage.set("variable", variable);

    // Este useEffect solo se ejecutará cuando cambie el nombre o el email
    console.log("Ha cambiado la variable");
  }, [variable]);

  return <>{/* código HTML */}</>;
}

export default App;
```
