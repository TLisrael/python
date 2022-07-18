#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
angulo = float(input('Informe um angulo: '))
#Metodo radians converte os valores em valores radianos.
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O ângulo {angulo} tem: \nSeno{seno:,.2f}\nCosseno {cosseno:,.2f}\nTangente {tangente:,.2f}')