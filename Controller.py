from enemy import Enemy

height = 600
width = 800




class ControllerClass:
    def __init__(self, filename, x=0, y=0):
        a = self.readFile(filename)
        self.x = x
        self.y =y
        self.w = width//len(a[0])
        self.h = height//5//len(a)
        self.a = a
        self.enemys = []

    def set_objects(self):
        global width
        global height
        x1 = 8
        y1 = 8
        x2 = self.w
        y2 = self.h
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                if self.a[i][j] != '_':
                    self.enemys.append(Enemy(x1, y1, x2, y2, int(self.a[i][j])).set_color().make_sqr())
                    x1 += self.w
                    x2 += self.w
                else:
                    x1 += self.w
                    x2 += self.w
            x1 = 8
            x2 = self.w
            y1 += self.h
            y2 += self.h
        return self

    def readFile(self, filename):
        file = open(filename, 'r', encoding='utf-8')
        a = file.readlines()

        for i in range(len(a)):
            a[i] = a[i].strip()
        return a