from graph import *
from config import *
from sqlite3 import *


class MenuClass:
    def __init__(self):
        pX = FIELD_PARTS * FIELD_SIZE + 10
        pY = 50
        db = connect('score.db')
        cursor = db.cursor()
        sql = "SELECT * FROM top_score WHERE id=1"
        cursor.execute(sql)
        self.score = 0
        self.height_score = cursor.fetchall()[0][0]
        self.space_info = label('Для установки паузы или продолжения игры \n нажмите пробел.', pX, pY, font=('Arial', 12), fg='green', justify='left')
        self.score_lable = label('Ваш счёт: 0', pX, pY+50, font=('Arial', 12), fg='green', justify='left')
        self.top_score = label('Рекорд: 0', pX, pY+70, font=('Arial', 12), fg='green', justify='left')
        self.top_score['text'] = 'Рекорд: ' + str(self.height_score)

    def score_update(self):
        self.score_lable['text'] = 'Ваш счёт: ' + str(self.score)
        if self.score > self.height_score:
            self.height_score = self.score
            self.top_score['text'] = 'Рекорд: ' + str(self.height_score)
