# Ejercicio 3.1.3
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> 
# has sacado <nota> donde <asignatura> es cada una de las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


asignaturas = [
    "Matemáticas",
    "Física",
    "Qúimica",
    "Historia",
    "Lengua",
]


def pedir_numero(msj: str) -> float:
    """
    Solicita al estudiante  introducir un número, validando que sea un número.

    Args:
        msj (str): Mensaje que se mostrará al solicitar el número.

    Returns:
        float: El número introducido, validado y convertido a float.
    """
    num = None
    while num is None:
        num = input(msj)
        if not validar_numero(num):
            num = None
        else:
            return float(num)


def validar_numero(num: str) -> bool:
    """
    Valida que la entrada sea un número tipo float y esté entre el rango de 0 a 10.

    Args:
        num (str): El número a validar.

    Returns:
        bool: True si es número válido, False en caso de no serlo.
    """
    try:
        num = float(num)
        if num >= 0 and num <= 10:
            return True
        else:
            raise Exception("*ERROR* La nota debe estar entre 0 y 10.")

    except ValueError:
        print("*ERROR* Debe ser un número.")
        return False
    except Exception as e:
        print(e)
        return False


def preguntar_nota(asignaturas: list) -> list:
    """
    Pregunta al usuario por su nota para cada asignatura proporcionada.

    Args:
        asignaturas (list): Lista de asignaturas para las que se pedirán notas.

    Returns:
        notas (list): Lista de notas introducidas por el estudiante para cada asignatura.
    """
    notas = []

    for asignatura in asignaturas:
        notas.append(pedir_numero(f"Introduce la nota de {asignatura}: "))

    return notas


def mostrar_notas(asignaturas: list, notas: list) -> str:
    """
    Recibe dos listas: las asignaturas y notas del estudiante, devolviendo
    una cadena de texto con cada asignatura y su respectiva nota redondeada con el formato
    "En 'asignatura' has sacado un 'nota'".

    Args:
        asignaturas (list): Lista de asignaturas del estudiante.
        notas (list): La lista con correspondientes a cada asignatura.

    Returns:
        str: Cadena de texto con cada asignatura y su nota correspondiente.
    """
    format_notas = ""
    for i in range(len(asignaturas)):
        format_notas += f"En {asignaturas[i]} has sacado un {round(notas[i])}.\n"

    return format_notas.rstrip()


def main():
    notas = preguntar_nota(asignaturas)

    print(mostrar_notas(asignaturas, notas))


if __name__ == "__main__":
    main()