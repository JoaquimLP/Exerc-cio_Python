"""
25.	Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
    Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo: Fatorial de: 5
    5! = 5 . 4 . 3 . 2 . 1 = 120
"""
num = int(input("Digite um número: "))
c = num
f = 1
print(f"Fatorial de: {num}")
print(f"{c}!: ", end='')
while c > 0:
    print(f"{c} ", end='')
    print(' x ' if c>1 else ' =',end='')
    f *= c
    c -= 1
print(f" {f}")