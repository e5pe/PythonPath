# tkinter - Componente text (campo de texto largo, de varias líneas, para introducir texto por teclado)

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

# Creamos nuestro componente Text

entrada = tkinter.Text(raiz)
entrada.config(width=20, height=10, font=("Verdana",15), padx = 10, pady=10) # Lo del final es el espaciado
entrada.pack()

raiz.mainloop()