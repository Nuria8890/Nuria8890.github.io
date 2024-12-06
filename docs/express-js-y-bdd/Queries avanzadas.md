# Queries avanzadas

## MIN y MAX

Devuelve los valores mínimo y máximo de una columna. Si son letras, "ordena alfabéticamente" y MIN devuelve la A y max devuelve la Z.

```sql
SELECT MIN(columna)
FROM tabla
```

## SUM

Devuelve la suma de valores numéricos.

```sql
SELECT SUM(columna)
FROM tabla
```

## AVG

Calcular el promedio (average).

```sql
SELECT AVG(columna)
FROM tabla
```

## COUNT

Contar el número de registros en un conjunto.

```sql
SELECT COUNT(columna)
FROM tabla;
```

## GROUP BY - HAVING

Agrupa filas en función de valores comunes en una columna y realiza cálculos y análisis dentro de esos grupos individuales.

```sql
SELECT columna_agrupada, función_agregación(columna_calculo)
FROM tabla
GROUP BY columna_agrupada
HAVING condición;
```

- `columna_agrupada`: Es la columna por la cual deseas agrupar tus datos.

- `función_agregación`: Es una función de agregación como SUM, AVG, MIN, MAX o COUNT que aplicarás a una columna para obtener un resultado agregado.

- `columna_calculo`: Es la columna a la cual aplicarás la función de agregación.

## CASE

Permite aplicar lógica condicional en las consultas (if ... else...).

```sql
SELECT salario,
CASE
    WHEN salario < 2000 THEN "Bajo"
    WHEN salario > 3000 THEN "Alto"
    ELSE "Medio"
    END AS RangoSalario
FROM empleadas;
```
