"""
7. Faça um programa que receba dois números inteiros e gere
    os números inteiros que estão no intervalo compreendido por eles.
"""
num1=int(input("digite um numero: "))
num2=int(input("digite outro numero: "))
while num2<num1:
    print("Erro... O primeiro número tem que menor do que segundo")
    num1=int(input("digite um numero: "))
    num2=int(input("digite outro numero: "))
for i in range(num1 + 1,num2):
    print(i)

