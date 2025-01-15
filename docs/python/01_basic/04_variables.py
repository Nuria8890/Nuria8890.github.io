# Variables

# Asignar variable:
my_name = "Nuria"
print(my_name)

age = 30
print(age)

age = 34
print(age)

# Tipado dinámico: el tipo de dato se determina en tiempo de ejecución. No hay que declarar el tipo de dato y luego podemos cambiarle el tipo.

name = "Nuria"
print(type(name))

name = 34
print(type(name))

# Tipado fuerte: python no realiza conversiones de tipo automático.

#No funciona
# print(10 + "2")

# f-sting (literal de cadena de formato)
print(f"Hola soy {my_name}, tengo {age + 1} años")

# Convenciones de nombres de variables
# snake_case: mi_nombre_de_variable
# NO recomendado --> CamelCase: MiNombreDeVariable
# upper case : MI_CONSTANTE --> para las constantes que no deben cambiar

# nombre no validos
# 1234_variable
# mi-variable
# palabras reservadas (true = False)

""" 
Existe una Guia de estilo creada por el propio creador de Python (VER)
"""


is_user_logged_in: bool = True
print(is_user_logged_in)

is_user_logged_in = 43
print(is_user_logged_in)