cubed = [num ** 3 for num in range(5)]
print(cubed)  # output: [0, 1, 8, 27, 64]

# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # output: ':('
print(table[0][3])  # output: ':)'

# Cubo - un arreglo tridimensional (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # output: ':('
print(cube[2][2][0])  # output: ':)'

###

i = 0
while i <= 3 :
    i += 2
    print("*")

###

i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
      break
    print("*")

###

for i in range(1):
    print("#")
else:
    print("#")

###

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

###

var = 1
while var < 10:
    print("#")
    var = var << 1
    print(var)

###

z = 10
y = 0
x = y < z and z > y or y > z and z < y

print(x)

###

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)

###

my_list = [3, 1, -2]
print(my_list[my_list[-1]])

###

my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

###

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]

print(vals)

###

nums = [1, 2, 3]
vals = nums
del vals[1:2]

print(vals)

###

nums = [1, 2, 3]
vals = nums[-1:-2]

print(vals)

###

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

###

my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)

###

my_list = [i for i in range(-1, 2)]
print(my_list)

###

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)

###

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])
