dados = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while dados not in 'MmFf':
    dados = str(input('Dados inválidos. Tente novamente'))
print('Sexo {} resgistrado com sucesso'.format(dados))