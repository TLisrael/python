# Faça um algoritmo que leia o salário do funcionario e mostre seu novo salário com 15% de aumento.

salario = float(input('Informe seu salário atual: '))
novoSalario = salario + (salario * 0.15)

print(f'Novo salário = {novoSalario:,.2f}')