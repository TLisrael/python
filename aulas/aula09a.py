# Fatiamento de string
frase_fatiamento = 'Readability counts.'
print(frase_fatiamento[1:10:2])

# Manipulação de strings -> Texto
print("""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
""")

# Em python tudo é um objeto, portanto, podemos colocar var.qualquerCoisa
# que não dará erro de sintaxe
frase = "Now is better than never."
print(frase.count('e'))

# Criando lista com separador
frase_lista = 'Errors should never pass silently.'
dividido = frase_lista.split()
# Puxando apenas a primeira palavra da lista
print(dividido[0])
# Pegue o elemento [0] e mostre a letra [3]
print(dividido[0][3])
