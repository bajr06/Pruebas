# Primera manera de escribir input
print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")

# Segunda manera
anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")

# Input es una cadena de carácteres, no un valor int o float
# anything = input("Ingresa un número:")
# something = anything ** 2.0
# print(anything, "al cuadrado es", something)
#Esto da error.

# La solución de lo anterior es usar int() o float().
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

# Calculo de la hipotenusa
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)
# No procesa valores negativos.

# Se puede omitir la variable hypo su escribimos la operación dentro del print
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es:", (leg_a**2 + leg_b**2) ** .5)

# Manejar cadenas
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".") # El signo los concadena, pero tienen que ser si o si cadenas.
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+") # El signo de multiplicación funciona como replicación; es decir, repite la misma cadena todas las veces que uno le indique.

# Pasar de enteros a cadenas con string()
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))
