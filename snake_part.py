from FieldStub import FieldStub
from config import *


class SnakePart(FieldStub):
    def __init__(self, part_type, field_x, field_y):
        super().__init__(field_x, field_y)
        if part_type == SNAKE_HEAD:
            self.set_color('red')
        if part_type == SNAKE_TAIL:
            self.set_color('red')
        if part_type == SNAKE_BODY:
            self.set_color('yellow')
        self.set_position(field_x, field_y)
