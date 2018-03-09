import numpy as np
import time, random
from tkinter import *

root = Tk()
canvas = Canvas(root, width=size*(numberSquare-1), height=size*(numberSquare-1), background='white')
vois = []
tab = []
ntab = []

def start(newNumber,newSize):

    global numberSquare
    numberSquare = newNumber
    global size
    size = newSize
    global vois
    vois = [[0]*numberSquare for e in range(numberSquare)]
    global tab
    tab = [[0]*numberSquare for e in range(numberSquare)]
    for i in range(int((numberSquare/2)**2)):
        tab[random.randint(1,numberSquare-1)][random.randint(1,numberSquare-1)] = 1
    global ntab
    ntab = np.copy(tab)
    dessin(tab,ntab)
    vie()
    #print(np.matrix(ntab))
    dessin(tab,ntab)
    while not np.array_equal(tab,ntab):
        time.sleep(.1)
        tab = np.copy(ntab)
        vie()
        #print(np.matrix(ntab))
        dessin(tab,ntab)


def vie():
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

def dessin(tab,ntab):
    for x in range(numberSquare):
        for y in range(numberSquare):
            if ntab[x][y] != tab[x][y]:
                if ntab[x][y] == 1:
                    canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='black')
                else:
                    canvas.create_rectangle(y*size-size,x*size-size,y*size,x*size, fill='white', outline='white')
    canvas.pack()
    root.update()
