##Insertar imagen


from tkinter import *

ventana=Tk()

logo=PhotoImage(file="python-image.png")

label1=Label(ventana,image=logo).grid(row=2)

texto="Solamente podemos utilizar imagenes GIF o PNG para la funcion PhothoImage, para otro formato utilizamos el modulo PIL"

label2=Label(ventana,justify=LEFT,padx=10,text=texto).grid(row=0)
ventana.title("Imagen chida")
ventana.mainloop()