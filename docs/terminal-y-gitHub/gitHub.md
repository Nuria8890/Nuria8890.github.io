# GitHub
## Subir repositorios
1. **git add -A**: git, añade *todos los ficheros que he modificado*, al nuevo historial de versiones.
2. **git commit -m "*mensaje*"**: mensaje que tiene que indicar en esta nueva versión de código.
3. **git push**: sube a github los ficheros.

## Comandos
### EFECTUAR CAMBIOS: revisa las ediciones y elabora una transacción de commit.
  - **git status**: indica en qué estado está el proyecto, si tengo cambios sin guardar.
  - **git diff .**: indica en rojo y en verde las diferencias de lo que has modificado. Muestra las diferencias de ficheros que no se han enviado aún al área de espera.
  - **git add *nombre del fichero***: toma una instantánea del fichero para preparar la versión.
  - **git diff --staged**: muestra las diferencias del fichero entre el área de espera y la última versión del fichero.
  - **git reset *nombre del fichero***: mueve el fichero del área de espera, pero preserva su contenido.
  - **git commit -m *mensaje descriptivo***: registra las instantáneas del fichero permanentemente en el historial de versión.
  - **git restore + *nombre del archivo a restaurar***: cuando has hecho "git add" y no quieres hacer "commit" y quieres volver a lo que había antes.

### CREAR REPOSITORIOS: inicia un nuevo repositorio y obtiene uno de una URL existente.
  - **git init *nombre del proyecto***: crea un nuevo repositorio local con el nombre especificado.
  - **git clone SSH*url o nombre del proyecto***: descarga un proyecto y toda su historia de versión. Se usa cuando eres nuevo en un proyecto y tienes que empezar a trabajar en él.

### CAMBIOS GRUPALES: nombra una serie de commits y combina esfuerzos ya culmonados.
  - **git branch**: enumera todas las ramas en el repositorio actual.
  - **git branch *nombre de la rama***: crea una nueva rama.
  - **git checkout *nombre del fichero***: vuelvo al último fichero que había guardado. (Para cuando hago modificaciones y la cago, volver para atrás a la última versión que estaba ok).
  - **git checkout *nombre de la rama***: cambia a la rama especificada y actualiza el directorio activo.
  - **git merge *nombre de la rama2***: fusiona la rama en la que me encuentro con la rama *nombre de la rama2*.
  - **git branch -d *nombre de la rama***: elimina la rama *nombre de la rama*. (Se suele hacer cuando se han añadido los cambios de esta rama a la rama main y se ha subido a producción).

### REPASAR HISTORIAL: navega e inspecciona la evolución de los ficheros de proyecto.
  - **git log**: me chiva quién y cuándo ha hecho un commit, y qué es lo que ha sido modificado.
  - **git log --follow *nombre del fichero***: 
  - **git diff *nombre de la rama*...*nombre de la rama2***: muestra las diferencias de contenido entre dos ramas.
  - **git reflog**: aparece el historial completo de interacciones entre las ramas, dónde me he movido, qué he eliminado y creado... TODO.

### REHACER COMMITS: borra errores y elabora historial de reemplazo.
  - **git reset *commit***: deshace todos los commits después de *commit*, preservando los cambios localmente.
  - **git reset --hard *commit***: desecha todo el historial y regresa al commit especificado.

### SINCRONIZAR CAMBIOS: registrar un marcador de repositorio e intercambiar historial de versión.
  - **git fetch**: descarga el historial de cambios pero NO descarga los cambios en el ordenador local.
  - **git merge *nombre de la rama del marcador*/*nombre de la rama***: combina la rama del marcador con la rama local actual.
  - **git push**: carga todos los commits de la rama local al GitHub.
  - **git pull**: descarga el historial de cambios y TAMBIÉN descarga los cambios en el ordenador local.
  
### GUARDAR FRAGMENTOS: almacena y restaura cambios incompletos.
  - **git stash**: hace un "commit temporal" que solo queda reflejado en mi local y que eso no afecta al árbol. Se usa cuando no has terminado de pulir el código y sabes que está mal y no lo quieres guardar aún.
  - **git stash pop**: recupera los ficheros guardados temporalmente cuando hiciste git stash.
  - **git stash list**: enumera todos los ficheros guardados temporalmente.
  - **git stash drop**: elimina el fichero guardado temporalmente cuando hiciste git stash.

### NOMBRES DEL FICHERO DE REFACTORIZACIÓN: reubica y retira los ficheros con versión
  - **git rm *nombre del fichero***: borra el fichero del directorio activo y pone en el área de espera el fichero borrado.
  - **git rm --cached *nombre del fichero***: retira el fichero del control de versiones, pero preserva el fichero a nivel local.
  - **git mv *nombre del fichero actual* *nuevo nombre del fichero***: cambia el nombre del fichero y lo prepara para commit.

### SUPRIMIR TRACKING: excluye los ficheros temporales y las rutas.
  - *** .log build/temp- ***: un fichero de texto llamado .gitignore suprime la creación accidental de versiones de archivos y rutas que concuerdan con los patrones especificados.
  - **$ git ls-files --other --ignored --exclude-standard**: enumera todos los ficheros ignorados en este proyecto.

### OTROS:  
  - **git config —global alias.*nombre del alias* "*comando que quiero añadir como alias*"**: cuando hay un comando largo que uso mucho, puedo ponerle un nombre corto y usarlo directamente (git status --> git st).
  - **git tag *nombre de la etiqueta***: en vez de los id, me aparece el nombre del tag y puedo moverme entre ellos con git checkout tag/nombre de la etiqueta.
  - **git switch + *nombre de la rama***: moverse entre ramas (también se puede utilizar checkout).
  
  
  
  
