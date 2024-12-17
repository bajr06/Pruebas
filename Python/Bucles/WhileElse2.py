blocks = int(input("Ingresa el número de bloques: "))
height = 0
row = 1

while row <= blocks:
    height = height + 1
    blocks = blocks - row
    row = row + 1
else:
    print("La altura de la pirámide:", height)
