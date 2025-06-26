al = input('Olá, aluno!, qual é o seu nome?')
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
med = (n1 + n2) / 2
print('A média do aluno {} é de {:.1f}'. format(al,n1, n2, med))