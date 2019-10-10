# tkinter - Componente messagebox (mostrar información)

import tkinter
from tkinter import messagebox # hay que importarlo de forma especifica

raiz = tkinter.Tk()
raiz.title("Mi programa")

# Crear componente "popup" (ventana de información)
def avisar():
    tkinter.messagebox.showinfo("Titulo", "Esto es un aviso")

boton = tkinter.Button(raiz, text="Pulsar para aviso", command=avisar)
boton.pack()

raiz.mainloop()