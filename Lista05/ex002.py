"""
2. Faça um programa para imprimir:
     1
     1 2
     1 2 3
     .....
     1 2 3 ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até
a n-ésima linha.
"""

def loop(n):
    for c in range(1, n+1):
        cont = 1
        while True:
            print(cont, end= " ")
            if cont == c:
                break
            cont += 1
        print()
numero = int(input("Informe um numero: "))
loop(numero)