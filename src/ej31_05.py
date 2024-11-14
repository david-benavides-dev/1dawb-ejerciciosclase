# Ejercicio 3.1.5
# Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.


lista_numeros = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
]


def formatear_lista_numeros(lista_numeros: list) -> str:
    """
    
    """
    lista_numeros = sorted(lista_numeros, reverse = True)

    return f"{', '.join(map(str, lista_numeros))}".rstrip()


def main():
    print(formatear_lista_numeros(lista_numeros))


if __name__ == "__main__":
    main()