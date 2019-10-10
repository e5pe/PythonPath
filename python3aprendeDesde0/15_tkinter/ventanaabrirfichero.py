# tkinter - Componente messagebox para hacer una pregunta

import tkinter
from tkinter import filedialog

raiz = tkinter.Tk()
raiz.title("Mi programa")

# Creamos un boton
def abrirfichero():
    rutafichero = filedialog.askopenfilename(title="Abrir un fichero")
    print(rutafichero)

boton = tkinter.Button(raiz, text="Pulsar para abrir fichero", command=abrirfichero)
boton.pack()

raiz.mainloop()