from FieldStub import FieldStub
from config import *


class SnakePart(FieldStub):
    def __init__(self, part_type, field_x, field_y, turn=UP):
        super().__init__(field_x, field_y)
        self.part_type = part_type
        if part_type == SNAKE_HEAD:
            self.set_image('snake_head')
        if part_type == SNAKE_TAIL:
            self.set_image('snake_tail')
        if part_type == SNAKE_BODY:
            self.set_image('snake_body', turn)
        self.set_position(field_x, field_y)
