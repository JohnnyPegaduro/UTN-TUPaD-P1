# TP 11 – Aplicación de la Recursividad
# Autor: Matias Ariel Deluca
# Descripción: soluciones recursivas de los ejercicios 1‑8.
# Cada función incluye doctring, casos base y una pequeña prueba
# dentro de un bloque `if __name__ == "__main__":` para mostrar
# su funcionamiento con los ejemplos solicitados.

from __future__ import annotations  # para type‑hinting recursivo en 3.9‑

# ----------------------------------------------------------------------------
# 1) Factorial recursivo y recorrido hasta N
# ----------------------------------------------------------------------------

def factorial(n: int) -> int:
    """Calcula factorial(n) de forma recursiva.

    Casos base → n == 0 ó n == 1 → 1
    Paso recursivo → n * factorial(n‑1)
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def factorial_hasta(n: int) -> list[int]:
    """Devuelve lista con factoriales de 1 … n usando la función factorial."""
    return [factorial(i) for i in range(1, n + 1)]

# ----------------------------------------------------------------------------
# 2) Serie de Fibonacci
# ----------------------------------------------------------------------------

def fibonacci(pos: int) -> int:
    """Devuelve el número de Fibonacci en posición pos (0‑based)."""
    if pos == 0:
        return 0
    if pos == 1:
        return 1
    return fibonacci(pos - 1) + fibonacci(pos - 2)


def serie_fibonacci(hasta: int) -> list[int]:
    """Genera la serie de Fibonacci hasta la posición `hasta` incluida."""
    return [fibonacci(i) for i in range(hasta + 1)]

# ----------------------------------------------------------------------------
# 3) Potencia recursiva
# ----------------------------------------------------------------------------

def potencia(base: float, exp: int) -> float:
    """Calcula base^exp recursivamente (exp ≥ 0)."""
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

# ----------------------------------------------------------------------------
# 4) Conversión decimal → binario
# ----------------------------------------------------------------------------

def decimal_a_binario(n: int) -> str:
    """Convierte un entero positivo a su representación binaria mediante recursión."""
    if n < 2:
        return str(n)
    return decimal_a_binario(n // 2) + str(n % 2)

# ----------------------------------------------------------------------------
# 5) Palíndromo recursivo
# ----------------------------------------------------------------------------

def es_palindromo(palabra: str) -> bool:
    """Devuelve True si `palabra` es un palíndromo (sin usar slicing invertido)."""
    longitud = len(palabra)
    if longitud <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    # Llamada recursiva sobre la sub‑cadena interna
    return es_palindromo(palabra[1:-1])

# ----------------------------------------------------------------------------
# 6) Suma de dígitos recursiva (sin convertir a string)
# ----------------------------------------------------------------------------

def suma_digitos(n: int) -> int:
    """Suma recursivamente los dígitos de un entero positivo."""
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# ----------------------------------------------------------------------------
# 7) Contar bloques en pirámide
# ----------------------------------------------------------------------------

def contar_bloques(n: int) -> int:
    """Devuelve bloques totales para pirámide con `n` bloques en la base."""
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# ----------------------------------------------------------------------------
# 8) Contar dígitos dentro de un número
# ----------------------------------------------------------------------------

def contar_digito(numero: int, digito: int) -> int:
    """Cuenta cuántas veces aparece `digito` (0‑9) en `numero`."""
    if numero == 0:
        return 1 if digito == 0 else 0
    def _aux(n: int) -> int:
        if n == 0:
            return 0
        return (1 if n % 10 == digito else 0) + _aux(n // 10)
    return _aux(numero)

# ----------------------------------------------------------------------------
# Pequeña batería de pruebas / demo interactiva
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    print("\nEjercicio 1 – Factoriales hasta N:")
    N = 6
    print(f"Factoriales 1…{N}:", factorial_hasta(N))

    print("\nEjercicio 2 – Serie de Fibonacci:")
    print("Serie hasta posición 10:", serie_fibonacci(10))

    print("\nEjercicio 3 – Potencia recursiva:")
    print("2^8 =", potencia(2, 8))

    print("\nEjercicio 4 – Decimal → Binario:")
    for num in (10, 42, 255):
        print(f"{num} → {decimal_a_binario(num)}")

    print("\nEjercicio 5 – Palíndromo:")
    for palabra in ("reconocer", "radar", "python"):
        print(palabra, es_palindromo(palabra))

    print("\nEjercicio 6 – Suma de dígitos:")
    for num in (1234, 9, 305):
        print(num, "→", suma_digitos(num))

    print("\nEjercicio 7 – Pirámide de bloques:")
    for base in (1, 2, 4):
        print(base, "→", contar_bloques(base))

    print("\nEjercicio 8 – Contar dígitos:")
    print("12233421, 2 →", contar_digito(12233421, 2))
    print("5555, 5 →", contar_digito(5555, 5))
    print("123456, 7 →", contar_digito(123456, 7))
