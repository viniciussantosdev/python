print('========== Gerenciador de Pagamentos ============')
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais''')
opcao = int(input('Qual é sua opção?'))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparcela = int(input('Quantas parcelas?'))
    parcela = total / totalparcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparcela,parcela))
else:
    total = preco
    print('Opção invalida! Tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no total.'.format(preco, total))