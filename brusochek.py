from graph import *

class Brusochek:
    def __init__(self, x=50,y=20,dx=5, h=10, w=100, color = randColor()):
        self.x = x
        self.dx = dx
        self.h = h
        self.w = w
        self.color = color
        self.object = object
        self.first_p = (0,0)
        self.second_p = (50,50)
        self.y = y

    def set_down(self):
        moveObjectTo(self.object,self.x,self.y-self.h)
        return self

    def make_sqr(self):
        penColor('black')
        brushColor('red')
        self.object = rectangle(0, 0, 100, 10)
        return self

    def position_update(self):
        self.x = xCoord(self.object)
        return self.x