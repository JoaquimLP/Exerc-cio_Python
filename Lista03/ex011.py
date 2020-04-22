"""
11. Faça um programa que peça 10 números inteiros, calcule e mostre a QUANTIDADE de
    números pares e a SOMA dos números impares.
"""
print("vai ser informado 10 numeros...")
c = 0
par = []
impar = 0
while c < 10:
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        par.append(num)
    else:
        impar += num
    c += 1
print(f"Foram digitado {len(par)} pares"
      f"\nA soma de todos os numeros impares é {impar}")