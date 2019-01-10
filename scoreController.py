from graph import *

class Score:
    def __init__(self, height, score=0):
        self.height = height
        self.score = score
        self.score_text = "Score - "
        self.mklable()

    def mklable(self):
        label(self.score_text + str(self.score), 0, self.height + 20)
