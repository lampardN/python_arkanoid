from graph import *


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
        if self.x - self.radius <= 0:
            self.dx *= -1
        if self.y - self.radius <= 0:
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
