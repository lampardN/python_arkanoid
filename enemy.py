from random import randint
from graph import *


def toHex(num):
    string = ''
    six = [0, 1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9, 'A', 'B', 'C', 'D', 'E', 'F']
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
        self.Red = 0
        self.deltaRed = 25
        self.Green = 250
        self.deltaGreen = 25
        self.Blue = 0
        self.deltaBlue = 0
        self.object = object
        self.borderWidth = borderWidth
        self.borderColor = borderColor
        self.mk_enemy()

    def mk_enemy(self):
        penSize(self.borderWidth)
        penColor(self.borderColor)
        Red = 0 + self.deltaRed * self.strength
        Green = 250 - self.deltaGreen * self.strength
        Blue = 0
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
