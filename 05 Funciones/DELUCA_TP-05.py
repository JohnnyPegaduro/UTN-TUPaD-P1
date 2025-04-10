"""
TP 2: Funciones en Python
TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA
Materia: Programación I
Alumno: Matías Ariel Deluca

Este archivo contiene la resolución de los ejercicios del TP 4, que abarca la definición y uso de funciones en Python.
Cada función está diseñada para resolver un problema específico, y se incluyen comentarios para facilitar su comprensión.
"""

import math

# Ejercicio 1: Función imprimir_hola_mundo
def imprimir_hola_mundo():
    """
    Imprime el mensaje 'Hola Mundo!' en pantalla.
    """
    print("Hola Mundo!")

# Ejercicio 2: Función saludar_usuario
def saludar_usuario(nombre):
    """
    Recibe un nombre y retorna un saludo personalizado.
    :param nombre: String con el nombre del usuario.
    :return: Un string con el saludo.
    """
    return f"Hola {nombre}!"

# Ejercicio 3: Función informacion_personal
def informacion_personal(nombre, apellido, edad, residencia):
    """
    Recibe datos personales e imprime un mensaje con esa información.
    :param nombre: Nombre del usuario.
    :param apellido: Apellido del usuario.
    :param edad: Edad del usuario.
    :param residencia: Lugar de residencia.
    """
    # Usamos f-string para formar el mensaje.
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Ejercicio 4: Funciones para cálculos con el círculo
def calcular_area_circulo(radio):
    """
    Calcula y retorna el área de un círculo dado su radio.
    :param radio: Radio del círculo (número).
    :return: Área del círculo.
    """
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    """
    Calcula y retorna el perímetro (circunferencia) de un círculo.
    :param radio: Radio del círculo (número).
    :return: Perímetro del círculo.
    """
    return 2 * math.pi * radio

# Ejercicio 5: Función segundos_a_horas
def segundos_a_horas(segundos):
    """
    Convierte una cantidad de segundos a horas.
    :param segundos: Número de segundos.
    :return: Cantidad de horas (float).
    """
    return segundos / 3600

# Ejercicio 6: Función tabla_multiplicar
def tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar del número dado, del 1 al 10.
    :param numero: Número entero.
    """
    print(f"Tabla de multiplicar de {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7: Función operaciones_basicas
def operaciones_basicas(a, b):
    """
    Realiza las operaciones básicas entre dos números: suma, resta, multiplicación y división.
    :param a: Primer número.
    :param b: Segundo número.
    :return: Tupla (suma, resta, multiplicación, división).
    """
    # Para la división, se verifica que b no sea 0.
    division = a / b if b != 0 else None
    return (a + b, a - b, a * b, division)

# Ejercicio 8: Función calcular_imc
def calcular_imc(peso, altura):
    """
    Calcula el índice de masa corporal (IMC) a partir del peso (kg) y altura (m).
    :param peso: Peso en kilogramos.
    :param altura: Altura en metros.
    :return: IMC calculado (float).
    """
    return peso / (altura ** 2)

# Ejercicio 9: Función celsius_a_fahrenheit
def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura en Celsius a Fahrenheit.
    :param celsius: Temperatura en grados Celsius.
    :return: Temperatura en grados Fahrenheit.
    """
    return (9/5) * celsius + 32

# Ejercicio 10: Función calcular_promedio
def calcular_promedio(a, b, c):
    """
    Calcula el promedio de tres números.
    :param a: Primer número.
    :param b: Segundo número.
    :param c: Tercer número.
    :return: Promedio de los tres números (float).
    """
    return (a + b + c) / 3

# Bloque principal: se llaman a las funciones y se interactúa con el usuario
if __name__ == "__main__":
    
    # Ejercicio 1: Imprimir "Hola Mundo!"
    print("Ejercicio 1:")
    imprimir_hola_mundo()
    print()
    
    # Ejercicio 2: Saludar al usuario
    print("Ejercicio 2:")
    nombre_usuario = input("Ingrese su nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)
    print()
    
    # Ejercicio 3: Información personal
    print("Ejercicio 3:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    residencia = input("Lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    print()
    
    # Ejercicio 4: Área y perímetro de un círculo
    print("Ejercicio 4:")
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")
    print()
    
    # Ejercicio 5: Convertir segundos a horas
    print("Ejercicio 5:")
    segundos = float(input("Ingrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")
    print()
    
    # Ejercicio 6: Tabla de multiplicar
    print("Ejercicio 6:")
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)
    print()
    
    # Ejercicio 7: Operaciones básicas
    print("Ejercicio 7:")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    suma, resta, mult, div = operaciones_basicas(a, b)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {mult}")
    if div is not None:
        print(f"División: {div}")
    else:
        print("División: Error (división por cero)")
    print()
    
    # Ejercicio 8: Calcular IMC
    print("Ejercicio 8:")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
    print()
    
    # Ejercicio 9: Convertir Celsius a Fahrenheit
    print("Ejercicio 9:")
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F")
    print()
    
    # Ejercicio 10: Calcular promedio
    print("Ejercicio 10:")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    promedio = calcular_promedio(num1, num2, num3)
    print(f"El promedio es: {promedio:.2f}")
