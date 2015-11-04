from Tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

### Histogram Part.
class histogram:

    def h1(self):
        self.v1 = np.random.normal(20, 2, 1000)
        return self.v1

    def h2(self):
        self.v2 = np.random.normal(70, 5, 1000)
        return self.v2

    def lin(self):
        self.linear_v = np.array([0])
        for i in range(0, 101):
            self.linear_v = np.append(self.linear_v, np.arange(0,i))
        return self.linear_v

    def merge(self, *args):
        self.v3 = np.hstack((args))
        return self.v3


### GUI Part.
root = Tk()
his = histogram()
v = [his.h1(), his.h2(), his.lin()]

##  Picture Frame.
frame1 = Frame(root, width=400, height=400, relief=FLAT)
frame1.pack(side=LEFT)

## Selection Frame.
frame2 = Frame(root, width=200, height=400)
var1 = IntVar()
check1 = Checkbutton(frame2, text='Left Gaussian', variable=var1)
check1.pack()
check1.place(relx=0.15, rely=0.3)
var2 = IntVar()
check2 = Checkbutton(frame2, text='Right Gaussian', variable=var2)
check2.pack()
check2.place(relx=0.15, rely=0.35)
var3 = IntVar()
check3 = Checkbutton(frame2, text='Linear histogram', variable=var3)
check3.pack()
check3.place(relx=0.15, rely=0.4)

#   Embedding matplotlib figures into Tkinter.
f = Figure(figsize=(3.98, 3.98), dpi=100, frameon=True)
canvas = FigureCanvasTkAgg(f, frame1)
def draw_option():
    f.clear()
    merged_histo = np.array([])
    var_list = [var1.get(), var2.get(), var3.get()]
    for i in range(len(var_list)):
        if var_list[i] == 1:
            merged_histo = his.merge(merged_histo, v[i])
        else:
            continue
    if sum(var_list) == 0:
        f.text(0.5, 0.5, "No entries are selected", horizontalalignment='center')
    else:
        p = f.gca()
        p.hist(merged_histo, 100)
    canvas.show()
canvas.get_tk_widget().pack()

#   Buttons of selection frame.
b1 = Button(frame2, text='Plot', command=draw_option)
b1.pack()
b1.place(relx=0.1, rely=0.7, height=50, width=150)
frame2.pack(side=LEFT)

### Main.
root.title("Histogram Plot")
root.mainloop()