# Ejercicio 3.1.12
# Escribir un programa que almacene las matrices 
# matriz 2x3
# A=  
#  1, 2, 3
#  4, 5, 6
# matriz 3x2
# B=  
# −1, 0    
#  0, 1
#  1, 1
# en una lista y muestre por pantalla su producto. El resultado debe ser una matriz de 2x2.

# def validar_entrada():
#     pass
# def pedir_numero():
#     pass
import random


def validar_matriz(v1: tuple, v2: tuple) -> bool:
    """
    Valida si dos matrices pueden multiplicarse.
    No se puede multiplicar dos matrices cuando el número de columnas de la primera matriz no coincide con el número de filas de la segunda matriz.

    Args:
        v1 (tuple): La primera matriz
        v2 (tuple): La segunda matriz

    Returns:
        bool: True si es posible la multiplicación, False en caso de no serlo.
    """
    if len(v1[0]) != len(v2):
        return False
    else:
        return True


def generar_matriz_aleatoria(filas: int, columnas: int, min: int, max: int) -> tuple:
    """
    Genera una matriz de números aleatorios con las dimensiones y el rango de valores especificados por parámetros.

    Args:
        filas (int): El número de filas de la matriz.
        columnas (int): El número de columnas de la matriz.
        min (int): El valor mínimo de cada número
        max (int): El valor máximo de cada número

    Returns:
        tuple: Tupla anidada que representa la matriz generada.
    """
    try:
        if min > max:
            raise ValueError("\033[31m*ERROR* El mínimo no puede ser mayor que el máximo.\033[0m")
    except ValueError as e:
        return str(e)

    matriz_generada = []

    for j in range(filas):
        matriz_generada.append([])
        for _ in range(columnas):
            numero_generado = random.randint(min, max)
            matriz_generada[j].append(numero_generado)

    matriz_tuplas = []

    for fila in matriz_generada:
        matriz_tuplas.append(tuple(fila))

    return tuple(matriz_tuplas)


def calcular_matriz(matriz1: tuple, matriz2: tuple) -> tuple:
    """
    Calcula la matriz resultante del producto entre dos matrices dadas

    Args:
        matriz1 (tuple): La primera matriz
        matriz2 (tuple): La primera matriz.

    Returns:
        tuple: Una tupla anidada que representa la matriz resultante del producto entre los dos matrices
    """
    matriz = []

    producto = 0
    producto2 = 0

    try:
        if not validar_matriz(matriz1, matriz2):
            raise ValueError("\033[31m*ERROR* No se puede multiplicar dos matrices si el número de columnas de la primera matriz no coincide con el número de filas de la segunda.\033[0m")

        # Fila 1 por columna 1, fila 1 por columna 2
        for i in range(len(matriz1[0])):
            producto += matriz1[0][i] * matriz2[i][0]
        for i in range(len(matriz1[0])):
            producto2 += matriz1[0][i] * matriz2[i][1]

        matriz.append((producto, producto2))

        producto = 0
        producto2 = 0

        # Fila 2 por columna 1, fila 2 por columna 2
        for i in range(len(matriz2)):
            producto += matriz1[1][i] * matriz2[i][0]
        for i in range(len(matriz2)):
            producto2 += matriz1[1][i] * matriz2[i][1]

        matriz.append((producto, producto2))

    except ValueError as e:
        return str(e)

    return tuple(matriz)


def mostrar_matriz(matriz: tuple) -> str:
    """
    Formatea una tupla pasada por parámetro para dar salto de linea por cada tupla anidada.

    Args:
        matriz (tuple): La matriz a formatear.

    Returns:
        str: La matriz formateada junto a un mensaje.
    """
    resultado = ""
    for fila in matriz:
        resultado += "\n" + f"{fila}"

    return resultado


def main():
    a = (
        (1, 2, 3),
        (4, 5, 6)
        )


    b = (
        (-1, 1),
        (0, 2),
        (2, 3)
        )


    matriz = calcular_matriz(a, b)
    print(matriz)

    matriz_generada = generar_matriz_aleatoria(3, 5, 5, 10)
    print (matriz_generada)

    print(mostrar_matriz(matriz_generada))

    print(mostrar_matriz(matriz))


if __name__ == "__main__":
    main()