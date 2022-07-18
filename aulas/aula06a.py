n1 = (input('Digite um número: '))  # Definindo numeros inteiros. Por padrão, é STRING.
n2 = (input('Digite mais um número: '))
soma = (n1 + n2)
print(type(n1))  # Descobrindo tipo da variavel
print(f'A soma entre {n1} e {n2} vale {soma}')
print(n1.isnumeric()) # Diz se o valor é numerico
print(n1.isalpha()) # Diz se é alfabetico

