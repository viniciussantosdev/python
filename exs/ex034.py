salario = float(input('Coloque aqui o valor do seu salário: R$'))
if salario <= 1250:
    novo = salario + (salario * 15 /100)
else :
    novo = salario + (salario * 10 /100)
print('Você tinha o salário de {:.2f}, com isso seu salário agora é de R${:.2f}'.format(salario, novo))