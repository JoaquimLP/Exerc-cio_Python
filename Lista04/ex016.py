"""
16. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
lista = []
for c in range(10):
    num = float(input(f"Informe um numero na posição {c+1}: "))
    lista.append(num)
for i in range(len(lista)):
    print(f" {lista[i]}", end = " - ")
print("Fim")
lista = lista[::-1]
print("__"*20)
print("Ordem inversa: ", end = "" )
for i in range(len(lista)):
    print(f" {lista[i]}", end = " - ")
print("Fim")