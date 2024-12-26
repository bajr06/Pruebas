def message(number):
    print("Ingresa un número:", number)

number = 1234
message(1)
print(number)

###

def message(what, number):
    print("Ingresa", what, "número", number)

message("teléfono", 11)
message("precio", 5)
message("número", "number")

### Paso de argumentos por Posición

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

###

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

### Paso de argumentos por clave

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

###

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(last_name="Skywalker", first_name="Luke")

### Mezcla de paso de argumentos

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(4, 3, c = 2)

### Funciones parametrizadas

def introduction(first_name, last_name="Smith"):
     print("Hola, mi nombre es", first_name, last_name)

introduction("Jorge", "Pérez")
introduction("Enrique")
introduction(first_name="Guillermo")

###

def introduction(first_name="Juan", last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)


introduction()
introduction(last_name="Rodríguez")
