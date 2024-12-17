# Autenticación JWD

**Autenticación**: proceso de identificación de usuarios mediante la adquisición de credenciales como correo electrónico, contraseña y tokens... Si estas credenciales coinciden con los datos de la bbdd, la autenticación se completa y el usuario accede a los recursos.

**Autorización**: ocurre después de la autenticación.

**JWT o JSON Web Token**: es un estándar abierto (RFC 7519) que se utiliza para transferir información de forma segura entre dos partes. JWT está formado por tres partes:

- **Cabecera**: algoritmo utilizado para generar el token.

```javascript
{
 "alg": "HS256",
 "typ": "JWT"
}
```

- **Playload**: parte central de los JWT, son los datos del usuario que se pasan entre el cliente y el servidor.

```javascript
{
 "id":"920021",
 "name": "Krishna"
}
```

- **Firma**: es la clave secreta generada por el servidor. Para crear la firma se combinan la cabecera y el playload codificados en base-64.

```javascript
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjkyMDAyMSIsIm5hbWUiOiJLcmlzaG5hIn0
  .tvORZ0xRXmRhVB_sYnckoEN8HYe -
  q4YUlZJ -
  ZNaWBiM;
```

## Utilizar JWT:

Sirve para generar tokens

1. Ejecutar `npm install jsonwebtoken`
2. Importar jsonweboken en el archivo principal de Express.js `const jwt = require('jsonwebtoken');`
3. Generar y verificar tokens:

```javascript
const generateToken = (payload) => {
  const token = jwt.sign(payload, "secret_key", { expiresIn: "1h" });
  return token;
};

const verifyToken = (token) => {
  try {
    const decoded = jwt.verify(token, "secret_key");
    return decoded;
  } catch (err) {
    return null;
  }
};
```

4. Middleware de autenticación (lógica de intercambio de información entre aplicaciones):

```javascript
const authenticateToken = (req, res, next) => {
  const token = req.headers["authorization"];

  if (!token) {
    return res.status(401).json({ error: "Token no proporcionado" });
  }

  const decoded = verifyToken(token);

  if (!decoded) {
    return res.status(401).json({ error: "Token inválido" });
  }

  req.user = decoded;
  next();
};
```

5. Usar middleware: se aplica en las rutas que se quieren proteger.

```javascript
const app = express();

// Ruta protegida
server.get("/ruta-protegida", authenticateToken, (req, res) => {
  // Acceso autorizado, se puede acceder al objeto `req.user` que contiene los datos decodificados del token
  res.json({ message: "Acceso autorizado", user: req.user });
});
```

## Encriptar contraseña

1. Ejecutar `npm install bcrypt`
2. Importar bcrypt en el archivo principal de Express.js `const bcrypt = require("bcrypt");`
3. Utilizar el método `has()` para encriptar la contraseña y que se almacene en bbdd el has, en vez de la contraseña directamente.

```javascript
const passwordHash = await bcrypt.hash(body.password, saltRounds);
```

4. Crear un endpoint para crear nuevos usuarios.

```javascript
server.post("/api/signup", async (req, res) => {
  const username = req.body.username;
  const email = req.body.email;
  const password = req.body.password;
  const passwordHash = await bcrypt.hash(password, 10); //se utiliza para crear un hash seguro de la contraseña antes de almacenarla en la base de datos.
  //El 10 es el número de rondas de salting, que agrega seguridad al hash.

  //es la consulta SQL que insertará un nuevo usuario en la base de datos.
  let sql = "INSERT INTO users (username,email,hashed_password) VALUES (?,?,?)";

  //para crear un token de seguridad
  //La clave secreta usada para firmar el JWT ('secret_key') debería almacenarse de manera segura y no estar codificada directamente en el código fuente. Se recomienda usar variables de entorno para este propósito.

  jwt.sign(password, "secret_key", async (err, token) => {
    if (err) {
      res.status(400).send({ msg: "Error" });
    } else {
      const connection = await getConnection();
      const [results, fields] = await connection.query(sql, [
        username,
        email,
        passwordHash,
      ]);
      connection.end();
      //Si todo sale bien, se envía una respuesta JSON con un mensaje de éxito, el token JWT y el insertId,
      //que es el ID del usuario recién insertado en la base de datos.
      res.json({ msg: "success", token: token, id: results.insertId });
    }
  });
});
```

5. Crear la funcionalidad que permita a los usuarios iniciar sesión.

```javascript
server.post("/api/login", async (req, res) => {
  //recibe el cuerpo de la solicitud, que debería contener el nombre de usuario y la contraseña.
  const body = req.body;

  //Buscar si el usuario existe en bbdd
  const sql = "SELECT * FROM users WHERE username= ?";
  const connection = await getDBConnection();
  const [users] = await connection.query(sql, [body.username]);
  connection.end();

  const user = users[0];
  //Comprueba si el usuario existe y si la contraseña proporcionada es correcta utilizando bcrypt.compare.
  const passwordCorrect =
    user === undefined
      ? false
      : await bcrypt.compare(body.password, user.password);

  //Si el usuario no existe o la contraseña es incorrecta, responde con un estado 401 y un mensaje de error.
  if (!passwordCorrect) {
    return res.status(401).json({
      error: "Credenciales inválidas",
    });
  } else {
    //Si las credenciales son correctas, se prepara un objeto userForToken que incluye el username y el id del usuario.
    const userForToken = {
      username: user.username,
      id: user.id,
    };
    //Crear el token para enviar al front
    const token = generateToken(userForToken);

    //Finalmente, si todo es correcto, la función responde con un estado 200 y envía un objeto JSON con el token, el nombre de usuario y el nombre real del usuario.
    res.status(200).json({ token, username: user.username });
  }
});
```

## Frontend

## Backend

```javascript
// Endpoint de registro

server.post("/api/register", async (req, res) => {
  // 1. Recojo los datos que me envía frontend
  const username = req.body.username;
  const password = req.body.password;

  // Otra manera de recoger los parámetros, con destructuring:
  // const {username, password} = req.body;

  // 2. Encripto la contraseña
  const passwordHash = await bcrypt.hash(password, 10);
  // 3. Me conecto a la bbdd
  const connection = await getDBConnection();
  // 4. Añado los datos a la bbdd
  const sql = "INSERT INTO users (username, password) VALUES (?,?);";

  const [result] = await connection.query(sql, [username, passwordHash]);

  connection.end();

  res.status(201).json({ status: "succes", id: result.insertId });
});
```

```javascript
// Enpoint de autenticación (login) verificar que el username y la contraseña existen en mi bbdd

server.post("/api/login", async (req, res) => {
  //1. Recoger los datos que me envían de frontend
  const body = req.body;

  //2. Buscar si el usuario existe en bbdd
  const sql = "SELECT * FROM users WHERE username= ?";
  // 3. Me conecto a la bbdd
  const connection = await getDBConnection();
  //  4. Ejecuto la consulta
  const [users] = await connection.query(sql, [body.username]);

  // 5. Compruebo si la usuaria está registrada
  if (users.length > 0) {
    // Comprueblo si la contraseña que me envía fronted coincide con la que tengo encriptada en bdd
    const isSamePassword = await bcrypt.compare(
      body.password,
      users[0].pasword
    );
    // Si la contraseña es la misma, genero un token y se lo envío a frontend
    if (isSamePassword) {
      // En el token guardo el email y el id
      const infoToken = {
        id: users[0].id,
        username: users[0].username,
      };
      const token = generateToken(infoToken);
      res.status(200).json({
        status: "succes",
        token: token,
      });
    } else {
      res.status(400).json({
        status: "error",
        message: "Contraseña incorrecta",
      });
    }
  } else {
    res.status(400).json({
      status: "error",
      message: "Usuario no registrado",
    });
  }

  //  Finalizo la conexión
  connection.end();
});

function generateToken(tokenData) {
  /*
  parámetros:
  - datos que quiero guardar en el token
  - clave secreta
  - caducidad del token
  */

  const token = jwt.sign(tokenData, secretKey, { expiresIn: "1h" });
  return token;
}
```

# Autorización JWT

El token que nos devuelve backen en el endpoint de /`login` lo almacenamos en la aplicación cliente para saber si ese usuario está logado o no.

Para verificar si el token llega de frontend a backend, utilizamos la función middleware `authenticateToken` añadiéndola como parámetro entre los puntos finales de la API y la función de devolución de llamada:

## Front

```javascript
let api_token = "";

fetch("http://localhost:4000/api/login", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(bodyParams),
})
  .then((response) => response.json())
  .then((responseData) => {
    console.log("Server response:", responseData);
    api_token = responseData.token;
  });

fetch("http://localhost:4000/articles", {
  method: "GET",
  headers: {
    "Content-Type": "application/json",
    authorization: api_token,
  },
})
  .then((response) => response.json())
  .then((responseData) => {
    console.log("Server response:", responseData);
  });
```

## Back

```javascript
const authenticateToken = (req, res, next) => {
  const token = req.headers["authorization"];

  if (!token) {
    return res.status(401).json({ error: "Token no proporcionado" });
  } else {
    const decoded = verifyToken(token);

    if (!decoded) {
      return res.status(401).json({ error: "Token inválido" });
    } else {
      req.user = decoded;
      next();
    }
  }
};

const authenticateTokenSINELSE = (req, res, next) => {
  const token = req.headers["authorization"];

  if (!token) {
    return res.status(401).json({ error: "Token no proporcionado" });
  }

  const decoded = verifyToken(token);

  if (!decoded) {
    return res.status(401).json({ error: "Token inválido" });
  }

  req.user = decoded;
  next();
};

// El usuario solo pordrá acceder a la sección de artículos si se ha registrado y logado previamente

server.get("/articles", authenticateToken, async (req, res) => {
  let sql = "SELECT * FROM articles WHERE email = ?";

  const connection = await getDBConnection();
  const [articles] = await connection.query(sql, [req.user.email]);
  connection.end();
  const response = {
    articles: articles,
  };
  res.json(response);
});
```
