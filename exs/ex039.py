print('\033[4;32mAlistamento Militar\033[m')
from datetime import date
atual = date.today().year
nas = int(input('Ano de nascimento:'))
idade = atual - nas
print('Quem nasceu em {} tem {} anos em {}'.format(nas, idade, atual))
if idade == 18:
    print('Você terá que se alistar imediatamente!')
elif idade < 18:
    tempo = 18 - idade
    print('Você ainda não tem 18 anos, faltam {} anos para o alistamento militar'.format(tempo))
elif idade > 18:
    tempo = idade - 18
    print('Você deveria ter se alistado há {} anos'.format(tempo))