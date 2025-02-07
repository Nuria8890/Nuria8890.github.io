###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")


### Completa aquí
my_name= "Nuria"
my_city= "Valladolid"

print(f"Mi nombre es {my_name}\nMi ciudad es {my_city}")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de dato de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print("El tipo de dato de la variable a es:", type(a))
print("El tipo de dato de la variable b es:", type(b))
print("El tipo de dato de la variable c es:", type(c))
print("El tipo de dato de la variable d es:", type(d))
print("El tipo de dato de la variable e es:", type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

print("Convierto la cadena 12345 a un entero:")
print(int("12345"), type(int("12345")))

print("Convierto el float 3.99 a un entero")
print(int(3.99), type(int(3.99)))
print("Lo que ocurre es que no rendodea al 4 que sería el número más cercano, sino que quita los decimales que hay después del punto y se queda con el número 3")

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
name = "midudev"
age = 39
height = 1.70

print(f"Hola! Me llamo {name} y tengo {age} años, mido {height:.2f} metros")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

pi = 3.1416
redondeo = round(pi)
division = int(redondeo/2)
print("el resultado es", division)