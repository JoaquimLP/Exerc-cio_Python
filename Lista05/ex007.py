"""
7. Faça uma função que informe a quantidade de dígitos de um determinado número
inteiro informado.
"""
def quant_numero(n):
    quant = len(n)
    print(f"Esse número tem {quant} dígitos")
n = input('Digite um número: ').strip()
quant_numero(n)