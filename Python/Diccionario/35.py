my_numbers = [10, 20, 30, 40, 50]

for i in range(4):
    my_numbers.insert(i, my_numbers[-1])

print(my_numbers)

###

# def compute_square(x):
#     return x * x


# def compute_quad(x):
#     return compute_square(x) * compute_square(None)


# print(compute_quad(4))

###

print(1//2)

###

# def raise_power(base, exponent):
#     return base ** exponent


# print(raise_power(exponent=3, 2))

###

z = 0
y = 10
x = y < z and z > y or y < z and z < y

print(x)

###

my_values = [3 * i for i in range(5)]


def modify_list(values):
    del values[values[2] // 3]
    return values


print(modify_list(my_values))

###

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)

###

a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

###

def custom_function(value):
    if value % 3 == 0:
        return 1
    else:
        return 2


print(custom_function(custom_function(4)))

###

inventory = ['apple', 'banana', 'cherry']
backup_inventory = inventory
del backup_inventory[:]

print(backup_inventory)
print(inventory)

###

first_input = input("Ingresa el primer número: ")
second_input = input("Ingresa el segundo número: ")
print(second_input + first_input)

###

print("a", "b", "c", sep="sep")

###

x = 1 // 5 + 1 / 5
print(x)

###

# sample_tuple[0] = 5
# print(sample_tuple)

###

x = float(input())
y = float(input())
print(y ** (1 / x))

###

dictionary = {'alpha': 'beta', 'gamma': 'alpha', 'beta': 'gamma'}
value = dictionary['gamma']

for key in range(len(dictionary)):
    value = dictionary[value]

print(value)

###

values = [i for i in range(-1, -3, -1)]

print(values)

###

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)


print(fun(0, 3))

###

# i = 0
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")

###

my_tuple = (10, 20, 30, 40, 50)
my_tuple = my_tuple[-3:-1]
my_tuple = my_tuple[-1]
print(my_tuple)

###

my_dict = {"apple": 1, "banana": 2, "cherry": 3}

for item in my_dict:
    print(item)

for value in my_dict.values():
    print(value)

###

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")

###

def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

###

matrix = [[x for x in range(3)] for y in range(3)]

count = 0
for row in matrix:
    for element in row:
        if element % 2 != 0:
            count += 1
print(count)

###

try:
    value = input("Ingresa un valor: ")
    print(int(value)/len(value))
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada erronea...")
except TypeError:
    print("Entrada muy erronea...")
except:
    print("¡Buuu!")

###

# try:
#     print(10 / 0)
#     break
# except ZeroDivisionError:
#     print("Se produjo un error de división entre cero...")
# except (ValueError, TypeError):
#     print("Se produjo un error de valor o tipo...")
# except
#     print("Se produjo un error desconocido..."))

###

# foo = (1, 2, 3)
# foo.index(0)

# print(foo)

###

print(3 + "5")
