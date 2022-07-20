# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.

nome = str(input('Informe seu nome completo: ')).strip()
# pegando o nome e transformando o mesmo em uma lista
n = nome.split()

# Imprindo o primeiro nome              Imprimindo o ultimo nome
print(f' Seu nome é {n[0]} e seu ultimo nome é {n[len(n) - 1]}')
