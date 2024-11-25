# Router

Para trabajar con rutas en React tenemos que instalar y configurar React Router DOM:

1. Instalamos la librería en el proyecto: `npm install react-router-dom`.
2. Añadimos `"homepage": "./"` al package.json.
3. Importampos en src/main.js `import { HashRouter } from "react-router-dom";`
4. Añadimos este código al src/main.js:

```
<HashRouter>
  <App />
</HashRouter>
```

Para mostrar u ocultar un contenido en función de la ruta debemos usar el componente:

```
<Routes>
  <Route to="/ruta" element={contenido_que_se_quiere_mostrar} />
</Routes>
```

Para crear los links debemos usar los componentes `<Link>` ó `<NavLink>`.

El componente `Route` muestra o no un contenido en función de la ruta actual.
si tenemos varios `Route` y solo queremos ejecutar uno de ellos, metemos todos los `Route` dentro de un `Routes`, así solo renderizará el que corresponda con el `path`.

## Ruta estática

Rutas que no cambian, que son fijas:

- /: inicio
- /contact: página de contacto
- /products: catálogo de productos

## Ruta dinámica

Rutas que cambian, es decir, una ruta dinámica es una única ruta con la que podemos gestionar todas las rutas que cumplan un patrón.

- /product/43823: Página del detalle del producto con id 43823, que es un iPhone.
- /product/345565: Página del detalle del producto con id 345565, que es un Nokia.
- /product/9745: Página del detalle del producto con id 9745, que es un Xiaomi.

Estas tres rutas, en el fondo, son la misma página, pero su contenido cambia.

Para gestionar rutas dinámicas tenemos que expresar una ruta con un patrón. La parte variable del patrón la expresamos con dos puntos :. Y para obtener los parámetros de la ruta dinámica tenemos dos opciones, useLocation o useParams

### useLocation

Obtenemos la ruta actual del navegador y luego la comparamos con una ruta dada.

Devuelve un objeto de ubicación que representa la URL actual.

`import { useLocation, matchPath } from 'react-router';`

### useParams

Nos da los parámetros de la ruta dinámica actual, pero solo se puede ejecutar en un componente hijo de un `<Route>` dinámico.

`import { useParams } from 'react-router-dom';`
