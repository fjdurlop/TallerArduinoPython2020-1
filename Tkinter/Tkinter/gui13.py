# CHECKBUTTON
from tkinter import *

# Cuando usamos Checkbuttons generalmente queremos
# que el usuario pueda escoger cero, uno o más de estos
# por este motivo debemos saber el estado de cacda uno de
# ellos, ya sea activo o inactivo, por esto a cada uno de
# ellos se les asocia una variable

raiz = Tk()
variables = []

var1 = IntVar()
chk1 = Checkbutton(raiz, text='Primer', variable=var1)
chk1.pack()
variables.append(var1)

var2 = IntVar()  # Variable de tipo int
chk2 = Checkbutton(raiz, text='Segundo', variable=var2)
chk2.pack()
variables.append(var2)

"""
entradas = ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto']

for entrada in entradas:
    var = IntVar()
    Checkbutton(raiz, text=entrada, variable=var).pack()
    variables.append(var)
"""


def darEstados():
    for variable in variables:
        print(variable.get(), end=' ')
    print()


Button(raiz, text='Estados', command=darEstados).pack()

raiz.mainloop()
