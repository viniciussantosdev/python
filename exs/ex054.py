from datetime import date
atual = date.today().year
totma = 0
totme = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu?'.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totma += 1
    else:
        totme += 1
print('Ao tivemos {} pessoas maiores de idade.'.format(totma))
print('Ao tivemos {} pessoas menores de idade.'.format(totme))