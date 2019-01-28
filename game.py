from graph import *
from Controller import ControllerClass

windowWidth = 600
windowHeight = 500
windowSize(windowWidth + 3, windowHeight + 40)
canvasSize(windowWidth, windowHeight)
canvasPos(0, 0)
controller = ControllerClass(windowWidth, windowHeight)
keyPressed = False


def update():
    controller.circle_move()


onTimer(update, 10)
onKey(controller.keys)
run()

