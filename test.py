from Circle import CircleClass
from brusochek import Brusochek
import graph
from random import randint

width = 400
height = 400
radius = 10
dots = []
graph.windowSize(width + 50, height + 50)
graph.canvasSize(width, height)
graph.canvasPos(0, 0)

graph.penColor('black')
graph.penSize(5)
graph.line(5,5,5,400)
graph.line(5,5,400,5)
graph.line(400,5,400,400)

platform = Brusochek(50, 400, 5, 10, 100).make_sqr().set_down()

for i in range(1):
    posX = randint(2 * radius, width - 2 * radius)
    posY = randint(2 * radius, height - 2 * radius)
    a = CircleClass(posX, posY, 1, 1, radius).color(graph.randColor()).createCircle()
    dots.append(a)

def mov(event):
    if event.keycode == graph.VK_LEFT:
        graph.moveObjectBy(platform.object, -platform.dx, 0)
    if event.keycode == graph.VK_RIGHT:
        graph.moveObjectBy(platform.object, platform.dx, 0)

def update():

    for dot in dots:
        if dot.getPosition('x') + dot.radius() >= width - radius:
            dot.setOffset(dx = -1 * dot.getOffset('x'))

        if platform.position_update() + platform.w >= dot.getPosition('x') + dot.radius() >= platform.position_update() and dot.getPosition('y') + dot.radius() == width - platform.h * 2:
            dot.setOffset(dy=-1 * dot.getOffset('y'))
            dot.setOffset(dx=1 * dot.getOffset('x'))

        if dot.getPosition('x') - dot.radius() < -dot.radius():
            dot.setOffset(dx = -1 * dot.getOffset('x'))
        if dot.getPosition('y') - dot.radius() < -dot.radius():
            dot.setOffset(dy = -1 * dot.getOffset('y'))

        dot.move()
        graph.moveObjectTo(dot.obj(), dot.getPosition('x'), dot.getPosition('y'))

        if dot.getPosition('y') + dot.radius() >= height - radius:
         graph.close()

graph.onKey(mov)
graph.onTimer(update, 50)

graph.run()
