from Circle import CircleClass
from brusochek import Brusochek
from win32api import GetSystemMetrics
import graph

width = GetSystemMetrics(0) - 500 #Размер экрана
height = GetSystemMetrics(0) - 1000 #Размер экрана
radius = 10                       #Радиус шарика
graph.windowSize(width + 50, height + 50)
graph.canvasSize(width, height)
graph.canvasPos(0, 0)

graph.penColor('black')
graph.penSize(5)
graph.line(5, 5, 5, height)
graph.line(5, 5, width, 5)
graph.line(width, 5, width, height)

platform = Brusochek(width/3, height, 20, 15, 100).make_sqr().set_down(width)


posX = width/2
posY = height/2
dot = CircleClass(posX, posY, 1, 1, radius).color(graph.randColor()).createCircle()

def mov(event):
    platform.mov(width, event.keycode)


def update():




    if dot.getPosition('x') + dot.radius() >= width - radius:
        dot.setOffset(dx=-1 * dot.getOffset('x'))

    if dot.getPosition('x') - dot.radius() < -dot.radius():
        dot.setOffset(dx=-1 * dot.getOffset('x'))
    if dot.getPosition('y') - dot.radius() < -dot.radius():
        dot.setOffset(dy=-1 * dot.getOffset('y'))

    if ((platform.position_update() + platform.w) /2)-20 <= dot.getPosition('x') + dot.radius() <= ((platform.position_update() + platform.w)/2)+20 \
    and dot.getPosition('y') + dot.radius() == height - platform.h * 1.6:
        dot.setOffset(dy=-1 * dot.getOffset('y'))
        dot.setOffset(dx=0)
        print('!!!!')

    #elif (platform.position_update() + platform.w) / 2 - 20 > dot.getPosition('x') + dot.radius() >= platform.position_update()\
    #and dot.getPosition('y') + dot.radius() == height - platform.h * 1.6:
    #    dot.setOffset(dy=-1 * dot.getOffset('y'))
    #    dot.setOffset(dx=1 * dot.getOffset('x'))

    #elif (platform.position_update() + platform.w) / 2 + 20 < dot.getPosition('x') + dot.radius() <= platform.position_update() + platform.w\
    #and dot.getPosition('y') + dot.radius() == height - platform.h * 1.6:
    #    dot.setOffset(dy=-1 * dot.getOffset('y'))
    #    dot.setOffset(dx=1 * dot.getOffset('x'))



    dot.move()
    graph.moveObjectTo(dot.obj(), dot.getPosition('x'), dot.getPosition('y'))

    if dot.getPosition('y') + dot.radius() >= height + radius:
        graph.close()



graph.onKey(mov)
graph.onTimer(update, 10)

graph.run()
