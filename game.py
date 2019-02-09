from FieldClass import FieldClass
from graph import *

e = FieldClass()


def update():
    e.move()


onTimer(update, 100)
onKey(e.set_direction)
run()
