from FieldClass import FieldClass
from graph import *

e = FieldClass()
onTimer(e.snake.move, 1000)
onKey(e.set_direction)
run()
