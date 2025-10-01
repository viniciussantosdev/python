num = int(input('Digite um número:'))
for c in range(1,num +1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total = 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end='')
print('O número {} foi divisível {} vezes'.format(num, total))
