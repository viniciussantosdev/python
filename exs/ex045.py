from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ]
[ 1 ]
[ 2 ]''')
jogador = int(input('Qual é a sua jogada?'))
sleep(0.5)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VOCÊ VENCEU!')
    elif jogador == 2:
        print('VOCÊ PERDEU!')
    else:
        print('Jogada inválida!')
elif computador == 1: #jogou papel
    if jogador == 0:
        print('VOCÊ PERDEU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VOCÊ VENCEU!')
    else:
        print('Jogada inválida!')
elif computador == 2: #jogou tesoura
    if jogador == 0:
        print('VOCÊ GANHOU!')
    elif jogador == 1:
        print('VOCÊ PERDEU!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida!')
