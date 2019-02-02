from graph import *
from config import *
from FieldStub import FieldStub
from snake import Snake
from Apple import Apple


class FieldClass:
    def __init__(self):
        windowSize(CANVAS_WIDTH, CANVAS_HEIGHT)
        canvasSize(CANVAS_WIDTH, CANVAS_HEIGHT)
        self.parts = []
        for i in range(FIELD_PARTS):
            self.parts.append([])
            for j in range(FIELD_PARTS):
                self.parts[i].append(None)
        self.draw()
        self.snake = Snake()
        self.apple = Apple(0, 0)

    def draw(self):
        for i in range(len(self.parts)):
            for j in range(len(self.parts[i])):
                self.parts[i][j] = FieldStub(i, j)

    def start(self):
        pass
