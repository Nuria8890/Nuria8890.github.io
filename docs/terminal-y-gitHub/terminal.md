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
   - **cat *nombre del archivo1* *nombre del archivo2***: concatena ambos archivos.
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
   - **echo *'Frase'***: al dar enter, devuelve la frase que has escrito.
   - **pipe operator**: es esta barrita: | Permite enviar la salida de un comando como entrada del siguiente. Por ejemplo: cowsay "Hola amigos" | lolcat --> crea una vaca que diga hola amigos | píntala con colorinchis (cowsay y lolcat hay que instalarlo para que funcione...)

### Ejecución de comandos:
   - Comandos separados **por punto y coma ";"**: Se ejecutan uno después del otro en el orden en que fueron puestos, es decir, de forma síncrona. --> *ls; touch archivo.txt; cal* 
   - Comandos separados **por *&***: Se ejecutan todos a la vez, es decir de forma asíncrona. --> *ls & date & cal* 
   - Comandos separados **por *&&*** : Se ejecutan solo si el comando anterior se ha ejecutado exitosamente. --> *mkdir prueba.txt && cd prueba.txt*. Si se hace al revés *cd prueba && mkdir prueba* va a dar error, porque no puede entrar en una carpeta que no está creada, y ya no continúa ejecutando el siguiente comando.
   - Comandos separados **por *||*** : Solo se ejecuta uno, el primero que se ejecute exitosamente, y descarta automaticamente los demas. --> *cd carpetaQueNoExite || touch nuevoArchivo.txt || mkdir nuevaCarpeta* va a ejecutar solo el segundo comando.

## Permisos
### Tipos de archivos
   - Guión *-*: archivo normal
   - *d*: directorio
   - *l*: link simbólico
   - *b*: archivo de bloque especial. Guardan información sobre un dispositivo, por ejemplo un USB.
### Tipos de modo
   - Dueño: el que ha creado el archivo. Ej: *rwx* --> puede leer, escribir y ejecutar 
   - Grupo: un archivo compartido entre varios usuarios. Ej: *r-x* --> puede leer y ejecutar
   - Mundo u Otros: cualquiera que no entre en las anteriores categorías. Ej: *r-x* --> puede leer y ejecutar.
#### Modo simbólico
Se pueden asignar permisos desde la terminal:
   - *u*: solo para el usuario o dueño.
   - *g*: solo para el grupo.
   - *o*: solo para otros (mundo u otros).
   - *a*: para todos, las tres categorías.
#### Modificar permisos
   - Al escribir el comando **chmod u-r *"nombre del archivo"*** se quita el permiso de lectura al usuario
   Al escribir el comando **chmod u+r *"nombre del archivo"*** se le da el permiso de lectura al usuario