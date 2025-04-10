"""
TP 6: Estructuras de datos complejas - UTN a distancia
Tecnicatura Universitaria en Programación a Distancia
Materia: Programación I
Alumno: Matías Ariel Deluca

Este TP abarca la manipulación de estructuras de datos complejas (diccionarios, listas, sets, 
clases, pilas, colas y listas enlazadas). Se incluyen ejercicios para agregar y actualizar datos en 
diccionarios, definir clases y utilizar estructuras de control para procesar datos complejos.
"""

import math
import random
from collections import deque

##############################
# Ejercicio 1: Diccionario - Añadir frutas
##############################

# Diccionario inicial con precios de frutas
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Añadir frutas adicionales
# Naranja = 1200, Manzana = 1500, Pera = 2300
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Ejercicio 1 - Diccionario actualizado con frutas añadidas:")
print(precios_frutas)
print("-" * 50)

##############################
# Ejercicio 2: Actualizar precios del diccionario
##############################

# Actualizar precios:
# Banana = 1330, Manzana = 1700, Melón = 2800
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Ejercicio 2 - Diccionario con precios actualizados:")
print(precios_frutas)
print("-" * 50)

##############################
# Ejercicio 3: Extraer frutas (llaves) en una lista
##############################

# Crear una lista que contenga únicamente las frutas (las keys del diccionario)
lista_frutas = list(precios_frutas.keys())

print("Ejercicio 3 - Lista de frutas:")
print(lista_frutas)
print("-" * 50)

##############################
# Ejercicio 4: Clase Persona
##############################

class Persona:
    def __init__(self, nombre, pais, edad):
        """
        Inicializa una nueva instancia de Persona.
        :param nombre: Nombre de la persona.
        :param pais: País de residencia.
        :param edad: Edad de la persona.
        """
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        """
        Imprime el saludo personal con formato.
        """
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

# Prueba de la clase Persona
print("Ejercicio 4 - Clase Persona:")
persona1 = Persona("Juan", "Argentina", 28)
persona1.saludar()
print("-" * 50)

##############################
# Ejercicio 5: Clase Círculo
##############################

class Circulo:
    def __init__(self, radio):
        """
        Inicializa un círculo con su radio.
        :param radio: Radio del círculo.
        """
        self.radio = radio

    def calcular_area(self):
        """
        Calcula y retorna el área del círculo.
        :return: Área del círculo.
        """
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        """
        Calcula y retorna el perímetro (circunferencia) del círculo.
        :return: Perímetro del círculo.
        """
        return 2 * math.pi * self.radio

# Prueba de la clase Círculo
print("Ejercicio 5 - Clase Círculo:")
circulo1 = Circulo(5)
print(f"Área del círculo: {circulo1.calcular_area():.2f}")
print(f"Perímetro del círculo: {circulo1.calcular_perimetro():.2f}")
print("-" * 50)

##############################
# Ejercicio 6: Balanceo de paréntesis usando pila
##############################

def balancear_parentesis(cadena):
    """
    Verifica si en el string 'cadena' los paréntesis, corchetes y llaves están balanceados.
    :param cadena: String a analizar.
    :return: True si están correctamente balanceados, False si no.
    """
    # Diccionario para pares de apertura y cierre.
    pares = {')': '(', ']': '[', '}': '{'}
    pila = []
    for caracter in cadena:
        if caracter in "([{":
            pila.append(caracter)
        elif caracter in ")]}":
            if not pila or pila.pop() != pares[caracter]:
                return False
    return len(pila) == 0

# Prueba de la función balancear_parentesis
print("Ejercicio 6 - Balance de paréntesis:")
cadena1 = "{[()()]}"    # Balanceado
cadena2 = "{[(])}"      # No balanceado
print(f"Cadena {cadena1} -> {balancear_parentesis(cadena1)}")
print(f"Cadena {cadena2} -> {balancear_parentesis(cadena2)}")
print("-" * 50)

##############################
# Ejercicio 7: Simulación de turnos en un banco usando cola
##############################

class SistemaTurnosBanco:
    def __init__(self):
        """
        Inicializa la cola para gestionar turnos en el banco.
        """
        self.cola = deque()

    def agregar_cliente(self, cliente):
        """
        Encola un cliente.
        :param cliente: Nombre del cliente (string).
        """
        self.cola.append(cliente)
        print(f"Se ha agregado a {cliente} a la cola.")

    def atender_cliente(self):
        """
        Desencola y atiende al siguiente cliente.
        :return: El nombre del cliente atendido o None si la cola está vacía.
        """
        if self.cola:
            cliente = self.cola.popleft()
            print(f"Atendiendo a {cliente}.")
            return cliente
        else:
            print("No hay clientes en cola.")
            return None

    def siguiente_cliente(self):
        """
        Muestra el siguiente cliente en la cola sin desencolarlo.
        """
        if self.cola:
            print(f"El siguiente cliente en la cola es: {self.cola[0]}")
            return self.cola[0]
        else:
            print("No hay clientes en cola.")
            return None

# Prueba del sistema de turnos
print("Ejercicio 7 - Sistema de turnos en un banco:")
sistema = SistemaTurnosBanco()
sistema.agregar_cliente("Carlos")
sistema.agregar_cliente("María")
sistema.agregar_cliente("José")
sistema.siguiente_cliente()
sistema.atender_cliente()
sistema.siguiente_cliente()
print("-" * 50)

##############################
# Ejercicio 8: Lista enlazada con inserción al inicio y recorrido
##############################

# Definición de un nodo para la lista enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Definición de la lista enlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, valor):
        """
        Inserta un nuevo nodo al inicio de la lista.
        :param valor: Valor a almacenar en el nodo.
        """
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def recorrer(self):
        """
        Recorre la lista y muestra los valores de cada nodo.
        """
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

# Prueba de la lista enlazada
print("Ejercicio 8 - Lista enlazada:")
lista = ListaEnlazada()
lista.insertar_al_inicio(10)
lista.insertar_al_inicio(20)
lista.insertar_al_inicio(30)
lista.recorrer()
print("-" * 50)

##############################
# Ejercicio 9: Invertir una lista enlazada
##############################

def invertir_lista_enlazada(lista_enlazada):
    """
    Invierte el orden de los nodos en una lista enlazada.
    :param lista_enlazada: Objeto de la clase ListaEnlazada.
    :return: La misma lista enlazada, ahora invertida.
    """
    anterior = None
    actual = lista_enlazada.cabeza
    while actual:
        siguiente = actual.siguiente  # guardar el siguiente nodo
        actual.siguiente = anterior   # invertir el enlace
        anterior = actual             # mover anterior al nodo actual
        actual = siguiente            # avanzar en la lista
    lista_enlazada.cabeza = anterior
    return lista_enlazada

# Prueba de la inversión de lista enlazada
print("Ejercicio 9 - Lista enlazada invertida:")
lista.recorrer()  # Lista original
invertir_lista_enlazada(lista)
lista.recorrer()  # Lista invertida
print("-" * 50)

