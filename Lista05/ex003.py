"""
3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a
soma desses três argumentos.
"""
def soma(a,b,c):
    s = a + b + c
    print("-"*20)
    print(f'A soma de {a} + {b} + {c} = {s}')
    print("Finalizando o programa...")

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))
soma(n1, n2, n3)