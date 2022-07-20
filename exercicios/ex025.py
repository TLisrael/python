# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# Sem ver resposta
nome_completo = str(input('Informe seu nome completo: ')).strip()
dividindo = nome_completo.split()
print(f'Seu nome tem Silva? {dividindo.count("Silva").__bool__()}')

# resposta
nome = str(input('Informe seu nome completo: ')).strip()
print(f'Seu nome tem Silva? {"silva" in nome.lower()}')
