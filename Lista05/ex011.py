"""
11. Reverso do número. Faça uma função que retorne o reverso de um número inteiro
informado. Por exemplo: 127 -> 721.
"""
def reverso(n):
    a = list(str(n))
    a.reverse()
    b = ''.join(a)
    print(f'o numero inversor de {n} -> {b}')

numero = int(input("Digite um numero inteiro: "))
reverso(numero)