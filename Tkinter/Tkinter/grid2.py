'''
from tkinter import *

master = Tk()

Label(master, text="First").grid(row=0)
Label(master, text="Second").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)





master.mainloop()
'''

#######
'''
N, S, E, W. To align the labels to the left border, you could use W (west):
'''
#######
'''
Label(master, text="First").grid(row=0, sticky=W)
Label(master, text="Second").grid(row=1, sticky=W)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

'''
#######The columnspan option is used to let a widget span more than one column, and the rowspan option lets it span more than one row.

from tkinter import *

master = Tk()

Label(master, text="First").grid(row=0)
Label(master, text="Second").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master,text="Boton").grid(row=2,columnspan=2)
Button(master,text="Boton").grid(row=2,column=3,rowspan=2)
Label(master, text="Second").grid(row=3)



master.mainloop()
