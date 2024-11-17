# Eventos y Estados en React

Los **eventos** en React se declaran con on, seguido del tipo de evento seguido de la función manejadora sin paréntesis y entre llaves:

`onClick={handleClick}`

`onKeyUp={handleInput}`

`onChange={handleInput}`

La _función manejadora_:

Tiene que estar _declarada dentro de la función App_.

Todo lo demás funciona exactamente igual que en JS.

```
// Fichero src/components/App.jsx
const App = () => {
  const handleButton = (ev) => {
    console.log("El botón ha sido pulsado");
    console.log("El evento lanzado es: ", ev);
  };

  return (
    <div>
      <button onClick={handleButton}>Púlsame</button>
    </div>
  );
};

export default App;
```

**Estado**: es un objeto que representa el conjunto de datos que pueden cambiar con el tiempo. Se maneja con `useState`

```
// Fichero src/components/App.jsx
import {useState} from 'react';

function App() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');

  return (
    <div>
      El nombre de la usuaria es {name} y su email es {email}.
    </div>
  );
}

export default App;
```

Para crear una **constante de estado** y que React renderice el componente cada vez que este dato cambie tenemos que:

1. Importar useState en las primeras líneas del fichero con `import { useState } from 'react'`.

2. Crear la constante, la función para modificar esta constante y asignar el valor inicial con `const [name, setName] = useState('')`;

3. La función modificadora tiene que empezar siempre por `setLoQueSea`.

4. Podemos usar y pintar la constante del estado donde queramos.

5. Para modificar la constante tenemos que usar la función manejadora con `setName('Mi nuevo valor')`.
