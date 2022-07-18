# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
work1 = input('Informe o seu nome: ')
work2 = input('Informe o seu nome: ')
work3 = input('Informe o seu nome: ')
work4 = input('Informe o seu nome: ')

workList = [work1, work2, work3, work4]
sortedNumbers = sorted(workList)
print(f'Ordem de apresentação: {sortedNumbers}')