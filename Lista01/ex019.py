"""
19. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as
quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    a. comprar apenas latas de 18 litros;
    b. comprar apenas galões de 3,6 litros;
    c. misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de
        folga e sempre arredonde os valores para cima, isto é, considere latas cheias
"""
import math
print("==============Loja do VOVO==============")
metros = float(input("Digite a quantidade de metros quadrados a serem pintados: "))

litros = metros/6
valorL = 80
valoG = 25
latas = math.floor(litros / 18+(18*0.10))
galao1 = math.floor(litros / 3.6+(3.6*0.10))
total = latas * valorL
totaG = galao1 * valoG

lata = math.floor(litros / 18 )
resto = litros % 18
if (resto > 0 and resto<= 3.6):
    galao = 1
elif  (resto==0):
    galao = 0
else:
    galao = math.floor(resto / 3.6+(3.6*0.10))

totalLG  = (lata * valorL) + (galao * valoG)

print(f'\n Quantidade de latas: {latas} latas. Preço latas:{total} reais. '
    f'\n Quantidades galões: {galao1} galões. Preço galões: {totaG}. '
    f'\n Solução Otima, latas: {lata} e galões: {galao} Valor: {totalLG}')
