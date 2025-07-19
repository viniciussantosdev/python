nome = str(input('Antes de você ver sua média das provas, digite seu nome:'))
pn = float(input('Digite a sua primeira nota:'))
sn = float(input('Digite sua segunda nota:'))
m = (pn + sn)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 5.0:
    print('Você passou na matéria de matemática, Meus Parabéns, {}!'.format(nome))
else:
    print('Infelizmente, você reprovou na matéria de matemática. Estude e se esforce mais na próxima')