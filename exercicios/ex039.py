# Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou passou do prazo.

ano_nascimento = int(input('Informe o ano em que você nasceu: '))

calculo_ano = 2022 - ano_nascimento

if calculo_ano == 18:
    print('Você já pode se alistar ao serviço militar.')
elif calculo_ano < 18:
    faltam = 18 - calculo_ano
    print(f'Faltam {faltam} anos para você se alistar.')
elif calculo_ano > 18:
    print('Já passou o tempo do alistamento obrigatório')
