class Robo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def Escrever_x(self):
        print(self.x)

    def move_up(self):
        if self.y < 10:
            self.y = self.y + 1
        else:
            print('Movimento inválido')

    def move_down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            print('Movimento inválido')
    def move_right(self):
        if self.x < 10:
            self.x = self.x + 1
        else:
            print('Movimento inválido')

    def move_left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            print('Movimento inválido')

class Robo3D(Robo):

    def __init__(self, x, y, z):
        super(Robo3D, self).__init__(x, y)
        self.z = z