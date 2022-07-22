# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# -3 para hexadecimal

opcao = int(input('Escolha a base de conversão:\n'
                  '1 - Binário\n'
                  '2 - Octal\n'
                  '3 - Hexadecimal\n'))

numero = int(input('Informe o número que deseja converter: '))

if opcao == 1:
    print(f'O número {numero} em binário é {bin(numero)}')
elif opcao == 2:
    print(f'O número {numero} em octal é {oct(numero)}')
elif opcao == 3:
    print(f'O número {numero} em hexadecimal é {hex(numero)}')
else:
    print('Opção inválida')
