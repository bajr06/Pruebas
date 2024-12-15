print((2+2)+5/5-3) # La división hace que el resultado sea un número flotante

# Los que tienen un punto (flotantes), harán que el resultado sea un flotante.
# Exponentes
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

# Multiplicación
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#División
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

# División entera (en división de enteros el resultado es entero, y en flotantes, se muestra redondeado). ("floor division")
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)
print(6. // 4)

# Los redondeos siempre van hacia abajo, no hacia arriba.
print(-6 // 4)
print(6. // -4)

# Residuo (también conocido como módulo).
print(14 % 4)

print(12 % 4.5)

# Suma
print(-4 + 4)
print(-4. + 8)

# Resta
print(4 - 4)
print(-4 -8.)

# Unitarios
print(-4 - 4)
print(4. - 8)
print(-1.1)
print(+2)

# Enlaces
print(9 % 6 % 2)
print(2 ** 2 ** 3)
print(-3 ** 2)
print(-2 ** 3)
print(-(3 ** 2))
print(2 * 3 % 5)


# Operadores y paréntesis
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))

# Prueba
print(1 // 2 * 3)

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)
