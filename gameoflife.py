import numpy as np
import time, random
from tkinter import *

taille=30
d=15

tab = [[0]*taille for e in range(taille)]
for i in range(int((taille/2)**2)):
    tab[random.randint(1,taille-1)][random.randint(1,taille-1)] = 1
ntab = np.copy(tab)
vois = [[0]*taille for e in range(taille)]

root = Tk()
canvas = Canvas(root, width=d*(taille-1), height=d*(taille-1), background='white')

def vie():
    for x in range(taille):
        for y in range(taille):
            i = adj(x,y)
            vois[x][y]=i
            if (i<2 or i>3) and tab[x][y]==1:
                ntab[x][y]=0
            elif i==3 and tab[x][y] == 0:
                ntab[x][y]=1

def adj(x,y):
    i = 0
    if x > 0 and y > 0 and x < taille-1 and y < taille-1:
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
    for x in range(taille):
        for y in range(taille):
            if ntab[x][y] != tab[x][y]:
                if ntab[x][y] == 1:
                    canvas.create_rectangle(y*d-d,x*d-d,y*d,x*d, fill='black')
                else:
                    canvas.create_rectangle(y*d-d,x*d-d,y*d,x*d, fill='white', outline='white')
    canvas.pack()
    root.update()
print(np.matrix(tab))
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
