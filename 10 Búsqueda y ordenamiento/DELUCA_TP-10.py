# Práctico 10: Búsqueda y Ordenamiento
# Este archivo contiene la implementación paso a paso de distintas técnicas de búsqueda y operaciones sobre listas.

# --------------------------------
# Ejercicio 1: Búsqueda lineal
# --------------------------------
# Recorre la lista elemento por elemento hasta encontrar el objetivo. Retorna su índice o -1 si no se encuentra.
# Ejercicio 1

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

lista = [10, 20, 30, 40, 50]
print(busqueda_lineal(lista, 30))  # Debe imprimir 2



# --------------------------------
# Ejercicio 2: Búsqueda lineal contando comparaciones
# --------------------------------
# Realiza la búsqueda lineal pero además cuenta cuántas comparaciones se hacen hasta encontrar el objetivo.


def busqueda_lineal_contando(lista, objetivo):
    comparaciones = 0
    for i in range(len(lista)):
        comparaciones += 1
        if lista[i] == objetivo:
            return comparaciones
    return comparaciones

print(busqueda_lineal_contando(lista, 50))  # Debe imprimir 5



# --------------------------------
# Ejercicio 3: Búsqueda binaria
# --------------------------------
# Requiere una lista ordenada. Compara el elemento central con el objetivo y descarta mitades progresivamente.


def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

lista = [1, 3, 5, 7, 9, 11, 13, 15]
print(busqueda_binaria(lista, 7))  # Debe imprimir 3



# --------------------------------
# Ejercicio 4: Búsqueda binaria contando pasos
# --------------------------------
# Igual a la anterior, pero además cuenta cuántos pasos se necesitan hasta encontrar el objetivo.


def busqueda_binaria_contando(lista, objetivo):
    pasos = 0
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        pasos += 1
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return pasos
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return pasos

lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
print(busqueda_binaria_contando(lista, 11))  # Pasos realizados



# --------------------------------
# Ejercicio 5: Generar lista aleatoria y buscar 50 con búsqueda lineal
# --------------------------------
# Genera 20 números aleatorios entre 1 y 100 e intenta encontrar el 50 usando búsqueda lineal.


import random
lista = [random.randint(1, 100) for _ in range(20)]
print("Lista aleatoria:", lista)

def busqueda_lineal_50(lista):
    for i in range(len(lista)):
        if lista[i] == 50:
            return i
    return -1

print("Índice de 50:", busqueda_lineal_50(lista))



# --------------------------------
# Ejercicio 6: Ordenar la lista y buscar 50 con búsqueda binaria
# --------------------------------
# Ordena la lista del ejercicio anterior y busca el 50 usando búsqueda binaria.


lista_ordenada = sorted(lista)
print("Lista ordenada:", lista_ordenada)
print("Índice de 50 con binaria:", busqueda_binaria(lista_ordenada, 50))



# --------------------------------
# Ejercicio 7: Contar ocurrencias de un número
# --------------------------------
# Cuenta cuántas veces aparece el número 5 en una lista dada.


def contar_ocurrencias(lista, numero):
    contador = 0
    for elemento in lista:
        if elemento == numero:
            contador += 1
    return contador

lista = [1, 5, 2, 5, 3, 5, 4, 5]
print(contar_ocurrencias(lista, 5))  # Debe imprimir 4



# --------------------------------
# Ejercicio 8: Comparar tiempos entre búsqueda lineal y binaria
# --------------------------------
# Mide cuánto tarda cada tipo de búsqueda al buscar el número 9999 en una lista de 10,000 elementos.


import time

lista_grande = list(range(10000))

# Búsqueda lineal
inicio = time.time()
busqueda_lineal(lista_grande, 9999)
fin = time.time()
print("Tiempo búsqueda lineal:", fin - inicio)

# Búsqueda binaria
inicio = time.time()
busqueda_binaria(lista_grande, 9999)
fin = time.time()
print("Tiempo búsqueda binaria:", fin - inicio)



# --------------------------------
# Ejercicio 9: Búsqueda en diccionario
# --------------------------------
# Usa un diccionario para buscar una clave a partir de un valor (edad -> nombre).


personas = {"Alice": 25, "Bob": 30, "Charlie": 22}

def buscar_por_edad(diccionario, edad):
    for nombre, valor in diccionario.items():
        if valor == edad:
            return nombre
    return None

print(buscar_por_edad(personas, 30))  # Debe imprimir "Bob"
