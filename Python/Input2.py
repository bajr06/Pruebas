# Calculadora simple
a = float(input("Ingrese el valor a: "))
b = float(input("Ingrese el valor b: "))

print("El resultado de la suma es: " + str(a + b))
print("El resultado de la resta es: " + str(a - b))
print("El resultado de la multiplicación es: " + str(a * b))
print("El resultado de la división es: " + str(a / b))

print("\n¡Eso es todo, amigos!")

# Operación matemática.
x = float(input("Ingresa el valor para x: "))

y = 1/(x+1/(x+1/(x+1/x)))

print("y =", y)

# Calculo de reloj.
hora = int(input("Hora de inicio (horas): "))
minutos = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))

minutos = minutos + duracion # encuentra el número total de minutos
hora = hora + minutos // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
minutos = minutos % 60 # corrige los minutos para que estén en un rango de (0..59)
hora = hora % 24 # corrige las horas para que estén en un rango de (0..23) 
print(hora, ":", minutos, sep='')

# Última prueba.
name = input("Ingresa tu nombre: ")
print("Hola, " + name + ". '¡Gusto en conocerte'!")

print("\nPresiona Enter para terminar el programa.")
input()
print("FIN.")
