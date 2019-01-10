from Circle import CircleClass
from brusochek import Brusochek
from Controller import ControllerClass
import graph

center = 10  # половина центральной части платформы

width = 800  # Размер экрана
height = 600  # Размер экрана
radius = 10                       # Радиус шарика
graph.windowSize(width + 50, height + 50)  # размер окна
graph.canvasSize(width, height)  # размер холста
graph.canvasPos(0, 0)  # позиция холста

platform = Brusochek(width/3, height, 20, 15, 100).set_down(width)  # брусочек

posX = width/2  # позиция шарика по х
posY = height - platform.h - 20  # позиция шарика по у
dots = []
dots.append(CircleClass(posX, posY, 1, 1, radius))  # шарик

controller = ControllerClass('position.txt')  # объект контроллера
blocks = controller.set_objects()  # враги

score_l = 'Your score - 0'
score = 0
graph.label(score_l, 0, height + 20)  # счёт

graph.penColor('black')  # цвет рамки
graph.penSize(6)  # ширина рамки
graph.line(5, 5, 5, height)  # левая сторона рамки
graph.line(5, 5, width, 5)  # верхняя сторона рамки
graph.line(width, 5, width, height)  # правая сторона рамки


def mov(event):
    platform.mov(width, event.keycode)


def update():

    global score
    global score_l

    for dot in dots:

        if platform.p != 0:

            for sqr in blocks.enemys:  # контакт шарика с блоками
                if (graph.xCoord(sqr.object) <= dot.getPosition('x') <= graph.xCoord(sqr.object) + blocks.w
                and graph.yCoord(sqr.object) + blocks.h == dot.getPosition('y'))\
                or (graph.xCoord(sqr.object) <= dot.getPosition('x') <= graph.xCoord(sqr.object) + blocks.w
                and graph.yCoord(sqr.object) == dot.getPosition('y') + dot.radius())\
                or (graph.yCoord(sqr.object) <= dot.getPosition('y') <= graph.yCoord(sqr.object) + blocks.h
                and graph.xCoord(sqr.object) == dot.getPosition('x') + dot.radius())\
                or (graph.yCoord(sqr.object) <= dot.getPosition('y') <= graph.yCoord(sqr.object) + blocks.h
                and graph.xCoord(sqr.object) + sqr.w == dot.getPosition('x') - dot.radius()):
                    score += sqr.s
                    sqr.s -= 1
                    dot.setOffset(dy=-1 * dot.getOffset('y'))
                    dot.setOffset(dx=1 * dot.getOffset('x'))
                    sqr.set_color().update_object()
                    if sqr.s == -1:
                        graph.deleteObject(sqr.object)
                        del blocks.enemys[blocks.enemys.index(sqr)]
                    score_l = 'Your score - ' + str(score)
                    graph.label(score_l, 0, height + 20)

            dot.circleInWindow(width)

            dot.checkBrusochekContact(platform.position_update(), platform.w, platform.h)

            dot.move()
            graph.moveObjectTo(dot.obj(), dot.getPosition('x'), dot.getPosition('y'))  # движение шарика

            if dot.getPosition('y') + dot.radius() >= height + radius:  # условие проигрыша
                graph.close()

        else:  # фиксация шарика над платформой
            graph.moveObjectTo(dot.object, platform.position_update() + platform.w/2, dot.getPosition('y') - dot.radius())
            dot.setPosition(graph.xCoord(dot.object), platform.y - dot.radius()*4)


graph.onKey(mov)
graph.onTimer(update, 10)
graph.run()

print(score_l)
