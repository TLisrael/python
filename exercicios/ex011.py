# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessaria para pinta-lam sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura
quantidade = area / 2

print(f'Area = {area}m² \nQuantidade de litros de tinta necessário = {quantidade:,.2f}')