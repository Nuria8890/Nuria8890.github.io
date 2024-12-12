# My SQL y Express JS

Para conectar la bbdd con el servidor:

- Ejecutar `npm install mysql2`
- Importar `const mysql = require("mysql2/promise");`
- Configurar la conexión servidor - bbdd

```javascript
async function getConnection() {
  const connection = await mysql.createConnection({
    // En workbench: click derecho -- edit connection
    host: "localhost",
    database: "nombre_de_la_bbdd",
    user: "root",
    password: "root",
  });
  await connection.connect();
  console.log(
    `Conexión establecida con la base de datos ${connection.threadId}`
  );
  return connection;
}
```

- Hacer una consulta

```javascript
server.get("/libros", async (req, res) => {
  try {
    // Conectarme a la bbdd
    const connection = await getConnection();
    // Hacer la consulta
    let sql = "SELECT * FROM libros";
    // Ejecutar la consulta
    const [results, fields] = await connection.query(sql);
    // Cierro la conexión
    connection.end();
    // Devolver el resultado a front
    if (results.length === 0) {
      res.status(404).json({
        status: "error",
        message: "No se encontraron estudiantes",
      });
    } else {
      res.status(200).json({
        status: "success",
        message: results,
      });
    }
  } catch (err) {
    console.log(err);
    res.status(500).json({
            status: "error",
            message: "Error en el servidor. Disculpe las molestias, inténtelo más tarde"
        })
});
```
