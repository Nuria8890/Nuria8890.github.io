# Funciones
**Expresión**: producen un valor y normalmente van acompañadas de una declaración. (1)\
**Declaración**: fragmentos de código que generan una instrucción que le damos al ordenador. (const numeroEntero = 1)

## 1. Funciones declarativas (o con nombre)
- Se definen con la palabra clave **function**.
- Pueden ser referenciadas antes de su declaración.

```javascript
function suma (a, b) {
  return a + b;
};
```

## 2. Funciones expresivas (o anónimas)
- Se asignan a variables.
- A menudo se utilizan para asignar funciones como valores a variables.

```javascript
const suma = function (a, b) {
  return a + b;
};
```

## 3. Funciones flecha (arrow functions)
- Proporcionan una sintaxis más concisa.
- Tienen un comportamiento ligeramente diferente con respecto al valor de *this*.

```javascript
const suma = (a, b) => a + b;
```
1. Función flecha con **retorno explícito**:

```javascript
const greeting = function (name) {
  return `Hi, ${name}`
}

const newGreeting = (name) => {
  return `Hi, ${name}`
}
```

2. Función flecha con **retorno implícito**:

```javascript
const greeting = function (name) {
  return `Hi, ${name}`
}

const newGreetingImplicit = name => `Hi, ${name}`
const newGreetingImplicitWithTwoParameters = (name, lastName) => `Hi, ${name} ${lastName}`
```

3. **Lexical Binding**: Ocurre cuando se utiliza *this* en una función dentro de otra función. En este caso, this se vincula al contexto léxico de la función exterior.

```javascript
const functionalCharacter = {
  name: 'Uncle Ben',
  messageWithTraditionalFunction: function (message) {
    console.log(`${this.name} says: ${message}`)
  },

  messageWithArrowFunction: message => { 
    console.log(`${this.name} says: ${message}`)
  }
}

functionalCharacter.messageWithTraditionalFunction('With reat power comes great responsability.')

functionalCharacter.messageWithArrowFunction('Beware of Doctor Octopus.')
```

## 4. Funciones constructoras
- Utilizadas para crear objetos con **new**.
- Utilizan **this** para asignar propiedades al nuevo objeto.

```javascript
function Persona(nombre, edad) {
	this.nombre = nombre;
	this.edad = edad;
}
const persona1 = new Persona('Juan', 25);
```

```javascript
const personalizedMessage = () => 'we are on fire'

function Rocket (name, ownMessage) {
  this.name = name
/*this.launchMessage = function (){
console.log(ownMessage)
}*/
  this.launchMessage = () => ownMessage
  this.launchMessage2 = ownMessage
}

const falcon9Rocket = new Rocket('Falcon9', 'Googdbye everybody')
console.log(falcon9Rocket.name) // Falcon9
console.log(falcon9Rocket.launchMessage()) // Googdbye everybody

const falconHeavyRocket = new Rocket('Falcon Heavy', personalizedMessage)
console.log(falconHeavyRocket.name) // Falcon Heavy
console.log(falconHeavyRocket.launchMessage2()) // we are on fire

const RocketWithArrowFunction = (name, ownMessage) => ({
  name: name,
  launchMessage: ownMessage
})

const personalizedMessageForArrowFunction = () => 'Successful launch !'
const falcon9Rocket1 = RocketWithArrowFunction('Falcon9-1', personalizedMessageForArrowFunction)

console.log(falcon9Rocket1.name) // Falcon9-1
console.log(falcon9Rocket1.launchMessage()) // Successful launch !
```

## 5. Funciones de orden superior (Higher-Order Functions)
- Aceptan funciones como argumentos o devuelven funciones.
- Ejemplos incluyen [map, filter, reduce.](./javascript/arrays.md#método-filter-y-reduce)

```javascript
function a () {}
function b (a) {}
b(a)



function f () {}
const obj = {}
f.call(obj)
```

## 6. Funciones recursivas
- Llamadas a sí mismas durante la ejecución.
- Útiles para problemas que se pueden dividir en subproblemas más pequeños.

```javascript
function factorial(n) {
	if (n === 0 || n === 1) {
		return 1;
	} else {
		return n * factorial(n – 1);
	}
}
```

## 7. Funciones anidadas (Nested Functions)
- Definidas dentro de otra función.
- Pueden acceder a las variables de la función contenedora (closure).

```javascript
function exterior() {
	let variableExterior = 'Exterior';
	function interior() {
		console.log(variableExterior);
	}
	interior();
}
exterior();


function g () {
  function h () {
    function i () {
    }
    i()
  }
  h()
}
g()
```

## 8. Métodos de objeto
- Funciones que son propiedades de objetos y se llaman métodos cuando se invocan en el contexto de ese objeto.

```javascript
const objeto = {
	metodo: function() {
		console.log('Hola desde el método');
	}
};
objeto.metodo();


const rocket = {
name: 'Falcon 9',
launchMessage: function launchMessage () {
console.log('on fire!!!')
}
}

rocket.launchMessage() // on fire!!!
```

## 9. Funciones asíncronas
- Utilizadas para manejar operaciones asíncronas con callbacks, Promesas o Async/Await. 

```javascript
async function fetchData() {
	const response = await fetch('<https://api.example.com/data>');
	const data = await response.json();
	console.log(data);
}
```

## 10. Funciones puras
- Siempre vamos a recibir la misma entrada y siempre vamos a obtener la misma salida, sin causar efectos secundarios observables.
- No dependen de, ni modifican estados externos.

```javascript
function suma(a, b) {
	return a + b;
}

function square(x) {
  return x * x
}

function addTen (y) {
  return y + 10
}

const number = 5
const finalResult = addTen(square(number)) // La combinación de dos funciones puras, sigue siendo una función pura
console.log(finalResult) // 35
```

## 11. Funciones impuras
- Aquellas que tienen efectos secundarios (side effects), es decir, al escribir el código de tal manera hace que nuestra función deje de ser pura.

1. Modificar variables globales: acceder a otras variables que tengamos en nuestro código dentro de una función.

```javascript
let total = 0
let e = 1

function sumWithSideEffect () { 
  total += e // total = total + e. La variable total es una variable global, y según vamos trabajando vamos a ir modificando esa variable global.
  return total
}
console.log('total = ' + total + ' + ' + e + ' --> ' + sumWithSideEffect()) // total = 0 + 1 --> 1
console.log('total = ' + total + ' + ' + e + ' --> ' + sumWithSideEffect()) // total = 1 + 1 --> 2
console.log('total = ' + total + ' + ' + e + ' --> ' + sumWithSideEffect()) // total = 2 + 1 --> 3
```

2. Modificar parámetros en una función.
3. Solicitudes HTTP.
4. Imprimir mensajes en la consola o pantalla (Al poner console.log() se convierte en impura).
5. Manipulación del DOM.
6. Acceder a la hora o día actual.