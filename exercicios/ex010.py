# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

reais = float(input('Informe o valor de reais que você possui: '));
dolar = reais / 5.34
print(f'Com R${reais:,.2f} você pode comprar U${dolar:,.2f}')
