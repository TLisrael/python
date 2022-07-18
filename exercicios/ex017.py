#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#Calcule e mostre o comprimento da hipotenusa
import math
oposto = float(input('Informe o comprimento do cateto oposto do triangulo retangulo: '))
adjacente = float(input('Informe o comprimento do cateto adjacente triangulo retangulo: '))
perimetro = math.pow(oposto,2) + math.pow(adjacente,2)
hipotenusa = pow(perimetro, 0.5)
print(f'Seu triangulo retangulo possui as seguintes dimensões: {oposto:,.0f}cmx{adjacente:,.0f}cm\nO comprimento da hipotenusa é de: {hipotenusa:,.0f}cm')