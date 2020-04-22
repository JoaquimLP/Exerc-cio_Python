"""
1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o
    valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
num = int(input("Digite um numero entre 0 é 10: "))
c  = 0

while(num > 10):
    print("informe um valor válido")
    num = int(input("Digite um numero entre 0 é 10: "))
    c += 1
print(f"O valor digitado e {num}")
