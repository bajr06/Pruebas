dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

###

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print(dictionary['cat'])
print(phone_numbers['Suzy'])

###

dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")

###

# Ejemplo 1:
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
}
# Ejemplo 2:
phone_numbers = {'jefe': 5551234567,
              'Suzy': 22657854310
}

###

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

###

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for spanish, french in dictionary.items():
    print(spanish, "->", french)

###

for key in sorted(dictionary.keys()):
    print(spanish, "->", french)

###

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for french in dictionary.values():
    print(french)

###

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary['cisne'] = 'cygne'
print(dictionary)

###

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

del dictionary['perro']
print(dictionary)

###

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary.popitem()
print(dictionary)    # salida: {'gato': 'chat', 'perro': 'chien'}
