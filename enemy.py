from graph import *


class Enemy:
    def __init__(self, x, y, window_width, window_height, strength):
        self.x = x
        self.y = y
        self.window_width = window_width
        self.window_height = window_height
        self.width = window_width//10
        self.height = 20
        self.strength = strength
        self.color = ''
        self.object = object
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
        penSize(1)
        penColor('black')
        brushColor(self.color)
        self.object = rectangle(self.x, self.y, self.x + self.width, self.y + self.height)

    def update(self):
        if self.strength <= 0:
            deleteObject(self.object)
        else:
            deleteObject(self.object)
            penSize(1)
            penColor('black')
            brushColor(self.color)
            self.object = rectangle(self.x, self.y, self.x + self.width, self.y + self.height)
        return self
