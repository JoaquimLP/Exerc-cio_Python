"""
27.	 Encontrar números primos é uma tarefa difícil. Faça um programa
    que gera uma lista dos números primos existentes entre 1 e um número
    inteiro informado pelo usuário.
"""

num = int(input("Digite um número: "))
lista = []
soma = 0

for i in range(1, num + 1):
    cont = 0
    for c in range(1, i + 1):
        if i % c == 0:
            cont += 1
    if cont == 2:
        lista.append(i)

print("Números primos: ", lista)
