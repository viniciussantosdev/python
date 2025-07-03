v1 = float(input('Qual é o preço do produto? R$'))
desc =  v1 - (v1 * 5/ 100)
print('O produto de R${:.2f} ficou com o desconto de 5% ficou por apenas R${:.2f}!'.format(v1,desc))