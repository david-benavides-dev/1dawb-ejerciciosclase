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
from os import system, name
import random


def clear():
    """
    Limpia la terminal.
    """
    if name == 'nt':
        _ = system('cls')


def generar_vector(min: int, max: int, rango_vector: int) -> tuple:
    """
    Args:
        min (int):
        max (int):

    Returns:
    """
    vector = list()

    for _ in range(rango_vector):
        vector.append(dame_numero_aleatorio(min, max))
    return tuple(vector)


def dame_numero_aleatorio(min: int, max: int):
    """
    Args:
        min (int): 
        max (int): 

    Returns:

    """
    numero_generado = random.randint(min, max)
    return numero_generado


def producto_escalar(v1: tuple, v2: tuple) -> int:
    """
    
    """
    producto = 0

    for i in range (len(v2)):
        producto += v1[i] * v2[i]

    return producto


def mostrar_resultado(v1: tuple, v2: tuple, resultado: int) -> str:
    """
    
    """
    resultado = "v1 = (" +  f"{', '.join(map(str, v1))}".rstrip() + ")\n" + "v2 = (" +  f"{', '.join(map(str, v2))}".rstrip() + ")\n" + f"Producto = {str(resultado)}"


    return resultado


def main():
    v1 = (1, 2, 3)
    v2 = (-1, 0, 2)

    resultado = producto_escalar(v1, v2)

    print(mostrar_resultado(v1, v2, resultado))

    print(generar_vector(-5, 5, 5))


if __name__ == "__main__":
    main()