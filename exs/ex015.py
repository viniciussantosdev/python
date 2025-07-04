dias = int(input('Quantos dias você percorreu com o carro alugado? '))
km = float(input('Quantos km você percorreu com o carro? '))
pago = (dias * 60) + (km * 0.15)
print('O valor que você deve pagar é de R${:.2f}'.format(pago))
