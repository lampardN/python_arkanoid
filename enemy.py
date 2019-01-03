from graph import *


class Enemy:
    def __init__(self, x=0, y=0, w=100, h=10, s=1, color=randColor()):
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.s = s
        self.color = color
        self.object = object

    def set_color(self):
        if self.s == 0:
            self.color = 'purple'
        elif self.s == 1:
            self.color = 'light blue'
        elif self.s == 2:
            self.color = 'cyan'
        elif self.s == 3:
            self.color = 'red'
        elif self.s == 4:
            self.color = 'pink'
        elif self.s == 5:
            self.color = 'green'
        return self

    def make_sqr(self):
        penSize(3)
        penColor('black')
        brushColor(self.color)
        self.object = rectangle(self.x, self.y, self.w, self.h)
        return self

    def update_object(self):
        if self.s == -1:
            deleteObject(self.object)
        deleteObject(self.object)
        penSize(3)
        penColor('black')
        brushColor(self.color)
        self.object = rectangle(self.x, self.y, self.w, self.h)
        return self
