from graph import *
from config import *
from FieldStub import FieldStub
from snake import Snake
from Apple import Apple
from random import randint


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
        self.in_pause = True
        self.move_apple()

    def draw(self):
        for i in range(len(self.parts)):
            for j in range(len(self.parts[i])):
                self.parts[i][j] = FieldStub(i, j)

    def move_apple(self):
        snake_position = []
        for i in range(len(self.snake.snake_parts)):
            snake_position.append((self.snake.snake_parts[i].field_x,
                                   self.snake.snake_parts[i].field_y))
        positions = []
        for i in range(FIELD_PARTS):
            for j in range(FIELD_PARTS):
                positions.append((i,j))
        result_positions = []
        for i in range(len(positions)):
            if snake_position.count(positions[i]) == 0:
                result_positions.append(positions[i])
        apple_pos = result_positions[randint(0, len(result_positions))]
        self.apple.set_position(apple_pos[0], apple_pos[1])

    def start(self):
        pass

    def revert_game_status(self):
        if self.in_pause:
            self.in_pause = False
        else:
            self.in_pause = True

    def set_direction(self, event):
        if event.keycode == VK_SPACE:
            if self.in_pause:
                self.in_pause = False
            else:
                self.in_pause = True

        if event.keycode == VK_UP and self.snake.turn != MOVE_DOWN:
            self.snake.set_turn(MOVE_UP)

        if event.keycode == VK_DOWN and self.snake.turn != MOVE_UP:
            self.snake.set_turn(MOVE_DOWN)

        if event.keycode == VK_LEFT and self.snake.turn != MOVE_RIGHT:
            self.snake.set_turn(MOVE_LEFT)

        if event.keycode == VK_RIGHT and self.snake.turn != MOVE_LEFT:
            self.snake.set_turn(MOVE_RIGHT)

    def move(self):
        if not self.in_pause:
            self.snake.move()
        if self.snake.eat(self.apple):
            self.move_apple()
