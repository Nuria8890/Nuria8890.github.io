# NodeJS

NodeJS sirve para ejecutar JS en la terminal o en un servidor, y nos permite leer o escribir en los ficheros del ordenador desde la terminal.

Con NodeJS no podemos manejar eventos (`document.querySelector(".main")` Si queremos ejecutar un archivo que contiene esta línea de código, no funcionaría, nos daría error)

## Ejecutar ficheros en la terminal con NodeJS:

`nodemon nombre_del_fichero`

## Exportar e importar un módulo

Módulo: sirve para separar el código y reutilizarlo (como en React, cuando poníamos el archivito de localStorage).

Para **exportarlo**:

```js
// Nombre del archivo operaciones.js
function suma(a, b) {
  return a + b;
}

function multiplicar(a, b) {
  return a * b;
}

module.exports = {
  suma: suma,
  multiplicar: multiplicar,
};
```

Para **importarlo**:

```js
let operaciones = require("./operaciones");

operaciones.suma(2, 3);
```

## Tipos de módulos

- **Custom**: módulos programados por nosotras mismas.
- **Nativos**: vienen instalados por defecto en NodeJS
  - HTTP: para configurar la comunicación entre servidores y clientes.
  - FileSystem: El módulo fs permite interactuar con el sistema de archivos
  - DNS: El módulo dns permite la resolución de nombres. Por ejemplo, para buscar direcciones IP de nombres de host.
- **Instalados con NPM**: por ejemplo el package.json (recoge la configuración inicial del proyecto).
  - Para inicializar un proyecto de nodeJS `npm init` -- pregunta la información del proyecto para que yo vaya rellenando los datos.
  - Cada vez que instalo una dependencia se me añade al package.json, para saber qué dependencia quiero usar entro en https://www.npmjs.com/

# ExpressJS

Es un módulo de NPM, sirve para programar un servidor y nos ayuda a escuchar las peticiones que se hacen desde el navegador al servidor y nos ayuda a obtener y procesar los datos de esas peticiones y a crear una respuesta que se devolverá al navegador.

Pasos a seguir para inicializar un proyecto:

- Ejecutar `npm init`
- Instalar express: `npm install express`
- Instalar cors: `npm install cors` para que se acepten peticiones que se hacen a un recurso que está en otro origen
- Agregar cors en el index.js

  ```
  const cors = require('cors');
  app.use(cors());
  ```

- Ejecutar el código: `nodemon nombre_del_fichero`
