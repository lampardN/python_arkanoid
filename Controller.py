from enemy import Enemy
from win32api import GetSystemMetrics

height = GetSystemMetrics(1) - 500
width = GetSystemMetrics(0) - 500

file = open('position.txt', 'r', encoding='utf-8')
a = file.readlines()

kw = len(a[0])
kh = len(a)

enemys = []

for i in range(len(a)):
    a[i] = a[i].strip()


class ControllerClass:
    def __init__(self, x=0, y=0):
        global kw
        global kh
        global a
        self.x = x
        self.y =y
        self.a = a
        self.kw = kw
        self.kh = kh

    def set_objects(self, x=0, y=0):
        global width
        global height
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                if a[j] != '_':
                    enemys.append(Enemy(x, y, 20, width//self.kw, int(self.a[i])).set_color().make_sqr())
                    x += width//self.kw
                else:
                    x += width//self.kw
            y += 20
        return self
