"""
TP 5: Listas en Python
TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA
Materia: Programación I
Alumno: Matías Ariel Deluca

Resolución de los ejercicios del Práctico 5: Listas.
Cada ejercicio incluye comentarios y salidas descriptivas.
"""

# Ejercicio 1: Lista de múltiplos de 4 entre 1 y 100
multiplos_cuatro = [i for i in range(1, 101) if i % 4 == 0]
print("Ejercicio 1 - Múltiplos de 4 de 1 a 100:", multiplos_cuatro)

# Ejercicio 2: Lista de cinco elementos y mostrar el penúltimo
gustos = ["pizza", "música", "viajar", "programar", "cine"]
print("Ejercicio 2 - Penúltimo de la lista de gustos:", gustos[-2])

# Ejercicio 3: Crear lista vacía, agregar tres palabras
lista_vacia = []
lista_vacia.append("hola")
lista_vacia.append("mundo")
lista_vacia.append("Python")
print("Ejercicio 3 - Lista con tres palabras:", lista_vacia)

# Ejercicio 4: Reemplazar el segundo y el último elemento de 'animales'
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"    # índice 1 (segundo)
animales[-1] = "oso"    # índice -1 (último)
print("Ejercicio 4 - Animales modificado:", animales)

# Ejercicio 5: Análisis del programa 
print("Ejercicio 5 - Análisis de programa:")
print('''El programa define una lista de números:
    numeros = [8, 15, 3, 22, 7]
Luego elimina de esa lista el valor máximo usando:
    numeros.remove(max(numeros))
Finalmente, imprime la lista resultante sin el elemento mayor.
Por ejemplo, tras eliminar 22, mostrará: [8, 15, 3, 7]''')


# Ejercicio 6: Lista de 10 a 30 con saltos de 5, mostrar los dos primeros
lista_10_30 = list(range(10, 31, 5))
print("Ejercicio 6 - Dos primeros de 10 a 30 saltando 5:", lista_10_30[:2])

# Ejercicio 7: Reemplazar valores centrales de 'autos'
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["camioneta", "coupe"]  # índices 1 y 2
print("Ejercicio 7 - Autos modificados:", autos)

# Ejercicio 8: Lista 'dobles' con el doble de 5, 10 y 15
dobles = []
for n in (5, 10, 15):
    dobles.append(n * 2)
print("Ejercicio 8 - Dobles:", dobles)

# Ejercicio 9: Manipulación de lista de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) agregar 'jugo' al tercer cliente
compras[2].append("jugo")
# b) reemplazar 'fideos' por 'tallarines' en el segundo cliente
compras[1][1] = "tallarines"
# c) eliminar 'pan' del primer cliente
compras[0].remove("pan")
print("Ejercicio 9 - Compras modificadas:", compras)

# Ejercicio 10: Crear lista anidada
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("Ejercicio 10 - Lista anidada:", lista_anidada)