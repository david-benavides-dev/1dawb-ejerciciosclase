def generar_tablero(filas: int, columnas: int, valor_defecto = "*") -> tuple:
    """
    
    """
    tablero_generado = []

    for j in range(filas):
        tablero_generado.append([])
        for _ in range(columnas):
            tablero_generado[j].append(valor_defecto)

    tablero_tuplas = []

    for fila in tablero_generado:
        tablero_tuplas.append(tuple(fila))

    return tuple(tablero_tuplas)


def mostrar_tablero(tablero: tuple) -> str:
    """
    
    """
    tablero_completo = ""
    separador_lineas = "-" * (len(tablero[0]) * 4) + "-"

    for fila in tablero:
        tablero_completo += f"\n| {' | '.join(map(str, fila))} |" + f"\n{separador_lineas}"
    
    tablero_completo = separador_lineas + tablero_completo
    return tablero_completo


def main():
    tablero = generar_tablero(10,10,0)

    print(mostrar_tablero(tablero))


if __name__ == "__main__":
    main()