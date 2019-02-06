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
        self.turn = MOVE_UP

    def move(self):
        turn = self.direction_offset()
        last_pos = (self.snake_parts[0].field_x,
                    self.snake_parts[0].field_y)
        moveObjectBy(self.snake_parts[0].object, turn[0], turn[1])
        self.snake_parts[0].field_x = last_pos[0] + turn[0]
        self.snake_parts[0].field_y = last_pos[1] + turn[1]
        for i in range(1, len(self.snake_parts)):
            moveObjectTo(self.snake_parts[i].object, last_pos[0], last_pos[1])
            last_pos = (self.snake_parts[i].field_x,
                        self.snake_parts[i].field_y)
            self.snake_parts[i].field_x = last_pos[0] + turn[0]
            self.snake_parts[i].field_y = last_pos[1] + turn[1]

    def eat(self):
        pass

    def strike(self):
        pass

    def set_turn(self, turn_direction):
        self.turn = turn_direction

    def direction_offset(self):
        if self.turn == MOVE_NONE:
            return [0,0]
        if self.turn == MOVE_UP:
            return [0,-FIELD_SIZE]
        if self.turn == MOVE_DOWN:
            return  [0,FIELD_SIZE]
        if self.turn == MOVE_LEFT:
            return [-FIELD_SIZE,0]
        if self.turn == MOVE_RIGHT:
            return [FIELD_SIZE,0]
