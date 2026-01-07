vendas_23 = {"jan": 15000, "fev": 10000, "mar": 5000}
vendas_24 = {"jan": 16000, "fev": 11000, "mar": 5100}
for mes in vendas_24:
    valor_23 = vendas_23[mes]
    valor_24 = vendas_24[mes]
    crescimento = valor_24 / valor_23 - 1
    print(f'No mês {mes} o crescimento foi de {crescimento:.1%}.')