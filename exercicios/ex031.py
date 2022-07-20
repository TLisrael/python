# Desenvolva um programa que pergunte a distância de uma viagem em KM.
# Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens até 200Km
# e R$0.45 para viagens mais longas.

distancia = int(input('Informe a distancia da viagem em KM: '))

if distancia <= 200:
    passagem = distancia * 0.50
    print(f'O preço da passagem é {passagem}')
else:
    passagem = distancia * 0.45
    print(f'O preço da passagem é {passagem}')
