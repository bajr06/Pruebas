secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
# Comillas multiples para poder imprimir cadenas de varias líneas.

user_number = int(input())

while user_number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    user_number = int(input("Intentalo de nuevo: "))

print("¡Bien hecho, muggle! Eres libre ahora.")
