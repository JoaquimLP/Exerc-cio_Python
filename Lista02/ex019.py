"""
19. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica:
    utilize o operador módulo (resto da divisão).
"""
num = int(input("Digite um numero inteiro: "))

if num % 2 == 0:
    print(f"O numero {num} e um numero PAR!")
else:
    print(f"O numero {num} e um numero IMPAR!")