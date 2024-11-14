# Ejercicio 3.1.2
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.


asignaturas = [
    "Matemáticas",
    "Física",
    "Qúimica",
    "Historia",
    "Lengua",
]


def mostrar_asignaturas(asignaturas: list) -> str:
    """
    Recibe una lista y retorna un string con el formato "Yo estudio: ObjetoN"
    por linea para cada objeto de la lista.

    Args:
        asignaturas (list): La lista a formatear.

    Returns:
        str: La lista con el formato adecuado.
    """
    asignaturas_string = ""

    for asignatura in asignaturas:
        asignaturas_string += f"Yo estudio {asignatura}.\n"

    return asignaturas_string.rstrip()


def main():
    print (mostrar_asignaturas(asignaturas))


if __name__ == "__main__":
    main()