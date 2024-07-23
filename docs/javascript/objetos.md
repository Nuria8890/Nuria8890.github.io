# Objetos
Los objetos son una estructura de datos que guardan valores de una forma particular (key: value)

## Métodos
Son funciones que están dentro del objeto que nos ayudan a generar interacción.

```javascript
const persona = {
nombre: 'John',
edad: 30,
direccion: {
calle: 'Av Insurgente 187',
ciudad: 'CDMX'
},
saludar() {
return `Hola, mi nombre es ${persona.nombre}`
}
};
console.log('Creo el objeto persona: ', persona);
/*
Creo el objeto persona: {
nombre: 'John',
edad: 30,
direccion: { calle: 'Av Insurgente 187', ciudad: 'CDMX' },
saludar: [Function: saludar]
}
*/

console.log('La función saludar dice: ', persona.saludar()); // La función saludar dice: Hola, mi nombre es John
```

### Añadir nueva propiedad

```javascript
persona.telefono = '555-555-5555';

console.log('Añado al objeto persona la propiedad teléfono: ', persona);
/*
Añado al objeto persona la propiedad teléfono: {
nombre: 'John',
edad: 30,
direccion: { calle: 'Av Insurgente 187', ciudad: 'CDMX' },
saludar: [Function: saludar],
telefono: '555-555-5555'
}
*/
```

### Añadir nuevo método al objeto

```javascript
persona.despedir = () => {
return 'Adiós, me voy'
};

console.log('La función despedir dice: ', persona.despedir()); // La función despedir dice: Adiós, me voy
```

## Enlace implícito o implicit binding
Ocurre cuando se invoca un método de un objeto y this se vincula al objeto que contiene el método.

```javascript
const house = { //objeto
  dogName: 'Firulais',
  dogGreeting: function () {// Función dentro del objeto
    console.log(`Hi, I'm ${this.dogName}`)//Con this accedo al objeto, y ya puedo acceder a la propiedades del objeto.
  } 
}
house.dogGreeting() // Llamo a la función que está dentro del objeto house
```

### Acceder a la propiedad de un objeto que está dentro de otro objeto

```javascript
console.log('La calle es: ', persona.direccion.calle); // La calle es: Av Insurgente 187
```

### Eliminar una propiedad o un método que ya existe

```javascript
delete persona.telefono;
console.log('He eliminado el teléfono: ', persona);
/*
He eliminado el teléfono: {
nombre: 'John',
edad: 30,
direccion: { calle: 'Av Insurgente 187', ciudad: 'CDMX' },
saludar: [Function: saludar],
despedir: [Function (anonymous)]
}
*/

delete persona.despedir;
console.log('He eliminado el método despedir: ', persona);
/*
He eliminado el método despedir: {
nombre: 'John',
edad: 30,
direccion: { calle: 'Av Insurgente 187', ciudad: 'CDMX' },
saludar: [Function: saludar]
}
*/
```

## Enlace explícito o explicit binding
Ocurre cuando se usan métodos como **call, apply o bind** para establecer explícitamente el valor de *this*.

```javascript
const newHouse = { // Objeto
  dogName: 'Coconut',
}
function dogGreeting () { // Función fuera del objeto
  console.log(`Hi, I'm ${this.dogName}`)
}
dogGreeting.call(newHouse) // Llamo a la función, y con .call vinculo esta función al objeto (newHouse) para poder acceder a sus propiedades


function newDogGreeting (owner, address) {
  console.log(`Hi, I'm ${this.dogName} and I live with ${owner} on ${address}`)
}
const owner = 'Lucy'
const address = 'Avenue 123'
newDogGreeting.call(newHouse, owner, address) // Puedo vincular una función con un objeto y a la vez mandarle diferentes parámetros
```
### Call

```javascript
const owner = 'Maca'
const address = '567 Avenue'

function dogGreeting (owner, address) {
  console.log(`Hi, I'm ${this.dogName}, and I live with ${owner} on ${address}`)
}

const newHouse = {
  dogName: 'Sheldom'
}

dogGreeting.call(newHouse, owner, address)
```
### Apply
Si tenemos muchos parámetros, lo mejor es usar apply, porque se añaden todos esos parámetros en a un array, y usamos el array como parámetro de la función.

```javascript
const necessaryValues = [owner, address]
dogGreeting.apply(newHouse, necessaryValues)
```

### Binds
Devuelve una función, y para poder ver el resultado tengo que ejecutar esa función.

```javascript
const bindingWithBind = dogGreeting.bind(newHouse, owner, address)
bindingWithBind()
```

## [Ejercicios](./javascript/objetos_ejercicios.md)