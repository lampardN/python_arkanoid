from FieldClass import FieldClass
from graph import *

e = FieldClass()


def update():
    e.move()


onTimer(update, 250)
onKey(e.set_direction)
run()
