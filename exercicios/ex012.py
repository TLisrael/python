#Faça um algoritmo que leia o preço de um produto e mostre sue novo preço com 5% de desconto

preco = float(input('Informe o valor do produto: '))
novoPreco = preco - (preco * 0.05)
print(f'Novo valor do produto: {novoPreco:,.2f}')