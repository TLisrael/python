# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Informe um número: '))
dobro = numero * 2
triplo = numero * 3
raizQ = numero ** (1 / 2)

print(f'O dobro de {numero} é {dobro}\nO triplo de {numero} é {triplo}\nA raizQ de {numero} é {raizQ:,.2f} ')
