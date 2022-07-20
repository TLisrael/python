# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# Em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: '))
print(f'A letra "A" aparece {frase.count("a")} vezes')
print(f'A letra "A" aparece primeiro na posição {frase.find("a")}')
print(f'A letra "A" aparece pela ultima vez na posição {frase.rfind("a")}')
