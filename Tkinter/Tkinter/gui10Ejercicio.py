# Ejercicio POO

from tkinter import *

'''
Interfaz con dos botones que permiten aumentar o disminuir una cuenta
'''


class Cuenta(Frame):
    def __init__(self, padre=None, **kwargs):
        Frame.__init__(self, padre, **kwargs)
        self.pack()
        self.cuenta = 0

        self.lbl = Label(self, text=self.cuenta, bg="#E8E813")
        self.lbl.pack(fill=BOTH, expand=YES)

        Button(self, text="Disminuir", bg="#15FF12",
               command=self.disminuir).pack(fill=BOTH, expand=YES, side=LEFT)
        Button(self, text="Aumentar", bg="#15FF12",
               command=self.aumentar).pack(fill=BOTH, expand=YES, side=RIGHT)

    def disminuir(self):
        self.cuenta -= 1
        self.lbl.config(text=self.cuenta)

    def aumentar(self):
        self.cuenta += 1
        self.lbl.config(text=self.cuenta)


if __name__ == '__main__':
    cuenta = Cuenta()
    cuenta.pack(fill=BOTH, expand=YES)
    mainloop()
