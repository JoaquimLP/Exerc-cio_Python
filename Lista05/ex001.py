"""
1. Faça um programa para imprimir:
     1
     2 2
     3 3 3
     .....
     n n n n n n ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima
até a n-ésima linha.

"""
def loop(n):
    for c in range(1, n+1):
        cont = 1
        while True:
            print(c, end="")
            if cont == c:
                break
            cont += 1
        print()
numero = int(input("Informe um numero: "))
loop(numero)