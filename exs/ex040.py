p1 = float(input('Primeira nota:'))
p2 = float(input('Segunda nota:'))
resul = (p1 + p2) / 2
print('Tirando {} e {}, a média do aluno é de {:.1f}'.format(p1, p2, resul))
if resul > 6:
    print('O aluno foi APROVADO!')
elif resul < 6 and resul > 5:
    print('O aluno está de RECUPERAÇÃO!')
else:
    print('O aluno foi REPROVADO!')