# Ejercicio BUTTON Y LABEL
from tkinter import *

contador = 0
def funcA(): #funcion aumentar
	global contador
	contador += 1
	label.config(text = contador)

def funcD(): #funcion disminuir
	global contador
	contador -= 1
	label.config(text = contador) 


raiz = Tk()
raiz.title('Contador')

label = Label(raiz, text = contador, bg = 'blue')
boton1 = Button(raiz, text = 'aumentar', command = funcA)
boton2 = Button(raiz, text = 'disminuir', command = funcD)

label.pack(fill = BOTH, expand = YES, side = TOP)
boton1.pack(fill = BOTH, expand = YES, side = RIGHT)
boton2.pack(fill = BOTH, expand = YES, side = LEFT)
raiz.mainloop()