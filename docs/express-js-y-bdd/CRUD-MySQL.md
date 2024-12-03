# CRUD

Create
Read
Update
Delete

## Añadir un nuevo registro

`INSERT INTO`

```sql
INSERT INTO nombre_de_la_tabla (nombre_de_una_columna, nombre_de_otra_columna)
VALUES (valor_de_una_columna, valor_de_otra_columna)

-- Añadir varios registros indicando algunas columnas y el valor de cada columna
INSERT INTO users (email, password, name)
VALUES ('maria@gmail.com', '987widJYVxyh', 'María'),
       ('lucia@hotmail.com', 'qwertyui', 'Lucía'),
       ('sofia@yahoo.com', 'mnbvcdfgu', 'Sofía');
```

## Leer uno o varios registros

`SELECT`

Es la única opción que NO modifica la bdd

```sql
SELECT columna
FROM tabla
WHERE (condicion) -- esta sección es opcional



-- Seleccionar solo el id y el email de todas las usuarias
SELECT id, email
FROM users



-- Seleccionar todas las columnas o datos de todas las usuarias
SELECT *
FROM users



-- Seleccionar todas las columnas de la usuaria cuyo email sea lucia@hotmail.com
SELECT *
FROM users
WHERE email = 'lucia@hotmail.com'



-- Seleccionar todas las columnas de todas las usuarias y las ordena por nombre de forma ascendente: A-Z
SELECT *
FROM users
ORDER BY name ASC -- es el orden por defecto, así que podemos omitir las letras ASC



-- Seleccionar todas las columnas de todas las usuarias y las ordena por nombre de forma descendente y a continuación por email de forma descendente
SELECT *
FROM users
ORDER BY name ASC, email DESC



-- Seleccionar todas las columnas hasta un máximo de 2 usuarias
SELECT *
FROM users
LIMIT 2
-- Esta query nos devuelve como máximo 2 registros aunque la tabla tenga más



-- Seleccionar todas las columnas hasta un máximo de 2 usuarias empezando en la posición 5
SELECT *
FROM users
LIMIT 2
OFFSET 5
-- Esta consulta nos devolverá los registros 6º y 7º
```

- Operador lógico **`AND`**: indicamos en SQL que sólo muestre los registro que cumplan con todas las condiciones indicadas

```sql
-- Seleccionar las usuarias cuyo email sea lucia@hotmail.com y el password sea qwertyui
SELECT *
FROM users
WHERE email = 'lucia@hotmail.com' AND password = 'qwertyui'
```

- Operador lógico **`OR`**: especificamos varias condiciones, y si se cumple alguna de ellas se muestra el registro.

```sql
-- Seleccionar las usuarias cuyo email sea lucia@hotmail.com o el name sea María
SELECT *
FROM users
WHERE email = 'lucia@hotmail.com' OR name = 'maria'
```

- Operador lógico **`NOT`**: cuando queremos seleccionar los registros que NO cumplen con cierta condición.

```sql
-- Seleccionar las usuarias cuyo nombre NO sea Sofía
SELECT *
FROM users
WHERE NOT name = 'Sofía'
-- Se descartará a las usuarias que su nombre sea Sofía
```

- Operador **`DISTINCT`**: lista el resultado final con únicamente los valores diferentes, es decir, elimina los valores duplicados.

```sql
SELECT DISTINCT name, email
FROM users;

-- 1º selecciona las columnas email y name para todos los registros de la tabla users
-- 2º selecciona los valores diferentes que tiene el atributo name y email
-- 3º el resultado serán todas las usuarias que tengan nombres y emails diferentes.
```

- Operador **`BETWEEN`**: busca valores que se encuentren en un rango dado (parecido a <= y >=) incluyendo los valores incial y final.

```sql
--  Selecciona las usuarias cuyo id se encuentre entre 5 y 10 (ambos incluidos)
SELECT name, email
FROM users
WHERE id BETWEEN 5 and 10
```

- Operador **`IN`**: selecciona los registros cuyo valor de una columna se encuenntra entre un listado dado. Es una forma abreviada de hacer múltiples condiciones con OR en un WHERE.

```sql
--  Selecciona las usuarias cuyo name sea María o Lucía
SELECT name AS Nombre, email as Usuario
FROM users
WHERE name IN ('María', 'Lucía');
```

- Operador **`AS`**: se usa para cambiar el nombre de una columna o tabla con un alias (el alias es temporal y solo existe mientras dura la consulta.)

```sql
-- el name lo cambia por el alias Nombre, y el email lo cambia por el alias Usuaria

SELECT name AS Nombre, email AS Usuaria
FROM users
WHERE name IN ('María', 'Lucía');
```

- Ejemplos de uso de SELECT

```sql
-- Seleccionar todas las columnas de todas las usuarias que tengan un id diferente de 2
SELECT * FROM users WHERE id <> 2



-- Seleccionar todas las columnas de la usuaria que tenga un id = 2 o un email = lucia@hotmail.com
SELECT * FROM users WHERE id = 2 OR email = 'lucia@hotmail.com'



-- Seleccionar todas las columnas de todas las usuarias cuyo email contenga la palabra: gmail
SELECT * FROM users WHERE email LIKE '%gmail%'
-- LIKE es muy usado para hacer búsquedas por palabras en una base de datos
```

## Modificar un registro exisitente

`UPDATE`

SIEMPRE hay que poner el `WHERE` porque tienes que especificar qué entrada quieres cambiar, si no se pone se modificarán todos los registros de la tabla.

- Si quiero hacer alguna operación matemática (`SET precio = precio*1.10`), tengo que desactivar el modo seguro porque me da un error con el where, y después volver a activarlo:

Para DESACTIVAR temporalmente el modo seguro:
`SET SQL_SAFE_UPDATES = 0;`

Para volver a ACTIVAR el modo seguro:
`SET SQL_SAFE_UPDATES = 1;`

```sql
UPDATE nombre_tabla
SET nombre_columna1 = valor_columna1, nombre_columna2 = valor_columna2
WHERE condiciones_que_cumplen_los_registros_a_modificar



-- Actualizar el email y la contraseña de la usuaria que tiene el id = 3
UPDATE users SET email = 'sofia.garcia@yahoo.com', password = 'abcdefgh'
WHERE id = 3
```

## Borrar un registro existente

`DELETE`

```sql
DELETE FROM nombre_tabla
WHERE condiciones_que_cumplen_los_registros_a_borrar



-- Borrar un registro indicando el id del registro a borrar
DELETE FROM users
WHERE id = 2;
```
