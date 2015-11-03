__author__ = 'Gun-woo'
from Tkinter import *
import histExam

root = Tk()
his = histExam.histogram()
v1 = his.h1()
v2 = his.h2()
v3 = his.lin()


frame = Frame(root, width=800, height=400)
frame.pack()
canvas = Canvas(root, width=790, height=200)
canvas.pack()
var = IntVar()
c1 = Checkbutton(root, text='Left Gussian')
root.mainloop()