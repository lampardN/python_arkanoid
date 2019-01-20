from graph import *


class Enemy:
    def __init__(self, x, y, width, height, strength, borderWidth, borderColor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.strength = strength
        self.color = ''
        self.object = None
        self.borderWidth = borderWidth
        self.borderColor = borderColor
        self.set_color()
        self.mk_enemy()

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

    def mk_enemy(self):
        penSize(self.borderWidth)
        penColor(self.borderColor)
        brushColor(self.color)
        self.object = rectangle(self.x, self.y, self.x + self.width, self.y + self.height)

    def update(self):
        if self.strength > 0:
            deleteObject(self.object)
            penSize(1)
            penColor('black')
            brushColor(self.color)
            self.object = rectangle(self.x, self.y, self.x + self.width, self.y + self.height)
        return self
