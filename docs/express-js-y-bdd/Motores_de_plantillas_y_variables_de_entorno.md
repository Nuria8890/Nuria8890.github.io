# Motor de plantillas

Es una funcionalidad que espera a que el navegador le solicite un fichero, desde un endpoint, y entonces coge una plantilla que hemos tenido que configurar previamente, coge los datos necesarios de la bbdd, los renderiza y devuelve la plantilla con los datos pintados.

Para poder hacer este proceso hay que:

- Instalar EJS ejecutando en la terminal `npm install ejs`
- Configurar EJS: `server.set('view engine', 'ejs')`
- Crear plantillas en la raíz del proyecto en una carpeta `views/` (dentro de esta carpeta podemos crear las carpetas y ficheros que queramos)
- Poner bien la ruta de las carpetas en `res.render('pages/film', filmData)`
- Poner bien la ruta de los partials dentro de las plantillas, escribiendo `<%- include('ruta-relativa-del-partial') %>`
- Para añadir un dato a la plantilla: `<%= nombreDeMiVariableOPropiedad %>`

```javascript
// Ejemplo de endpoint para utilizar el motor de plantillas
server.get("/api/libro/:idLibro", (req, res) => {
  const libroData = libros.find((libro) => libro.id === req.params.idLibro);

  console.log("libroData", libroData);

  if (libroData) {
    libroData.titulo = libroData.titulo || "";
    libroData.fecha_publi = libroData.fecha_publi || "";
    libroData.genero = libroData.genero || "";
    libroData.precio = libroData.precio || "";
    libroData.autor = libroData.autor || "";
    libroData.pais_autor = libroData.pais_autor || "";
    libroData.num_paginas = libroData.num_paginas || "";
    libroData.stock = libroData.stock || "";
    libroData.tipo = libroData.tipo || "";
    libroData.premios = libroData.premios || [];

    res.render("pages/libro", libroData); // entra en views por defecto y busca la ruta, y le pasa los datos de libroData
  } else {
    res.render("pages/libro-no-encontrado");
  }
});
```

```javascript
// Ejemplo de plantilla

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Este es el libro que has seleccionado</h1>
    <h3>Título: <%= titulo %></h3>
    <p>Fecha de publicación: <%= fecha_publi %></p>
    <p>Género: <%= genero %></p>
    <p>Precio: <%= precio %> €</p>
    <h4>Nombre del autor/a: <%= autor %></h4>
    <% if(pais_autor !== ""){%>
    <p>País del autor/a: <%= pais_autor %></p>
    <%}%>
    <p>Número de páginas del libro: <%= num_paginas %></p>
    <p>Número de libros en stock: <%= stock %></p>

    <% if(tipo == 0) { %>
    <p>Libro digital</p>
    <% }else { %>
    <p>Libro físico</p>
    <% } %> <% if (premios.length !== 0) { %>
    <p>Premios</p>
    <ul>
      <% premios.forEach(function(premio){ %>
      <li><%= premio.año %>: <%= premio.info %></li>
      <% }) %>
    </ul>
    <% } %>
  </body>
</html>
```

# Variables de entorno

Sirven para saber en qué entorno se está ejecutando mi web (en local, en testing o QA, en producción...).

Para saber en qué entorno estamos, hay que ejecutar en consola `npm install process`, y consultar el objeto con `console.log(process.env.NODE_ENV)`

```javascript
const serverUrl = process.env.NODE_ENV === 'production' ? 'https://misuperweb.com' : 'http://localhost:3000';

const getDataFromApi = () => {
  fetch(`${serverUrl}/ruta-de-mi-endpoint`)
   .then(response => response.json())
   .then(...)
};
```

Utilizar variables de entorno:

- Ejecutar `npm install dotenv`
- Crear un fichero en la raiz del repositorio `.env` donde metemos todas las variables de entorno que quiera
- Meter este fichero en `.gitignore`
- Configurar el servidor para que acepte variables de entorno con la librería dotenv
- Crear las variables de entorno. (Por ejemplo: `process.env.USER_DATABASE,`)
- Crear archivo `.env_example` donde escribo toda la información que está en `.env`, pero vacía, así facilito la vida a quien quiera descargarse mi proyecto.
