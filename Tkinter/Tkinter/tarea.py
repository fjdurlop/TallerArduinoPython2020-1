from tkinter import *

raiz = Tk()
frames = [Frame(raiz) for i in range(4)]
for frame in frames: frame.pack(fill = X, expand = YES)
Label(frames[0], text = 'Contacto Nuevo').pack(side=LEFT)
btnAgregar = Button(frames[0], bg = 'green')
btnAgregar.pack(side=RIGHT, expand = YES, fill = X)


Label(frames[1], text = 'Nombre: ').pack(side=LEFT)
entradaNombre = Entry(frames[1])
entradaNombre.pack(side=RIGHT, fill = X, expand = YES)
Label(frames[2], text = 'Teléfono:').pack(side=LEFT)
entradaTel = Entry(frames[2])
entradaTel.pack(side=RIGHT, fill = X, expand = YES)
varNombre = StringVar()
varTel = StringVar()
entradaNombre.config(textvariable = varNombre)
entradaTel.config(textvariable = varTel)


btnConsultar = Button(frames[3], bg = 'yellow', text = 'CONSULTAR')
btnConsultar.pack(fill = X, expand = YES)

contactos = {}

def crearContacto():
    contactos[varNombre.get()] = varTel.get()
    varTel.set('')
    varNombre.set('')

def consultarContactos():
    print(contactos)

btnAgregar.config(command = crearContacto)
btnConsultar.config(command = consultarContactos)

raiz.mainloop()
