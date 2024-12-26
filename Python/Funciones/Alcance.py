def my_function():
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)

###

def my_function():
    var = 2
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)

### Global

def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 1
my_function()
print(var)

###

def my_function(n):
    print("Yo recibí", n)
    n += 1
    print("Ahora tengo", n)


var = 1
my_function(var)
print(var)

###

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

###

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Presta atención a esta línea.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
