# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Informe a quantidade de KMs rodados: '))
dias = int(input('Informe a quantidade de dias em que o carro foi alugado: '))

valorTotalDias = dias * 60
valorTotalKm = km * 0.15
valorTotal = valorTotalDias + valorTotalKm

print(f'Total a pagar {valorTotal}\nTotal a pagar pelos dias {valorTotalDias}\nTotal a pagar pelos KMs {valorTotalKm}')
