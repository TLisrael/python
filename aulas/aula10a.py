n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2
print(f'A sua média é {media}')

if media >= 6.0:
    print('Sua média foi boa.')
else:
    print('Sua média foi ruim.')
