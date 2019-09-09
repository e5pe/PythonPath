# tkinter - Componente label

import tkinter

raiz =  tkinter.Tk()
raiz.title("Mi programa Label")

# Creamos el componente label (etiqueta)
texto = "Hola mundo" # el texto que mostrará la etiqueta

etiqueta = tkinter.Label(raiz, text = texto)
etiqueta.config(fg="green", bg="lightgrey",font=("Cortana",30))
etiqueta.pack()

raiz.mainloop()