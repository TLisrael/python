# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('Três retas formam um triangulo? ')

a = int(input('Informe o valor da primeira linha: '))
b = int(input('Informe o valor da segunda linha: '))
c = int(input('Informe o valor da terceira linha: '))

if a == b == c:
    print('Equilátero')
elif a == b and a != c or b == c and b != a or c == a and c != b:
    print('Isósceles')
elif a != b and b != c and c != a:
    print('Escaleno')
