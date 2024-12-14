# Peticiones con parámetros

## Peticiones con query params

Query params es una forma de enviar parámetros desde front al API REST mediante la url. Van detrás de `?`, y si hay varios parámetros se separan con `&`.

`https://randomuser.me/api/?gender=female&results=500`

- En **front**:

```javascript

```

- En el **servidor** los datos que nos están enviando desde front los recibimos en el parámetro `req.query` como un **string**.

```javascript
// Endpoints
app.get("/api/students", async (req, res) => {
  // 1. Contectarme a la bbdd
  const connection = await getConnection();

  // 2. Recoger la información que me envían desde front
  const name = req.query.name;

  // 3. Escribir la query
  const query = "SELECT * FROM students WHERE name = ?;";

  // 4. Ejecutar la query
  const [result] = await connection.query(query, [name]);

  // 5. Finalizar la conexión con la bbdd
  connection.end();

  // 6. Responder a frontend
  res.json({
    status: "success",
    message: result,
  });
});
```

## Peticiones con body params

Los body params sirven para obtener los valores que un formulario envía a nuestra API. Se utilizan para enviar valores que no queremos que se vean en la URL (contraseñas).

- **En front**: enviamos los datos en el cuerpo del `fetch` de tipo `POST`. Acepta todos los métodos menos el GET, es decir, cualquier método que _envíe_ información.

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

- **En el servidor**: obtenemos los datos con `req.body`

```javascript
app.post("/api/student", async (req, res) => {
  // 1. Contectarme a la bbdd
  const connection = await getConnection();
  // comprueblo la conexión con Postman simulando un POST

  // 2. Recoger la información que me envían desde front
  const studentData = req.body;
  console.log("Datos que me envía frontend: ", studentData);

  // 3. Escribir la query
  const query =
    "INSERT INTO students (name, lastname, age, email) VALUES (?,?,?,?);";

  // 4. Ejecutar la query
  const [result] = await connection.query(query, [
    studentData.name,
    studentData.lastname,
    studentData.age,
    studentData.email,
  ]);

  // 5. Finalizar la conexión con la bbdd
  connection.end();
  console.log("Resultado de la query: ", result);

  // 6. Responder a frontend
  res.status(201).json({
    status: "success",
    result: "User created",
    id: result.insertId,
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
