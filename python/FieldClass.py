from graph import *
from config import *
from FieldStub import FieldStub


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

    def draw(self):
        for i in range(len(self.parts)):
            for j in range(len(self.parts[i])):
                self.parts[i][j] = FieldStub()
                self.parts[i][j].set_position(i, j)

    def start(self):
        pass
