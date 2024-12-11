# Endpoints

Es una ruta o path a la que atiende una aplicación servidor para un verbo o method determinado.

```javascript
// Ejemplo de endpoint
const variable_con_datos = [
  { datos: "datos del primer elemento" },
  { datos: "datos del segundo elemento" },
  { datos: "datos del tercer elemento" },
];
server.método("/nombre_de_la_ruta", (request, response) => {
  // request: objeto que trae toda la información de la petición.
  // response: objeto para responder la petición.
  /* Pasos:
  1. Buscar la información en un fichero o en la bbdd.
  2. Procesar esa información
  3. Enviar la respuesta
  */
  if (variable_con_datos.length === 0) {
    response
      .status(404)
      .json({ succes: false, error: "No se ha encontrado el resultado" });
  } else {
    response.status(200).json({ succes: true, result: variable_con_datos });
  }
});
```

- `req`: objeto que contiene información sobre la petición HTTP que ha provocado el evento
- `res`: se utiliza para devolver la respues HTTP deseada.

# Métodos

- **GET**: obtener información del servidor. `SELECT * FROM...`
- **POST**: añadir información al servidor. `INSERT INTO`

```javascript
server.post("/ruta", (req, res) => {
  // actualizo mi bbdd
  // envío respuesta
  res.status(201).json({
    success: true,
    message: "Recurso añadido correctamente",
  });
});
```

- **PUT**: reemplazar información en el servidor. `UPDATE ... SET`

```javascript
server.put("/ruta/:id", (req, res) => {
  // recojo el id que me envía front
  // actualizo mi bbdd
  // envío respuesta
  res.status(200).json({
    success: true,
    message: "Recurso actualizado correctamente",
  });
});
```

- **DELETE**: eliminar totalmente información del servidor. `DELETE`
- **PATCH**: actualizar una parte de la información que hemos enviado al servidor.
- **OPTIONS**: sirve para pedir información sobre los métodos.

# Cabeceras

Permiten al cliente y al servidor enviar información adicional junto a una petición o respuesta. En las cabeceras se especifican indicaciones especiales que queremos darle al servidor.

# Tipos de respuesta

- `res.json`: el método envía una respuesta json

```javascript
res.json(null);
res.json({ user: "tobi" });
res.status(500).json({ error: "message" });
```

- `res.render`: Tiene tres parámetros:

  - El argumento de la vista es una cadena con la ruta del archivo vista para representar. Puede ser una ruta absoluta o una ruta relativa a la configuración de vistas.
  - locals: un objeto cuyas propiedades definen variables locales para la vista.
  - callbacks: una función callback. Si se proporciona, el método devuelve tanto el posible error como la cadena procesada, pero no realiza una respuesta automática. Cuando ocurre un error, el método invoca next(err) internamente.

```javascript
// send the rendered view to the client
res.render("index");

// if a callback is specified, the rendered HTML string has to be sent explicitly
res.render("index", function (err, html) {
  res.send(html);
});

// pass a local variable to the view
res.render("user", { name: "Tobi" }, function (err, html) {
  // ...
});
```

- `res.send`: envía una respuesta de varios tipos:

```javascript
res.send(Buffer.from("whoop"));
res.send({ some: "json" });
res.send("<p>some html</p>");
res.status(404).send("Sorry, we cannot find that!");
res.status(500).send({ error: "something blew up" });
```

- `res.status(code)`: establece el estado HTTP para la respuesta

```javascript
res.status(403).end();
res.status(400).send("Bad Request");
res.status(404).sendFile("/absolute/path/to/404.png");
```

# Códigos de respuesta HTTP

- Respuestas informativas (100–199),

- Respuestas satisfactorias (200–299) todo ha ido bien,

- Redirecciones (300–399) la petición se redirige a otro sitio,

- Errores de los clientes (400–499) ha enviado algo mal, no está autorizado...,

- Errores de los servidores (500–599).

Para cambiar el código de estado de la respuesta usamos `res.status`.

```javascript
app.post("/newItem", function (req, res) {
  res.status(201).json({ success: true });
});
```
