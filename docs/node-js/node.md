# Node.js

Es código JavaScript ejecutado en una terminal.

## NPM
Gestor de paquetes de node.js.

Paquete: código que ha desarrollado otra persona y lo ha subido a una biblioteca pública y así el resto lo podemos coger.

- **npm run dev** o **vite**:  lanza un servidor web y varios watchers estarán pendientes de los cambios en los archivos SCSS, JS, HTML... para recargar el navegador cuando se necesite. También
  - compila los ficheros SCSS a los que hayamos hecho referencia en HTML.
  - agrupa las media queries.

- **npm run build** o **vite build**: solo se ejecuta una vez, y genera una versión lista para producción en la carpeta docs/. Es hacer un **deploy**, ya que despliega el código en un servidor.


- **package.json**: fichero obligatorio en un proyecto de node.js. Aquí se describe la configuración del proyecto (nombre, licencia, url, autor, dependencias, scripts...). Las *dependencias* son librerías, paquetes o módulos que nuestro proyecto usa.

1. En la terminal **npm install**: abre la carpeta package.json, busca todas las dependencias y las instala para poder utilizarlas en nuestro proyecto. Crea una carpeta *node_modules* (meterla en .gitignore) y las mete ahí. Esta instalación solo hay que hacerla la primera vez que empezamos a trabajar en el proyecto, o cuando una compañera crea una dependencia nueva, para estar actualizados.
2. Cuando acabe de instalar, hacer **npm start** o npm run dev. Arranca el proyecto. Se va a *scripts* (dentro del package.json), busca start y ejecuta lo que pone.

## Migración de proyectos colaborativos EN ADALAB
1. Mergear todas las ramas en la rama `dev`.
2. Crear carpeta `version-0`y mover todos los ficheros dentro.
3. Arrastrar ficheros de *adalab-web-starter-kit* a la raíz de nuestro proyecto (no en la carpeta version-0).
4. Ejecutar `npm install`. Ejecutar `npm run dev`
5. Migramos los ficheros de version-0 al Starter Kit.
5.1. Copiar imágenes de version-0 a `public/images`.
5.2. Copiar index.html de version-0 a `src` (sustituir el que hay).
5.3. Copiar *el contenido* de styles.css y de reset.css de version-0 en `src/scss/main.scss` (no eliminar contenido) y `src/scss/core/_reset.scss` (eliminar contenido).
6. En index.html corregir la ruta de los estilos. La ruta de los estilos reset la borramos (ya están incluidos en .scss)
