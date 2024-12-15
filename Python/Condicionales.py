#
#   EJEMPLOS DE CONDICIONALES IF
#

#if sheep_counter >= 120: # Evaluar una expresión condicional
#   sleep_and_dream() # Ejecutar si la expresión condicional es verdadera

# if sheep_counter >= 120:
#    make_a_bed()
#    take_a_shower()
#    sleep_and_dream()
#feed_the_sheepdogs()


#
#   EJEMPLOS DE CONDICIONALES IF / ELSE
#

#if true_or_false_condition:
#    perform_if_condition_true
#else:
#    perform_if_condition_false

#if the_weather_is_good:
#    go_for_a_walk()
#    have_fun()
#else:
#    go_to_a_theater()
#    enjoy_the_movie()
#have_lunch()


#
#   EJEMPLOS ANIDADOS
#

#if the_weather_is_good:
#    if nice_restaurant_is_found:
#        have_lunch()
#    else:
#        eat_a_sandwich()
#else:
#    if tickets_are_available:
#        go_to_the_theater()
#    else:
#       go_shopping()


#
#   ELIF
#

#if the_weather_is_good:
#    go_for_a_walk()
#elif tickets_are_available:
#    go_to_the_theater()
#elif table_is_available:
#    go_for_lunch()
#else:
#    play_chess_at_home()


# EJECUCION
# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2:
    larger_number = number1 # Es posible colocar esto arriba
else:
    larger_number = number2 # Lo mismo

# Imprime el resultado
print("El número más grande es:", larger_number)

# Otro ejemplo
# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1

# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2

# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3

# Imprime el resultado.
print("El número más grande es:", largest_number)


