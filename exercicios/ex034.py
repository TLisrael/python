# Escreva um programa que pergunte o salário de um funcionário
#  e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Informe o valor do seu salário: '))

if sal <= 1250:
    novo_sal = sal * 0.15
    print(f'Você recebeu um aumento de R$ {novo_sal}')
else:
    novo_sal = sal * 0.10
    print(f'Você recebeu um aumento de R$ {novo_sal}')
