from graph import *

class Brusochek:
    def __init__(self, x=50, y=20, dx=5, h=10, w=100, color=randColor()):
        self.x = x
        self.dx = dx
        self.h = h
        self.w = w
        self.color = color
        self.object = object
        self.first_p = (0, 0)
        self.second_p = (50, 50)
        self.y = y

    def set_down(self):
        moveObjectTo(self.object, self.x, self.y-self.h)
        return self

    def make_sqr(self):
        penColor('black')
        brushColor('red')
        self.object = rectangle(0, 0, 100, 10)
        return self

    def position_update(self):
        self.x = xCoord(self.object)
        return self.x

    def mov(self, width, turn):
        if self.x + self.w >= width - 5 and turn == VK_RIGHT:
            return

        if self.x <= 5 and turn == VK_LEFT:
            return

        if turn == VK_LEFT:
            self.x -= self.dx/2

        if turn == VK_RIGHT:
            self.x += self.dx

        if turn == VK_RIGHT or turn == VK_LEFT:
            moveObjectTo(self.object, self.x, self.y - self.h)
