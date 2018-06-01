#import das classes no arquivo robo.py
from robo import Robot
from robo import Reward
from robo import Validacao
import random

#Criação dos robôs com as posições x e y na matriz
caminhoneiro = Robot(random.randint(0,10),random.randint(0,10))

#Estanciação das recompensas presentes na matriz
comida = Reward(random.randint(0,10),random.randint(0,10),'Comida')
gasolina = Reward(random.randint(0,10),random.randint(0,10),'Gasolina')
arma = Reward(random.randint(0,10),random.randint(0,10),'Arma')

#Criação da lista de recompensas
rewards = [comida, gasolina, arma]

#Criação do validador 
Validador = Validacao()

print('Posição inicial do caminhoneiro na matriz: %s' % (caminhoneiro))
for i in range(10):
    movimento = input("Digite up, down, left ou right para o movimento: ")
    if movimento == 'up':
        caminhoneiro.move_up()
    elif movimento == 'down':
        caminhoneiro.move_down()
    elif movimento == 'left':
        caminhoneiro.move_left()
    elif movimento == 'right':
        caminhoneiro.move_right()
    else:
        print('Movimento inválido')
        continue #se chegar no contiue o sistema ignora o loop atual e continua o ciclo de repetição ignorando o código abaixo
    
    print('Número de tentativas %d' % (i))
    print('Posição atual do caminhoneiro na matriz: %s' % (caminhoneiro))
    #Validação da recompensa
    Validador.check_reward(caminhoneiro,rewards)
    