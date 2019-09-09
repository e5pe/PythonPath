# tkinter - Componente frame

import tkinter

raiz =  tkinter.Tk()
raiz.title("Mi programa 2")

# Creamos el componente frame
frame = tkinter.Frame(raiz) # Le tenemos que indicar la raiz
frame.config(bg = "blue", width=450, height=300)
frame.pack()

raiz.mainloop()