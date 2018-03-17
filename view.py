import time
from tkinter import *
from core import Core

class View(object):

    def __init__(self,newNumber, newSize,randomly, pRoot):

        self.root = pRoot
        self.numberSquare = newNumber+1
        self.core = Core(self.numberSquare)
        self.size = newSize
        self.randomly = randomly
        self.root = pRoot
        self.f2 = Frame()
        self.canvas = Canvas(self.f2, width=self.size*(self.numberSquare-1), height=self.size*(self.numberSquare-1), background='white')
        self.start()

    def start(self):

        if (self.randomly):
            self.randomize()
        else:
            self.selection()
        run = Button(self.f2,text='RUN',command=self.begin)
        run.grid(row=2,columnspan=2,sticky='n')
        rand = Button(self.f2,text='RANDOM',command=self.randomize)
        rand.grid(row=1,column=1)
        self.f2.pack()
        self.root.mainloop()

    def action(self,event):
        x = int(event.x/self.size)
        y = int(event.y/self.size)
        print(x,y)
        self.core.switch(y,x)
        self.canvas.create_rectangle(x*self.size,
        y*self.size,x*self.size+self.size,y*self.size+self.size, fill='black')

    def resetCell(self):

        self.core.reset()
        for x in range(self.numberSquare):
            for y in range(self.numberSquare):
                self.canvas.create_rectangle(y*self.size-self.size,
                x*self.size-self.size,y*self.size,x*self.size, fill='white', outline='white')

    def selection(self):
        self.resetCell
        self.canvas.bind("<Button-1>", self.action)
        self.canvas.grid(row=0,columnspan=2)
        resetC = Button(self.f2,text = 'RESET',command=self.resetCell)
        resetC.grid(row=1,column=0)

    def randomize(self):
        self.core.randomize()
        self.render()

    def begin(self):
        while self.core.lifeCycle():
            time.sleep(.1)
            self.render()


    def render(self):
        for x in range(self.numberSquare):
            for y in range(self.numberSquare):
                if self.core.get(x+3,y+3):
                    self.canvas.create_rectangle(y*self.size-self.size,
                    x*self.size-self.size,y*self.size,x*self.size, fill='black')
                else:
                    self.canvas.create_rectangle(y*self.size-self.size,
                    x*self.size-self.size,y*self.size,x*self.size, fill='white', outline='white')
        self.canvas.grid(row=0,columnspan=2)
        self.root.update()
