import random
print('Ordem do Trabalho.')
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite outro nome: '))
n3 = str(input('Digite mais um nome: '))
n4 = str(input('Digite o último nome:'))
ordem = [n1,n2,n3,n4]
random.shuffle(ordem)
print('A ordem do trabalho')
print(ordem)