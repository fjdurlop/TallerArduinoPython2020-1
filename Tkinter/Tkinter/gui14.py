# RADIOBUTTON
from tkinter import *

raiz = Tk()
var = StringVar()

# Utilizando los radiobutton, por lo general queremos
# que solo uno de ellos esté activo, por este motivo
# los asociamos a una sola variable
Radiobutton(raiz, text='radio1',
            variable=var, value='1').pack()
Radiobutton(raiz, text='radio2',
            variable=var, value='2').pack()

var.set('1')  # Valor con el que va a iniciar

Button(raiz, text='Estado', command=lambda: print(var.get())).pack()
raiz.mainloop()
