"""
 Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome.

"""
# A função strip elimina os espaços antes e depois da string
nome = str(input('Informe seu nome completo: ')).strip()

print(f'O nome em maiusculo é {nome.upper()}')
print(f'O nome em minusculo é {nome.lower()}')
# Removendo os espaços do nome para a contagem no print
print(f'O nome inteiro tem {len(nome) - nome.count(" ")} letras')
# print(f'O seu primeiro nome tem {nome.find(" ")} letras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} ')
