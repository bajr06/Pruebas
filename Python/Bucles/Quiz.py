# Ejercicio 1
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
    else:
        continue

# Ejercicio 2
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
        x += 1
    else:
        x += 1

# Ejercicio 3
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    else:
        print(ch, end="")

# Ejercicio 4
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
