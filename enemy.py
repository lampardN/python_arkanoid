from graph import *


class Enemy:
    def __init__(self, x=0, y=0, width=100, height=10, strength=1, color=randColor()):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.strength = strength
        self.color = color
        self.object = object
        self.set_color()
        self.make_sqr()

    def set_color(self):
        if self.strength == 1:
            self.color = 'purple'
        elif self.strength == 2:
            self.color = 'light blue'
        elif self.strength == 3:
            self.color = 'cyan'
        elif self.strength == 4:
            self.color = 'red'
        elif self.strength == 5:
            self.color = 'pink'
        elif self.strength == 6:
            self.color = 'green'
        return self

    def make_sqr(self):
        penSize(3)
        penColor('black')
        brushColor(self.color)
        self.object = rectangle(self.x, self.y, self.width, self.height)
        return self

    def update_object(self):
        if self.strength == -1:
            deleteObject(self.object)
        deleteObject(self.object)
        penSize(3)
        penColor('black')
        brushColor(self.color)
        self.object = rectangle(self.x, self.y, self.width, self.height)
        return self
