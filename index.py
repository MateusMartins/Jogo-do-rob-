#import das classes no arquivo robo.py
from robo import Robot
from robo import Reward
from robo import Validacao

#Criação dos robôs com as posições x e y na matriz
r1 = Robot(0, 9)
r2 = Robot(9, 0)

#Estanciação das recompensas presentes na matriz
comida = Reward(10,0,'Comida')
gasolina = Reward(0,10,'Gasolina')

#Criação da lista de recompensas
rewards = [comida, gasolina]

#Criação do validador 
Validador = Validacao()

#Movimentando robô em direção a uma recompensa
r1.move_up()

#Validação da recompensa
Validador.check_reward(r1,rewards)