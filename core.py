import numpy as np
import time, random

def initiate(numberSquare):
    tab = [[0]*(numberSquare+2) for e in range(numberSquare+2)]
    print (np.matrix(tab))
    return tab

def randomize(numberSquare):
    tab = []
    for i in range(int(((numberSquare+2)/2)**2)):
        tab[random.randint(1,numberSquare+1)][random.randint(1,numberSquare+1)] = 1
    return tab
