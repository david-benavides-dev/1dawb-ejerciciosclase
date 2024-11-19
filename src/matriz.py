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
    if len(v1[0]) > len(v2):
        return False
    else:
        return True


def generar_matriz_aleatoria(filas: int, columnas: int, min: int, max: int) -> tuple:
    """
    Genera una matriz aleatoria dependiendo de los valores y las dimensiones especificadas.

    Args:
        filas (int): El número de filas de la matriz.
        columnas (int): El número de columnas de la matriz.
        min (int): El valor mínimo de cada número
        max (int): El valor máximo de cada número

    Returns:
        tuple: Tupla anidada que representa la matriz generada.
    """
    matriz_generada = []

    return tuple(matriz_generada)


def generar_matriz(vector1: tuple, vector2: tuple) -> tuple:
    """
    Calcula la matriz resultante del producto entre dos vectores dados.

    Args:
        vector1 (tuple): El primer vector.
        vector2 (tuple): El segundo vector.

    Returns:
        tuple: Una tupla anidada que representa la matriz resultante del producto entre los dos vectores.
    """
    matriz = []

    producto = 0
    producto2 = 0

    try:
        if not validar_matriz(vector1, vector2):
            raise ValueError("\033[31m*ERROR* No se puede multiplicar dos matrices si el número de columnas de la primera matriz no coincide con el número de filas de la segunda.\033[0m")

        # Fila 1 por columna 1, fila 1 por columna 2
        for i in range(len(vector1[0])):
            producto += vector1[0][i] * vector2[i][0]
        for j in range(len(vector1[0])):
            producto2 += vector1[0][j] * vector2[j][1]

        matriz.append((producto, producto2))

        producto = 0
        producto2 = 0

        # Fila 2 por columna 1, fila 2 por columna 2
        for i in range(len(vector2)):
            producto += vector1[1][i] * vector2[i][0]
        for j in range(len(vector2)):
            producto2 += vector1[1][j] * vector2[j][1]

        matriz.append((producto, producto2))

    except ValueError as e:
        return e

    return tuple(matriz)


def mostrar_matriz():
    pass


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


    matriz = generar_matriz(a, b)
    print(matriz)


if __name__ == "__main__":
    main()