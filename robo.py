#Classe utilizada para definir a posição x e y
class Point(object):
    #Definidor de posição na matriz
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Classe utilizada para criar o robô e movimenta-lo
class Robot(Point):
    #Construtor do robô
    def __init__(self, x, y):
        super(Robot, self).__init__(x, y)
    
    #Escreve qual é a posição x do robô na matriz
    def Escrever_x(self):
        print(self.x)

    #Escreve qual é a posição y do robô na matriz
    def Escrever_y(self):
        print(self.y)

    #Movimenta o robô para cima
    def move_up(self):
        if self.y < 10:
            self.y = self.y + 1
        else:
            print('Movimento inválido')

    #Movimenta o robô para baixo
    def move_down(self):
        if self.y > 0:
            self.y = self.y - 1
        else:
            print('Movimento inválido')

    #Movimenta o robô para a direita  
    def move_right(self):
        if self.x < 10:
            self.x = self.x + 1
        else:
            print('Movimento inválido')

    #Movimenta o robô para a esquerda
    def move_left(self):
        if self.x > 0:
            self.x = self.x - 1
        else:
            print('Movimento inválido')

#Classe utilizada para criar as recompensas
class Reward(Point):
    #Construtor da recompensa
    def __init__(self, x, y, name):
        super(Reward, self).__init__(x, y)
        self.name = name

#Classe utilizada para validar os dados
class Validacao(object):
    #Validador de procura de recompensa
    def check_reward(self, robot, rewards):
            for reward in rewards:
                if reward.x == robot.x and reward.y == robot.y:
                    print('Você encontrou a seguinte recompensa: %s' % reward.name)

#class Robo3D(Point):
#    def __init__(self, x, y, z):
#        super(Robo3D, self).__init__(x, y)
#        self.z = z