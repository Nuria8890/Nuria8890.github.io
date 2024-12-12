# Peticiones con parámetros

## Peticiones con query params

Query params es una forma de enviar parámetros desde front al API REST mediante la url. Van detrás de `?`, y si hay varios parámetros se separan con `&`.

`https://randomuser.me/api/?gender=female&results=500`

En el **servidor** los datos que nos están enviando desde front los recibimos en el parámetro `req.query` como un **string**.

```javascript
server.get("/api", (req, res) => {
  const gender = req.query.gender; // cuyo valor en el ejemplo de arriba es female
  const results = req.query.results; // cuyo valor en el ejemplo de arriba es 500
});
```

## Peticiones con body params

Los body params sirven para obtener los valores que un formulario envía a nuestra API. Se utilizan para enviar valores que no queremos que se vean en la URL (contraseñas).

**En front**: enviamos los datos en el cuerpo del `fetch` de tipo `POST`.

```javascript
const bodyParams = {
  userName: "Maricarmen",
  userEmail: "mari@gmail.com",
};

fetch("http://localhost:3000/user", {
  method: "POST",
  body: JSON.stringify(bodyParams),
  headers: {
    "Content-Type": "application/json",
  },
});
```

**En el servidor**: obtenemos los datos con `req.body`

```javascript
app.post("/user", (req, res) => {
  console.log("Body params:", req.body);
  console.log("Body param userName:", req.body.userName);
  console.log("Body param userEmail:", req.body.userEmail);

  // add new user to dababase
  users.push({
    name: req.body.userName,
    email: req.body.userEmail,
  });

  res.json({
    result: "User created",
  });
});
```

## Peticiones con url params

URL params sirve para crear rutas dinámicas y mostrar información específica de cada producto en particular (`product/:productId`)

## Peticiones con header params

Igual que los body params, se tienen que enviar siempre desde un `fetch`, no los podemos indicar en la barra de direcciones del navegador como los query o URL params.
Se envían añadiendo un objeto headers al fetch

```javascript
fetch('http://localhost:3000/ruta-del-endpoint', {
    method: 'POST', // o GET, PUT, PATCH...
    headers: {
      unParametroEnLaCabecera: 'Hola mundo',
      'otro-parametro-de-la-cabecera': 123,
      otroParametroMas: 'Soy un dato'
    }
  })
  .then(response => response.json())
  .then(data => {...});
```

En el **servidor**:

- Recibimos los datos en `req.headers`, que es un objeto, o a través del método `req.header('nombre-de-header-param')` que nos devuelve el valor de un header param.

- Todos los datos enviados por header param **se reciben en el servidor como string en minúsculas**, aunque desde el fetch los hayamos enviado como número u otro tipo de dato.

Resumen de header params

Desde el navegador:

Se pueden enviar en todos los tipos de peticiones (GET, POST, PUT, PATCH...).

Se tienen que enviar siempre desde un fetch.

Se envían añadiendo un objeto headers al fetch.

En el servidor:

Recibimos los datos en el objeto req.headers o a través del método req.header('nombre-de-header-param').

Todos los datos enviados por header param se reciben en el servidor como string.

Todos los nombres de propiedades del objeto req.headers nos llegan al servidor en minúsculas.
