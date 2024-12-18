var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

# Ejemplo 1
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))


# Ejemplo 2
x = 4
y = 1

a = x & y
b = x | y
c = ~x  # ¡difícil!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)
