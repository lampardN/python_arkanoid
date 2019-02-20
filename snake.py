from config import *
from snake_part import SnakePart


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
        self.strike_status = False
        self.turn = MOVE_UP
        self.last_turn = self.turn

    def move(self):
        head_turn = self.direction_offset()
        head_x = self.snake_parts[0].field_x
        head_y = self.snake_parts[0].field_y
        head_x += head_turn[0]
        head_y += head_turn[1]
        for i in range(len(self.snake_parts)-1, -1, -1):
            current = self.snake_parts[i]
            next = self.snake_parts[i-1]
            current.set_position(next.field_x, next.field_y)
        self.snake_parts[0].set_position(head_x, head_y)
        self.snake_parts[0].set_image(self.snake_parts[0].part_type, head_turn)
        for i in range(1, len(self.snake_parts)):
            current_pos = (self.snake_parts[i].field_x,
                           self.snake_parts[i].field_y)
            second_pos = (self.snake_parts[i-1].field_x,
                          self.snake_parts[i-1].field_y)
            try:
                first_pos = (self.snake_parts[i+1].field_x,
                             self.snake_parts[i+1].field_y)
            except:
                first_pos = second_pos

            turn = (second_pos[0] - current_pos[0],
                    second_pos[1] - current_pos[1])

            '''if first_pos[0] != second_pos[0] + 2\
            and first_pos[1] != second_pos[1] + 2\
            and first_pos != second_pos:
                res = (first_pos[0]-second_pos[0],
                       first_pos[1]-second_pos[1])
                if head_turn == UP:
                    if res == TURN_1:
                        self.snake_parts[i].set_image(self.snake_parts[i].part_type, 1)
                    if res == TURN_2:
                        self.snake_parts[i].set_image(self.snake_parts[i].part_type, 4)
                if head_turn == DOWN:
                    if res == TURN_3:
                        self.snake_parts[i].set_image(self.snake_parts[i].part_type, 4)
                    if res == TURN_4:
                        self.snake_parts[i].set_image(self.snake_parts[i].part_type, 3)
                if head_turn == LEFT:
                    if res == TURN_1:
                        self.snake_parts[i].set_image(self.snake_parts[i].part_type, 1)
                    if res == TURN_4:
                        self.snake_parts[i].set_image(self.snake_parts[i].part_type, 2)
                if head_turn == RIGHT:
                    if res == TURN_2:
                        self.snake_parts[i].set_image(self.snake_parts[i].part_type, 3)
                    if res == TURN_3:
                        self.snake_parts[i].set_image(self.snake_parts[i].part_type, 4)
            else:'''
            self.snake_parts[i].set_image(self.snake_parts[i].part_type, turn)

    def eat(self, apple):
        turn = self.direction_offset()
        apple_coord = (apple.field_x, apple.field_y)
        snake_next_coord = (self.snake_parts[0].field_x + turn[0],
                            self.snake_parts[0].field_y + turn[1])
        if apple_coord == snake_next_coord:
            self.snake_parts[0].set_image(self.snake_parts[0].part_type, turn, est=True)
            self.snake_parts.insert(1, SnakePart(SNAKE_BODY,
                                                 self.snake_parts[0].field_x,
                                                 self.snake_parts[0].field_y, turn))
            self.snake_parts[0].field_x += turn[0]
            self.snake_parts[0].field_y += turn[1]
            self.snake_parts[0].set_position(self.snake_parts[0].field_x,
                                             self.snake_parts[0].field_y)
            return True

    def strike(self):
        head_pos = (self.snake_parts[0].field_x,
                    self.snake_parts[0].field_y)
        for i in range(1, len(self.snake_parts)):
            pos = (self.snake_parts[i].field_x,
                   self.snake_parts[i].field_y)
            if head_pos == pos:
                self.strike_status = True

        if head_pos[0] == FIELD_PARTS\
        or head_pos[1] == FIELD_PARTS:
            self.strike_status = True

        if head_pos[0] < 0\
        or head_pos[1] < 0:
            self.strike_status = True

    def set_turn(self, turn_direction):
        self.turn = turn_direction

    def direction_offset(self):
        if self.turn == MOVE_NONE:
            return (0, 0)
        if self.turn == MOVE_UP:
            return (0, -1)
        if self.turn == MOVE_DOWN:
            return (0, 1)
        if self.turn == MOVE_LEFT:
            return (-1, 0)
        if self.turn == MOVE_RIGHT:
            return (1, 0)
