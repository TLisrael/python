# Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input('Informe um ano: '))

if ano % 4 == 0:
    print('bissexto')
else:
    print('Não é bissexto')
