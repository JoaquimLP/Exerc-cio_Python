"""
13. Faça um programa que, dado um conjunto de N números, determine o menor valor, o
    maior valor e a soma dos valores.
"""
n = int(input("Digite a quantidade de numero deseja informa: "))
lista = []
c = 0
maior = 0
menor = 0
while c < n:
    num = int(input("Informe um numero: "))
    lista.append(num)
    c += 1
maior = max(lista)
menor = min(lista)
print(f"O maior valor enviado é {maior}")
print(f"O menor valor enviado é {menor}")