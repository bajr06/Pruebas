c0 = int(input("Escribe un número: "))
contador = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
        contador += 1
        print(c0)
        continue
    elif c0 % 2 != 0:
        c0 = 3 * c0 + 1
        contador += 1
        print(c0)
        continue

print("Pasos:", contador)
