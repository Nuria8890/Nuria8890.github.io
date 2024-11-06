# Peticiones al servidor

**API** (Application Programming Interface) programa que está escrito en backend, que expone cierta información para que frontend pueda acceder a esa información.

**Linter** sirve para prevenir errores y ayuda a mantener un estilo homogéneo en el código.

**Asincronía** se espera a que ocurran determinadoes eventos para ejecutar una parte del código, es decir, nos permite ejecutar operaciones en segundo plano. Le decimos a js qué hacer, pero no sabemos cuándo se va a ejecutar ese código (ej: un evento es un código asíncrono).

**AJAX** (Asynchronous JavaScript And XML) es el puente entre el cliente (navegador) y el servidor, entre el frontend y el backend de nuestra aplicación. Las peticiones AJAX nos permiten **acceder y manipular datos en el servidor**, pero **iniciando el proceso en el frontend**.

**Método GET**: se usa para decir al sevidor que esa petición es para consultar datos que él ya tiene.

**Método POST**: se usa para enviar nosotros datos al servidor.

**Método PUT**: actualiza un recurso, y si no existe ese recurso lo va a crear.

**Método DELETE**: elimina un recurso.

## fetch

Me permite hacer una petición de forma asíncrona. Sirve para comunicarnos con el servidor, tanto para enviar datos (de un formulario) como para solicitar datos. Y me devuelve una promesa (objeto que representa la finalización de una operación asíncrona)

```javascript
const div = document.querySelector(".js-randomNumber");

const button = document.querySelector(".js-getRandomNumber");

function randomNumber() {
  fetch("https://api.rand.fun/number/integer?min=0&max=100")
    .then((response) => {
      // response es la respuesta
      return response.json(); // lo paso a json() porque esta respuesta me da da en bites y no lo entendemos
    })
    .then((data) => {
      // recibimos los datos con los que vamos a trabajar
      console.log(data); // hay que ver qué tipo de dato nos devuelve para poder saber cómo pintarlo luego en html o hacer lo que quiera con él...
      div.innerHTML = data.result;
    });
}

button.addEventListener("click", randomNumber);
```

## JSON

Son como objetos con estas diferencias:

- Las claves siempre van entre comillas `{"userName": "Paco"}`

- No se pueden almacenar funciones, por lo que los JSON nunca tendrán métodos.

```JSON
{
"status": "success",
"message": "https://dog.ceo/api/img/terrier-australian/n02096294_4492.jpg"
}
```

## Petición al servidor

```javascript
const input = document.querySelector(".js-input");
const button = document.querySelector(".js-button");

const getUser = (event) => {
  event.preventDefault();

  const nameSearch = input.value;

  fetch(`https://api.github.com/users/${nameSearch}`)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const name = document.querySelector(".js-name");
      const repos = document.querySelector(".js-repos");
      const img = document.querySelector(".js-img");

      name.innerHTML = data.login;
      repos.innerHTML = data.public_repos;
      img.src = data.avatar_url;
      img.alt = data.login;
    });
};

button.addEventListener("click", getUser);
```

## Petición en paralelo al servidor

Para trabajar con varias promesas en paralelo usamos el método `Promise.all` que toma como parámetro un array de promesas y devuelve otra promesa que se resuelve cuando todas las del array se han resuelto. Por tanto, sobre el resultado podremos hacer un `then()` que recibe como parámetro un array con todos los resultados de las promesas anteriores, es decir, donde tendremos todos los JSON de la respuesta del servidor.

```javascript
const btn = document.querySelector(".js-btn");
const div = document.querySelector(".dogs");

const createPromise = () =>
  fetch("https://dog.ceo/api/breeds/image/random").then((response) =>
    response.json()
  );

function getBreedImages() {
  const promises = [];
  for (let i = 0; i < 10; i++) {
    promises.push(createPromise());
  }
  console.log(promises);

  Promise.all(promises).then((responses) => {
    for (let i = 0; i < responses.length; i++) {
      const img = document.querySelector(".dog" + (i + 1));

      div.innerHTML += `
        <img class="${img}" src="${responses[i].message}" alt="Dog" />
      `;
    }
  });
}

btn.addEventListener("click", getBreedImages);
```

## Respuestas del servidor:

- 200: todo OK.
- 400: errores.
- 500: error en servidor.

## LocalStorage

Nos permite guardar datos en el propio navegador del usuario. Por ejemplo, podemos guardar un listado que hemos pedido a un API y que utilizamos mucho, así la próxima vez, comprobamos primero el caché, y si ya está almacenada esa información, nos ahorramos hacer una petición al servidor, y así conseguimos que la página vaya más rápida.

- localStorage.**setItem**('key', 'value'): añade un elemento con una clave y un valor al almacenamiento local.

- localStorage.**getItem**('key'): recupera el valor de la clave especificada en el almacenamiento local.

- localStorage.**removeItem**('key'): elimina el elemento del almacenamiento local según la clave especificada.

- localStorage.**clear()**: elimina todo el almacenamiento local.

Local Storage solo puede guardar strings, números y booleanos, así que cada vez que queramos guardar algo en localStorage hay que utilizar la siguiente función:

- JSON.**stringify**(): convierte arrays u objetos en strings.

Si queremos leer lo que hemos guardado en Local Storage utilizamos la siguiente función:

- JSON.**parse**(): convierte un string en array u objeto.

```javascript
const defaultTodos = [
  { text: "Cortar cebolla", completed: true },
  { text: "Curso React.js", completed: false },
  { text: "Saltar a la comba", completed: false },
  { text: "Piscina", completed: true },
];

console.log(defaultTodos);
/*
0
: 
{text: 'Cortar cebolla', completed: true}
1
: 
{text: 'Curso React.js', completed: false}
2
: 
{text: 'Saltar a la comba', completed: false}
3
: 
{text: 'Piscina', completed: true}
*/

//  1. Convierto mi array en cadena de texto y lo guardo en una constante
const stringifyedTodos = JSON.stringify(defaultTodos);

console.log(stringifyedTodos); // [{"text":"Cortar cebolla","completed":true},{"text":"Curso React.js","completed":false},{"text":"Saltar a la comba","completed":false},{"text":"Piscina","completed":true}]

// 2. Guardo esa constante en localStorage
localStorage.setItem("defaultTodos", stringifyedTodos);

// 3. Recupero el valor guardado en localStorage y lo guardo en una constante
const getTodos = localStorage.getItem("defaultTodos");

console.log(getTodos); // [{"text":"Cortar cebolla","completed":true},{"text":"Curso React.js","completed":false},{"text":"Saltar a la comba","completed":false},{"text":"Piscina","completed":true}]

// 4. Convierto el valor recuperado en un array y lo guardo en una constante
const parseTodos = JSON.parse(getTodos);

console.log(parseTodos);
/*
0
: 
{text: 'Cortar cebolla', completed: true}
1
: 
{text: 'Curso React.js', completed: false}
2
: 
{text: 'Saltar a la comba', completed: false}
3
: 
{text: 'Piscina', completed: true}
*/
```

## Asincronía y temporizadores

**Asincronía**: capacidad de realizar operaciones sin tener que esperar a que se ejecute el código completo.

- **setInterval**: permite ejecutar una función cada x milisegundos. Se cancela con **clearInterval**

- **setTimeout**: permite ejecutar una función pasados x milisegundos. Se cancela con **clearTimeout**
