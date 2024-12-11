# My SQL y Express JS

Para conectar la bbdd con el servidor:

- Ejecutar `npm install mysql2`
- Importar `const mysql = require("mysql2/promise");`
- Configurar la conexión servidor - bbdd

```javascript
async function getConnection() {
  const connection = await mysql.createConnection({
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
  let sql = "SELECT * FROM libros";
  const connection = await getConnection();
  const [results, fields] = await connection.query(sql);
  res.status(200).json(results);
  connection.end();
});
```
