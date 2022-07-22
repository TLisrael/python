"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
O programa vai perguntar o valor da casa, o valor do salário do comprador em quantos
anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o empréstimo será negado
"""

valor_casa = float(input('Informe o valor da casa que deseja comprar: '))
valor_salario = float(input('Informe o valor do seu salário: '))
anos_pagamento = int(input('Informe a quantidade de anos em que deseja pagar: '))

meses = anos_pagamento * 12
prestacao = valor_casa / meses

if prestacao > valor_salario * 0.30:
    print('Não podemos oferecer seu empréstimo agora')
else:
    print('Empréstimo aprovado.')
