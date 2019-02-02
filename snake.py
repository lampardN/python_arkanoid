from config import *
from snake_part import SnakePart
from graph import *


class Snake:
    def __init__(self):
        self.snake_length = SNAKE_DEFAULT_PARTS
        self.field_x = SNAKE_DEFAULT_POSITION_X
        self.field_y = SNAKE_DEFAULT_POSITION_Y
        self.snake_parts = []
        self.snake_parts.append(SnakePart(SNAKE_HEAD, self.field_x, self.field_y))
        self.field_y += 1
        for i in range(self.snake_length - 2):
            self.snake_parts.append(SnakePart(SNAKE_BODY, self.field_x, self.field_y))
            self.field_y += 1
        self.snake_parts.append(SnakePart(SNAKE_TAIL, self.field_x, self.field_y))
        self.field_y += 1

    def move(self):
        pass

    def eat(self):
        pass

    def strike(self):
        pass
