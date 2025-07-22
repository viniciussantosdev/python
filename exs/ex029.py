vel = float(input('Qual a velocidade do seu automóvel atual?'))
if vel <= 80:
    print('Tenha um bom dia e dirija com segurança!')
else:
    multa = (vel-80) * 10
    print('Você foi MULTADO! Você ultrapassou o limite permetido de 80Km/h')
    print('Você terá que pagar uma multa de R${:.2f}.'.format(multa))
    print('Tenha um bom dia e dirija com segurança')