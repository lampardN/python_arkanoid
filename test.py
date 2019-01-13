from brusochek import Brusochek
from Controller import ControllerClass
import graph

center = 10  # половина центральной части платформы

width = 800  # Размер экрана
height = 600  # Размер экрана
radius = 10     # Радиус шарика
FrameSize = 6
graph.windowSize(width + 50, height + 50)  # размер окна
graph.canvasSize(width, height)  # размер холста
graph.canvasPos(0, 0)  # позиция холста

objects = ControllerClass('position.txt', width, height, FrameSize, radius)  # объект контроллера

graph.penColor('black')  # цвет рамки
graph.penSize(FrameSize)  # ширина рамки
graph.line(5, 5, 5, height)  # левая сторона рамки
graph.line(5, 5, width, 5)  # верхняя сторона рамки
graph.line(width, 5, width, height)  # правая сторона рамки


def mov(event):
    objects.brusochek.mov(width, event.keycode)


def update():

    for dot in objects.dots:

        if objects.brusochek.p != 0:


            dot.circleInWindow()

            objects.cirleMov()

            objects.mklable()

            if dot.getPosition('y') + dot.radius() >= height + radius:  # условие проигрыша
                graph.close()

        else:  # фиксация шарика над платформой
            graph.moveObjectTo(dot.object, objects.brusochek.position_update() + objects.brusochek.width/2, dot.getPosition('y') - dot.radius())
            dot.setPosition(graph.xCoord(dot.object), objects.brusochek.y - dot.radius()*4)


graph.onKey(mov)
graph.onTimer(update, 10)
graph.run()
