from tkinter import *
from tkSimpleDialog import &
import math
import string

def Add():
	xy = x + y


def Sub():
	xy = x - y


def Mul():
	xy = x * y


def Div():
	xy = x / y


root = Tkinter.Tk()

x = Entry(root)
x.grid(row=0, column=0, columnspan=2)

y = Entry(root)
y.grid(row=0, column=2, columnspan=2)

text = Label(root, text="summa")
text.grid(row=1, column=0)

Button(root, text='add', command=Add).grid(row=2, column=0, columnspan=1)
Button(root, text='sub', command=Sub).grid(row=2, column=1, columnspan=1)
Button(root, text='mul', command=Mul).grid(row=2, column=2, columnspan=1)
Button(root, text='div', command=Div).grid(row=2, column=3, columnspan=1)

root.mainloop()
