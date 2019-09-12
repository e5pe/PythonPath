# tkinter - Componente button (Botón)

import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

def accion():
    print("Hola mundo")

# Creamos nuestro componente Button

boton = tkinter.Button(raiz, text="Ejecutar",command=accion) 
# Le pasamos la raiz, el texto que mostrará el botón y por último el comando que tiene que ejecutar, 
# en nuestro caso será una función llamada accion
boton.config() # lo podemos configurar
boton.pack()

raiz.mainloop()