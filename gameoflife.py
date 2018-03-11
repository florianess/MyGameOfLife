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
        for i in range(int((numberSquare/2)**2)):
            tab[random.randint(1,numberSquare-1)][random.randint(1,numberSquare-1)] = 1
        begin()
    else:
        selection()

def callback(event):
    x = int(event.x/size)
    y = int(event.y/size)
    print ("clicked at",x , y)
    canvas.create_rectangle(x*size,y*size,x*size+size,y*size+size, fill='black')
    global tab
    tab[y][x] = 1
    print (np.matrix(tab))

def resetCell():
    print('RESET')
    global tab
    for x in range(numberSquare):
        for y in range(numberSquare):
            canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='white', outline='black')
            tab[x][y]=0

def selection():
    for x in range(numberSquare):
        for y in range(numberSquare):
            canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='white', outline='black')
    canvas.bind("<Button-1>", callback)
    canvas.pack()
    run = Button(root,text='RUN',command=begin)
    run.pack()
    resetC = Button(root,text = 'RESET',command=resetCell)
    resetC.pack()
    root.mainloop()

def begin():

    global tab
    global ntab
    ntab = np.copy(tab)
    draw(tab,ntab)
    lifeCycle()
    #print(np.matrix(ntab))
    draw(tab,ntab)
    while not np.array_equal(tab,ntab):
        time.sleep(.1)
        tab = np.copy(ntab)
        lifeCycle()
        #print(np.matrix(ntab))
        draw(tab,ntab)


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

def draw(tab,ntab):
    for x in range(numberSquare):
        for y in range(numberSquare):
            if ntab[x][y] != tab[x][y]:
                if ntab[x][y] == 1:
                    canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='black')
                else:
                    canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='white', outline='white')
    canvas.pack()
    root.update()
