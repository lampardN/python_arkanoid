from Circle import CircleClass
from brusochek import Brusochek
from Controller import ControllerClass
from win32api import GetSystemMetrics
from random import randint
import graph

center = 10  # половина центральной части платформы

width = GetSystemMetrics(0) - 500  # Размер экрана
height = GetSystemMetrics(1) - 500  # Размер экрана
radius = 10                       # Радиус шарика
graph.windowSize(width + 50, height + 50)  # размер окна
graph.canvasSize(width, height)  # размер холста
graph.canvasPos(0, 0)  # позиция холста

graph.penColor('black')  # цвет рамки
graph.penSize(5)  # ширина рамки
graph.line(5, 5, 5, height)  # левая сторона рамки
graph.line(5, 5, width, 5)  # вепхняя сторона рамки
graph.line(width, 5, width, height)  # правая сторона рамки

platform = Brusochek(width/3, height, 20, 15, 100).make_sqr().set_down(width)  # брусочек


posX = width/2  # позиция шарика по х
posY = height - platform.h - 20  # позиция шарика по у
dot = CircleClass(posX, posY, 0, 1, radius).color(graph.randColor()).createCircle()  # шарик

blocks = ControllerClass.set_objects

def mov(event):
    platform.mov(width, event.keycode)


def update():
    if platform.p != 0:

        if dot.getPosition('x') + dot.radius() >= width - radius:  # если ушёл за рамку вправо
            dot.setOffset(dx=-1 * dot.getOffset('x'))

        if dot.getPosition('x') - dot.radius() < -dot.radius():  # если ушёл за рамку влево
            dot.setOffset(dx=-1 * dot.getOffset('x'))
        if dot.getPosition('y') - dot.radius() < -dot.radius():  # если ушёо за рамку вниз
            dot.setOffset(dy=-1 * dot.getOffset('y'))

        if ((platform.position_update() + platform.w/2) - center <= dot.getPosition('x') + dot.radius() <= (platform.position_update() + platform.w/2) + center)\
        and dot.getPosition('y') + dot.radius() == height - platform.h * 1.6:  # если шарик упал на центр платформы
            dot.setOffset(dy=-1 * dot.getOffset('y'))
            dot.setOffset(dx=0)

        if ((platform.position_update() + platform.w / 2) - center > dot.getPosition('x') + dot.radius() >= platform.position_update()\
        and dot.getPosition('y') + dot.radius() == height - platform.h * 1.6)\
        or ((platform.position_update() + platform.w / 2) - center > dot.getPosition('x') + dot.radius() >= platform.position_update() - dot.radius()\
        and dot.getPosition('y') == height - platform.h * 1.6):  # если шарик упал на левую половину платформы
            if dot.getOffset('x') == 0:
                dot.setOffset(dx=-1)
            dot.setOffset(dy=-1 * dot.getOffset('y'))
            dot.setOffset(dx=1 * dot.getOffset('x'))

        if ((platform.position_update() + platform.w / 2) + center < dot.getPosition('x') + dot.radius() <= platform.position_update() + platform.w\
        and dot.getPosition('y') + dot.radius() == height - platform.h * 1.6)\
        or ((platform.position_update() + platform.w / 2) + center < dot.getPosition('x') - dot.radius() <= platform.position_update() + platform.w + dot.radius()\
        and dot.getPosition('y') == height - platform.h * 1.6):  # если упал на правую половину платформы
            if dot.getOffset('x') == 0:
                dot.setOffset(dx=1)
            dot.setOffset(dy=-1 * dot.getOffset('y'))
            dot.setOffset(dx=1 * dot.getOffset('x'))

        dot.move()
        graph.moveObjectTo(dot.obj(), dot.getPosition('x'), dot.getPosition('y'))  # движение шарика

        if dot.getPosition('y') + dot.radius() >= height + radius:  # условие проигрыша
            graph.close()

    else:
        graph.moveObjectTo(dot.object, platform.position_update() + platform.w/2, dot.getPosition('y') - dot.radius())
        dot.setPosition(graph.xCoord(dot.object), platform.y - dot.radius()*4)


graph.onKey(mov)
graph.onTimer(update, 10)

graph.run()
