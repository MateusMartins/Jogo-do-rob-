from robo import Robot
from robo import Reward

r1 = Robot(0, 9)
r2 = Robot(9, 0)

comida = Reward(10,0,'Comida')
gasolina = Reward(0,10,'Gasolina')
rewards = [comida, gasolina]

Validador = r1.check_reward(r1,rewards)