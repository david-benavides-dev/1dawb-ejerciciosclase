# Ejercicio 3.1.4
# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.


def validar_numero(num: str) -> bool:
    """
    Valida que la entrada sea un número tipo entero y esté entre el rango de 1 a 49.

    Args:
        num (str): El número a validar.

    Returns:
        bool: True si es número válido, False en caso de no serlo.
    """
    try:
        num = int(num)
        if num >= 1 and num <= 49:
            return True
        else:
            raise Exception("\033[31m*ERROR* El número debe estar entre 1 y 49.\033[0m")

    except ValueError:
        print("\033[31m*ERROR* Debe ser un número entero.\033[0m")
        return False
    except Exception as e:
        print(e)
        return False


def pedir_numero(msj: str) -> int:
    """
    Solicita al usuario introducir un número, validando que sea un número entero.

    Args:
        msj (str): Mensaje que se mostrará al solicitar el número.

    Returns:
        float: El número introducido, validado y convertido a entero.
    """
    num = None
    while num is None:
        num = input(msj)
        if not validar_numero(num):
            num = None
        else:
            return int(num)


def crear_lista():
    """
    
    """
    lista_numeros = []

    for i in range(6):
        if i == 0:
            lista_numeros.append(pedir_numero(f"Introduce el primer número de la loteria primitiva (hasta 6): "))
        elif i == 5:
            lista_numeros.append(pedir_numero(f"Introduce el último número de la loteria primitiva: "))    
        else:
            lista_numeros.append(pedir_numero(f"Introduce el {i+1}º número de la loteria primitiva (hasta 6): "))
    return lista_numeros


def ordenar_lista(numeros_ganadores):
    """
    
    """
    return sorted(numeros_ganadores)


def mostrar_lista(lista_numeros):
    """
    
    """

    numeros_ordenados = ordenar_lista(lista_numeros)

    return "Los números son:\n" +  f"{' '.join(map(str, numeros_ordenados))}".rstrip()


def main():
    lista_numeros = crear_lista()
    print(mostrar_lista(lista_numeros))


if __name__ == "__main__":
    main()