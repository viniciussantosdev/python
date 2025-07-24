a = int(input('Digite o primeiro valor:'))
b = int(input('Digite o segundo valor:'))
c = int(input('Digite o terceiro valor:'))
# Menor Valor:
menor = a
if a > b and b < c:
    menor = b
if a > c and c < b:
    menor = c
# Maior Valor:
maior = a
if a < b and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
