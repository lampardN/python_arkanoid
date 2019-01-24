from graph import *
from random import randint
from Circle import Circle
from enemy import Enemy
from platform import Platform


class ControllerClass:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.x = 0
        self.y = 0
        self.blocks_in_line = 10
        self.radius = 10
        self.dots = []
        self.enemies = []
        self.platform = Platform(100, 20, self.window_width, self.window_height)
        self.score = 0
        self.score_label = 'Score >> '
        self.make_label()
        self.make_circles()
        self.set_enemies()

    def set_enemies(self):
        blockWidth = self.window_width // self.blocks_in_line
        blockHeight = 20
        top = 0
        left = -blockWidth
        for i in range(3):
            for j in range(self.blocks_in_line):
                strength = randint(1, 10)
                left += blockWidth
                if strength == 0: continue
                self.enemies.append(
                    Enemy(left, top, blockWidth, blockHeight, strength, 1, 'black')
                )

            top += blockHeight
            left = -blockWidth

    def make_circles(self):
        penSize(0)
        self.dots.append(Circle(self.platform.x + self.platform.width//2, self.platform.y - self.radius*2, 1, 1, self.radius))

    def make_label(self):
        label(self.score_label + str(self.score), 0, self.window_height + 20)

    def circle_move(self):
        if self.platform.p == 0:
            for dot in self.dots:
                moveObjectTo(dot.object, self.platform.x + self.platform.width//2 - self.radius, self.platform.y - self.radius*2 - 4)
                dot.x = xCoord(dot.object)
                dot.y = yCoord(dot.object)
        else:
            for dot in self.dots:
                self.circle_block_contact()
                dot.circle_in_window(self.window_width, self.window_height)
                dot.check_platform_contact(self.platform.x, self.platform.y, self.platform.width, self.platform.height)
                dot.move()
            self.lose()

    def circle_block_contact(self):
        for block in self.enemies:
            for dot in self.dots:
                if dot.block_contact(block.x, block.y, block.width, block.height):
                    self.score += block.strength
                    self.make_label()
                    block.strength -= 1
                    block.set_color()
                    if block.strength <= 0:
                        deleteObject(block.object)
                        del self.enemies[self.enemies.index(block)]
                    else:
                        block.update()

    def lose(self, event):
        for i in self.dots:
            if i.pos == 'out':
                self.platform.p = 0
                moveObjectTo(self.platform.object, self.window_width - 50, self.window_height - 20)
                for dot in self.dots:
                    deleteObject(dot.object)
                    del dot
                self.dots = []
                self.make_circles()
                for block in self.enemies:
                    deleteObject(block)
                    del block
                self.set_enemies()
                self.score = 0
                self.make_label()
                i.pos = ''
