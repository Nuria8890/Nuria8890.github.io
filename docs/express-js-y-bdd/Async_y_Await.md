# Async/Await

El término asíncrono se refiere a una situación en la que dos o más eventos no ocurren al mismo tiempo. Es decir, que pueden suceder varias cosas relacionadas sin esperar a que se complete la acción anterior.

La palabra clave `async` se añade a las funciones para que devuelvan una promesa en lugar de un valor directamente; `await` hace que JavaScript espere hasta que la promesa responda y después devuelve su resultado.

```javascript
// Sintaxis función flecha
const cargarDatos = async () => {
  const res = await fetch("url");
  const data = await res.json();
  console.log(data);
  datosList = data;
};
cargarDatos();

// Sintaxis función normal
async function cargarDatos2() {
  const response = await fetch("url");
  const data = await response.json();
  console.log(data);
  datosList = data;
}
cargarDatos2();
```
