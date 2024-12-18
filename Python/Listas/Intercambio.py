variable_1 = 1
variable_2 = 2

variable_2 = variable_1
variable_1 = variable_2
# Pierdes la variable 2

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary
# Solución 1


variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1
# Solución 2

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)
# Ejemplo

length = 5
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
# Para una cantidad considerable de elementos
