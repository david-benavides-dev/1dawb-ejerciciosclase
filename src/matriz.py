



def generar_matriz(a: tuple, b: tuple) -> tuple:
    """
    
    """
    matriz = []

    producto_suma = 0

    long_a = len(a[1])
    long_b = len(b)


    for i in range(long_a):
        
        for j in range(long_b):
            



    # for i in range(len(a[0])):
    #     for j in range(len(b)):
    #         producto_suma = a[j-1][i] * b[i][j-1]
    #         matriz.append(producto_suma)

    # return matriz


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


    long_a = len(a[1])
    long_b = len(b)

    print(long_a)
    print(long_b)


if __name__ == "__main__":
    main()


# generar_matriz_aleatoria(filas, columnas, min, max)

#5, 14 8, 32