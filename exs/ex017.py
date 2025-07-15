from math import hypot
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
cal = hypot(c1, c2)
print('A hipotenusa deste valor vai medir {:.2f}'.format(cal))