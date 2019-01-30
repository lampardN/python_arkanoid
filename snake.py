from config import *


class Snake:
    def __init__(self):
        self.snake_length = SNAKE_DEFAULT_PARTS
        self.x = 0
        self.y = 0
        self.snake_parts = []
        for i in range(self.snake_length):
            self.snake_parts.append(None)

    def move(self):
        pass

    def eat(self):
        pass

    def strike(self):
        pass
