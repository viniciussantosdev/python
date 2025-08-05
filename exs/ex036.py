print('\033[4;35mAnalisando e aprovando empréstimos\033[m')
casa = int(input('Valor da casa:R$'))
salario = int(input('Salário do comprador:R$'))
anos = int(input('Anos de financiamento:'))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo poderá ser concedido!')
else:
    print('Empréstimo negado!')