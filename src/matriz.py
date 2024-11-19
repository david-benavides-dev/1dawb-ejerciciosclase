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
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
# Prueba ahora con estas matrices
# El resultado debe ser una matriz de 3x3.


def generar_matriz_aleatoria(filas, columnas, min, max):
    pass


def generar_matriz(vector1: tuple, vector2: tuple) -> tuple:
    """
    
    """
    matriz = []
    sumatoria = 0
    sumatoria2 = 0

    for i in range(len(vector1[0])):
        sumatoria += vector1[0][i] * vector2[i][0]
    for j in range(len(vector1[0])):
        sumatoria2 += vector1[0][j] * vector2[j][1]

    matriz.append((sumatoria, sumatoria2))

    sumatoria = 0
    sumatoria2 = 0

    for i in range(len(vector1[0])):
        sumatoria += vector1[1][i] * vector2[i][0]
    for j in range(len(vector1[0])):
        sumatoria2 += vector1[1][j] * vector2[j][1]

    matriz.append((sumatoria, sumatoria2))
    return tuple(matriz)


def main():
    # Fila 1 por columna 1, fila 1 por columna 2
    # Fila 2 por columna 1, fila 2 por columna 2
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