from random import choice

# Escreva um programa eu faça o computador "pensar" em um número inteiro entre
# 0 e 6 e peça para o usuário tentar descobrir qual foi o número escolhido pelo
# computador. O programa deverá mostrar na tela se o usuário venceu ou perdeu.

numero = [0, 1, 2, 3, 4, 5]
numero_random = choice(numero)

print('******* Adivinhe o número *******')
print('Adivinhe o número em que estou pensando!')
print('Dica: ele está entre 0 e 5')

chute = input(" ")

if chute == numero_random:
    print(f'Acertou! o número era {numero_random}')
else:
    print(f'Errou! o numero era {numero_random}')
