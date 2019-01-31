from graph import *
from random import randint
from Circle import Circle
from enemy import Enemy
from platform import Platform
from bonus import Bonus


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
        self.bonuses = []
        self.platform = Platform(100, 20, self.window_width, self.window_height)
        self.score = 0
        self.score_label = 'Score >> '
        self.make_label()
        self.make_circles()
        self.random = randint(0, 300)
        self.set_enemies()

    def set_enemies(self):
        blockWidth = self.window_width // self.blocks_in_line
        blockHeight = 20
        top = 0
        left = -blockWidth
        for i in range(3):
            for j in range(self.blocks_in_line):
                strength = randint(1, 1)
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
                self.platform.update_timer()
            if len(self.bonuses) != 0:
                for bonus in self.bonuses:
                    bonus.move()
                    if bonus.block_contact(self.platform.x,
                                           self.platform.y,
                                           self.platform.width,
                                           self.platform.height):
                        self.platform.effect += 1
                        self.platform.update_effect()
                        deleteObject(bonus.object)
                        del self.bonuses[self.bonuses.index(bonus)]
            self.lose()

    def circle_block_contact(self):
        for block in self.enemies:
            for dot in self.dots:
                if dot.block_contact(block.x, block.y, block.width, block.height):
                    self.score += block.strength
                    self.make_label()
                    block.strength -= 1
                    if block.strength <= 0:
                        if randint(0, 0) == 0:
                            self.bonuses.append(Bonus(block.x, block.y, block.width))
                        deleteObject(block.object)
                        del self.enemies[self.enemies.index(block)]
                    else:
                        block.update()

    def keys(self, event):
        if event.keycode == VK_ESCAPE:
            return close()
        if event.keycode == VK_SPACE:
            return self.platform.move('VK_SPACE')
        if event.keycode == VK_RIGHT:
            return self.platform.move('VK_RIGHT')
        if event.keycode == VK_LEFT:
            return self.platform.move('VK_LEFT')
        if event.keycode == VK_RETURN:
            return self.lose('VK_ENTER')

    def lose(self, event=None):
        for i in self.dots:
            if i.pos == 'out' or len(self.enemies) == 0:
                for d in self.dots:
                    d.dx = 0
                    d.dy = 0
                self.platform.dx = 0
                if event == 'VK_ENTER':
                    self.platform.dx = 8
                    self.platform.p = 0
                    self.platform.x = self.platform.window_width//2 - self.platform.width//2
                    moveObjectTo(
                        self.platform.object,
                        self.window_width//2 - self.platform.width//2,
                        self.window_height - 20
                    )
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
