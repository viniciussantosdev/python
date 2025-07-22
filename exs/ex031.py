dis = int(input('Qual é a distância da sua viagem?'))
print('Você irá inicar uma viagem de {}Km.'.format(dis))
pp = dis * 0.5 if dis <= 200 else dis * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(pp))