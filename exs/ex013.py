salario = float(input('Qual é om salário do funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print('O salário do funcionário era de R${:.2f}, e com o aumento de 15%, passou a receber R${:.2f}'.format(salario, aumento))