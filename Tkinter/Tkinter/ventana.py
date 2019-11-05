'''from tkinter import *
ventana = Tk()###inicializa el script
ventana.mainloop()###finaliza el script
'''

from tkinter import *
ventana = Tk()###inicializa el script
ventana.title("Python PM")
etiqueta = Label(ventana,text = "Intro a Tkinter")
etiqueta2 = Label(ventana,text = "Etiqueta 2")
etiqueta.grid(row=1,column=1)
etiqueta2.grid(row=2,column=3)
boton = Button(ventana,text="Botoncito")
boton.grid(row=2,column=1)
boton1 = Button(ventana,text="BotonVerde",bg="green",fg="blue")
boton1.grid(row=3,column=1)
ventana.mainloop()###finaliza el script