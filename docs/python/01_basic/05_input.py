# Input: para pedir info al usuario

print("Hola, cómo te llamas")
nombre = input()

print(f"Hola {nombre}, encantado de conocerte")

age = input("Cuántos años tienes??\n")

print(f"Dentro de 20 tendrás {int(age) + 20}")

print("Obtener múltiples valores a la vez")
country, city = input("En qué país y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")