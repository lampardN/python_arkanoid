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

    def set_image(self, part, turn=UP, est=False):
        deleteObject(self.object)
        if part == SNAKE_BODY:
            if type(turn) == type(()):
                if turn == UP or turn == DOWN:
                    self.object = image(self.x, self.y, './image/telo_y.gif')
                if turn == LEFT or turn == RIGHT:
                    self.object = image(self.x, self.y, './image/telo_x.gif')
            if type(turn) == int:
                if turn == 1:
                    self.object = image(self.x, self.y, './image/povorot_1.gif')
                if turn == 2:
                    self.object = image(self.x, self.y, './image/povorot_2.gif')
                if turn == 3:
                    self.object = image(self.x, self.y, './image/povorot_3.gif')
                if turn == 4:
                    self.object = image(self.x, self.y, './image/povorot_4.gif')
        if part == SNAKE_HEAD:
            if est:
                if turn == UP:
                    self.object = image(self.x, self.y, './image/est_U.gif')
                if turn == DOWN:
                    self.object = image(self.x, self.y, './image/est_D.gif')
                if turn == LEFT:
                    self.object = image(self.x, self.y, './image/est_L.gif')
                if turn == RIGHT:
                    self.object = image(self.x, self.y, './image/est_R.gif')
            else:
                if turn == UP:
                    self.object = image(self.x, self.y, './image/golova_U.gif')
                if turn == DOWN:
                    self.object = image(self.x, self.y, './image/golova_D.gif')
                if turn == LEFT:
                    self.object = image(self.x, self.y, './image/golova_L.gif')
                if turn == RIGHT:
                    self.object = image(self.x, self.y, './image/golova_R.gif')
        if part == SNAKE_TAIL:
            if turn == UP:
                self.object = image(self.x, self.y, './image/hvost_U.gif')
            if turn == DOWN:
                self.object = image(self.x, self.y, './image/hvost_D.gif')
            if turn == LEFT:
                self.object = image(self.x, self.y, './image/hvost_L.gif')
            if turn == RIGHT:
                self.object = image(self.x, self.y, './image/hvost_R.gif')
