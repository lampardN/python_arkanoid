from random import randint
from graph import *


def toHex(num):
    string = ''
    six = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    while num > 1:
        string += str(six[num%16])
        num //= 16
    while len(string) != 2:
        string = '0' + string
    return string[::-1]


class Enemy:
    def __init__(self,
                 x,
                 y,
                 width,
                 height,
                 strength,
                 borderWidth,
                 borderColor,
                 ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.strength = strength
        self.Red = 140
        self.deltaRed = 11
        self.Green = 60
        self.deltaGreen = 14
        self.Blue = 215
        self.deltaBlue = 21
        self.object = object
        self.borderWidth = borderWidth
        self.borderColor = borderColor
        self.mk_enemy()

    def mk_enemy(self):
        penSize(self.borderWidth)
        penColor(self.borderColor)
        Red = 140 + self.deltaRed * self.strength
        Green = 60 + self.deltaGreen * self.strength
        Blue = 215 - self.deltaBlue * self.strength
        self.Red = Red
        self.Green = Green
        self.Blue = Blue
        brushColor('#'+toHex(Red)+toHex(Green)+toHex(Blue))
        self.object = rectangle(self.x, self.y, self.x + self.width, self.y + self.height)

    def update(self):
        if self.strength > 0:
            deleteObject(self.object)
            penSize(1)
            penColor('black')
            self.Red -= self.deltaRed
            self.Green += self.deltaGreen
            self.Blue += self.deltaBlue
            brushColor('#'+toHex(self.Red)+toHex(self.Green)+toHex(self.Blue))
            self.object = rectangle(self.x, self.y, self.x + self.width, self.y + self.height)
        return self
