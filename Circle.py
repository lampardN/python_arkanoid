from graph import *
from math import sqrt


def top_bottom(x0, y0, x1, y_up, y_down, r):
    koren = sqrt(r**2 - (x1 - x0)**2)
    y1 = y0 + koren
    y2 = y0 - koren
    return min(
        abs(y_up - y1),
        abs(y_up - y2),
        abs(y_down - y1),
        abs(y_down - y2)
    )


def left_right(x0, y0, y1, x_right, x_left, r):
    koren = sqrt(r**2 -(y1 - y0)**2)
    x1 = x0 + koren
    x2 = x0 - koren
    return min(
        abs(x_right - x1),
        abs(x_right - x2),
        abs(x_left - x1),
        abs(x_left - x2)
    )


class Circle:
    def __init__(self, x=100, y=100, dx=1, dy=1, radius=5, color=(randint(0, 255), randint(0, 255), randint(0, 255))):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.pos = ''
        self.radius = radius
        self.color = color
        self.object = object
        self.mk_circle()

    def mk_circle(self):
        brushColor(self.color)
        self.object = circle(self.x - self.radius, self.y - self.radius, self.radius)

    def circle_in_window(self, window_width, window_height):
        if self.x <= self.radius:
            self.dx *= -1
        if self.y - self.radius <= -self.radius:
            self.dy *= -1
        if self.x + self.radius >= window_width:
            self.dx *= -1
        if self.y + self.radius >= window_height:
            self.pos = 'out'
        return self

    def move(self):
        self.x += self.dx
        self.y += self.dy

        objectX = self.x - self.radius
        objectY = self.y - self.radius

        moveObjectTo(self.object, objectX, objectY)
        return self

    def check_platform_contact(self, platform_pos_x, platform_pos_y, platform_width, platform_height):
        self.block_contact(platform_pos_x, platform_pos_y, platform_width, platform_height)

    def block_contact(self, block_x, block_y, block_width, block_height):

        '''Касание снизу и сверху'''
        blockDown = block_y + block_height
        blockUp = block_y

        '''Если центр шарика располагается между левой и правой точкой блока'''
        if block_x <= self.x <= block_x + block_width:

            '''Если шарик снизу от блока'''
            circleUp = self.y - self.radius
            if abs(circleUp - blockDown) < 1:
                self.y = blockDown + self.radius + 1
                self.dy *= -1
                return True

            '''Если шарик сверху от блока'''
            circleDown = self.y + self.radius
            if abs(blockUp - circleDown) < 1:
                self.y = blockUp - self.radius - 1
                self.dy *= -1
                return True

        '''Если шарик располагается рядом с левым углом блока'''
        if self.x <= block_x <= self.x + self.radius:
            d = sqrt(self.radius ** 2 - (self.x - block_x)**2)

            '''Если шарик располагается снизу от левого угла'''
            y = self.y - d
            if abs(y - blockDown) < 1:
                self.y = blockDown + self.radius + 1
                self.dy *= -1
                return True

            '''Если шарик располагается сверху от левого угла'''
            y = self.y + d
            if abs(blockUp - y) < 1:
                self.y = blockUp - self.radius - 1
                self.dy *= -1
                return True

        '''Если шарик располагается рядом с правым углом блока'''
        if self.x - self.radius <= block_x + block_width <= self.x:
            block_right = block_width + block_x
            d = sqrt(self.radius ** 2 - (self.x - block_right) ** 2)

            '''Если шарик располагается снизу от правого угла'''
            y = self.y - d
            if abs(y - blockDown) < 1:
                self.y = blockDown + self.radius + 1
                self.dy *= -1
                return True

            '''Если шарик располагается сверху от правого угла'''
            y = self.y + d
            if abs(blockUp - y) < 1:
                self.y = blockUp - self.radius - 1
                self.dy *= -1
                return True

        '''Если центр шарика лежит между верхней и нижней границей блока'''
        if block_y <= self.y <= block_y + block_height:

            '''Если шарик лежит слева от блока'''
            circleX = self.x + self.radius
            if abs(circleX - block_x) < 1:
                self.x = block_x - self.radius - 1
                self.dx *= -1
                return True

            '''Если шарик лежит справа от блока'''
            circleX = self.x - self.radius
            blockRight = block_x + block_width
            if abs(circleX - blockRight) < 1:
                self.x = blockRight + self.radius + 1
                self.dx *= -1
                return True

        '''Если шарик касается нижнего угла блока'''
        blockDown = block_y + block_height
        if self.y + self.radius <= blockDown <= self.y:
            d = sqrt(self.radius ** 2 - (self.y - blockDown) ** 2)

            '''Если шарик лежит слева от нижнего угла'''
            circleX = self.x + d
            if abs(circleX - block_x) < 1:
                self.x = block_x - self.radius - 1
                self.dx *= -1
                return True

            '''Если шарик лежит справа от нижнего угла'''
            circleX = self.x - d
            blockRight = block_x + block_width
            if abs(circleX - blockRight) < 1:
                self.x = blockRight + self.radius + 1
                self.dx *= -1
                return True

        '''Если шарик касается верхнего угла блока'''
        if self.y - self.radius <= block_y <= self.y:
            d = sqrt(self.radius ** 2 - (self.y - block_y) ** 2)

            '''Если шарик лежит слева от верхнего угла'''
            circleX = self.x + d
            if abs(circleX - block_x) < 1:
                self.x = block_x - self.radius - 1
                self.dx *= -1
                return True

            '''Если шарик лежит справа от верхнего угла'''
            circleX = self.x - d
            blockRight = block_x + block_width
            if abs(circleX - blockRight) < 1:
                self.x = blockRight + self.radius + 1
                self.dx *= -1
                return True


        return False
