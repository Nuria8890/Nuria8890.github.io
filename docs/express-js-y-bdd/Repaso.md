Ver resumen Express

- Leer el enunciado
- Crear repo
- Crear la bbdd
  - Crear las tablas y columnas
  - Rellenar contenido a la tabla para ir probando los endpoints
- Crear y configurar el servidor con NODEJS y EXPRESS

  - Copiar el template o hacerlo desde cero:

    - Si lo hago desde cero:

      - Generar archivo packaje.json (`npm init`)

      - Agregar en package.json los scripts que necesite (`"start": "node src/index.js"`, `"dev": "nodemon src/index.js"`)

      - Instalar: cors, express, mysql2, (dotenv para las variables de entorno) (`npm install express cors mysql2 dotenv`)

      - Crear carpeta src y un fichero index.js

      - Crear un .gitignore para meter los node_modules y la carpeta .env si hago las variables de entorno

      - Importar librerías que me acabo de instalar (`const express = require("express")`, `const cors = require("cors")`, `const mysql = require("mysql2/promise")`)

      - Crear el servidor (`const server = express()`)

      - Configurar el servidor para que acepte peticiones (`server.use(cors())` y `server.use(express.json({ limit: "25MB" })`)

      - Establecer y arrancar el puerto de conexión:

```javascript
const serverPort = process.env.PORT;

server.listen(serverPort, () => {
  console.log(`Server listening at http://localhost:${serverPort}`);
});
```

      - Crear la función para conectarme a la bbdd:

```javascript
async function getDBConnection() {
  const connection = await mysql.createConnection({
    host: "hostname",
    user: "username",
    password: "root",
    datbase: "nombre de la bbdd",
  });
  connection.connect();
  return connection;
}
```

- Desarrollar los endpoints
