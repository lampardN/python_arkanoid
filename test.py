from Circle import CircleClass
from brusochek import Brusochek
from win32api import GetSystemMetrics
import graph

width = GetSystemMetrics(0) - 500  # Размер экрана
height = GetSystemMetrics(0) - 1000  # Размер экрана
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
posY = height/2  # позиция шарика по у
dot = CircleClass(posX, posY, 1, 1, radius).color(graph.randColor()).createCircle()  # шарик


def mov(event):
    platform.mov(width, event.keycode)


def update():

    if dot.getPosition('x') + dot.radius() >= width - radius:  # если ушёл за рамку вправо
        dot.setOffset(dx=-1 * dot.getOffset('x'))

    if dot.getPosition('x') - dot.radius() < -dot.radius():  # если ушёл за рамку влево
        dot.setOffset(dx=-1 * dot.getOffset('x'))
    if dot.getPosition('y') - dot.radius() < -dot.radius():  # если ушёо за рамку вниз
        dot.setOffset(dy=-1 * dot.getOffset('y'))

    if ((platform.position_update() + platform.w / 2)-20 <= dot.getPosition('x') + dot.radius() <= (platform.position_update() + platform.w/2)+20)\
    and dot.getPosition('y') + dot.radius() == height - platform.h * 1.6:  # если шарик упал на центр платформы
        dot.setOffset(dy=-1 * dot.getOffset('y'))
        dot.setOffset(dx=0)

    if platform.position_update() + platform.w / 2 - 20 >= dot.getPosition('x') + dot.radius() >= platform.position_update()\
    and dot.getPosition('y') + dot.radius() == height - platform.h * 1.6:  # если шарик упал на левую половину платформы
        dot.setOffset(dy=-1 * dot.getOffset('y'))
        dot.setOffset(dx=1 * dot.getOffset('x'))

    if platform.position_update() + platform.w / 2 + 20 <= dot.getPosition('x') + dot.radius() <= platform.position_update() + platform.w\
    and dot.getPosition('y') + dot.radius() == height - platform.h * 1.6:  # если упал на правую половину платформы
        dot.setOffset(dy=-1 * dot.getOffset('y'))
        dot.setOffset(dx=1 * dot.getOffset('x'))

    dot.move()
    graph.moveObjectTo(dot.obj(), dot.getPosition('x'), dot.getPosition('y'))  # движение шарика

    if dot.getPosition('y') + dot.radius() >= height + radius:  # условие проигрыша
        graph.close()


graph.onKey(mov)
graph.onTimer(update, 10)

graph.run()
