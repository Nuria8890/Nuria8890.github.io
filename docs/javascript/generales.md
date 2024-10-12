# *APUNTES DE JAVASCRIPT*

Poner un comentario: ctrl + /
Programar es pensar en los pasos para resolver un problema.

**Sentencia**: es la unidad mínima de código que expresa una acción u orden.

# Propiedades

`document.querySelector('.title').innerHTML = '¡Hola mundo!';` Permite cambiar el texto de un determinado elemento de HTML (el que tiene la clase 'title')

`classList` contiene varios métodos que nos permiten añadir (**classList.add**) o eliminar (**classList.remove**) una clase o comprobar si el elemento contiene una clase o no.

# Variables
**let**: se usa cuando el valor va a ir cambiando. Por ejemplo un contador, se iniciará en 0 y va a ir sumando a lo largo del tiempo.
```javascript
let contador
contador = contador + 1
```
**const**: se usa cuando el valor no va a cambiar.
```javascript
const pi = 3.14
```
# Operadores de comparación
- Compara si un valor es igual a otro.\
1 == 1 --> true. 1 es igual a 1, por tanto esta condición es verdadera.

- Compara si, tanto el valor como el tipo de dato, es extríctamente igual.\
2 === '2' --> false. number no es igual a string, por tanto esta condición es falsa.

- Compara si un valor es diferente a otro. Es una negación.\
3!='3' --> false. 3 es igual a 3, por tanto esta condición es falsa.

- Compara si, tanto el valor como el tipo de dato, es extrictamente diferente\
3!=='3' --> true. number no es igual a string, por tanto esta condición es verdadera.

const a = 10;\
const b = 20;\
const c = "10";

a == b; --> false\
a === c; --> false\
a == c; --> true\
a != b; --> true\
a !== c; --> true\
a > b; --> false\
a <= b; --> true\
a > c; --> false

# Operadores lógicos
a && b --> Si valor a **y** valor b se cumplen, entonces devuelve true.\
a || b --> Si valor a **o** valor b se cumplen, entonces devuelve true.\
! --> Negación. Lo que hace es cambiar true por false, y false por true. 

const a = 10;\
const b = 20;\
const c = "10";

a == b && a === c; --> false\
a == b || a == c; --> true\
a != b || a === c; --> true\
!(a === c) --> true

# Tipos de datos
## Primitivos
Son **inmutables** (no cambia el dato original), se pasan por **valor** (“copiar y pegar un archivo cambiándole el contenido”):

### String: cadenas de texto
_String literals_: lo que escribimos en consola entre comillas.\
_String values_: el propio valor de ese string, es decir, lo que nos devuelve la terminal.

1. **Creación** strings:

```javascript
const primeraOpcion = 'Comillas simples'
const segundaOpcion = "Comillas dobles"
const terceraOpcion = `Comillas ladeadas`
```

2. **Concatenación**: juntar un string con otro string:
- Utilizando el operador +:

```javascript
const direccion = 'Calle falsa 123'
const ciudad = 'Springfield'
const direccionCompleta = 'Mi dirección completa es ' + direccion + ' ' + ciudad
console.log(direccionCompleta)
```
- Utilizando Template Literals:

```javascript
const nombre = 'Nuria'
const pais = '🇪🇸'
const presentacion = `Hola, me llamo ${nombre}, y soy de ${pais}`
console.log(presentacion) 
```

- Utilizando .join():

```javascript
const primeraParte = 'Me encanta'
const segundaParte = 'la gente de '
const terceraParte = '🇨🇵'
const pensamiento = [primeraParte, segundaParte, terceraParte]
console.log(pensamiento.join(' '))
```

- Utilizando .concat():

```javascript
const hobbie1 = 'patinar'
const hobbie2 = 'puñetear'
const hobbie3 = 'escalar'
const hobbies = 'Mis hobbies son: '.concat(hobbie1, ', ', hobbie2, ' y ', hobbie3, '.')
console.log(hobbies)
```

3. Caracteres de **escape**:
- Escape alternativo:

```javascript
const escapeAlternativo = "I'm software engineer"
```

- Escape barra invertida:

```javascript
const escapeBarraInvertida = 'I\'m software engineer'
```

- Escape con template literals:

```javascript
const escapeComillaInvertida = `I'm software engineer`
```
\’ --> Comilla simple

\” --> Comilla doble

\\ --> Barra invertida

\n --> Línea nueva

\r --> Retorno de carro???

\t --> Tabulación

\b --> Retroceso

\f --> Salto de página


4. Strings **largos**:

```javascript
const poema1 = 'Poema 1\n' +
'Las rosas son rojas,\n' +
'las violetas son azules,\n' +
'caracter inesperado,\n' +
'en la línea 86.'

console.log(poema1)

const poema2 = 'Poema 2\n\
Las rosas son rojas,\n\
las violetas son azules,\n\
caracter inesperado,\n\
en la línea 86.'

console.log(poema2)

const poema3 = `Poema 3 
Las rosas son rojas,
las violetas son azules,
caracter inesperado,
en la línea 86.`

console.log(poema3)
```

5. **Métodos**:\
Más información sobre métodos aquí: [Arrays - Tipos de métodos](./javascript/arrays.md#tipos-de-métodos)

```javascript
const saludo = 'Hola ¿Cómo estás?'
console.log(saludo[2]) // l
console.log(saludo.charAt(2)) // l
console.log(saludo.indexOf('o')) // 1
console.log(saludo.indexOf('Cómo')) // 6
console.log(saludo.indexOf('como')) // -1
console.log(saludo.lastIndexOf('o')) // 9
console.log(saludo.slice(3, 7)) // a ¿C
console.log(saludo.length) // 17
console.log(saludo.toLocaleUpperCase()) // HOLA ¿CÓMO ESTÁS?
console.log(saludo.toLocaleLowerCase()) // hola ¿cómo estás?

const saludoDividido = saludo.split(' ')
console.log(saludoDividido) // [ 'Hola', '¿Cómo', 'estás?' ]


const saludoConEspacios = ' Hola Mundo '
const saludoSinEspacios = saludoConEspacios.trim()
console.log(saludoSinEspacios) // Hola Mundo


const saludoOriginal = 'Hola Mundo'
const nuevoSaludo = saludoOriginal.replace('Mundo', 'gente')
console.log(nuevoSaludo) // Hola gente
```

### Number: números
Entero y decimal:

```javascript
const entero = 42
const decimal = 3.14
console.log(typeof entero, typeof decimal) // number number
```

Notación científica:

```javascript
const cientifico = 5e3
```

Infinitos y NotANumber:

```javascript
const infinito = Infinity
const noEsUnNumero = NaN
```

1. Operaciones aritméticas:
- Suma, resta, multiplicación y división:

```javascript
const suma = 3 + 4
const resta = 4 - 3
const multiplicacion = 4 * 3
const division = 16 / 2
```

- Módulo y exponenciación:

```javascript
const modulo = 15 % 8 // Para saber si un número es múltiplo de otro
const exponenciacion = 2 ** 3 // Para saber la potencia
```

2. Operaciones avanzadas:
- Precisión: **.toFixed()**

```javascript
const resultado = 0.1 + 0.2
console.log(resultado) // Salen muchísimos decimales
console.log(resultado.toFixed(1)) // Indica cuántos decimales quiero que tenga el resultado
```

- Raiz cuadrada: **.Math.sqrt()**

```javascript
const raizCuadrada = Math.sqrt(16)
console.log(raizCuadrada) // 4
```

- Valor absoluto: **.Math.abs()**

```javascript
const valorAbsoluto = Math.abs(-7)
console.log(valorAbsoluto) // 7
```

- Número aleatorio: **.Math.random()**

```javascript
const aleatorio = Math.random()
console.log(aleatorio)
```

###	Boolean: verdadero o falso

```javascript
const isActive = true
const hasPermission = false
```

Conversión implícita: directamente, js, lo convierte en booleano:

```javascript
const result = 5 > 3
console.log(result) // true

const name = 'Platzi'
console.log(!!name) // true
```

Conversión explícita: lo convertimos nosotros:

```javascript
const value = 0
const explicitBoolean = Boolean(value)
console.log(explicitBoolean) // False

const otherValue = -24
const otherExplicitBoolean = Boolean(otherValue)
console.log(otherExplicitBoolean) // True
```

###	Null: valores nulos, no hay nada
Cuando un objeto en el código no existe, es un espacio vacío en memoria, que todavía no se le ha asignado ningún dato.

```javascript
const snoopy = null
console.log(snoopy) // null
console.log(typeof null) // objet
```

###	Undefined: indefinidos
Cuando no existe un valor asignado en memoria, es un valor indefinido

```javascript
let name
console.log(name) // Undefined: no se le ha asignado ningún valor
```

### Symbol: elementos únicos

```javascript
const uniqueId = Symbol('id')
const symbol1 = Symbol('1')
const symbol2 = Symbol('1')
console.log(symbol1 === symbol2) // False. Compara el valor y el tipo, no son iguales porque el id es único, así que aunque tengan el mismo valor, son diferentes...

const ID = Symbol('id')
let user = {}
user[ID] = '1234'
console.log(user) // { [Symbol(id)]: '1234' }
```

###	Bigint: números muy grandes

```javascript
const bigNumber = 23432434543579874986325764n
console.log(bigNumber) // 23432434543579874986325764n

const numberIfParticlesInTheUniverse = 100000000000000000n
console.log(numberIfParticlesInTheUniverse) // 100000000000000000n
```




## Complejos
Son **mutables** (cambia el valor original), se pasan por **referencia** (“crear un acceso directo y así, los cambios que haga en el nuevo archivo, son referenciados en el archivo original”).

###	Objet: objetos
[Apuntes de objetos](./javascript/objetos.md)

###	Array: listado de objetos
[Apuntes de arrays](./javascript/arrays.md)

[Ejercicios de arrays](./javascript/arrays_ejercicios.md)

###	Function: funciones
[Apuntes de funciones](./javascript/funciones.md)

# Type Casting y Coerción (conversión de tipos)
- **Lenguajes compilados**: el código se traduce ANTES de la ejecución del programa. C, C++, Rust, Go, Swift (Primero traduzco la receta al castellano y luego cocino). Chequeo *estático* de tipos.
- **Lenguajes interpretados**: se van traduciendo a medida que se va ejecutando el código. JavaScript, Python, ruby, PHP (Según voy cocinando, mi amigo francés me va diciendo en castellano qué tengo que ir haciendo) Chequeo *dinámico* de tipos.

## Explicity Type Casting
### parseInt()
Convierte la cadena de texto en un número entero.

```javascript
const string = '42'
const integer = parseInt(string)
console.log(integer) // 42
console.log(typeof integer) // number
```

### parseFloat()
Convierte la cadena de texto en un número flotante.

```javascript
const stringDecimal = '3.14'
const float = parseFloat(stringDecimal)
console.log(float)// 3.14
console.log(typeof float)// number
```

## Implicity Type Casting

```javascript
const sum = '5' + 3
console.log(sum) // 53

const sumWithBoolean = '3' + true
console.log(sumWithBoolean) // 3true

const sumWithNumber = 2 + true
console.log(sumWithNumber) // 3

const stringValue = '10'
const numberValue = 10
const booleanValue = true

// Si hay string CONCATENA, si no hay string SUMA
console.log(stringValue + stringValue) // 1010
console.log(stringValue + numberValue) // 1010
console.log(stringValue + booleanValue) // 10true
console.log(numberValue + stringValue) // 1010
console.log(numberValue + numberValue) // 20
console.log(numberValue + booleanValue) // 11
console.log(booleanValue + stringValue) // true10
console.log(booleanValue + numberValue) // 11
console.log(booleanValue + booleanValue) // 2
```
