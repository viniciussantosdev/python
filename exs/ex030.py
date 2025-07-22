num = int(input('Me diga um número que eu direi se é par ou ímpar:'))
resul =  num % 2
if resul == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é ímpar'.format(num))