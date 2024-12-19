# Testing

Para poder hacer Testing hay que instalarse las librerías:

- ejecutar `npm install --save-dev jest` para instalar jest
- en packaje.json: `"jest": {"testEnviroment":node}`
- ejecutar `npm install --save-dev supertest` para instalar supertest
- SOLO en windows: `npm install --save-dev cross-env`
- en packaje.json:
  - windows: `CROSS.ENV NODE_ENV=test jest --verbose --runInBand`
  - mac: ``
- Crear una carpeta nueva test y añadir un archivo que termine en `nombre_del_test.test.js`
- Importar: `const supertest = require("supertest");`
- En index.js `module.exports = server` Exporto todo el servidor
- En test.js importar el servidor `const server = require("..srce/index");`
- A supertest hay que pasarle el api que quiero testear: `const api = supertest(server)`
- Para agrupar los conjuntos de test `describe("")`
