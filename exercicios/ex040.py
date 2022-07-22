# Crie um programa que leia duas notas de um aluno e calcule sua média
# mostrando uma mensagem no final de acordo com a média:
# - Media abaixo de 5.0: Reprovado
# - Media entre 5.0 e 6.9: Recuperação
# - Media 7.0 ou superioor: Aprovado

n1 = float(input('Informe sua nota: '))
n2 = float(input('Informe sua nota: '))

media = n1 + n2 / 2

if media < 5.0:
    print('Reprovado:')
elif media >= 5.0 and media <= 6.9:
    print('Recuperação')
elif media >= 7.0:
    print('Aprovado')
