# Docstrings - Cadenas para la documentación

def saludar(nombre):
    """ 
    Esto será un comentario de la función saludar
    Esta función recibirá como parámetro una cadena con el nombre e
    imprimirá por pantalla un saludo con el nombre concatenado 
    """

    print("Buenos días {}".format(nombre))

saludar("Antonio")

help(saludar)

class Saludos:
    """ 
    Esta clase tendrá dos funciones
    Ambas funciones recibirán como parámetro un nombre
    """

    # Hay que poner el self porque es una función dentro de una clase
    def buenosdias(self, nombre):
        """ Esta función sirve para decir buenos días """
        print("Buenos días {}".format(nombre))

    def adios(self, nombre):
        """ Esta función sirve para decir adiós """
        print("Adiós {}".format(nombre))

saludo = Saludos()
saludo.adios("Esperanza")

help(Saludos)