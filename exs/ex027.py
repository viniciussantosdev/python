nome = str(input('Digite seu nome completo:')).strip()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome.split()[0].capitalize()))
print('Seu último nome é {}'.format(nome.split()[-1].capitalize() ))
