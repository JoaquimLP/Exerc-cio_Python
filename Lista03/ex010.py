"""
10. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
   número elevado ao segundo número. Não utilize a função de potência da linguagem.
"""
print("Calculadora de Pontencia... ")
c = 0
p = 1
num1 = int(input("Base: "))
num2 = int(input("Expoente: "))
for c in range(num2):
    p *= num1
    c += 1
print(f"{num1}^{num2} = {p}")

