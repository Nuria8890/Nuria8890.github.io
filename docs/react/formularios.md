# Formularios en React

## Input de tipo text, number, email...

- Guardamos el value seleccionado en nuestra variable de estado. `setEmail(ev.target.value)` esto lo haré dentro de una función manejadora.
- En la propiedad value, guardo el valor de mi variable de estado. `value={email}`

## Input de tipo select

- Se escucha el evento en el propio select, no en las option.
- Guardamos el value seleccionado en nuestra variable de estado. `setRegion(ev.target.value)` esto lo haré dentro de una función manejadora.
- En la propiedad value, guardo el valor de mi variable de estado. `value={region}`

## Input de tipo checkbox

- Cuando marcamos o desmarcamos no cambia el value, sino que cambia la propiedad `checked`, por lo que es el estado de esta propiedad (marcada o desmarcada, true o false) lo que tengo que guardar en mi variable de estado: `const [acceptsConditions, setAcceptsContitions] = useState("false")`
- Y en la propia propiedad checked tengo que guardar el valor de mi variable de estado `checked={acceptsConditions}` para controlar este input.

## Input de tipo radio

- Igual que en checkbox, cuando marcamos un valor, lo que cambia es la propiedad `checked`.
- En mi variable de estado tengo que guardar el valor de value. `setPaymentType(ev.target.value)` esto lo haré dentro de una función manejadora.
- En mi propiedad checked tengo que igualar la variable de estado al valor de value. `checked={paymentType === "cash"}`.

## Input de tipo file

- Utilizamos `useRef` para guardar el archivo.

## Botón de enviar

- hay que usar event.preventDefault()

## Evento onChange

- SIEMPRE se usa este evento en los formularios porque los formularios se pueden manejar con el ratón (click), pero también con el teclado (keyUp, keyDown...), y el evento que SIEMPRE ocurre es el cambio (onChange).
