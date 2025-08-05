nome = str(input('Qual é o seu nome?'))
if nome == 'Vinicius':
    print('Que nome top!')
elif nome == 'João' or nome == 'Silvana' or nome == 'Lucas':
    print('Seu nome é muito popular!')
elif nome in 'Pedro Eduardo Mauro':
    print('Seu nome é muito grande!')
else:
    print('Seu nome é PAIA.')
print('Tenha um bom dia {}'.format(nome))
