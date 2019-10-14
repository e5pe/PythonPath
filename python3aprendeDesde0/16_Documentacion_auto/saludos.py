# pydoc - Generar documentación automática desde la consola o Terminal de comandos

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