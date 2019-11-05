from gui10Ejercicio import Cuenta

'''
Interfaz con dos botones que permiten aumentar o disminuir una cuenta
y al ser presionados realiza una impresión de la acción
'''


class CuentaNueva(Cuenta):
    def disminuir(self):
        Cuenta.disminuir(self)
        print('Disminuyendo...')

    def aumentar(self):
        Cuenta.aumentar(self)
        print('Aumentando...')


if __name__ == '__main__':
    CuentaNueva().mainloop()
