# Etiquetas

**< html > </ htm >**:  TODO el contenido de la página

**< head > </ head >**: Título de la página que aparece en la pestaña del navegador. Elementos no visibles. Contiene los metadatos (todos los elementos que están “detrás de escena”)

**< body > </ body >**: Contiene los elementos visibles. Toda la estructura de la página tiene que estar dentro de esta etiqueta.

**< main > </ main >**: Es el contenido principal de < body >. Debe ser único.

**< h1 > </ h6 >**: Encabezados o títulos por nivel de índice.

**< p > </ p >**: Párrafos

**< a > </ a >**: Enlace a otra página web o a un apartado de la propia página que estamos creando.

**< strong > </ strong >**: Para resaltar texto importante (negrita).

**< em > </ em >**: Para resaltar texto importante (cursiva).

**< s > </ s >**: Para tachar el texto.

**< small > </ small >**: Para hacer el texto un poquito más pequeño que el del resto de la web.

**< form > </ form >**: Para crear un [formulario.](./html-y-css/html-formularios.md)

**< input >**: Cada una de las “casillas” del formulario.

**< footer > </ footer >**: Pie de página. Se pone después del elemento </ main >.

**< link >**: Para importar “referencias externas” (CSS).

**< hr >**: Línea horizontal (para separar secciones).

**< div > </ div >**: Es un contenedor que sirve para agrupar otros elementos.

## < datalist > </ datalist >

Aparece un desplegable donde puedes escribir para localizar más rápidamente la opción deseada.

```html
  <label for="cursos">Busca tu curso</label>
  <input type="text" list="cursos">
  <datalist id="cursos">
    <option value="JavaScript">JavaScript</option>
    <option value="HTML5">HTML5</option>
    <option value="CSS3">CSS3</option>
    <option value="WebStandards">WebStandards</option>
  </datalist>
  ```

![ejemplo de etiqueta datalist](./img/image-1.png)

## < select > </ select >

```html
<select>
	<option>Opción 1</option>
	<option>Opción 2</option>
	<option>Opción 3</option>
</select>
```

![ejemplo de etiqueta select](./img/image-10.png)

## < img >

.png: para logos. Se puede poner el cuadrado de fondo en transparente y así quedarnos solo con el logo.

.jpg: para imágenes.

.svg: para iconos o logotipos. Muy ligero, No perdemos calidad al aumentar o disminuir la ventana de navegación.

**width**: determina el ancho de la imagen.

**height**: determina el alto de la imagen.

```html
<img src= "https://www.google.com/search-gato" alt= "un lindo gato naranja" width="300" height="300">

<img src= "home/nuria/imágenes/gatete.jpg">
```

## < video > </ video >
Se utilizan varias etiquetas < source > para asegurar que el navegador puede mostrar el video, ya que dentro de cada etiqueta ponemos diferentes extensiones de video (debería tenerlas todas desgargadas y guardadas en la carpeta...)

**width**: determina el ancho del vídeo.

**height**: determina el alto del vídeo.

**controls**: para que salgan los controles de reproducción del vídeo.

**autoplay**: se reproduce automáticamente.

**muted**: el audio está silenciado.

**loop**: se reproduce en bucle.


```html
<video controls width="300" height="300" controls autoplay muted loop>
<source src="./5764223-sd_426_240_24fps.mp4" #t="10,90"> 
<source src="./5764223-sd_426_240_24fps.m4v">
</video>

<audio controls autoplay loop>
	<source src=”gnr-welcome.mp3” type=”audio”>
</audio>
```

## < picture > </ picture >
Esta etiqueta carga las imágenes

```html
<picture>
<source srcset="./imgs/large.jpg">
<source srcset="./imgs/medium.jpg">
<img src="./imgs/small.jpg" alt="Es una imagen de ejemplo”>
</picture>
```

## < table > </ table >

```html
<table>
	<tr>
		<th>Alumn@</th>
		<th>Lunes</th>
		<th>Martes</th>
		<th>Miércoles</th>
		<th>Jueves</th>
		<th>Viernes</th>
	</tr>

	<tr>
		<td>María</td>
		<td>9 - 13</td>
		<td>10 - 14</td>
		<td>9 - 13</td>
		<td>Descanso</td>
		<td>9 - 13</td>
	</tr>

	<tr>
		<td>Íñigo</td>
		<td>10 - 14</td>
		<td>9 - 13</td>
		<td>Descanso</td>
		<td>10 - 14</td>
		<td>10 - 14</td>
	</tr>
</table>
```

![ejemplo de etiqueta table](./img/image-11.png)