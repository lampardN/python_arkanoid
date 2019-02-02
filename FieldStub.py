from graph import *
from config import *


class FieldStub:
    def __init__(self, field_x, field_y):
        self.color = (115, 250, 162)
        self.x = 0
        self.y = 0
        self.field_x = field_x
        self.field_y = field_y
        penSize(1)
        brushColor(self.color)
        self.object = rectangle(self.x, self.y, self.x + FIELD_SIZE, self.y + FIELD_SIZE)
        self.set_position(field_x, field_y)

    def get_object(self):
        return self.object

    def set_position(self, field_x, field_y):
        self.field_x = field_x
        self.field_y = field_y
        self.x = field_x * FIELD_SIZE
        self.y = field_y * FIELD_SIZE
        moveObjectTo(self.object, self.x, self.y)

    def move(self):
        pass

    def set_color(self, color):
        self.color = color
        changeFillColor(self.object, color)
