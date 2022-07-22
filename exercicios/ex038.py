# Escreva um programa que leia dois números inteiros e compare-os
# mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais.

num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))

if num1 > num2:
    print(f'O numero {num1} é maior que o numero {num2}')
elif num2 > num1:
    print(F'O numero {num2} é maior que o numero {num1}')
elif num2 == num1:
    print('Os numeros informados são iguais.')
