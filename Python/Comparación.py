#
# OPERACIONES DE COMPARACIÓN
#

2 == 2

2 == 2. # Son lo mismo (Python los idenificao como iguales a los 2).

1 == 2

black_sheep = 0
white_sheep = 1
black_sheep == 2 * white_sheep
# Es tratada como black_sheep == (2 * white_sheep)

var = 0  # Asignando 0 a var
print(var == 0)

var = 1  # Asignando 1 a var
print(var == 0)


#
# OPERACIONES DE DESIGUALDAD
#

var = 0  # Asignando 0 a var
print(var != 0)

var = 1  # Asignando 1 a var
print(var != 0)

black_sheep > white_sheep  # Mayor que

centigrade_outside = 5
centigrade_outside >= 0.0  # Mayor o igual que

current_velocity_mph = 10
current_velocity_mph < 85  # Menor que
current_velocity_mph <= 85  # Menor o igual que

# LAB
n = 100
print(n >= 100)
