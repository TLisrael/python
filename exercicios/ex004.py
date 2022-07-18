# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

string = input('Teste algo: ')
print('O tipo primitivo é', type(string))
print('É alfabetico?', string.isalpha())
print('Esta em caixa alta?', string.isupper())
print('É númerico?', string.isnumeric())
print('É printavel? ', string.isprintable())