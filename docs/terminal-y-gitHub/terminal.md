# Terminal

Ctrl + r --> cuando empiezo a escribir, me autocompleta cosas anteriores que ya he escrito. (crtl + r prett --> me escribe el comando para indentar el css o el html)

## [Instalar cosas](https://aur.archlinux.org/)

yay -S nombre del programa a descargar\
 (comprobar si la versión que va a descargar es la que quiero, si es así, escribir):\
 ctrl+C\
 yay -S _nombre del programa a descargar_ --noconfirm

## Actualizar cosas

Revisa si hay actualizaciones pendientes y las instala:

```
sudo pacman -Syu
```

Reiniciar al terminar.

## Comandos

- **ls -la**: listado de los ficheros, incluso los ocultos (los que tienen un puntito delante).
- **ls -lh**: listado de los ficheros con el peso en kb.
- **ls \*.html**: listado de todos los archivos que terminan en .html
- **cd _nombre carpeta_**: entrar en la carpeta.
- **pwd**: me dice la ruta en la que me encuentro.
- **history**: veo qué es lo que he escrito antes, cuando hago clear y no veo lo anterior.
- **file _nombre del archivo_**: muestra la información del archivo.
- **mkdir _nombre de la carpeta_**: crear una carpeta nueva.
- **rm -r _nombre de la carpeta_**: borrar la carpeta _nombre de la carpeta_ y todo lo que contiene.
- **rm -ri _nombre de la carpeta_**: pregunta antes de borrar el contenido, si tienes varios archivos, va preguntando uno a uno si quieres borrarlo o no.
- **cd ..**: ir hacia arriba en las carpetas.
- **touch _nombre del archivo_**: crear un archivo.
- **vim _nombre del archivo_**: escribir dentro del archivo. Hay que pulsar "i" para poder escribir.
- **cat _nombre del archivo_**: leer lo que hay dentro del archivo.
- **cat _nombre del archivo1_ _nombre del archivo2_**: concatena ambos archivos.
- **head _nombre del archivo_**: muestra las primeras 10 líneas de texto del archivo.
- **tail _nombre del archivo_**: muestra las últimas 10 líneas de texto del archivo.
- **less _nombre del archivo_**: muestra todo el texto del archivo. Una vez dentro, si se escrire **/_palabra a buscar_**, busca la palabra en todo el archivo.
- **:q**: estando dentro del archivo, salir sin guardar.
- **:wq**: estando dentro del archivo, guardar y salir.
- **mv _nombre del archivo que quiero mover_ _nombre de la carpeta a la que quiero mover el archivo_**: mover un archivo a una carpeta.
- **mv _nombre del fichero actual_ _nuevo nombre del fichero_**: renombrar un fichero.
- **cp _nombre del archivo que quiero copiar_ _nombre de la carpeta a la que quiero copiar el archivo_**: copiar un archivo en una carpeta.
- **../**: por ejemplo, cuando quiero copiar un archivo en otra carpeta, al poner ../ indico que quiero ir a la carpeta madre de donde me encuentro actualmente, y si pongo **../../** voy a la carpeta abuela...
- **./**: indica la carpeta en la que estoy
- **alias _comando que quiero utilizar como alias_=_"comando real"_**: cuando hay un comando largo que uso mucho, puedo ponerle un nombre corto y usarlo directamente (ls -lh --> l). Es temporal, no se guarda definitivamente.
- **man _comando_**: muestra el manual de uso del comando.
- **whatis _comando_**: muestra una breve explicación de qué hace ese comando.
- **echo _'Frase'_**: al dar enter, devuelve la frase que has escrito.
- **pipe operator**: es esta barrita: | Permite enviar la salida de un comando como entrada del siguiente. Por ejemplo: cowsay "Hola amigos" | lolcat --> crea una vaca que diga hola amigos | píntala con colorinchis (cowsay y lolcat hay que instalarlo para que funcione...)

### Ejecución de comandos:

- Comandos separados **por punto y coma ";"**: Se ejecutan uno después del otro en el orden en que fueron puestos, es decir, de forma síncrona. --> _ls; touch archivo.txt; cal_
- Comandos separados **por _&_**: Se ejecutan todos a la vez, es decir de forma asíncrona. --> _ls & date & cal_
- Comandos separados **por _&&_** : Se ejecutan solo si el comando anterior se ha ejecutado exitosamente. --> _mkdir prueba.txt && cd prueba.txt_. Si se hace al revés _cd prueba && mkdir prueba_ va a dar error, porque no puede entrar en una carpeta que no está creada, y ya no continúa ejecutando el siguiente comando.
- Comandos separados **por _||_** : Solo se ejecuta uno, el primero que se ejecute exitosamente, y descarta automaticamente los demas. --> _cd carpetaQueNoExite || touch nuevoArchivo.txt || mkdir nuevaCarpeta_ va a ejecutar solo el segundo comando.

### Comandos de búsqueda:

- **which**: ayuda a encontrar la ruta de nuestros binarios (programa que se va a ejecutar). Ej: which code --> muestra la ruta en la que está localizado visual studio code
- **find**: permite encontrar un archivo. Ej: find ./ -name _.txt --> muestra todos los archivos .txt Ej: find ./ -type d _(directorio ó f file)\* -name Documents --> muestra todos los directorios o archivos con el nombre Documents.
- **grep**: encuentra coincidencias de una búsqueda dentro de un archivo de texto. Ej: grep -i the movies.csv --> en el archivo movies.csv localiza todas las líneas en las que aparece la palabra the, ignorando si es mayúscula o minúscula (-i). Ej: grep -ci the movies.csv --> al poner -c, lo que hace es contar cuántas veces aparece la palabra.

## Permisos

### Tipos de archivos

- _-_ guión: archivo normal
- _d_: directorio
- _l_: link simbólico
- _b_: archivo de bloque especial. Guardan información sobre un dispositivo, por ejemplo un USB.

### Tipos de modo

- Dueño: el que ha creado el archivo. Ej: _rwx_ --> puede leer, escribir y ejecutar
- Grupo: un archivo compartido entre varios usuarios. Ej: _r-x_ --> puede leer y ejecutar
- Mundo u Otros: cualquiera que no entre en las anteriores categorías. Ej: _r-x_ --> puede leer y ejecutar.

#### Modo simbólico

Se pueden asignar permisos desde la terminal:

- _u_: solo para el usuario o dueño.
- _g_: solo para el grupo.
- _o_: solo para otros (mundo u otros).
- _a_: para todos, las tres categorías.

#### Modificar permisos

- **r**: read, lectura.
- **w**: write, escritura.
- **x**: execution, ejecución o acceso a carpetas.
- Al escribir el comando **chmod u-r _"nombre del archivo"_** se quita el permiso de lectura al usuario
  Al escribir el comando **chmod u+r _"nombre del archivo"_** se le da el permiso de lectura al usuario

## Variables de entorno

Cuando hay un comando largo que uso mucho, puedo ponerle un nombre corto y usarlo directamente. Hay que abrir con vsc el archivo de la terminal (code .zshrc o code .bashrc), y escribir **alias _comando que quiero utilizar como alias_=_"comando real"_**, por ejemplo: alias st="git status". Luego, volver a la terminal y escribir zsh o bash, para actualizar, y ya se puede utilizar el nuevo alias.

## Utilidades de la terminal en la red.

- **ifconfig**: muestra información de nuestra red.
- **netstat**: parecido a ifconfig pero más ordenado.
- **ping**: nos dice si una página está activa. Ej: ping www.google.com
- **curl**: trae un archivo de texto a través de la red. Ej: curl www.google.com > index.html --> saca el html de google y lo guarda en un archivo index.html.
- **wget**: hace lo mismo que curl pero organiza mucho mejor el archivo y lo guarda directamente sin decírselo. Ej: wget www.google.com
- **traceroute**: cuando visitamos una dirección ip, nos dice todos los puntos a los que nos vamos conectando hasta llegar a la página que queremos. Ej: traceroute www.google.com

## Comprimir y descomprimir archivos

- zip -r _"nombre de la carpeta en la que quiero guardar los archivos comprimidos"_.zip _"nombre de la carpeta en la que están guardados los archivos a comprimir"_
- unzip _"nombre de la carpeta en la que he guardado los archivos comprimidos"_.zip

## Procesos (en windows ctrl+alt+sup)

- **ps**: indica qué procesos están corriendo en background.
- **top**: muestra los procesos que está utilizando más recursos.
- **kill**: matar procesos cuando se quedan atascados.
