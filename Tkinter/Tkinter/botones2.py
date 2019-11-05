#########################################
#Método GRID
#########################################

from tkinter import *

v=Tk()

i=0
for x in range(6):
	for y in range(6):
		i+=1
		Button(v,text=str(i),borderwidth=1).grid(row=x,column=y)
'''

buttonI=Button(v,text="ESTOY A LA IZQUIERDA").grid(row=0,column=0)
buttonC=Button(v,text="ESTOY CENTRADO").grid(row=0,column=1)
buttonD=Button(v,text="ESTOY A LA DERECHA").grid(row=0,column=2)
'''
v.mainloop()