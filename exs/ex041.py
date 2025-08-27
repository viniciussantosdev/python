from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento:'))
idade = atual - nascimento
if idade <= 9:
    print('O atleta é da categoria MIRIM!')
elif idade <= 14:
    print('O atleta é da categoria INFANTIL!')
elif idade <= 19:
    print('O atleta é da categoria JUNIOR!')
elif idade <= 25:
    print('O atleta é da categoria SÊNIOR!')
else:
    print('O atleta é da categoria MASTER!')