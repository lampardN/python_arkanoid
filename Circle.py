from graph import *

class CircleClass:
    def __init__(self, x=0, y=0, dx=1, dy=1, radius=1, color=randColor()):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.object = object
        self.r = radius
        self.col = color

    def getPosition(self, pType):
        if pType == 'x':
            return self.x
        else:
            return self.y

    def setPosition(self, x=1, y=1):
        self.x = x
        self.y = y
        return self

    def getOffset(self, oType):
        if oType == 'x':
            return self.dx
        else:
            return self.dy

    def setOffset(self, dx=None, dy=None):
        if not (dx is None):
            self.dx = dx
        if not (dy is None):
            self.dy = dy
        return self

    def radius(self, r=None):
        if r is None:
            return self.r
        else:
            self.r = r
            return self

    def color(self, color=None):
        if color is None:
            return self.col
        else:
            self.col = color
            return self

    def obj(self, object=None):
        if object is None:
            return self.object
        else:
            self.object = object
            return self

    def createCircle(self):
        brushColor(self.color())
        penColor(self.color())
        self.object = circle(self.getPosition('x'), self.getPosition('y'), self.radius())
        return self

    def move(self):
        self.x += self.getOffset('x')
        self.y += self.getOffset('y')

