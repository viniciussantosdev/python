lista_precos = [1500,1000,800,2000]
taxa_impostos = 0.1
for precos in lista_precos:
    imposto = precos * taxa_impostos
    print(f'Preço do produto {precos}, imposto de {imposto}')
print('--------------------------')
for precos in lista_precos:
    if precos >= 1000:
        taxa = 0.15
    else:
        imposto = precos * taxa
    print('Preço do produto {}, imposto de {}'.format(precos, imposto))