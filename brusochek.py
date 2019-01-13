from graph import *


class Brusochek:
    def __init__(self,windowWidth, x=50, y=20, dx=5, height=10, width=100, color=randColor()):
        self.x = x
        self.y = y
        self.dx = dx
        self.height = height
        self.width = width
        self.color = color
        self.object = object
        self.p = 0
        self.make_sqr()
        self.set_down(windowWidth)

    def set_down(self, width):
        moveObjectTo(self.object, width/2 - self.width/2, self.y-self.height)
        return self

    def make_sqr(self):
        penSize(4)
        penColor('black')
        brushColor('red')
        self.object = rectangle(0, 0, 100, 15)
        penSize(0)
        return self

    def position_update(self):
        self.x = xCoord(self.object)
        return self.x

    def mov(self, width, turn):
        if turn == VK_SPACE and self.p == 0:
            self.p += 1
        else:
            if self.x + self.width >= width - 5 and turn == VK_RIGHT:
                return

            if self.x <= 5 and turn == VK_LEFT:
                return

            if turn == VK_LEFT:
                self.x -= self.dx/1.5

            if turn == VK_RIGHT:
                self.x += self.dx

            if turn == VK_RIGHT or turn == VK_LEFT:
                moveObjectTo(self.object, self.x, self.y - self.height)
