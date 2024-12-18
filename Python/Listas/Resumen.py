my_list = [1, None, True, 'Soy una cadena', 256, 0]
print(my_list[3])  # output: Soy una cadena
print(my_list[-1])  # output: 0

my_list[1] = '?'
print(my_list)  # output: [1, '?', True, 'Soy una cadena', 256, 0]

my_list.insert(0, "primero")
my_list.append("último")
print(my_list)  # output: ['primero', 1, '?', True, 'Soy una cadena', 256, 0, 'último']

###

# my_list = [1, 'a', ["lista", 64, [0, 1], False]] (Listas Anidadas)

###

my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # output: [1, 2, 4]

del my_list  # borra la lista entera

###

my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]

for color in my_list:
    print(color)
# Posible ser interadas

###


my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
print(len(my_list))  # output 5

del my_list[2]
print(len(my_list))  # output 4
# Ver la longitud de una cadena len()

###
