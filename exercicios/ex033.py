#  Faça um programa que leia três números e mostre
#  qual é o maior e qual é o menor.

A = int(input('Informe um número: '))
B = int(input('Informe um número: '))
C = int(input('Informe um número: '))

if A > B and A > C:
    print(f'{A} é maior que {B} e {C}')
elif B > A and B > C:
    print(f'{B} é maior que {A} e {C}')
else:
    print(f'{C} é maior que {A} e {B}')
