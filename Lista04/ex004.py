"""
4. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene
    os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três
    vetores.
"""
from time import sleep
import random
print("===Gerando numeros Aleatorio===")
par = []
impar = []
lista = []
for c in range(0,20):
    num = random.randint(0,20)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    lista.append(num)
print("Carregando...")
sleep(2)
print(f"Os numeros digitados pares são: {par}")
print(f"Os numeros digitados impares são: {impar}")
print(f"{lista}")
