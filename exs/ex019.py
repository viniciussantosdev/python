import random
print('Sorteio de Nomes!')
n1 = input('Digite o primeiro nome:')
n2 = input('Digite o segundo nome:')
n3 = input('Digite o terceiro nome:')
n4 = input('Digite o quarto nome:')
sorteio = random.choice([n1,n2,n3,n4])
print('O nome sorteado foi {}!'.format(sorteio))