# Terminal

## [Instalar cosas](https://aur.archlinux.org/)
   yay -S nombre del programa a descargar\
      (comprobar si la versión que va a descargar es la que quiero, si es así, escribir):\
   ctrl+C\
   yay -S *nombre del programa a descargar* --noconfirm

## Comandos
   - **ls -la**: listado de los ficheros, incluso los ocultos (los que tienen un puntito delante).
   - **ls -lh**: listado de los ficheros con el peso en kb.
   - **ls *.html**: listado de todos los archivos que terminan en .html
   - **cd *nombre carpeta***: entrar en la carpeta.
   - **pwd**: me dice la ruta en la que me encuentro.
   - **file *nombre del archivo***: muestra la información del archivo.
   - **mkdir *nombre de la carpeta***: crear una carpeta nueva.
   - **rm -r *nombre de la carpeta***: borrar la carpeta *nombre de la carpeta* y todo lo que contiene.
   - **rm -ri *nombre de la carpeta***: pregunta antes de borrar el contenido, si tienes varios archivos, va preguntando uno a uno si quieres borrarlo o no.
   - **cd ..**: ir hacia arriba en las carpetas.
   - **touch *nombre del archivo***: crear un archivo.
   - **vim *nombre del archivo***: escribir dentro del archivo.
   - **cat *nombre del archivo***: leer lo que hay dentro del archivo.
   - **head *nombre del archivo***: muestra las primeras 10 líneas de texto del archivo.
   - **tail *nombre del archivo***: muestra las últimas 10 líneas de texto del archivo.
   - **less *nombre del archivo***: muestra todo el texto del archivo. Una vez dentro, si se escrire **/*palabra a buscar***, busca la palabra en todo el archivo.
   - **:q**: estando dentro del archivo, salir sin guardar.
   - **:wq**: estando dentro del archivo, guardar y salir.
   - **mv *nombre del archivo que quiero mover* *nombre de la carpeta a la que quiero mover el archivo***: mover un archivo a una carpeta.
   - **mv *nombre del fichero actual* *nuevo nombre del fichero***: renombrar un fichero.
   - **cp *nombre del archivo que quiero copiar* *nombre de la carpeta a la que quiero copiar el archivo***: copiar un archivo en una carpeta.
   - **../**: por ejemplo, cuando quiero copiar un archivo en otra carpeta, al poner ../ indico que quiero ir a la carpeta madre de donde me encuentro actualmente, y si pongo **../../** voy a la carpeta abuela...
   - **./**: indica la carpeta en la que estoy
   - **alias *comando que quiero utilizar como alias*=*"comando real"***: cuando hay un comando largo que uso mucho, puedo ponerle un nombre corto y usarlo directamente (ls -lh --> l). Es temporal, no se guarda definitivamente.
   - **man *comando***: muestra el manual de uso del comando.
   - **whatis *comando***: muestra una breve explicación de qué hace ese comando.  
