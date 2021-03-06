import numpy as np
import random

class Core(object):

    def __init__(self,numberSquare):
        self.matrixSize = numberSquare+5
        self.tab = np.zeros((self.matrixSize,self.matrixSize),dtype=int)
        self.cells = {}

    def randomize(self):
        self.reset()
        for i in range(int(((self.matrixSize)/2)**2)):
            self.tab[random.randint(1,self.matrixSize-1)][random.randint(1,self.matrixSize-1)] = 1

    def lifeCycle(self):
        self.log()
        nTab = np.zeros((self.matrixSize,self.matrixSize),dtype=int)
        for x in range(self.matrixSize):
            for y in range(self.matrixSize):
                i = self.adj(x,y)
                if ( i<2 or i>3 ) and self.tab[x][y] == 1:
                    nTab[x][y] = 0
                elif i == 3 and self.tab[x][y] == 0:
                    nTab[x][y]=1
                else:
                    nTab[x][y]=self.tab[x][y]
        if (not (self.tab==nTab).all()):
            self.tab = np.copy(nTab)
            return True
        else:
            return False

    def adj(self,x,y):
        i = 0
        if x > 1 and y > 1 and x < self.matrixSize-1 and y < self.matrixSize-1:
            i = self.test(i,x,y,-1)
            i = self.test(i,x,y,1)
        return i

    def test(self,i,x,y,e):
        if self.tab[x+e][y+e] == 1:
            i+=1
        if self.tab[x][y+e] == 1:
            i+=1
        if self.tab[x+e][y] == 1:
            i+=1
        if self.tab[x+e][y-e] == 1:
            i+=1
        return i

    def switch(self,x,y):
        self.tab[x+4,y+4] = 1;
        self.addCell(x+4,y+4)

    def reset(self):
        self.tab = [[0]*(self.matrixSize) for e in range(self.matrixSize)]

    def get(self,x,y):
        return self.tab[x][y]

    def log(self):
        print (np.matrix(self.tab))

    def addCell(self,x,y):

        for i in range (3):
            if not x+i-1 in self.cells:
                self.cells[x+i-1] = []
            for n in range (3):
                if not y+1-n in self.cells[x+i-1]:
                    self.cells[x+i-1].append(y+1-n)
            print (self.cells)
