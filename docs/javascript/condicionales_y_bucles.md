# Condicionales y bucles
## Condicional if
if (condición) {\
  código a ejecutar\
} else if (condición) {\
  código a ejecutar\
} else {\
  código a ejecutar\
}

```javascript
let nombre = "Ana";

if(nombre == "Nuria") {
  console.log("Hola Nuria");
} else if (nombre === "Ana") {
  console.log ("Hola Ana");
} else {
  console.log("Nombre no encontrado");
};
```

## Condición ternaria
Solo se usa cuando:
- queremos guardar un valor en una variable.
- queremos hacer una operación o sentencia dentro del ? y del : (si queremos hacer más cosas, usamos if - else).
- queremos hacer una operación dentro del ? y otra dentro del : (si no queremos hacer nada en el :, es decir el else, no podemos usar un operador ternario).


condición ? true : false

Este sería un if normal:

```javascript
let mensaje;

const edad = 15;

if (edad >= 18) {
  mensaje = "Es mayor de edad";
} else {
  mensaje = "No es mayor de edad";
};

console.log(mensaje); // No es mayor de edad
```

Este sería un if con condición ternaria:
```javascript
const edad2 = 20;
const mensaje2 = edad2 >= 18 ? "Yeah! Es mayor de edad" : "Oooh, no es mayor de edad"

console.log(mensaje2) // Yeah! Es mayor de edad
```

## Ejecución condicional switch
switch (expresión) {\
  case valor1:\
    código a ejecutar\
  break;\
  case valor2:\
    código a ejecutar\
  break;\
  case valor3:\
    código a ejecutar\
  break;\
.\
.\
.\
  default:\
    código a ejecutar\
}

```javascript
let expresion = "Uvas"

switch(expresion) { // ===
  case "Najanjas":
    console.log("Las naranjas valen $20/kg")
  break;
  case "Manzanas":
    console.log("Las manzanas valen $43/kg")
  break;
  case "Plátanos":
    console.log("Los plátanos valen $30/kg")
  break;
  case "Mangos":
  case "Papayas":
    console.log("Los mangos y las papallas valen $25/kg")
  break;
  
  default:
    console.log(`Lo siento, no tenemos ${expresion}`)
}
console.log("¿Hay algo más que desees?")
```

## Bucle for()

```javascript
/*
for (variable; condición; incremento) {
  código a ejecutar
}
*/

for (let i = 0; i < 2; i++) {
  console.log("Voy por la vuelta ", i);
}
```

1. Revisa la variable inicial (let i = 0)
2. Evalúa la condición (i < 2) // true
3. Ejecuta el código (Voy por la vuelta 0)
4. Incrementa el valor de la variable (i++)


5. Revisa la variable que ha incrementado en el bucle anterior (let i = 1)
6. Evalúa la condición (i < 2)// true
7. Ejecuta el código (Voy por la vuelta 1)
8. Incrementa el valor de la variable (i++)


9. Revisa la variable que ha incrementado en el bucle anterior (let i = 2)
10. Evalúa la condición (i < 2) // false
11. Fin


Ejemplo 1: recorre la lista y píntala en consola:

```javascript
let list = ["eat", "sleep", "code", "repeat"];

for (let i = 0; i < list.length; i++) {
console.log(list[i]);
// eat
// sleep
// code
// repeat
}
```

Ejemplo 2:

```javascript
const coches = ["rojo", "azul", "rojo"];

function compruebaSiLosCochesSonDelColor(color) {
  
  let colorDelCoche = true;
  
  for (let i = 0; i < coches.length; i++) {
    if (coches[i] === color) {
      console.log("coche del mismo color");
    } else {
      console.log("coche distinto color");
      colorDelCoche = false;
    }
  }

  return colorDelCoche;
}

console.log(compruebaSiLosCochesSonDelColor("rojo"));  // false
```

Ejemplo 3:

```javascript
const scores = [4, 2, 7, 8, 6, 7, 9, 1, 2, 6, 7];

// Creamos una variable fuera del bucle para que no se sobrescriba en cada iteración
// En esta variable iremos sumando cada una de las puntuaciones
let acc = 0;

// La i empieza en 0 porque el índice de los arrays empieza en 0 también
for (let i = 0; i < scores.length; i++) {
  acc += scores[i];
  // Sumamos a `acc` el valor actual del array en cada iteración del bucle
  // acc += arr[i] es igual a acc = acc + arr[i]
}

console.log("La puntuación final es " + acc); // 59
```

## Bucle forOf()
Permite recorrer un objeto iterable, como son los arrays, sin tener que escribir las condiciones de un for. Además, nos permite usar nombres mucho más reconocibles para los valores dentro del array.
ForOf solo nos permite leer los datos, ya que no nos da información sobre el índice, por lo que no podemos modificar los valores del array.

```
for (variable of objeto) {\
  código a ejecutar\
}
```

Se usa en objetos iterables como arrays o strings (porque son una lista de algo).

```javascript
let list = ["eat", "sleep", "code", "repeat"]

for (let fruta of canasta) {
  console.log(fruta);
// eat
// sleep
// code
// repeat
}
```

## Bucle forEach()
[otro ejemplo de .forEach()](./javascript/arrays.md#método-map-y-foreach)

Ejecuta el código por cada uno de los elementos (items) que hay en mi array.

```
array.forEach((item)=> {
  código a ejecutar
})
```


```javascript
let list = ["eat", "sleep", "code", "repeat"]

list.forEach((item) => {
  console.log(item);
// eat
// sleep
// code
// repeat
})
```

## Bucle forIn()

```
for (variable in objeto) {
  código a ejecutar
}
```

Se usa en objetos enumerables.
Los objetos tienen propiedades, y las propiedades tienen un valor.

```javascript
const listaDeCompras = {
  manzana: 5,
  peras: 3,
  naranjas: 2,
  uvas: 1
}

for (let fruta in listaDeCompras) {
  console.log(fruta);
// manzana
// peras
// naranjas
// uvas
}

for (let fruta in listaDeCompras) {
  console.log(`${fruta}: ${listaDeCompras[fruta]}`)
// manzana: 5
// peras: 3
// naranjas: 2
// uvas: 1
}
```

## Bucle while()
while(condición) {\
  código a ejecutar\
}

Siempre que la condición sea verdad, se repite el bucle:

1. Evalúa la condición // true
2. Ejecuta el código


3. Evalúa la condición // true
4. Ejecuta el código


5. Evalúa la condición // false
6. Fin

```javascript
let contador = 0;

while (contador < 10) {
  console.log(contador);
// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
  contador++;
}
```

## Bucle do{} while()
do {\
  código a ejecutar\
} while (condición)

Se repite el bucle, y luego evalúa si la condición es verdad:

1. Ejecuta el código
2. Evalúa la condición // true


3. Ejecuta el código
4. Evalúa la condición // true


5. Ejecuta el código
6. Evalúa la condición // false
7. Fin

```javascript
let contador = 0;

do {
  console.log(contador);
// 0
// 1
// 2
// 3
// 4
// 5
// 6
// 7
// 8
// 9
  contador++;
} while (contador < 10);
```