"""
8. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a
    soma dos quadrados dos elementos do vetor.
"""
print("===========Calculos rapido===========")
listaA = []
elementos = []
soma = 0
for c in range(10):
    valores = int(input(f"Digite o {c+1}º: "))
    soma += valores ** 2
    listaA.append(valores)
print(f"Os numeros digitatos foram {listaA}")
print(f"A soma dos quadrados dos elementos do vetor é {soma}")

