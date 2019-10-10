# tkinter - Componente messagebox para hacer una pregunta

import tkinter
from tkinter import messagebox # hay que importarlo de forma especifica

raiz = tkinter.Tk()
raiz.title("Mi programa")

# Crear componente "popup" (ventana para preguntar o confirmar algo)
def preguntar():
    resultado = tkinter.messagebox.askquestion("Titulo de la pregunta","¿Quieres borrar este fichero?")
    if resultado == "yes":
        print("Sí, quiero borrar el fichero")
    else:
        print("No, no quiero borrar el fichero")

boton = tkinter.Button(raiz, text="Pulsar para recibir pregunta", command=preguntar)
boton.pack()

raiz.mainloop()