from random import randint
from graph import *


class Enemy:
    def __init__(self,
                 x,
                 y,
                 width,
                 height,
                 strength,
                 borderWidth,
                 borderColor,
                 Red=randint(0, 255),
                 Green=randint(0,255),
                 Blue=randint(0,255)
                 ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.strength = strength
        self.Red = Red
        self.deltaRed = Red // 10
        self.Green = Green
        self.deltaGreen = Green // 10
        self.Blue = Blue
        self.deltaBlue = Blue // 10
        self.object = object
        self.borderWidth = borderWidth
        self.borderColor = borderColor
        self.set_color()
        self.mk_enemy()

    def set_color(self):

        return self

    def mk_enemy(self):
        penSize(self.borderWidth)
        penColor(self.borderColor)
        Red = 0
        Green = 0
        Blue = 0
        for i in range(self.strength):
            Red += self.deltaRed
            Green += self.deltaGreen
            Blue += self.deltaBlue
        self.Red = Red
        self.Green = Green
        self.Blue = Blue
        brushColor((Red, Green, Blue))
        self.object = rectangle(self.x, self.y, self.x + self.width, self.y + self.height)

    def update(self):
        if self.strength > 0:
            deleteObject(self.object)
            penSize(1)
            penColor('black')
            self.Red -= self.deltaRed
            self.Green -= self.deltaGreen
            self.Blue -= self.deltaBlue
            brushColor((self.Red, self.Green, self.Blue))
            self.object = rectangle(self.x, self.y, self.x + self.width, self.y + self.height)
        return self
