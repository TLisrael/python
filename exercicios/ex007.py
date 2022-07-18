# Desenvolva um progama que leia as duas notas de um aluno, calcule e mostre sua média

nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2

print(f'Sua media final foi de {media:,.2f}')