# Ejercicio 1: Imprimir todos los números enteros del 0 al 100.
# Utilizamos un bucle for con range(101) para incluir el 100.
for i in range(101):
    print(i)


# Ejercicio 2: Contar la cantidad de dígitos de un número entero.
# Convertimos la entrada a entero y luego usamos abs() para considerar números negativos.
numero = int(input("Ingrese un número entero: "))
# Convertimos el valor absoluto a string y usamos len() para contar los dígitos.
cantidad_digitos = len(str(abs(numero)))
print("El número tiene", cantidad_digitos, "dígitos.")


# Ejercicio 3: Sumar los números enteros entre dos valores dados (excluyendo ambos extremos).
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))

# Nos aseguramos de que 'a' sea menor que 'b'. En caso contrario, los intercambiamos.
if a > b:
    a, b = b, a

suma = 0
# Iteramos desde a+1 hasta b-1 (excluyendo a y b)
for num in range(a + 1, b):
    suma += num

print("La suma de los números entre", a, "y", b, "es:", suma)


# Ejercicio 4: Sumar números enteros ingresados por el usuario hasta que se ingrese 0.
suma = 0

while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break  # Termina el bucle cuando el usuario ingresa 0.
    suma += num

print("La suma total es:", suma)


# Ejercicio 5: Juego de adivinar un número aleatorio entre 0 y 9.
import random

numero_aleatorio = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número entre 0 y 9: "))
    intentos += 1
    if intento == numero_aleatorio:
        print("¡Acertaste!")
        print("Número de intentos:", intentos)
        break  # Sale del bucle cuando se adivina el número.
    else:
        print("Intenta de nuevo.")


# Ejercicio 6: Imprimir los números pares entre 0 y 100 en orden decreciente.
# Empezamos en 100 y restamos de 2 en 2.
for num in range(100, -1, -2):
    print(num)


# Ejercicio 7: Sumar todos los números desde 0 hasta un número entero positivo (incluyéndolo).
n = int(input("Ingrese un número entero positivo: "))
# Usamos range(n+1) para incluir el valor n en la suma.
suma = sum(range(n + 1))
print("La suma de los números de 0 a", n, "es:", suma)


# Ejercicio 8: Contar la cantidad de números pares, impares, negativos y positivos de 100 números ingresados.
total_numeros = 100  # Cambiar este valor para procesar otra cantidad en pruebas.
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(total_numeros):
    num = int(input(f"Ingrese el número {i + 1}: "))
    # Verificar si es par o impar
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    # Verificar si es positivo o negativo (cero no se considera ni positivo ni negativo)
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)


# Ejercicio 9: Calcular la media de 100 números enteros ingresados.
total_numeros = 100  # Modificar este valor en caso de querer probar con otra cantidad.
suma = 0

for i in range(total_numeros):
    num = int(input(f"Ingrese el número {i + 1}: "))
    suma += num

media = suma / total_numeros
print("La media de los números ingresados es:", media)


# Ejercicio 10: Invertir el orden de los dígitos de un número.
numero = input("Ingrese un número: ")
# Invertir la cadena utilizando slicing.
numero_invertido = numero[::-1]
print("El número invertido es:", numero_invertido)
