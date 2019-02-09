from graph import *
from config import *


class FieldStub:
    def __init__(self, field_x, field_y):
        self.x = 0
        self.y = 0
        self.field_x = field_x
        self.field_y = field_y
        self.object = image(self.x, self.y, './image/trava.gif')
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

    def set_image_for_apple(self, part):
        if part == 'Apple':
            self.object = image(self.x, self.y, './image/yabloko.gif')

    def set_image(self, part, turn=UP):
        if part == SNAKE_BODY:
            if turn == UP or turn == DOWN:
                self.object = image(self.x, self.y, './image/telo_y.gif')
            if turn == LEFT or turn == RIGHT:
                self.object = image(self.x, self.y, './image/telo_x.gif')
        if part == SNAKE_HEAD:
            if turn == UP:
                self.object = image(self.x, self.y, './image/golova_U.gif')
            if turn == DOWN:
                self.object = image(self.x, self.y, './image/golova_D.gif')
            if turn == LEFT:
                self.object = image(self.x, self.y, './image/golova_R.gif')
            if turn == RIGHT:
                self.object = image(self.x, self.y, './image/golova_L.gif')
        if part == SNAKE_TAIL:
            if turn == UP:
                self.object = image(self.x, self.y, './image/hvost_U.gif')
            if turn == DOWN:
                self.object = image(self.x, self.y, './image/hvost_D.gif')
            if turn == LEFT:
                self.object = image(self.x, self.y, './image/hvost_R.gif')
            if turn == RIGHT:
                self.object = image(self.x, self.y, './image/hvost_L.gif')
