from graph import *
from Controller import ControllerClass

windowWidth = 600
windowHeight = 800
windowSize(windowWidth, windowHeight + 40)
canvasSize(windowWidth, windowHeight)
canvasPos(0, 0)
controller = ControllerClass(windowWidth, windowHeight)


def update():
    controller.circle_move()


onTimer(update, 10)
onKey(controller.platform.move)
run()
