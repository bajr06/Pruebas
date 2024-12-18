beatles = []

print("Paso 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Paso 2:", beatles)

for i in range(2):
    beatles.append(input("Inserte un integrante de los Beatles: "))

print("Paso 3:", beatles)

del beatles[4]
del beatles[3]

print("Paso 4:", beatles)

beatles.insert(0, "Rigo Starr")

print("Paso 5:", beatles)
