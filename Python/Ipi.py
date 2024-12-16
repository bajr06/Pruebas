ipi = float(input("Introduzca sus ingresos anuales:"))

if ipi < 85528:
    ipi = ipi * 0.18 - 556.02
elif ipi > 85528:
    ipi = ipi * 0.32 + 14839.02
elif ipi <= 0:
    ipi = 0

ipi = round(ipi, 0)
print("El impuesto es:", ipi, "pesos")
