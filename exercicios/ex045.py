from random import choice

# Crie um programa que faça o computador jogar Jokenpô com você.

jogada = int(input('Informe o número da sua jogada:\n'
                   '1 - Pedra\n'
                   '2 - Papel\n'
                   '3 - Tesoura\n'
                   'Qual você escolhe? '))

jogadas_list = ['Pedra', 'Papel', 'Tesoura']
random_jogada = choice(jogadas_list)
if jogada == 1 and random_jogada == 'Pedra':
    print('Empate')
elif jogada == 2 and random_jogada == 'Papel':
    print('Empate')
elif jogada == 3 and random_jogada == 'Tesoura':
    print('Empate')
elif jogada == 1 and random_jogada == 'Papel':
    print(f'Escolhi {random_jogada} e você pedra. Eu ganhei.')
elif jogada == 1 and random_jogada == 'Tesoura':
    print(f'Okay. Sua pedra esmagou minha tesoura aqui, parça.')
elif jogada == 2 and random_jogada == 'Pedra':
    print(f'Você ganhou.')
elif jogada == 2 and random_jogada == 'Tesoura':
    print('Você perdeu. Cortei seu papel kakakaka')
elif jogada == 3 and random_jogada == 'Pedra':
    print('Quebrei sua tesoura com minha pedra de crack.')
elif jogada == 3 and random_jogada == 'Papel':
    print(f'Você venceu. Você me cortou todinho ="(')
else:
    print('Jogada inválida.')
