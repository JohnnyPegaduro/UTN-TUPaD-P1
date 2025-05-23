# Trabajo Práctico: Análisis de Algoritmos - Programación I

Este repositorio contiene el desarrollo y análisis de la complejidad temporal de diferentes algoritmos utilizando la notación Big-O, como parte de la materia **Programación I** de la Tecnicatura Universitaria en Programación a Distancia.

Objetivo: Determinar la complejidad temporal de diferentes algoritmos utilizando la notación Big-O. Comparar distintas soluciones para un mismo problema y analizar cuál es más eficiente.

## Ejercicios y análisis

### Ejercicio 1: Suma con bucle

```python
def suma_numeros(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma
```

- T(n): n operaciones

- O(n): Complejidad lineal

- Justificación: El bucle se ejecuta n veces y realiza una operación constante por iteración.

### Ejercicio 2: Suma con fórmula

```python
def suma_numeros_formula(n):
    return (n * (n + 1)) // 2
```

- T(n): 1 operación
- O(1): Complejidad constante
- Justificación: Solo una operación matemática sin bucles.

**Comparación:** La función con fórmula (Ejercicio 2) es más eficiente porque su complejidad es constante (O(1)), a diferencia del bucle (O(n)).

### Ejercicio 3: Búsqueda lineal

```python
def buscar_elemento(lista, objetivo):
    for elemento in lista:
        if elemento == objetivo:
            return True
    return False
```

- Peor caso: El elemento no está
- O(n): Complejidad lineal
- Justificación: En el peor caso, se recorren los n elementos hasta el final.

### Ejercicio 4: Encontrar máximo

```python
def encontrar_maximo(lista):
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo
```

- O(n): Complejidad lineal
- Justificación: El algoritmo revisa cada elemento una vez para encontrar el máximo.

### Ejercicio 5: Ordenamiento por selección

```python
def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista
```

- O(n^2): Complejidad cuadrática
- Justificación: Dos bucles anidados recorren la lista. En el peor caso se hacen n(n-1)/2 comparaciones, lo que implica crecimiento cuadrático.

## Conclusión

El análisis teórico con notación Big-O permite predecir la eficiencia de los algoritmos sin ejecutarlos. Se recomienda elegir soluciones con menor complejidad cuando el tamaño de entrada es grande.