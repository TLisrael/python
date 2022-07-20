# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

print('Três retas formam um triangulo? ')

a = int(input('Informe o valor da primeira linha: '))
b = int(input('Informe o valor da segunda linha: '))
c = int(input('Informe o valor da terceira linha: '))

if a + b > c:
    print('Suas linhas podem formar um triangulo!')
else:
    print('Não é possivel transformar essas linhas em um triangulo!')
