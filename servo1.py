import time
import serial
#import Tkinter
from tkinter import *

# Iniciando conexión serial
arduinoPort = serial.Serial('COM18', 9600) #cambiar el puerto
#encender = b'e'
#apagar = b'a'
 
# Retardo para establecer la conexión serial
time.sleep(1.8)
'''
def servo(posiciones):
	print(str.encode(posiciones))
	arduinoPort.write(str.encode(posiciones))
	reachedPos = str(arduinoPort.readline())            # read serial port for arduino echo
	print(reachedPos)   
	#valorRecibidoCrudo2 = arduinoPort.readline()
	#valor = valorRecibidoCrudo2.strip().decode('ascii')#Esto daa una cadena
'''


def regresa():
	arduinoPort.write(str.encode("0"))
	reachedPos = str(arduinoPort.readline())            # read serial port for arduino echo
	print(reachedPos)   

def avanza():
	arduinoPort.write(str.encode("1"))
	reachedPos = str(arduinoPort.readline())            # read serial port for arduino echo
	print(reachedPos)  

def derecha():
	arduinoPort.write(str.encode("3"))
	reachedPos = str(arduinoPort.readline())            # read serial port for arduino echo
	print(reachedPos)   

def izquierda():
	arduinoPort.write(str.encode("2"))
	reachedPos = str(arduinoPort.readline())            # read serial port for arduino echo
	print(reachedPos) 

root=Tk() #define ventana
root.title("Control de un servo")
root.minsize(300,150)

#Barra de Angulo
#angulo=Scale(root,command=servo,from_= 0,to=179,orient=HORIZONTAL,length=300,troughcolor='blue',width=30,cursor='dot',label='Angulo Servo')
#angulo.grid(column=2,row=1)

#Boton aVANZA
boton=Button(root,text="Avanza",command=avanza)
boton.grid(column=1,row=3)

#Boton encendido
boton1=Button(root,text="Regresa",command=regresa)
boton1.grid(column=3,row=3)

boton2=Button(root,text="Derecha",command=derecha)
boton2.grid(column=4,row=3)

boton3=Button(root,text="Izquierda",command=izquierda)
boton3.grid(column=5,row=3)

root.mainloop()

arduinoPort.close()