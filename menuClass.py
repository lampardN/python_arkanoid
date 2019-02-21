from graph import *
from config import *


class MenuClass:
    def __init__(self):
        pX = FIELD_PARTS * FIELD_SIZE + 10
        pY = 50
        self.score = 0
        self.space_info = label('Для установки паузы или продолжения игры \n нажмите пробел.', pX, pY, font=('Arial', 12), fg='green', justify='left')
        self.score_lable = label('Ваш счёт: 0', pX, pY+50, font=('Arial', 12), fg='green', justify='left')

    def score_update(self):
        self.score_lable['text'] = 'Ваш счёт: ' + str(self.score)
