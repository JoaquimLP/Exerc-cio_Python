"""
6. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""
from  time import  sleep
n = 0
print("Carregando....")
sleep(2)
for c in range(1,50):
    if c % 2 != 0:
        print(c, end=' - ')
    c += 1
print("Fim")