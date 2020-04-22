'''
18. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
preço total.
'''
import math
print("==============Loja do VOVO==============")
metros = float(input("Digite a quantidade de metros quadrados a serem pintados: "))

litros = metros/3
valor = 80
latas = math.ceil(litros/18)

total = latas * valor
print(f'Vai precisar usar {latas} latas de 18 litros, vai cutar {total}')
