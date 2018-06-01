class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Robot(Point):
    def __init__(self, x, y):
        super(Robot, self).__init__(x, y)
        
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
    
    def check_reward(self, robot, rewards):
        for reward in rewards:
            if reward.x == robot.x and reward.y == robot.y:
                print('Você encontrou a seguinte recompensa %s' % reward.name)

class Reward(Point):

    def __init__(self, x, y, name):
        super(Reward, self).__init__(x, y)
        self.name = name





#class Robo3D(Point):
#
#    def __init__(self, x, y, z):
#        super(Robo3D, self).__init__(x, y)
#        self.z = z