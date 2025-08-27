print('Calcule o seu Índice de massa corporal')
peso = float(input('Qual é o seu peso (kg):'))
altura = float(input('Qual é sua altura (m):'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal!')
elif imc >= 18.5 and imc < 25:
    print('Parabéns! Você está nom peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Você está obeso!')
else :
    print('Você está com obesidade mórbida!')