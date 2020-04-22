"""
 1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
"""
print("============Vamos roda============")
i = 0
lista = []
for c in range(0,5):
    num = int(input(f"Digite um numero na posição {c}º: "))
    i += num
    lista.append(num)
print("<>"*10)
print(f"Os numeros digitados foram -> {lista}")