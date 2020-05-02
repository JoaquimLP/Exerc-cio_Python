"""
15. Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias
    vezes e limitando o fatorial a números inteiros positivos e menores que 16.
"""
res = ""
while True:
    n = int(input('Digite umm numero para calcular seu fatorial: '))
    while n <= 0 or n > 16:
        print("Erro: iforme um numero entre 1 e 16")
        n = int(input('Digite umm numero para calcular seu fatorial: '))
    c = n
    f = 1
    print(f"Calculando {n}! = ", end='')
    while c > 0:
        print(f"{c}", end= '')
        print(' x ' if c > 1 else '=', end= '')
        f *= c
        c -= 1
    print(f' {f}')
    res = input("Deseja continuar? [S/N] ").strip().upper()[0]
    while res not in 'SN':
        res = input("Deseja continuar? [S/N] ").strip().upper()[0]
    if res in 'N':
        break
print("Finalizando.....")