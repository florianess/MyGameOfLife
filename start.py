import gameoflife
from tkinter import *

def start():
    nNumberSquare = int(numberSquare.get())
    nSize = int(size.get())
    randoml = intGr.get()
    f1.destroy()
    gameoflife.start(nNumberSquare,nSize,randoml,root)

root = Tk()
f1 = Frame()

numberSquare = Scale(f1, orient='horizontal', from_=0, to=50,
      resolution=1, tickinterval=5, length=200,
      label='Number of Square')
numberSquare.grid(row=0, column=0)

size = Scale(f1, orient='horizontal', from_=0, to=50,
      resolution=1, tickinterval=5, length=200,
      label='Size of each Square')
size.grid(row=0,column=1)

vals = [True,False]
etiqs = ['Generate Randomly', 'Choose cells']
intGr = IntVar()
intGr.set(vals[0])
for i in range(2):
    b = Radiobutton(f1, variable=intGr, text=etiqs[i], value=vals[i])
    b.grid(row=1, column=i)

#randomly = input("Generate randomly the cells? (Y or N)\n")

start = Button(f1,text='START',command=start)

start.grid(row=2,columnspan=2,sticky='n')

f1.pack()
root.mainloop()
