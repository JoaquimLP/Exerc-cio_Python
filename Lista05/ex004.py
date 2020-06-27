"""
4. Faça um programa, com uma função que necessite de um argumento. A função retorna
o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero
ou negativo.
"""
from time import sleep
def resultado(n):
    print("Resultado... este numero é: ")
    if n > 0:
        print("P")
    else:
        print("N")

print("P - positivo | N - negativo")
numero = int(input("Informe um numero: "))
print("Carregando...")
sleep(1)
resultado(numero)

