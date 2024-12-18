my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("Esta es la lista actual:", my_list)
question = input("¿Deseas que no se repitan los números? ")

if question:
    elem = my_list[0]

    for i in range(len(my_list)):
        if i == elem:
            elem += 1

else:
        print("Entendido.")


print("La lista con elementos únicos:")
print(my_list)
