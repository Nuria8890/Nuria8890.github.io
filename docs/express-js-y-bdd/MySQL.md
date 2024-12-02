# MySQL

MySQL es un sistema de administración de bases de datos que nos va a permitir crear, leer, actualizar y borrar datos.

SQL guarda los datos en formato de tabla (SQLite, Microsoft SQL, Postgres SQL)

## MySQL Workbench

Permite escribir código en SQL y crear modelado de datos (hacer el diseño de la bdd de forma gráfica).

- **Crear nueva base de datos** El nombre de la base de datos debe ser único

```
CREATE DATABASE Nombre_base_datos;
CREATE DATABASE Person

USE Nombre_base_datos;
USE Person
```

- **Crear una nueva tabla en la base de datos** En cada columna hay que indicar el tipo de dato

```
CREATE TABLE nombre_tabla(
  columna1 tipo_dato1 otras_caracteristicas,
  columna2 tipo_dato2 otras_caracteristicas,
);


CREATE TABLE nombre_tabla(
  id_person INT auto_increment primary key,
  name VARCHAR(30) not null,
  lastname VARCHAR(30) not null,
  birthday date
);
```

`id_person`: Columna de tipo de datos número entero y entre sus característica o restricciones encontramos que es clave primaria de la tabla y auto incrementable.

`name`: Columna de tipo de datos cadena de caracteres variables de máximo tamaño 30 y con una restricción de que debe ser obligatoria, es decir nunca puede tener un valor NULL

`lastname`: Columna de tipo de dato cadena de caracteres variables de máximo tamaño 30y con una restricción de que debe ser obligatoria, es decir nunca puede tener un valor NULL

`birthday`: Columna de tipo de dato fecha y no tiene restricciones.

## Tipos de datos en MySQL

**De texto**:

- CHAR: caracteres individuales (e.g., a, Z, @).
- VARCHAR: textos de longitud variable, con un límite máximo definido.
- TINYTEXT: textos de hasta 255 caracteres.
- TEXT: textos de hasta 65535 caracteres.
- MEDIUMTEXT: textos de hasta 16777215 caracteres.
- LONGTEXT: textos de hasta 4294967295 caracteres.
- SET: elementos de un conjunto predefinido (e.g., user, admin, customer).

**Numéricos**:

- BOOL: representaa valores booleanos (0 ó 1).
- TINYINT: enteros entre 0 y 255 (para la edad de un usuario)
- SMALLINT: enteros entre 0 y 65535.
- MEDIUMINT: enteros entre 0 y 16777215.INTEGER: Enteros entre 0 y 4294967295.
- BIGINT: enteros entre 0 y 9223372036854775807.
- FLOAT: con decimales.

**De fechas**:

- DATE: en formato YYYY-MM-DD.
- DATETIME: en formato YYYY-MM-DD hh:mm:ss.
- TIMESTAMP: milisegundos desde el 1 de enero de 1970, útil para manejar usos horarios.

### Primary key (PK)

Le indicamos a la bdd que es la columna pricipal, siempre suele ser la del `id`

### Autoincrement (AI)

Le indicamos a la bdd que debe de ir sumando de uno en uno, siempre suele indicarse esto en la columa del `id`

### Unique (U)

Le indicamos a la bdd que este dato debe der único, se suele indicar en la columna del `id`, del `email`...

## ALTER TABLE

Se utiliza para modificar la estructura de las tablas y sus columnas de una base de datos. Por ejemplo, agrega o elimina columnas, crea o elimina índices, modifica el tipo de columnas existentes o renombra columnas o la propia tabla. También modifica las características tales como el tipo de almacenamiento utilizado para las tablas.

- Estructura básica:

```
ALTER [ONLINE | OFFLINE] [IGNORE] TABLE nombre_tabla
[alter_specification [, alter_specification] ...]
```

- Diferentes opciones para modificar una tabla en MySQL

```
# alter_specification:
# table_options
| ADD [COLUMN] col_name column_definition
      [FIRST | AFTER col_name ]
| ADD [COLUMN] (col_name column_definition,...)
| ADD {INDEX|KEY} [index_name]
      [index_type] (index_col_name,...) [index_option] ...
| ADD [CONSTRAINT [symbol]] PRIMARY KEY
      [index_type] (index_col_name,...) [index_option] ...
| ADD [CONSTRAINT [symbol]]
      UNIQUE [INDEX|KEY] [index_name]
      [index_type] (index_col_name,...) [index_option] ...
| ADD FULLTEXT [INDEX|KEY] [index_name]
      (index_col_name,...) [index_option] ...
| ADD SPATIAL [INDEX|KEY] [index_name]
      (index_col_name,...) [index_option] ...
| ADD [CONSTRAINT [symbol]]
      FOREIGN KEY [index_name] (index_col_name,...)
      reference_definition
| ALTER [COLUMN] col_name {SET DEFAULT literal | DROP DEFAULT}
| CHANGE [COLUMN] old_col_name new_col_name column_definition
      [FIRST|AFTER col_name]
| MODIFY [COLUMN] col_name column_definition
      [FIRST | AFTER col_name]
| DROP [COLUMN] col_name
| DROP PRIMARY KEY
| DROP {INDEX|KEY} index_name
| DROP FOREIGN KEY fk_symbol
| DISABLE KEYS
| ENABLE KEYS
| RENAME [TO|AS] new_tbl_name
| ORDER BY col_name [, col_name] ...
| CONVERT TO CHARACTER SET charset_name [COLLATE collation_name]
| [DEFAULT] CHARACTER SET [=] charset_name [COLLATE [=] collation_name]
```

### Ejemplos

#### Para tablas

- **Renombrar** y/o cambiar el nombre la tabla:

```
ALTER TABLE nombre_tabla RENAME nombre_nuevo_tabla;
```

- **Eliminar** una **columna** de la tabla:

```
ALTER TABLE nombre_tabla DROP COLUMN nombre_columna;
```

- **Eliminar varias columnas** de la tabla

```
ALTER TABLE nombre_tabla DROP COLUMN nombre_columna, DROP COLUMN nombre_columna2;
```

- **Eliminar** una **clave** primaria y clave externa (FOREING KEY y PRIMARY KEY):

```
<!-- Eliminar clave primaria -->
ALTER TABLE nombre_tabla DROP PRIMARY KEY;

<!-- Eliminar clave externa -->
ALTER TABLE nombre_tabla DROP FOREIGN KEY nombre_columna;
```

- **Insertar** una nueva **columna al final** de la tabla

```
ALTER TABLE nombre_tabla ADD fecha_nacimiento date;
```

- **Añadir** una nueva **columna** después de otra:

```
ALTER TABLE nombre_tabla ADD nombre_columna VARCHAR(5) AFTER nombre_columna_anterior;
```

- **Insertar** una nueva **columna** en la **primera posición** de la tabla:

```
ALTER TABLE nombre_tabla ADD nombre_columna VARCHAR(5) INT FIRST;
```

- **Asignar** como **clave primaria** a una columna:

```
ALTER TABLE nombre_Tabla ADD PRIMARY KEY(nombre_columna);
```

- DROP TABLE: elimina una o varias tablas.

```
DROP [TEMPORARY] TABLE [IF EXISTS]
tbl_name [, tbl_name] ...
[RESTRICT | CASCADE]
```

- TRUNCATE TABLE: vacía una tabla por completo.

```
TRUNCATE [TABLE] tbl_name
```

- RENAME TABLE: renombra una o más tablas.

```
RENAME TABLE
tbl_name TO new_tbl_name
[, tbl_name2 TO new_tbl_name2] ...
```

#### Para columnas

- **Renombrar** una columna:

```
ALTER TABLE nombre_tabla CHANGE nombre_viejo_columna nombre_nuevo_columna;
```

- **Cambiar** el **nombre y tipo de dato** de una columna:

```
ALTER TABLE nombre_tabla CHANGE nombre_viejo_columna nombre_nuevo_columna VARCHAR(20);
```

- Solamente **cambiar el tipo de dato** de una columna:

```
ALTER TABLE nombre_tabla MODIFY nombre_columna DATE NOT NULL;
```
