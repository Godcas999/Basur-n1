==> English:
Write a program that reads an integer number and prints its previous and next numbers. See the examples below for the exact format your answers should take. There shouldn't be a space before the period.
Remember that you can convert the numbers to strings using the function str.
==> Español:
Escriba un programa que lea un número entero e imprima sus números anterior y siguiente. Consulte los ejemplos a continuación para conocer el formato exacto que deben adoptar sus respuestas. No debería haber un espacio antes del punto.
Recuerda que puedes convertir los números a cadenas usando la función str.

Código:
#################################################################################
n = int(input())
print('The next number for the number ' + str(n) + ' is ' + str(n + 1) + '.')
print('The previous number for the number ' + str(n) + ' is ' + str(n - 1) + '.')
#################################################################################
