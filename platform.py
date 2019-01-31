from graph import *


class Platform:
    def __init__(self, width=100, height=10, window_width=1, window_height=1):
        self.window_width = window_width
        self.window_height = window_height
        self.width = width
        self.height = height
        self.x = self.window_width//2 - self.width//2
        self.y = self.window_height - self.height
        self.dx = 8
        self.p = 0
        self.effect = 0
        self.timer = 0
        self.object = object
        self.mk_platform()

    def mk_platform(self):
        brushColor('red')
        penSize(4)
        penColor('black')
        self.object = rectangle(self.x, self.y, self.x + self.width, self.y + self.height)
        return self

    def update_timer(self):
        self.timer += 1
        if self.timer == 1000:
            deleteObject(self.object)
            self.width = 100
            penSize(4)
            brushColor('red')
            self.object = rectangle(self.x, self.y, self.x + self.width, self.y + self.height)
            self.effect = 0
            self.timer = 0


    def update_effect(self):
        if self.effect > 0:
            deleteObject(self.object)
            self.x -= 10
            self.width += 10
            penSize(4)
            brushColor('red')
            self.object = rectangle(self.x, self.y, self.x + self.width, self.y + self.height)

    def move(self, event):
        if event == 'VK_SPACE':
            self.p += 1
        dx = 0
        if event == 'VK_LEFT' or event == 'VK_RIGHT':
            if self.x + self.width >= self.window_width and event == 'VK_RIGHT':
                return

            if self.x <= 0 and event == 'VK_LEFT':
                return

            if event == 'VK_RIGHT':
                dx = self.dx

            if event == 'VK_LEFT':
                dx = -self.dx

            self.x += dx
            moveObjectTo(self.object, self.x, self.y)
        return self