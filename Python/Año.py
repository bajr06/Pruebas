año = int(input("Ingrese un año cualquiera: "))

if año >= 1582:
    if año % 4 != 0 and año % 400 != 0:
        print("El", año, "es un año común")
    elif año % 100 != 0:
        print("El", año, "es un año bisiesto")
    else:
        print("El", año, "es un año bisiesto")
else:
    print("No está dentro del período del calendario Gregoriano")
