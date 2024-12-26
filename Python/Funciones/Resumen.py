# Ejemplo 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # salida: 3
subtra(2, 5)    # salida: -3


# Ejemplo 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # salida: 3
subtra(b=2, a=5)    # salida: 3

# Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # salida: 3
subtra(5, 2)    # salida: 3

# Ex. 4
def name(first_name, last_name="Pérez"):
    print(first_name, last_name)

name("Andy")    # salida: Andy Pérez
name("Bety", "Rodríguez")    # salida: Bety Rodríguez (el argumento de palabra clave es reemplazado por "Rodríguez")
