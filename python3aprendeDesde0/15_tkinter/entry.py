# tkinter - Componente entry (texto corto para la entrada de datos por teclado)

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

# Creamos nuestro componente entry

entrada = tkinter.Entry(raiz)
entrada.config(justify="center") # para password poner , show = '*'
entrada.pack()

raiz.mainloop()