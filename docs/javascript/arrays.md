# Arrays

Array: conjunto de elementos que se crean dentro de una variable. Es un objeto, por lo que puede tener diferentes métodos y, dependiendo del método, puede ser mutable o inmutable.

## ¿Cómo crear un array?

1. new Array() o Array()

```javascript
const fruits = Array("apple", "bannana", "orange");
console.log(fruits); // [ 'apple', 'bannana', 'orange' ]

const justOneNumber = Array(12);
console.log(justOneNumber); // [ <12 empty items> ]

const numbers = Array(1, 2, 3, 4, 5);
console.log(numbers); // [ 1, 2, 3, 4, 5 ]
```

2. Sintaxis literal del array

```javascript
const oneNumber = [4];
console.log(oneNumber); // [ 4 ]

const emptyArray = [];
console.log(emptyArray); // [] Sirve por ejemplo para cuando queremos inicializar algún programa.

const sports = ["soccer", "tennis", "rugby"];
console.log(sports); // [ 'soccer', 'tennis', 'rugby' ]

const recipeIngredients = [
  "Flour",
  true,
  2,
  {
    ingredient: "Milk",
    quantity: "1 cup",
  },
  false,
];
console.log(recipeIngredients); // [ 'Flour', true, 2, { ingredient: 'Milk', quantity: '1 cup' }, false ]
```

## ¿Cómo acceder a los elementos de un array?

array[índice]

```javascript
const fruits = ["apple", "bannana", "orange"];
const firstFruit = fruits[0];
console.log(firstFruit); // apple
```

## ¿Cómo saber el tamaño de un array?

.length

```javascript
const fruits = ["apple", "bannana", "orange"];
const numberOfFruits = fruits.length;
console.log(numberOfFruits); // 3
```

## Tipos de métodos

Otros métodos [aquí](./javascript/generales.md#string-cadenas-de-texto)

### MÉTODOS MUTABLES

Son aquellos que modifican el array original

#### Método .push(), .pop() y .unshift()

```javascript
var countries = ["USA", "Canada", "UK"];
```

.push(): **añade** uno o más elementos **al final** de un array y devuelve la nueva longitud del array.

```javascript
var newCountries = countries.push("Germany", "Australia");
console.log(countries); //[ 'USA', 'Canada', 'UK', 'Germany', 'Australia' ]
console.log(newCountries); // 5
```

.pop(): **elimina el último** elemento de un array y devuelve ese elemento eliminado.

```javascript
var removedCountry = countries.pop();
console.log(countries); // [ 'USA', 'Canada', 'UK', 'Germany' ]
console.log(removedCountry); // Australia
```

.unshift(): **añade** uno o más elementos **al inicio** de un array.

#### Método .shift() y .unshift()

```javascript
var colors = ["yellow", "blue", "red"];
```

.shift(): **elimina el primer** elemento de un array, y nos devuelve ese elemento que hemos eliminado.

```javascript
var removedColors = colors.shift();
console.log(colors); // [ 'blue', 'red' ]
console.log(removedColors); // yellow
```

.unshift(): **añade** uno o más elementos **al principio** del array, y nos devuelve el tamaño en el que queda el array.

```javascript
var newColors = colors.unshift("pink", "purple");
console.log(colors); // [ 'pink', 'purple', 'blue', 'red' ]
console.log(newColors); // 4
```

#### Método .splice(), .reverse(), .sort() y .fill()

.splice(): cambia el contenido de un array **eliminando** elementos existentes **y/o agregando** nuevos elementos.

_.splice(posición inicial, cuántos elementos quiero cambiar a partir de la posición inicial incluida, elemento/s que quiero añadir en su lugar)_

```javascript
var vegetables = ["carrot", "broccoli", "spinach", "tomato"];
var removeVegetables = vegetables.splice(2, 1, "cucumber", "onion"); // Desde la posición 2(incluida), elimina 1 elemento y, en su lugar, añade cucumber, onion.
console.log(vegetables); // [ 'carrot', 'broccoli', 'cucumber', 'onion', 'tomato' ]
```

.reverse(): **invierte el orden** de los elementos de un array. El primer elemento pasa a ser el último y el último pasa a ser el primero.

```javascript
var numbers = [1, 2, 3, 4, 5];
var reverseNumbers = numbers.reverse();
console.log(numbers); // [ 5, 4, 3, 2, 1 ]
```

.sort(): **ordena** los elementos de un array localmente y devuelve el array ordenado.

- Si es un array de números: los convierte en string y los ordena **de menor a mayor**.

```javascript
var unsortedNumbers1 = [4, 18, 1, 62, 34];
var sortedNumbers1 = unsortedNumbers1.sort();
console.log(unsortedNumbers1); // [ 1, 18, 34, 4, 62 ]

var unsortedNumbers2 = [4, 18, 1, 62, 34];
var sortedNumbers2 = unsortedNumbers2.sort((a, b) => a - b);
/*
4 - 18 = -14 // 4 es menor que 18, no hace nada 
18 - 1 = 17 // 18 es mayor que 1, cambia la posición --> [4, 1, 18, 62, 34]
18 - 62 = -44 // 18 es menor que 62, no hace nada
62 - 34 = 28 // 62 es mayor que 34, cambia la posición --> [4, 1, 18, 34, 62]
4 - 1 = 3 // 4 es mayor que 1, cambia la posición --> [1, 4, 18, 34, 62]
4 - 18 = -14 // 4 es menor que 18, no hace nada
18 - 34 = -16 // 18 es menor que 34, no hace nada
34 - 62 = -28 // 34 es menor que 62, no hace nada. El array está ordenado de menor a mayor número.
*/
console.log(sortedNumbers2); // [ 1, 4, 18, 34, 62 ]
```

- Si es un array de strings: UTF-16, es decir, lo ordena **alfabéticamente**.

```javascript
var cities = ["New York", "Paris", "Tokio", "London"];
var sortedCities = cities.sort();
console.log(cities); // [ 'London', 'New York', 'Paris', 'Tokio' ]
```

.fill(): **sustituye** los elementos en un array **por un valor** estático, desde el índice start (por defecto 0) hasta el índice end (por defecto array.lenght).

```javascript
var ages = [21, 35, 45, 50];
var agesEmogi = ages.fill("😎", 1, 3); // Llena con emogi, desde la posición 1 (incluida) hasta la posición anterior a la 3.
console.log(ages); // [ 21, '😎', '😎', 50 ]
```

### MÉTODOS INMUTABLES

Son aquellos que NO modifican el array original, pero sí iteran con él.

#### Método .map() y .forEach()

.map(): **devuelve un nuevo array**, siempre de la misma longitud que el original, con el resultado de aplicar una función a cada elemento del array original. El único argumento que recibe la función map es una función.

Se utiliza para transformar los elementos de un array.

```javascript
const names = ["María", "Lucía", "Susana", "Rocío", "Inmaculada"];
const capitalNames = names.map((name) => name.toUpperCase());

console.log(capitalNames); // ["MARÍA","LUCÍA","SUSANA","ROCÍO","INMACULADA"]

//Es igual que hacer esto:

const names = ["María", "Lucía", "Susana", "Rocío", "Inmaculada"];
const getUperCaseName = (name) => name.toUpperCase();
const capitalNames = names.map(getUperCaseName);

console.log(capitalNames); // ["MARÍA","LUCÍA","SUSANA","ROCÍO","INMACULADA"]
```

Ejemplo diferenciando map con un bucle for

```javascript
const users = [
  {
    name: "Lucía",
    age: 67,
  },
  {
    name: "Blanca",
    age: 43,
  },
];

// Con bucle for:
const sentences = [];

for (const user of users) {
  const text = `${user.name} tiene ${user.age} años`;

  sentences.push(text);
}

console.log(sentences); // [Lucía tiene 67 años], [Blanca tiene 43 años]

// con .map()

const sentencesUsers = users.map((user) => {
  return `${user.name} tiene ${user.age} años`;
});

/* Lo de arriba es IGUAL que esto:
const sentencesUsers = users.map((user) => `${user.name} tiene ${user.age} años`)
*/

console.log(sentencesUsers); // [Lucía tiene 67 años], [Blanca tiene 43 años]
```

```javascript
const numbers = [1, 2, 3, 4, 5];
var squaredNumbers = numbers.map((num) => num * 2); // Multiplica cada elemento por 2
console.log(squaredNumbers); // [ 2, 4, 6, 8, 10 ]

const coloresDeEquipo = ["rojo", "verde", "azul"];
var buscaElNombreDelEquipo = coloresDeEquipo.map((color) => {
  console.log(color);
  // Hago una función para localizar el nombre de cada equipo
  return "nombre del equipo de cada color";
});
console.log(buscaElNombreDelEquipo);
/*
rojo
verde
azul
['nombre del equipo de cada color', 'nombre del equipo de cada color', 'nombre del equipo de cada color']
*/
```

.forEach(): ejecuta una función sobre cada elemento del array, **sin crear un nuevo array**.\
[otro ejemplo de .forEach()](./javascript/condicionales_y_bucles.md#bucle-foreach)

```javascript
const colors = ["red", "pink", "blue"];
let iteratedColors = colors.forEach((color) => console.log(color));
/*
red
pink
blue
*/
console.log(iteratedColors); // undefined
```

#### Método .filter() y .reduce()

.filter(): **crea un nuevo array** con los elementos del array original que cumplen una condición dada por una función.

Se utiliza para buscar _todos_ los elementos de un array que cumplan una condición.

```javascript
const names = ["María", "Lucía", "Susana", "Rocío", "Inmaculada"];
const longNames = names.filter((name) => name.length > 5);

/*Es lo mismo que hacer esto:
const longNames = names.filter((name) => {
  return name.length > 5;
});
*/

console.log(longNames); // ["Susana","Inmaculada"]
```

```javascript
const numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let numerosPares = numeros.filter((numero) => numero % 2 === 0); // Devolverá los números pares. Por ejemplo, si tenemos 4 % 2, el resultado es 0 (4/2 = 2 y el resto es 0). Si tenemos 5 % 2, el resultado sería 1 (5/2 = 2 con un resto de 1).
console.log("El array números es: " + numeros); // El array numeros es: 1,2,3,4,5,6,7,8,9,10

console.log("Los números pares son: " + numerosPares); // Los números pares son: 2,4,6,8,10
```

.reduce(): ejecuta una función reductora sobre cada elemento de un array, **devolviendo** como resultado **un único valor**.

```javascript
const numeros = [1, 2, 3, 4, 5];
const sum = numeros.reduce(
  (accumulator, currentValue) => accumulator + currentValue,
  0
); // accumulator: acumula el valor de la suma de cada uno de los datos. currentValue: cada uno de los valores del array.
console.log("El array de números es: " + numeros); // El array de números es: 1,2,3,4,5
console.log("El array de la suma es: " + sum); // El array de la suma es: 15

const palabras = ["apple", "banana", "hello", "bye", "banana", "bye", "bye"];
let frecuenciaDePalabras = palabras.reduce((accumulator, currentValue) => {
  if (accumulator[currentValue]) {
    accumulator[currentValue]++;
  } else {
    accumulator[currentValue] = 1;
  }
  return accumulator;
}, []);
console.log(frecuenciaDePalabras); // [ apple: 1, banana: 2, hello: 1, bye: 3 ]
```

#### Método .find() y .findIndex()

.find(): **devuelve el _valor_ del primer elemento** del array que cumple la condición proporcionada.

Se utiliza para buscar un elemento en un array.

```javascript
const multiplosDe5 = [5, 10, 15, 20];
const primerNumeroMayorQue10 = multiplosDe5.find((numero) => numero > 10);
console.log(primerNumeroMayorQue10); // 15
```

.findIndex(): **devuelve el _índice_ del primer elemento** del array que cumple la condición proporcionada en forma de función. Si no encuentra ningún elemento que cumpla la condición, devuelve -1.

Se utiliza para buscar un elemento en un array.

```javascript
const numerosAleatorios = [6, 14, 27, 56, 40];
const indiceDelNumero = numerosAleatorios.findIndex((numero) => numero < 50);
console.log(indiceDelNumero); // 0 (el número 6)
```

#### Método .concat(), Spread Operator, .join()

Estos métodos sirven para unir y entrelazar los elementos de dos o más arrays.

```javascript
const primeraParte = ["H", "O"];
const segundaParte = ["L", "A"];
```

.concat(): **une dos o más arrays** devolviendo un único array.

```javascript
// Forma nº1:
const palabraCompleta1 = primeraParte.concat(segundaParte);
console.log(palabraCompleta1); // ['H','O','L','A']

//Forma nº2:
const palabraCompleta2 = [].concat(primeraParte, segundaParte);
console.log(palabraCompleta2); // ['H','O','L','A']
```

Para hacer una copia de un array:

```javascript
const animals = ["perro", "caballo", "vaca"];
const animalsCopy = animals.concat();
```

Spread Operator:

```javascript
//Ejemplo 1
function palabraCompleta3(array1, array2) {
  console.log([array1, array2]); // ['H','O','L','A']
}
palabraCompleta3(primeraParte, segundaParte);

//Ejemplo 2
const numeros = [1, 2, 3];
const string = "palabra";
palabraCompleta3(numeros, string);
/*
[
1,2,3,'p'
'a','l','a','b',
'r','a'
]
*/
```

.join(): **junta todos los elementos** de un array y nos devuelve un solo valor

```javascript
const palabraCompletaString = palabraCompleta1.join("");
console.log(palabraCompletaString); // HOLA
```

#### Método .split()

**Separa todos los elementos** de un array y nos devuelve un array con la palabra dividida.

```javascript
const palabra = "abeja";
const palabraSeparada = palabra.split("");
console.log(palabraSeparada); // ['a', 'b', 'e', 'j', 'a']
```

#### Método .every() y .some()

```javascript
const edades = [21, 25, 31, 19, 22];
```

.every(): determina si **todos** los elementos de un array cumplen la condición dada.

```javascript
const sonTodosAdultos = edades.every((edad) => edad > 18);
console.log(sonTodosAdultos); // true
```

.some(): determina si, **al menos un elemento** cumple la condición dada.

```javascript
const algunoEsMayorDe30 = edades.some((edad) => edad > 30);
console.log(algunoEsMayorDe30); // true
```

#### Método .includes(), .indexOf y .lastIndexOf()

.includes(): determina si un determinado elemento está incluido en un array.

```javascript
const numeros = [1, 2, 3, 4, 5];

const resultado1 = numeros.includes(3);
console.log(resultado1); //true

const resultado2 = numeros.includes(8);
console.log(resultado2); //false
```

.indexOf(): **devuelve el primer índice** en el que se puede encontrar un elemento dado en el array, **o devuelve-1** si el elemento no está. NO FUNCIONA con arrays de objetos.º

```javascript
const frutas = ["manzana", "uvas", "cereza", "mango", "cereza"];

const index1 = frutas.indexOf("cereza");
console.log(index1); // 2

const index2 = frutas.indexOf("pera");
console.log(index2); // -1
```

.lastIndexOf(): **devuelve el último índice** en el que se puede encontrar un elemento dado en el array, **o devuelve -1** si el elemento no está.

```javascript
const frutas = ["manzana", "uvas", "cereza", "mango", "cereza"];

const index3 = frutas.lastIndexOf("cereza");
console.log(index3); // 4

const index4 = frutas.lastIndexOf("pera");
console.log(index4); // -1
```

#### Método .slice()

.slice(): crea una **copia** superficial (shallow copy) de una porción **del array**, especificada por índices de **inicio (incluido) y fin (no incluido)**.

_.slice(posición inicial, posición final NO incluida)_

```javascript
const animales = ["ant", "bison", "camel", "duck", "elephant"];

const unParametro = animales.slice(2); // del índice 2 (incluido) en adelante.
console.log("Utilizando solo un parámetro (2): ", unParametro); // [ 'camel', 'duck', 'elephant' ]

const dosParametros = animales.slice(2, 4); // del indice 2(incluido) hasta el 4(sin incluir), es decir, hasta el 4-1
console.log("Utilizando dos parámetros (2, 4): ", dosParametros); // [ 'camel', 'duck' ]

const dosUltimos = animales.slice(-2); // cuenta desde el final del array
console.log("Utilizando valores negativos(-2): ", dosUltimos); // [ 'duck', 'elephant' ]

const unParametroPositvioYUnoNegativo = animales.slice(1, -2); // del indice 1(incluido) hasta el -2(sin incluir), es decir, hasta el -2-1
console.log(
  "Utilizando un parámetro positivo y otro negativo (1, -2): ",
  unParametroPositvioYUnoNegativo
); // [ 'bison', 'camel' ]
```

#### Spread Operator

Sirve para:

1. Copiar arrays

```javascript
const originalArray = [1, 2, 3, 4, 5];

const copyOfArray = [...originalArray];
console.log(copyOfArray); // [1, 2, 3, 4, 5]
```

2. Combinar arrays

```javascript
const array1 = [1, 2, 3];
const array2 = [4, 5, 6];

const combinerArray = [...array1, ...array2];
console.log(combinerArray); // [ 1, 2, 3, 4, 5, 6 ]
```

3. Crear arrays con elementos adicionales

```javascript
const baseArray = [1, 2, 3];

const arrayConElementosAdicionales = [...baseArray, 4, 5, 6];
console.log(arrayConElementosAdicionales); // [ 1, 2, 3, 4, 5, 6 ]
```

4. Pasar parámetros a una función

```javascript
function sum(a, b, c) {
  return a + b + c;
}

const numbers = [1, 2, 3];

const resut = sum(...numbers);
console.log(resut); // 6
```

## Arrays Bidimensionales

Array unidimensional. En este caso tiene 3 columnas y 1 fila.

```javascript
let array1D = [1, 2, 3];
```

Array Bidimensional. En este caso tiene 3 columnas y 4 filas.

```javascript
let array2D = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12],
];
```

También se pueden escribir de la siguiente manera:

```javascript
let matriz = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [10, 11, 12],
];
```

Para **cambiar un valor** a la matriz, hay que indicar en qué fila y qué columna está el valor que queremos modificar:

```javascript
matriz[1][2] = 10; // Cambiamos el 6 (que se encuentra en la fila 1, columna 2) por un 10
console.log(matriz); // [ [ 1, 2, 3 ], [ 4, 5, 10 ], [ 7, 8, 9 ], [10, 11, 12] ]
```

Para saber cuál es el valor situado en una posición:

```javascript
let value = matriz[0][1];
console.log("El valor colocado en la fila 0 columna 1 es: ", value); // 2
```

### Operaciones más comunes

1. **Recorrer** un array bidimensional:

```javascript
for (let i = 0, i < matriz.length; i++){ // Entra en las filas {[F0], [F1] [F2], [F3]}
  for (let j = 0; j < matriz[i].length; j++) { // Entra en las columnas {[C0, C1, C2], [C0, C1, C2], [C0, C1, C2], [C0, C1, C2]}
    console.log ('Array recorrido: ', matriz[i][j]);
  }
}
```

2. **Buscar** elementos específicos en un array bidimensional:

```javascript
function findElement(array, elemento) {
  for (let i = 0; i < array.length; i++) {
    for (let j = 0; j < array[i].length; j++) {
      if (array[i][j] === elemento) {
        return true;
      }
    }
  }
  return false;
}

const elementoABujcar = 5;

let varFindElement = findElement(matriz, elementoABujcar);
console.log(
  "¿En el array ",
  matriz,
  " existe el número ",
  elementoABujcar,
  "?: ",
  varFindElement
); // true
```

3. **Duplicar** los valores de una matriz:

```javascript
function duplicateMatriz(array) {
  let newMatriz = [];
  for (let i = 0; i < array.length; i++) {
    newMatriz[i] = [...array[i]];
  }
  return newMatriz;
}

console.log("El valor de la nueva matriz es: ", duplicateMatriz(matriz));
```

## [Ejercicios](./javascript/arrays_ejercicios.md)
