# 1. Suma los elementos de un array.

```javascript
const numbersArray = [1, 2, 3, 4, 5];
let sum = 0;

for (let i = 0; i < numbersArray.length; i++) {
sum += numbersArray[i]; // recorre el array y va sumando sus elementos.
}
console.log(sum); // 15 --> 1+2+3+4+5=15
```

# 2. .map()
Convierte grados fahrenheit en celsius usando la siguiente fórmula: C = 5/9 * (F-32):

```javascript
const gradosFahrenheit = [32, 68, 95, 104];

let gradosCelsius = gradosFahrenheit.map(grado => 5/9 * (grado-32));
console.log('La temperatura en grados celsius es: ' + gradosCelsius); // La temperatura en grados celsius es: 0,20,35,40
```

# 3. .forEach(). Suma los elementos de un array:
Crea un programa que coja los números de un array y calcula la suma de todos los elementos de ese array.

```javascript
const numeros = [2, 4, 6, 8, 10];
let sumaDeNumeros = 0;

numeros.forEach(numero => {
  sumaDeNumeros = sumaDeNumeros + numero // sumaDeNumeros += numero
});
console.log('La suma de los números es: ' + sumaDeNumeros); // La suma de los números es: 30
```

# 4. .filter() y .reduce()
Crea un programa donde haya un array con calificaciones. Calcula el promedio de las calificaciones que son aprobatorias (mayores o iguales a 70).

```javascript
const calificaciones = [50, 68, 75, 89, 43, 90, 70, 78, 39, 90, 78, 87, 50, 90, 68];

let calificacionesAprobatorias = calificaciones.filter(nota => nota >= 70);
console.log('Las calificaciones aprobatorias son: ', calificacionesAprobatorias); // 75,89,90,70,78,90,78,87,90

let promedioCalificaciones = calificacionesAprobatorias.reduce((suma, nota) => suma + nota, 0) / calificacionesAprobatorias.length;

console.log('El promedio de las calificaciones aprobatorias es: ' + promedioCalificaciones); // 83
```

# 5. .find() 
Crea un programa para verificar si hay alguna persona ganadora en la lista. Ingresa el número del ticket o el nombre de la persona para verificar si existe ganador, y muéstralo.

```javascript
const participantes = [
  {id: 1, name: 'Jennifer', ticketNumber: 100},
  {id: 8, name: 'Michael', ticketNumber: 800},
  {id: 15, name: 'Emily', ticketNumber: 150},
  {id: 47, name: 'Charlie', ticketNumber: 470}
];

function encontrarNombreGanador (nombre) {
  let nombreGanador = participantes.find(persona => persona.name === nombre);
  if(nombreGanador === undefined){
  console.log('En la lista no existe ese nombre. Lo sentimos, no hay ganador');
  } else {
    console.log('El ganador es: ' + nombreGanador.name); // Michael
  };
};
encontrarNombreGanador('Michael');

function encontrarTicketGanador (ticket) {
  let ticketGanador = participantes.find(numero => numero.ticketNumber === ticket);
  if(ticketGanador === undefined){
    console.log('En la lista no existe ese número de ticket. Lo sentimos, no hay ganador');
  } else {
    console.log('El ganador es: ' + ticketGanador.name); // Emily
  };
};
encontrarTicketGanador(150);
```

La profesora lo hace así:

```javascript
const winningParticipants = [
  {id: 1, name: 'Jennifer', ticketNumber: 100},
  {id:8, name: 'Michael', ticketNumber: 800},
  {id: 15, name: 'Emily', ticketNumber: 150},
  {id: 47, name: 'Charlie', ticketNumber: 470}
];

function findWinnerByName (name) {
  const winner = winningParticipants.find(participants => participants.name === name);
  return winner || 'No winner found with that name.';
};

function findIndexWinnerByTicket (ticketNumber) {
  const index = winningParticipants.findIndex(participants => participants.ticketNumber === ticketNumber);
  return index !== -1 ? index : 'No winner found with that ticket number.'
};

function displayWinnerInformation (winner) {
  if(winner !== undefined && winner !== null && winner !== 'No winner found with that ticket number.'){
    console.log('Winner information: ', winner);
  } else {
    console.log('No winner found');
  };
};

const winnerByName = findWinnerByName('Emily'); // { id: 15, name: 'Emily', ticketNumber: 150 }
const indexWinnerByTicket = findIndexWinnerByTicket(470); // 3

displayWinnerInformation(winnerByName);
console.log('Index of winner by ticket number: ', indexWinnerByTicket);
```

# 6. .reduce(), .filter(), .find(), .findIndex() y .forEach() 
1. Crea una lista de transaciones financieras para realizar varias operaciones con ella:

```javascript
const transacciones = [
  {
    id: 1,
    descripcion: 'Mercadona',
    total: -67,
  },
  {
    id: 2,
    descripcion: 'Nómina',
    total: 1500,
  },
  {
    id: 3,
    descripcion: 'Alquiler',
    total: -500,
  },
  {
    id: 4,
    descripcion: 'Compra on line',
    total: -250,
  },
  {
    id: 5,
    descripcion: 'Devolución compra',
    total: 36,
  }
];
```
1. Calcula el saldo total utilizando .reduce():

```javascript
function calculaSaldoTotal(){
  const saldoTotal = transacciones.reduce((acumulador, importe) => acumulador + importe.total, 0);
  return saldoTotal;
};
calculaSaldoTotal()
console.log('El saldo total es: ', calculaSaldoTotal()); // El saldo total es: 719
```

La profesora lo hace así:

```javascript
const totalBalance = transacciones.reduce((acc, transaction) => acc + transaction.total, 0);
console.log('TotalBalance: ', totalBalance); // TotalBalance: 719
```

2. Encuentra la transacción más elevada utilizando el método .reduce(), ya sea, ese importe, un ingreso o un gasto:

```javascript
function encuentraTransaccionMasElevada(){
  const transaccionMasElevada = transacciones.reduce((importeGuardado, importe) => {
    if (Math.abs(importeGuardado.total) > Math.abs(importe.total)){
      return importeGuardado;
    } else {
      return importe;
    }
  }, 0);
  return transaccionMasElevada;
};

encuentraTransaccionMasElevada()
console.log('La transacción más elevada es: ', encuentraTransaccionMasElevada()); //La transacción más elevada es: { id: 2, descripcion: 'Nómina', total: 1500 }
```

La profesora lo hace así:

```javascript
const largestTransaction = transacciones.reduce((maxTransaction, transaction) => {
  return Math.abs(transaction.total) > Math.abs(maxTransaction.total) ? transaction : maxTransaction
}, transacciones[0]);
console.log('Largest transaction: ', largestTransaction); // Largest transaction: { id: 2, descripcion: 'Nómina', total: 1500 }
```

3. Utiliza el método .filter() para obtener las transaciones efectuadas por compra.

```javascript
let transaccionesPorCompra = transacciones.filter(importe => importe.total < 0);
console.log('Las transacciones efectuadas por compras son: ', transaccionesPorCompra);
/*
Las transacciones efectuadas por compras son: [
  { id: 1, descripcion: 'Mercadona', total: -67 },
  { id: 3, descripcion: 'Alquiler', total: -500 },
  { id: 4, descripcion: 'Compra on line', total: -250 }
]
*/
```

4. Ecuentra una transacción por descripción utilizando el método .find():

```javascript
function encuentraTransaccionPorDescripcion(descripcion){
  return transaccionPorDescripcion = transacciones.find(movimiento => movimiento.descripcion === descripcion);
};
encuentraTransaccionPorDescripcion('Compra on line');
console.log('La transacción descrita es: ', encuentraTransaccionPorDescripcion('Compra on line')); // La transacción descrita es: { id: 4, descripcion: 'Compra on line', total: -250 }
```

La profesora lo hace así:

```javascript
const specificTransaction = transacciones.find(transaction => transaction.descripcion === 'Compra on line');
console.log('Specific Transaction: ', specificTransaction); // Specific Transaction: { id: 4, descripcion: 'Compra on line', total: -250 }
```

5. Encuentra el índice de una transacción por importe utilizando .findIndex():

```javascript
let IndiceDeTransaccionPorImporte = transacciones.findIndex(movimiento => movimiento.total === -250);
console.log('El índice por importe -250 es: ', IndiceDeTransaccionPorImporte); // El índice por importe -250 es: 3
```

6. Actualiza las descripciones de las transaciones utilizando .forEach().

```javascript
transacciones.forEach(movimiento => {
  if (movimiento.total < 0) {
    movimiento.descripcion = `Gasto: ${movimiento.descripcion}`;
  } else {
    movimiento.descripcion = `Ingreso: ${movimiento.descripcion}`;
  }
});
console.log('Transacciones actualizadas: ', transacciones);
// Transacciones actualizadas: [
// { id: 1, descripcion: 'Gasto: Mercadona', total: -67 },
// { id: 2, descripcion: 'Ingreso: Nómina', total: 1500 },
// { id: 3, descripcion: 'Gasto: Alquiler', total: -500 },
// { id: 4, descripcion: 'Gasto: Compra on line', total: -250 },
// { id: 5, descripcion: 'Ingreso: Devolución compra', total: 36 }
// ]
```

# 7. .includes(), .indexOf(), .lastIndexOf()
Dado un array de string y un string suelto, escribe una función que determine si el string suelto está presente en el array. De ser así, devuelve el índice de la primera posición y el índice de la última posición; si no está presente, devuelve -1.

```javascript
const stringArray = ['apple', 'banana', 'orange', 'grape', 'banana', 'kiwi'];
const target = 'banana';

function encuentraElIndiceEnElArray(stringArray, target){
  if (stringArray.includes(target)){
    const firstIndex = stringArray.indexOf(target);
    const lastIndex = stringArray.lastIndexOf(target);
    return {
      primerIndice: firstIndex,
      ultimoIndice: lastIndex
    }
  }
  return {
    primerIndice: -1,
    ultimoIndice: -1
  };
};

console.log('Los índices son: ', encuentraElIndiceEnElArray(stringArray, target)); // Los índices son: { primerIndice: 1, ultimoIndice: 4 }
```

Otra chica lo hace así:

```javascript
const pokemones = ['pikachu', 'pikachu', 'charmander', 'bulbasaur', 'squirtle','charmander', 'cyndaquil', 'charmander', 'magikarp', 'raichu']

const targets = 'charmander'

function findMyPokemonIndex (pokemones, targets){
  return {
    targetInArray: pokemones.includes(targets),
    firstOcurrence: pokemones.indexOf(targets),
    lastOcurrence: pokemones.lastIndexOf(targets)
  }
}
console.log(findMyPokemonIndex(pokemones, targets)) // { targetInArray: true, firstOcurrence: 2, lastOcurrence: 7 }
```

# 8. Examen de entrevista

Está teniendo lugar un torneo algorítmico en el que equipos de programadores compiten entre sí para resolver problemas algorítmicos lo más rápido posible. Los equipos compiten en un formato de todos contra todos, donde cada equipo se enfrenta a todos los demás. Solo dos equipos compiten entre sí en cada enfrentamiento, y en cada competición, un equipo es designado como equipo local, mientras que el otro es el equipo visitante.

Siempre hay un claro ganador y perdedor en cada competición, sin empates. Los equipos obtienen 3 puntos por una victoria y 0 puntos por una derrota. El ganador general del torneo es el equipo con la mayor cantidad de puntos.

Tu tarea es escribir una función que determine al ganador del torneo en función de los resultados de las competiciones. La entrada consta de dos arrays: competitions y results. El array competitions contiene pares de equipos representados como [equipoLocal, equipoVisitante], donde cada equipo es una cadena de hasta 30 caracteres. El array results indica el ganador de cada competición correspondiente en el array competitions. Específicamente, results[i] denota el ganador de competitions[i], donde un 1 en el array results significa que el equipo local ganó y un 0 significa que el equipo visitante ganó.

Se garantiza que exactamente un equipo ganará el torneo, y cada equipo competirá contra todos los demás equipos exactamente una vez. Además, se garantiza que el torneo siempre tendrá al menos dos equipos.

```javascript
const competitions = [
  ['JavaScript', 'C#'],
  ['C#', 'Python'],
  ['Python', 'JavaScript']
];

const results = [0, 0, 1];

var puntuaciones = {
  'JavaScript': 0,
  'C#': 0,
  'Python': 0
};

for(let i = 0; i < competitions.length; i++){ // Hay que hacer un for porque hay que ir revisando todos los datos uno por uno.
  const equipoLocal = competitions [i][0];
  const equipoVisitante = competitions [i][1];

  const equipoGanador = results[i] === 1 ? equipoLocal : equipoVisitante; // Si el valor de results en la posición i es 1, el ganador es el equipo local, sino, es el equipo visitante.

  if(puntuaciones.hasOwnProperty(equipoGanador)){ // Si dentro de puntuaciones está el equipo ganador, devuelve true y entonces ejecuta el código.
    puntuaciones[equipoGanador] = puntuaciones[equipoGanador] + 3;
  }
};
console.log(puntuaciones);

var puntuacionGanador = 0;
var nombreGanador = '';

for (const equipo in puntuaciones) { // Compruebo qué puntuación es mayor
  if(puntuaciones[equipo] - puntuacionGanador > 0){
    puntuacionGanador = puntuaciones[equipo]
    nombreGanador = equipo;
  }
};
console.log('Ganador: ', nombreGanador);
```

La profesora lo hace así:

```javascript
function tournamentWinner(competitions, results) {
  const scores = {}
  let winner = ''

  for (let i = 0; i < competitions.length; i++) {
    const [home, away] = competitions[i]
    const winningTeam = results[i] === 0 ? away : home

    scores[winningTeam] = (scores[winningTeam] || 0) + 3

    if(!winner || scores[winningTeam]> scores[winner]) {
      winner = winningTeam
    }
  }
return winner
}

console.log('El ganador con el ejercicio de la profe es: ', tournamentWinner(competitions, results))
```