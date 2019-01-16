from graph import *


class Platform:
    def __init__(self, width=100, height=10, window_width=1, window_height=1):
        self.window_width = window_width
        self.window_height = window_height
        self.width = width
        self.height = height
        self.x = self.window_width//2 - self.width//2
        self.y = self.window_height - self.height
        self.dx = 5
        self.object = object
        self.mk_platform()

    def mk_platform(self):
        brushColor('red')
        penSize(4)
        penColor('black')
        self.object = rectangle(self.x, self.y, self.x + self.width, self.y + self.height)
        return self

    def move(self, event):
        dx = 0
        if event.keycode == VK_LEFT or event.keycode == VK_RIGHT:
            if self.x + self.width >= self.window_width and event.keycode == VK_RIGHT:
                return

            if self.x <= 0 and event.keycode == VK_LEFT:
                return

            if event.keycode == VK_RIGHT:
                dx = self.dx

            if event.keycode == VK_LEFT:
                dx = -self.dx

            self.x += dx
            moveObjectTo(self.object, self.x, self.y)
        return self
