from enemy import Enemy


class ControllerClass:
    def __init__(self, filename, width, height, x=0, y=0):
        a = self.readFile(filename)
        self.a = a
        self.x = x
        self.y =y
        self.width = (width-6)//10
        self.height = 20
        self.enemys = []
        self.set_objects()

    def set_objects(self):
        self.x = 8
        self.y = 8
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                if self.a[i][j] != '_':
                    self.enemys.append(Enemy(self.x, self.y, self.x + self.width, self.y + self.height, int(self.a[i][j])))
                self.x += self.width
            self.x = 8
            self.y += self.height
        return self

    def readFile(self, filename):
        file = open(filename, 'r', encoding='utf-8')
        a = file.readlines()

        for i in range(len(a)):
            a[i] = a[i].strip()
        return a
