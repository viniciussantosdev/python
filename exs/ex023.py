num = int(input('Coloque aqui um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Vamos analisar o número {}...'.format(num))
print('Unidade:{} '.format(u))
print('Dezena:{} '.format(d))
print('Centena:{} '.format(c))
print('Milhar:{} '.format(m))