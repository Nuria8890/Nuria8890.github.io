# GitHub
## Subir repositorios
1. **git add -A**: git, añade *todos los ficheros que he modificado*, al nuevo historial de versiones.
2. **git commit -m "*mensaje*"**: mensaje que tiene que indicar en esta nueva versión de código.
3. **git push**: sube a github los ficheros.

## Comandos
  - **git status**: me indica en qué estado está el proyecto, si tengo cambios sin guardar.
  - **git fetch**: descarga el historial de cambios pero NO descarga los cambios en el ordenador local.
  - **git pull**: descarga el historial de cambios y TAMBIÉN descarga los cambios en el ordenador local.
  - **git log**: me chiva quién y cuándo ha hecho un commit, y qué es lo que ha sido modificado.
  - **git reflog**: aparece el historial completo de interacciones entre las ramas, dónde me he movido, qué he eliminado y creado... TODO.
  - **git diff .**: indica en rojo y en verde las diferencias de lo que has modificado.
  - **git checkout + *nombre del archivo***: vuelvo al último archivo que había guardado. (Para cuando hago modificaciones y la cago, volver para atrás a la última versión que estaba ok).
  - **git restore + *nombre del archivo a restaurar***: cuando has hecho "git add" y no quieres hacer "commit" y quieres volver a lo que había antes.
  - **git config —global alias.*nombre del alias* "*comando que quiero añadir como alias*"**: cuando hay un comando largo que uso mucho, puedo ponerle un nombre corto y usarlo directamente.
  - **git tag *nombre de la etiqueta***: en vez de los id, me aparece el nombre del tag y puedo moverme entre ellos con git chackout tag/nombre de la etiqueta.
  - **git branch + *nombre de la rama***: crea una nueva rama.
  - **git switch + *nombre de la rama***: moverse entre ramas (también se puede utilizar checkout).
  - **git merge + *nombre de la rama2***: fusiona la rama en la que me encuentro con la rama *nombre de la rama2*.
  - **git stash**: hace un "commit temporal" que solo queda reflejado en mi local y que eso no afecta al árbol. Se usa cuando no has terminado de pulir el código y sabes que está mal y no lo quieres guardar aún.
  - **git stash pop**: recupera los archivos guardados temporalmente cuando hiciste git stash.
  - **git stash drop**: elimina el archivo guardado temporalmente cuando hiciste git stash.
  - **git branch -d + *nombre de la rama***: elimina la rama *nombre de la rama*. (Se suele hacer cuando se han añadido los cambios de esta rama a la rama main y se ha subido a producción).
  - **git clone + SSH*dirección o nombre del proyecto***: cuando eres nuevo en un proyecto y tienes que empezar a trabajar en él.
