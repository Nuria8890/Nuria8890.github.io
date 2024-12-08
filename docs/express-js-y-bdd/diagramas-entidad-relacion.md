# Diagramas de entidad relación (E-R)

- Abrir el delfín (workbench)
- Click en el icono de los cuadraditos (diagrama)
- Click en Add Diagram - Add Table
- Click en icono de Place a New Table, click en la hoja de cuadros y doble click en la tabla (entidad) para renombrar y añadir atributos.

- Database - forward engineer: para transformar el diagrama en bbdd real (que escriba el código por mi)

- file - save model: para guardar el diagrama que he creado. También se puede exportar como una imagen.

## Claves foráneas (foreign key FK)

Son columnas que se definen en una tabla y hacen referencia obligatoriamente a claves primarias de otra tabla.

`FOREIGN KEY (FK_nombre_columna) REFERENCES nombre_tabla (PK_tabla_referenciada)`

- FK_nombre_columna: es la columna previamente definida donde se guardará la información. Puede tener el prefijo FK.

- nombre_tabla: es la tabla de donde vienen los datos de la clave foránea.

- PK_tabla_referenciada: es la clave primaria de la tabla de donde vienen los datos.

```sql
CREATE DATABASE games;
USE games;

CREATE TABLE country (
	idCountry INT AUTO_INCREMENT PRIMARY KEY,
    nameCountry VARCHAR(50)
);

CREATE TABLE users (
	idUser INT AUTO_INCREMENT PRIMARY KEY,
    nameUser VARCHAR(20) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    fk_country INT,
    CONSTRAINT fk_country_user FOREIGN KEY (fk_country) REFERENCES country(idCountry)
);
```

Estas claves foráneas sirven para hacer consultas combinando columnas de diferentes tablas.
Hacer un producto cartesiano de dos tablas significa que se combinan todos los registros de una tabla con los de otra tabla.

## Cláusula INNER JOIN / LEFT JOIN / RIGHT JOIN / FULL JOIN

Permite unir y enlazar más de dos tablas.

Al unir la tabla A con la tabla B, a **LEFT JOIN** simplemente incluye filas de A independientemente de si se encuentra una fila coincidente en B. **RIGHT JOINE** lo mismo, pero al revés, manteniendo las filas en B independientemente de si se encuentra una coincidencia en A. Por último, **FULL JOIN** simplemente significa que se mantienen las filas de ambas tablas, independientemente de si existe una fila coincidente en la otra tabla.

```sql
SELECT tabla1.columna1, tabla1.columna2, tabla2.columna1
FROM tabla1
INNER/LEFT/RIGHT/FULL JOIN tabla2
    ON tabla1.columna1 = tabla2.columna1
```
