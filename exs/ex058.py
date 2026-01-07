from random import randint
computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 a 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
apostas = 0
while not acertou:
    jogador = int(input('Qual é sua aposta? '))
    apostas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente mais uma vez')
        elif jogador > computador:
            print('Menos.. Tente denovo')
print('Acertou com {} tentativas'.format(apostas))