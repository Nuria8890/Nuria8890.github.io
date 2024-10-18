# GitHub
**Git** es un sistema de control de versiones.
**GitHub** es un espacio en la nube donde almacenamos nuestros documentos. GitHub utiliza Git para controlar las versiones.

- VSC nos ayuda con git:
  1. En el explorador (menú de la izquierda) aparecen:
    - En color verde los ficheros nuevos respecto al último commit local.
    - En color amarillo los ficheros modificados desde el último commit local.

  2. También en el panel principal del editor del fichero que estamos editando, aparece a la izquierda del número de línea una franja de color:
    - Amarillo para las líneas modificadas desde el último commit.
    - Verde para las líneas nuevas desde el último commit.


## Subir repositorios
1. **git status**: ver los cambios que están sin guardar
2. **git add -A**: git, añade *todos los ficheros que he modificado*, al nuevo historial de versiones.
3. **git commit -m "*mensaje*"**: mensaje que tiene que indicar en esta nueva versión de código. (*“Resolved conflict and merge”*)
4. **git push**: sube a github los ficheros.

## Comandos
### EFECTUAR CAMBIOS: revisa las ediciones y elabora una transacción de commit.
  - **git status**: indica en qué estado está el proyecto, si tengo cambios sin guardar.
  - **git diff .**: indica en rojo y en verde las diferencias de lo que has modificado. Muestra las diferencias de ficheros que no se han enviado aún al área de espera.
  - **git add *nombre del fichero***: toma una instantánea del fichero para preparar la versión.
  - **git diff --staged**: muestra las diferencias del fichero entre el área de espera y la última versión del fichero.
  - **git reset *nombre del fichero***: mueve el fichero del área de espera, pero preserva su contenido.
  - **git commit -m *"mensaje descriptivo"***: registra las instantáneas del fichero permanentemente en el historial de versión.
  - **git restore + *nombre del archivo a restaurar***: cuando has hecho "git add" y no quieres hacer "commit" y quieres volver a lo que había antes.

### CREAR REPOSITORIOS: inicia un nuevo repositorio y obtiene uno de una URL existente.
  - **git init *nombre del proyecto***: crea un nuevo repositorio local con el nombre especificado.
  - **git clone SSH*url o nombre del proyecto***: descarga un proyecto y toda su historia de versión. Se usa cuando eres nuevo en un proyecto y tienes que empezar a trabajar en él.

### CAMBIOS GRUPALES: nombra una serie de commits y combina esfuerzos ya culminados.
  - **git branch**: enumera todas las ramas en el repositorio actual.
  - **git branch *nombre de la rama***: crea una nueva rama.
  - **git checkout *nombre del fichero***: vuelvo al último fichero que había guardado. (Para cuando hago modificaciones y la cago, volver para atrás a la última versión que estaba ok).
  - **git checkout *nombre de la rama***: cambia a la rama especificada y actualiza el directorio activo.
  - **git merge *nombre de la rama2***: fusiona la rama en la que me encuentro con la rama *nombre de la rama2*.
  - **git branch -r**: me dice las ramas que hay en remoto. Las ramas con las que están trabajando mis compañeras.
  - **git branch -d *nombre de la rama***: elimina la rama *nombre de la rama*. (Se suele hacer cuando se han añadido los cambios de esta rama a la rama main y se ha subido a producción).
  - **git clean -df**: borra todos los ficheros nuevos que no tiene registrados en un commit.

### REPASAR HISTORIAL: navega e inspecciona la evolución de los ficheros de proyecto.
  - **git log**: me chiva quién y cuándo ha hecho un commit, y qué es lo que ha sido modificado.
  - **git log --follow *nombre del fichero***: 
  - **git diff *nombre de la rama*...*nombre de la rama2***: muestra las diferencias de contenido entre dos ramas.
  - **git reflog**: aparece el historial completo de interacciones entre las ramas, dónde me he movido, qué he eliminado y creado... TODO.

### REHACER COMMITS: borra errores y elabora historial de reemplazo.
  - **git reset *commit***: deshace todos los commits después de *commit*, preservando los cambios localmente.
  - **git reset --hard *commit***: desecha todo el historial y regresa al commit especificado.
  - **git revert *has del commit que quiero borrar***: revertimos el último commit que hemos hecho.

### SINCRONIZAR CAMBIOS: registrar un marcador de repositorio e intercambiar historial de versión.
  - **git fetch**: descarga el historial de cambios pero NO descarga los cambios en el ordenador local.
  - **git merge *nombre de la rama del marcador*/*nombre de la rama***: combina la rama del marcador con la rama local actual.
  - **git push**: carga todos los commits de la rama local al GitHub.
  - **git pull**: descarga el historial de cambios y TAMBIÉN descarga los cambios en el ordenador local.
  - **git fetch --prune**: cuando he borrado ramas tanto de github como de mi local, al hacer git branch -a siguen saliendo, si las quier eliminar de ahí, escribo este comando.

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
  
  
## Archivo .gitignore
<https://choosealicense.com/> Aquí se especifica qué se puede y qué no se puede hacer con los archivos asociados al .gitignore.

## Ramas
`main` es la rama principal o versión de producción.
`dev`es la rama de desarrollo. Desde aquí vamos creando ramas para ir desarrollando (rama header, footer, styled_section...), y cuando termino de trabajar en una rama, mergeo el contenido en dev.

- Crear una rama: **git branch *nombre de la rama***
- Movernos a una rama: **git checkout *nombre de la rama***
- Crear rama y movernos a ella: **git checkout -b *nombre de la rama***
- Primera ver que usamos git push: **git push -u origin *nombre de la rama***
- Siguientes veces que usamos el push: **git push origin *nombre de la rama***

### Fusionar ramas
Cuando ya hemos terminado el trabajo en la rama y lo queremos subir al main:
1. Hacer git pull en la rama en la que hemos terminado el trabajo (*nombre de la rama*). 
2. Ir a la rama de destino (main): **git checkout main** y hacer git pull.
3. Mergear en esta rama (main), la rama donde hemos terminado el trabajo (*nombre de la rama*): ***git merge *nombre de la rama*** y creará un commit automático.
4. Comprobar que la páginia web está bien, no se ha desbarajustado todo.
6. Hacer push.

### Git flow
- Cuando he terminado el trabajo en mi rama secundaria:
1. Mergeo la rama master (main) en la rama secundaria, para comprobar aquí que todo está Ok, y si no lo está, poder cambiarlo sin estropear el main.
2. Una vez he comprobado que todo funciona, mergear toda la rama secundaria a la rama master. (Hay que hacerlo en un período corto de tiempo para que nadie meta un commit en la rama master entre medias, porque sino me tocaría volver a mergear ambas ramas.)

### RESUMEN DE CÓMO TRABAJAR CON RAMAS:
- Configurar atajos / alias de git:
  - git config --global alias.st status
  - git config --global alias.br branch
  - git config --global alias.co checkout
  - git config --global alias.dc diff --cached

- **Crear una nueva rama**:
   1. git pull en rama dev
   2. git co -b nombre de la nueva rama
   3. Trabajo en mi nueva rama

- **Trabajar en mi rama:**
   1. git st
   2. git add -A
   3. git dc (reviso el diff de lo que he modificado antes de hacer el commit)
   4. git commit -m "mensaje descriptivo"
   5. git push en mi rama (si es la primera vez que hago push: git push -u origin nombre de mi rama)

- **Mergear** el trabajo de mi rama con la rama dev:
   1. git fetch
   2. git st (si git me dice que hay cambios con respecto origen hacer pull o push)
   3. git merge origin/dev
   4. Solucionar conflictos si los hay ((si no hay conflictos pasar al punto 6.)). Una vez solucionados hacer:
       4.1. git st
       4.2. git add-A
       4.3. git commit -m "Result conflict and merge"
       4.4. git push
   5. git co dev
   6. git merge nombre de mi rama
   7. Aviso de que he hecho un merge en dev. 


EL RESTO DE COMPAÑERAS, cuando alguien ha hecho merge en dev:
- Si están en su rama
   1. git st
   2. Si hay modificaciones sin guardar ((si NO hay modificaciones, pasar al punto 3))
       2.1. git add -A
       2.2. git commit -m "mensaje descriptivo"
       2.3. git push.
   3. git fetch
   4. git merge origin/dev
- Si estoy en dev, hacer desde el punto 4
