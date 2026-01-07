somaidade = 0
maiorh = 0
nomevelho = 0
totm = 0
for p in range(1,5):
    print('--------{}°Pessoa--------'.format(p))
    nome = str(input('Nome: '.strip()))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): '.strip()))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorh = idade
        nomevelho = nome
    if sexo in 'Mm'and idade > maiorh:
        maiorh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 25:
        totm += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O nome do homem mais velho tem {} anos e se chama {}'.format(maiorh, nomevelho))
print('O total de mulheres com menos de 25 anos é de {}'.format(totm))