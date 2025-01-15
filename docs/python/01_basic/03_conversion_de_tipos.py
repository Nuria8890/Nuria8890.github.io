# Transformación de tipos de datos
# Casting de tipos

print("Conversión de tipos")
print(type(int("100")))
print(int("100")+2)
print("100"+str(2))

print(type(float("3.1426")))

print(bool(3))
print(bool(0))
print(bool(-1))
print(bool(""))
print(bool(" "))
print(bool("False"))

# No se puede:
print(int("Hola mundo"))