from graph import *


class Enemy:
    def __init__(self, x=0, y=0, width=100, height=10, strenght=1, color=randColor()):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.strenght = strenght
        self.color = color
        self.object = object

    def set_color(self):
        if self.strenght == 1:
            self.color = 'purple'
        elif self.strenght == 2:
            self.color = 'light blue'
        elif self.strenght == 3:
            self.color = 'cyan'
        elif self.strenght == 4:
            self.color = 'red'
        elif self.strenght == 5:
            self.color = 'pink'
        elif self.strenght == 6:
            self.color = 'green'
        return self

    def make_sqr(self):
        penSize(3)
        penColor('black')
        brushColor(self.color)
        self.object = rectangle(self.x, self.y, self.width, self.height)
        return self

    def update_object(self):
        if self.strenght == -1:
            deleteObject(self.object)
        deleteObject(self.object)
        penSize(3)
        penColor('black')
        brushColor(self.color)
        self.object = rectangle(self.x, self.y, self.width, self.height)
        return self
