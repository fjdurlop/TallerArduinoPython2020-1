# Ejercicio ENTRY

from tkinter import *
from random import choice

raiz = Tk()
label = Label(raiz, text = "Hola a todos!!")
entrada = Entry(raiz)
btnCambiarColor = Button(raiz, text = 'Cambiar color')
btnCambiarText = Button(raiz, text = 'Cambiar texto')

var = StringVar()
entrada.config(textvariable = var)

colores = ['red','blue','green','yellow','purple']

def cambiarColor():
    label.config(bg = choice(colores))#The choice() method returns a random item from a list, tuple, or string.

def cambiarTexto():
    label.config(text = var.get())
    var.set('')

btnCambiarColor.config(command = cambiarColor)
btnCambiarText.config(command = cambiarTexto)

label.pack()
entrada.pack()
btnCambiarColor.pack()
btnCambiarText.pack()
raiz.mainloop()