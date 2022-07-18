# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
student1 = input('Informe o nome do aluno 1: ')
student2 = input('Informe o nome do aluno 2: ')
student3 = input('Informe o nome do aluno 3: ')
student4 = input('Informe o nome do aluno 4: ')

list = [student1, student2, student3, student4]
shuffle = choice(list)
print(f'O nome do aluno escolhido é: {shuffle.upper()}')
