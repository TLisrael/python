# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.

km = int(input('Informe a velocidade em que você estava: '))

if km > 80:
    v_t = float(km - 80) * 7
    print(f'Você foi multado em R$ {v_t} ')
else:
    print('Você está na velocidade permitida.')
