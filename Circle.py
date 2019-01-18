from graph import *
from math import sqrt


def top_bottom(x0, y0, x1, y_up, y_down, r):
    koren = sqrt(r**2 - (x1 - x0)**2)
    y1 = y0 + koren
    y2 = y0 - koren
    return min(abs(y_up-y1), abs(y_up-y2),
               abs(y_down-y1), abs(y_down-y2))


def left_right(x0, y0, y1,x_right, x_left, r):
    koren = sqrt(r**2 -(y1 - y0)**2)
    x1 = x0 + koren
    x2 = x0 - koren
    return min(abs(x_right-x1 - 10), abs(x_right-x2- 10),
               abs(x_left-x1- 10), abs(x_left-x2-10))


class Circle:
    def __init__(self, x=100, y=100, dx=1, dy=1, radius=5, color='black'):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color
        self.object = object
        self.mk_circle()

    def mk_circle(self):
        brushColor(self.color)
        self.object = circle(self.x, self.y, self.radius)

    def circle_in_window(self, window_width, window_height):
        if self.x - self.radius <= -self.radius:
            self.dx *= -1
        if self.y - self.radius <= -self.radius:
            self.dy *= -1
        if self.x + self.radius >= window_width:
            self.dx *= -1
        if self.y + self.radius >= window_height:
            self.dy *= -1
        return self

    def move(self):
        self.x += self.dx
        self.y += self.dy
        moveObjectTo(self.object, self.x, self.y)
        return self

    def check_platform_contact(self, platform_pos_x, platform_pos_y, platform_width):
        if platform_pos_x <= self.x <= platform_pos_x + platform_width and self.y + self.radius*2 == platform_pos_y:
            self.dy *= -1
        return self

    def block_contact(self, platform_x, platform_y, platform_width, platform_height):
        x1 = None
        y1 = None
        if platform_x <= self.x <= platform_x + platform_width:
            x1 = self.x
        if self.x <= platform_x <= self.x + self.radius:
            x1 = platform_x
        if self.x - self.radius <= platform_x + platform_width <= self.x:
            x1 = platform_x + platform_width
        if platform_y <= self.y <= platform_y + platform_height:
            y1 = self.y
        if self.y <= platform_y <= self.y + self.radius:
            y1 = platform_y
        if self.y - self.radius <= platform_y + platform_height <= self.y:
            y1 = platform_y + platform_height

        if x1 != None:
            if top_bottom(self.x, self.y, x1, platform_y, platform_height + platform_y, self.radius) < 1:
                self.dy *= -1
                return True

        if y1 != None:
            if left_right(self.x, self.y, y1, platform_x, platform_x + platform_width, self.radius) < 1:
                self.dx *= -1
                return True

        return False
