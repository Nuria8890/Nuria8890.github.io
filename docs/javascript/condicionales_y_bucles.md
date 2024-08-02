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
for (variable; condición; incremento) {\
  código a ejecutar\
}

Una vez que se evalúe la condición se ejecuta el código, después la variable se incrementa. Se inicia una segunda vuelta y la variable vale más (porque se ha incrementado antes), vuelve a evaluar la condición, ejecuta el código e incrementa la variable... así sucesivamente hasta que la condición se evalúe y sea false, entonces el código deja de ejecutarse.

1. Evalúa la condición teniendo en cuenta la variable inicial // true
2. Ejecuta el código
3. Incrementa el valor de la variable


4. Evalúa la condición teniendo en cuenta la variable incrementada en el bucle anterior// true
5. Ejecuta el código
6. Incrementa el valor de la variable


7. Evalúa la condición teniendo en cuenta la variable incrementada en el bucle anterior // false
8. Fin



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

## Bucle forEach()
[otro ejemplo de .forEach()](./javascript/arrays.md#método-map-y-foreach)\
array.forEach((item)=> {\
  código a ejecutar\
})

Ejecuta el código por cada uno de los elementos (items) que hay en mi array.

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

## Bucle forOf()
for (variable of objeto) {\
  código a ejecutar\
}

Se usa en objetos iterables como arrays o strings (porque son una lista de algo).

```javascript
let canasta = ["manzana", "pera", "naranja", "uva"]

for (fruta of canasta) {
  console.log(fruta);
// manzana
// pera
// naranja
// uva
}
```

## Bucle forIn()
for (variable in objeto) {\
  código a ejecutar\
}

Se usa en objetos enumerables.
Los objetos tienen propiedades, y las propiedades tienen un valor.

```javascript
const listaDeCompras = {
  manzana: 5,
  peras: 3,
  naranjas: 2,
  uvas: 1
}

for (fruta in listaDeCompras) {
  console.log(fruta);
// manzana
// peras
// naranjas
// uvas
}

for (fruta in listaDeCompras) {
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