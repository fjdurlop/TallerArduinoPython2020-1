# Aplicación de POO
'''
Contador de veces que se presionó un botón
'''
from tkinter import *


class Contador(Frame):
    def __init__(self, padre=None):
        Frame.__init__(self, padre)
        self.pack()
        self.cuenta = 0
        self.lbl = Label(self, text=self.cuenta, bg="#E8E813")
        self.lbl.pack(fill=BOTH, expand=YES)
        Button(self, text="aumentar", bg="#15FF12",
               command=self.aumentar).pack(fill=BOTH, expand=YES)

    def aumentar(self):
        self.cuenta += 1
        self.lbl.config(text=self.cuenta)


if __name__ == '__main__':
    cont = Contador()
    cont.pack(fill=BOTH, expand=YES, side=LEFT)
    # cont2 = Contador()
    # cont2.pack(fill=BOTH, expand=YES, side=RIGHT)
    mainloop()
