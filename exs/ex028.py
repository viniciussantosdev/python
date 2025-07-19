from random import randint
computer = randint(0,5) #O computador vai escolher um número com o randint
print('Seja bem vindo ao jogo da adivinhação!')
print('Pense no mesmo número em que estou pensando entre 0 a 5!')
player = int(input('Em que número eu pensei?'))
print('Parabéns,Você ganhou!' if player == computer else 'Você perdeu, tente novamente!')