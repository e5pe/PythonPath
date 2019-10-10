import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

# Creamos los checkbutton
def verificar():
    valor = check1.get()
    if valor == 1:
        print("El check está activado")
    else:
        print("El check está desactivado")
    
check1 = tkinter.IntVar()

boton1 = tkinter.Checkbutton(raiz, text="Opción 1", variable=check1, onvalue=1, offvalue=0,command=verificar)
boton1.pack() # Lo empaquetamos para que salga por nuestro programa

raiz.mainloop()

