# DocTest - Generar pruebas dentro de la documentación

def sumar(numero1, numero2):
    """ 
    Esto es la documentación de esta función
    Recibe dos números como parámetros y devuelve su suma

    >>> sumar(4,3)
    7
    """

    return numero1 + numero2

resultado = sumar(2,4)
print(resultado)

import doctest
doctest.testmod()