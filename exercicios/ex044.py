# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

prod = int(input('Informe o produto que deseja comprar:\n'
                 '1 - Teclado\n'
                 '2 - Mouse\n'
                 '3 - Monitor\n'
                 ': '))

valor = float(input('Informe o valor do produto: '))

forma_pagamento = int(input(f'Informe a forma de pagamento para {prod}:\n '
                            f'1 - á vista no dinheiro ou cheque 10% de desconto\n'
                            f'2 - á vista no cartão 5% de desconto\n'
                            f'3 - Em até 2x no cartão\n'
                            f'4 - 3x ou mais no cartão com 20% de juros\n'
                            f': '))
if forma_pagamento == 1:
    valor_total = valor - 0.10 * valor
    print(f'O valor total para ser pago é de {valor_total}')
elif forma_pagamento == 2:
    valor_total = valor - 0.5 * valor
    print(f'O valor total para ser pago é de {valor_total}')
elif forma_pagamento == 3:
    print(f'O valor total de pagamento é de: {valor}')
elif forma_pagamento == 4:
    valor_total = valor + 0.20 * valor
    print(f'O valor total para ser pago é de {valor_total}')
