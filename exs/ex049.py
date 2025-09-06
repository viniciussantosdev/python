tab = int(input('Digite um número para revelar sua tabuada:'))
for c in range(1,11):
    res = tab * c
    print('{} x {} = {}'.format(tab,c,res))