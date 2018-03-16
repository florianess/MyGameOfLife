import numpy as np
import time, random
from tkinter import *
import core

numberSquare = 0
size = 0
root = ''
canvas = 0
vois = []
tab = []
ntab = []
f2 = ""

def start(newNumber, newSize,randomly, pRoot):

    global root
    root = pRoot
    global f2
    f2 = Frame()
    global numberSquare
    numberSquare = newNumber
    global size
    size = newSize
    global canvas
    canvas = Canvas(f2, width=size*(numberSquare-1), height=size*(numberSquare-1), background='white')
    global vois
    global tab
    vois = core.initiate(numberSquare)
    if (randomly):
        randomize()
    else:
        selection()
    run = Button(f2,text='RUN',command=begin)
    run.grid(row=2,columnspan=2,sticky='n')
    rand = Button(f2,text='RANDOM',command=randomize)
    rand.grid(row=1,column=1)
    f2.pack()
    root.mainloop()

def callback(event):
    x = int(event.x/size)
    y = int(event.y/size)
    canvas.create_rectangle(x*size,y*size,x*size+size,y*size+size, fill='black')
    global tab
    tab[y+1][x+1] = 1

def resetCell():
    global tab
    tab = core.initiate(numberSquare)
    for x in range(numberSquare):
        for y in range(numberSquare):
            canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='white', outline='white')

def selection():
    for x in range(numberSquare):
        for y in range(numberSquare):
            canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='white', outline='white')
    canvas.bind("<Button-1>", callback)
    canvas.grid(row=0,columnspan=2)
    resetC = Button(f2,text = 'RESET',command=resetCell)
    resetC.grid(row=1,column=0)

def begin():

    global tab
    global ntab
    ntab = np.copy(tab)
    draw()
    lifeCycle()
    #print(np.matrix(ntab))
    draw()
    while not np.array_equal(tab,ntab):
        time.sleep(.1)
        tab = np.copy(ntab)
        lifeCycle()
        #print(np.matrix(ntab))
        draw()


def lifeCycle():
    for x in range(numberSquare+2):
        for y in range(numberSquare+2):
            i = adj(x,y)
            vois[x][y]=i
            if (i<2 or i>3) and tab[x][y]==1:
                ntab[x][y]=0
            elif i==3 and tab[x][y] == 0:
                ntab[x][y]=1

def adj(x,y):
    i = 0
    if x > 1 and y > 1 and x < numberSquare and y < numberSquare:
        i = test(i,x,y,-1)
        i = test(i,x,y,1)
    return i

def randomize():
    resetCell()
    global tab
    tab = core.randomize(numberSquare)
    for x in range(numberSquare):
        for y in range(numberSquare):
            if tab[x+1][y+1] == 1:
                canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='black')
            else:
                canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='white', outline='white')
    canvas.grid(row=0,columnspan=2)

def test(i,x,y,e):
    if tab[x+e][y+e] == 1:
        i+=1
    if tab[x][y+e] == 1:
        i+=1
    if tab[x+e][y] == 1:
        i+=1
    if tab[x+e][y-e] == 1:
        i+=1
    return i

def draw():
    global ntab
    global tab
    for x in range(numberSquare):
        for y in range(numberSquare):
            if ntab[x+1][y+1] != tab[x+1][y+1]:
                if ntab[x+1][y+1] == 1:
                    canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='black')
                else:
                    canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='white', outline='white')
    canvas.grid(row=0,columnspan=2)
    root.update()
