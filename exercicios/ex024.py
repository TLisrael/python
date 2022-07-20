# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Informe sua cidade: ')).strip()
print(cidade[0:5].lower() == 'santo')
