# Ejercicio 3.1.1
# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.


asignaturas = [
    "Matemáticas",
    "Física",
    "Qúimica",
    "Historia",
    "Lengua",
]


def mostrar_asignaturas(asignaturas: list) -> str:
    """
    Recibe una lista y retorna un string con el formato "Objeto1, Objeto2 y Objeto3"

    Args:
        asignaturas (list): La lista a formatear.

    Returns:
        str: La lista con el formato adecuado.
    """
    return ', '.join(asignaturas[:-1]) + ' y ' + asignaturas[-1] + "."


def main():
    print(mostrar_asignaturas(asignaturas))


if __name__ == "__main__":
    main()