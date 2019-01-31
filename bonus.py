from graph import *
from math import *

class Bonus:
    def __init__(self,x ,y, width):
        self.r = 10
        self.x = x + width//2 - self.r
        self.y = y + self.r
        self.object = object
        self.make()

    def make(self):
        brushColor('black')
        self.object = circle(self.x, self.y, self.r)
        return self

    def move(self):
        self.y += 4
        moveObjectTo(self.object, self.x, self.y)
        return self
    
    def block_contact(self, block_x, block_y, block_width, block_height):

        '''Касание снизу и сверху'''
        blockDown = block_y + block_height
        blockUp = block_y

        '''Если центр шарика располагается между левой и правой точкой блока'''
        if block_x <= self.x <= block_x + block_width:


            '''Если шарик сверху от блока'''
            circleDown = self.y + self.r
            if abs(blockUp - circleDown) < 1:
                self.y = blockUp - self.r - 1
                return True

        '''Если шарик располагается рядом с левым углом блока'''
        if self.x <= block_x <= self.x + self.r:
            d = sqrt(self.r ** 2 - (self.x - block_x)**2)

            '''Если шарик располагается снизу от левого угла'''
            y = self.y - d
            if abs(y - blockDown) < 1:
                self.y = blockDown + self.r + 1
                return True

            '''Если шарик располагается сверху от левого угла'''
            y = self.y + d
            if abs(blockUp - y) < 1:
                self.y = blockUp - self.r - 1
                return True

        '''Если шарик располагается рядом с правым углом блока'''
        if self.x - self.r <= block_x + block_width <= self.x:
            block_right = block_width + block_x
            d = sqrt(self.r ** 2 - (self.x - block_right) ** 2)

            '''Если шарик располагается снизу от правого угла'''
            y = self.y - d
            if abs(y - blockDown) < 1:
                self.y = blockDown + self.r + 1
                return True

            '''Если шарик располагается сверху от правого угла'''
            y = self.y + d
            if abs(blockUp - y) < 1:
                self.y = blockUp - self.r - 1
                return True

        '''Если центр шарика лежит между верхней и нижней границей блока'''
        if block_y <= self.y <= block_y + block_height:

            '''Если шарик лежит слева от блока'''
            circleX = self.x + self.r
            if abs(circleX - block_x) < 1:
                self.x = block_x - self.r - 1
                return True

            '''Если шарик лежит справа от блока'''
            circleX = self.x - self.r
            blockRight = block_x + block_width
            if abs(circleX - blockRight) < 1:
                self.x = blockRight + self.r + 1
                return True

        '''Если шарик касается нижнего угла блока'''
        blockDown = block_y + block_height
        if self.y + self.r <= blockDown <= self.y:
            d = sqrt(self.r ** 2 - (self.y - blockDown) ** 2)

            '''Если шарик лежит слева от нижнего угла'''
            circleX = self.x + d
            if abs(circleX - block_x) < 1:
                self.x = block_x - self.r - 1
                return True

            '''Если шарик лежит справа от нижнего угла'''
            circleX = self.x - d
            blockRight = block_x + block_width
            if abs(circleX - blockRight) < 1:
                self.x = blockRight + self.r + 1
                return True

        '''Если шарик касается верхнего угла блока'''
        if self.y - self.r <= block_y <= self.y:
            d = sqrt(self.r ** 2 - (self.y - block_y) ** 2)

            '''Если шарик лежит слева от верхнего угла'''
            circleX = self.x + d
            if abs(circleX - block_x) < 1:
                self.x = block_x - self.r - 1
                return True

            '''Если шарик лежит справа от верхнего угла'''
            circleX = self.x - d
            blockRight = block_x + block_width
            if abs(circleX - blockRight) < 1:
                self.x = blockRight + self.r + 1
                return True


        return False