# Arquitectura de un servidor

MVC: Modelo - Vista - Controlador

## Modelo

Se encarga de los datos consultando la base de datos: realiza actualizaciones, consultas, búsquedas, etc. todo eso va aquí, en el modelo.

Carpeta `models`: escribimos las funcionalidades y la lógica relacionadas con la bbdd (insertar, recuperar, actualizar y eliminar consultas).

## Controlador

Se encarga de controlar. Recibe peticiones, solicita los datos al modelo y se los comunica a la vista. También recibe las solicitudes de la vista, se las envía al modelo, y envía la respuesta a la vista.

Carpeta `controllers`: escribimos las funcionalidades y la lógica para desarrollar aplicaciones web dinámicas

## Vista

Es la representación visual de los datos.

Carpeta `views`: escribimos código HTML para mostrar la página web en el navegador. También envía datos desde el controlador para mostrarlos de forma dinámica.
