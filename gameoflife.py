import numpy as np
import time, random
from tkinter import *

numberSquare = 0
size = 0
root = Tk()
canvas = 0
vois = []
tab = []
ntab = []

def start(newNumber, newSize):

    global numberSquare
    numberSquare = newNumber
    global size
    size = newSize
    global canvas
    canvas = Canvas(root, width=size*(numberSquare-1), height=size*(numberSquare-1), background='white')
    global vois
    vois = [[0]*numberSquare for e in range(numberSquare)]
    global tab
    tab = [[0]*numberSquare for e in range(numberSquare)]

    randomly = input("Generate randomly the cells? (Y or N)\n")
    if (randomly == "Y"):
        randomize()
    else:
        selection()
    run = Button(root,text='RUN',command=begin)
    run.pack()
    rand = Button(root,text='RANDOM',command=randomize)
    rand.pack()
    close = Button(root,text='CLOSE',command=root.quit)
    close.pack()
    root.mainloop()

def callback(event):
    x = int(event.x/size)
    y = int(event.y/size)
    canvas.create_rectangle(x*size,y*size,x*size+size,y*size+size, fill='black')
    global tab
    tab[y][x] = 1

def resetCell():
    global tab
    for x in range(numberSquare):
        for y in range(numberSquare):
            canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='white', outline='white')
            tab[x][y]=0

def selection():
    for x in range(numberSquare):
        for y in range(numberSquare):
            canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='white', outline='white')
    canvas.bind("<Button-1>", callback)
    canvas.pack()
    resetC = Button(root,text = 'RESET',command=resetCell)
    resetC.pack()

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
    for x in range(numberSquare):
        for y in range(numberSquare):
            i = adj(x,y)
            vois[x][y]=i
            if (i<2 or i>3) and tab[x][y]==1:
                ntab[x][y]=0
            elif i==3 and tab[x][y] == 0:
                ntab[x][y]=1

def adj(x,y):
    i = 0
    if x > 0 and y > 0 and x < numberSquare-1 and y < numberSquare-1:
        i = test(i,x,y,-1)
        i = test(i,x,y,1)
    return i

def randomize():
    resetCell()
    global tab
    for i in range(int((numberSquare/2)**2)):
        tab[random.randint(1,numberSquare-1)][random.randint(1,numberSquare-1)] = 1
    for x in range(numberSquare):
        for y in range(numberSquare):
            if tab[x][y] == 1:
                canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='black')
            else:
                canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='white', outline='white')
    canvas.pack()

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
            if ntab[x][y] != tab[x][y]:
                if ntab[x][y] == 1:
                    canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='black')
                else:
                    canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='white', outline='white')
    canvas.pack()
    root.update()
