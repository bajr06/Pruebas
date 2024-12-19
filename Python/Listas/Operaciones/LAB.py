my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("Lista actual:", my_list)

question = input("¿Desear borrar las repeticiones de la lista? ")

if question == "Si":
    new_list = []

    for i in my_list:
        if i not in new_list:
            new_list.append(i)
            my_list = new_list
else:
    print("No se ha realizado la limpia de lista.")

print("La lista con elementos únicos:")
print(my_list)
