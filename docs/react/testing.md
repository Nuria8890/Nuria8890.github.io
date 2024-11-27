# Testing

- **Tests unitarios**: prueban un trozo o pieza de código que solo hace una cosa (unidad), por ejemplo, una función.

- **Tests de regresión**: son un tipo de test que comprueba que las nuevas funcionalidades desarrolladas no rompen las funcionalidades anteriores.

- **Tests de integración**: prueban que varias piezas de código funcionan bien juntas, que se integran bien las unas con las otras. Por ejemplo, una función que llama a otras funciones o un componente que le pasa props a otro componente. Podemos juntar tantas piezas como queramos hasta llegar a la aplicación completa.

- **Tests de aceptación o end-to-end**: también llamados **e2e**, son un tipo especial de tests de integración que están relacionados con los criterios de aceptación definidos por el cliente, es decir, que prueban algo que tiene valor a nivel de negocio y suele ser una funcionalidad completa. Por ejemplo, que un usuario pueda crear una nueva tarea en nuestra aplicación de gestión de tareas.

## Tests unitarios

Los escribimos en ficheros especiales JS. Cuando finalizamos una tarea de programación ejecutamos los test parra comprobar si funcionan o no, para ello, ejecutamos `npm test`.

Los test unitarios deben ser FIRST: Fast, Isolated, Repeatable, Self verifying, Timely.

- **First / Rápidos**: los tests unitarios deben ejecutarse muy rápido. Por ejemplo, cientos de tests en menos de un segundo.

- **Isolated / Aislados**: los tests unitarios deben probar una funcionalidad aislada de nuestra aplicación, es decir, una porción de código. Por ejemplo, un componente, sin hacer uso de otros componentes hijos ni externos (DOM, API, etc).

- **Repeatable / Repetibles**: cuando repito un test con las mismas condiciones el resultado debe ser el mismo. Por ejemplo, es complicado hacer tests de cosas no predecibles como números aleatorios o cuando alguna condición depende del tiempo. Pero una función que calcula la raíz cuadrada de un número siempre debería devolver el mismo retorno cuando se ejecuta con los mismos argumentos.

- **Self verifying / Automatizados**: los test unitarios se deben poder comprobar sin intervención humana. Por ejemplo, no debe haber una persona revisando logs manualmente sino que debe ser un proceso totalmente automático.

- **Timely / Hechos a tiempo**: deberíamos hacer estos tests antes de que sucedan los errores, no como consecuencia de ellos. Y según el TDD deben ser hechos antes incluso que el código.

Los test tienen tres pasos: AAA (Arrange (preparación (renderizar el componente)), Act (acción (la acción que quieremos probar)), Assert (aserción (comprobar si el restultado de la acción es el esperado)))

```javascript
// Con este título describimos lo que hace el test
test("add function returns 3 when inputs are 1 and 2", () => {
  // Arrange: especificamos qué datos vamos a usar en el test
  const numberA = 1;
  const numberB = 2;

  // Act: ejecuta la función que se va a probar
  const result = add(numberA, numberB);

  // Assert: compruebo que el resultado devuelto por la función es lo que yo espero
  expect(result).toBe(3);
});
```

### Librerías de testing:

- **Jest**: https://jestjs.io/es-ES/

Para configurar esta librería:

1. Ejecutar:

```
npm install --save-dev jest babel-jest @babel/preset-env @babel/preset-react react-test-renderer
npm install --save-dev @testing-library/react
npm install jest-environment-jsdom --save-dev
```

2. Crear un archivo de configuración de Babel `babel.config.cjs` que contenga:

```
module.exports = {
  presets: [
    "@babel/preset-env",
    ["@babel/preset-react", { runtime: "automatic" }],
  ],
};
```

3. En el fichero `package.json` escribir:

```
 "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint . --ext js,jsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview",
    "test": "jest",
    "test:watch": "jest --watch"
  },
 "jest": {
    "testEnvironment": "jsdom"
  },
```

4. Crear un carpeta `test` dentro de `src` para crear archivos de prueba (por ejemplo: App.test.js)

- Para hacer un test de un botón, saber si ese botón, que es super importante, existe:
  1. Importar el componente a testear
  2. Importar lo necesario para renderizar el componente, por ejemplo el navegador
  3. Escribir el test agrupándolos en `describe()`, recibe siempre dos parámetros:
  - string (descripción de mi suite de tests)
  - función. Dentro de esta función metemos la función `test()`, que recibe dos parámetros también, un string y una función.

```
import App form "../components/App";
import {render, screen, fireEvent} from "@testing-library/react";

describe("App component", ()=>{
  test("renders button CTA correctly", ()=>{
    <!-- preparación -->
    render(<App />)

    <!-- actuación -->
    const button = screen.getAllByText("Soliciar información");
  <!-- getAllByText me devuelve un array con todos los elementos que tienen ese texto -->

    <!-- aserción -->
    expect(button.length).tobe(1);
  <!-- aquí estoy comprobando si la constante button tiene de longitud 1 (solo quiero que exita un botón con ese texto) -->

  })

})
```

```
describe("Counter component", ()=>{
  test("renders button CTA correctly", ()=>{

    render(<Counter />)


    const incrementButton = screen.getByText("Incrementar");
    fireEvent.click(incrementButton);
    const countText = screen.getAllByText("Contador: 1");

    expectcountText.length).tobe(1);

  })
})
```

5. Ejecutar `npm test` para ejecutar un test normal, o `npm run test:watch` para ejecutar pruebas en modo de observación, así cuando los archivos cambien se vuelven a ejecutar las pruebas automáticamente. Si quiero que solo me ejecute el text en el que estoy trabajando justo ahora tengo que ejecutar `npm test --testPathPattern=Nombre-de-mi-archivo.test.js`

- **React Testing library**: https://testing-library.com/
