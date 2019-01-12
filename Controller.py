from graph import *
from enemy import Enemy
from Circle import CircleClass


class ControllerClass:
    def __init__(self, filename, width, height, frameSize, radius, x=0, y=0, score=0):
        a = self.readFile(filename)
        self.a = a
        self.x = x
        self.y =y
        self.width = width
        self.height = height
        self.Block_width = (width-6)//10
        self.Block_height = 20
        self.frameSize = frameSize
        self.circlePosX = width/2
        self.circlePosY = height - self.Block_height*2
        self.circleRadius = radius
        self.score = score
        self.score_text = "Score - "
        self.mklable()
        self.enemys = []
        self.dots = []
        self.set_circles()
        self.set_objects()


    def set_objects(self):
        self.x = 8
        self.y = 8
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                if self.a[i][j] != '_':
                    self.enemys.append(Enemy(self.x, self.y, self.x + self.Block_width, self.y + self.Block_height, int(self.a[i][j])))
                self.x += self.Block_width
            self.x = 8
            self.y += self.Block_height
        return self

    def set_circles(self):
        self.dots.append(CircleClass(self.width - self.frameSize, self.height - self.frameSize, self.circlePosX, self.circlePosY, 1, 1, self.circleRadius))

    def readFile(self, filename):
        file = open(filename, 'r', encoding='utf-8')
        a = file.readlines()

        for i in range(len(a)):
            a[i] = a[i].strip()
        return a

    def mklable(self):
        label(self.score_text + str(self.score), 0, self.height + 20)

    def cirleMov(self):
        for block in self.enemys:
            for dot in self.dots:
                if dot.blocks_contact(block.x, block.y, self.Block_width,  self.Block_height) == True:
                    self.score += block.strength
                dot.move()
                moveObjectTo(dot.obj(), dot.getPosition('x'), dot.getPosition('y'))

