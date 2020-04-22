"""
9. Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
from time import sleep
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
print("--"*20)
print("Carregando...")
sleep(2)
print("-----------Resultado-----------")

if num2 < num1 > num3:
    if num1 > num2 > num3:
        print(f"Colocando em ordem decrescente {num1} - {num2} - {num3}")
    else:
        print(f"Colocando em ordem decrescente {num1} - {num3} - {num2}")
elif num1 < num2 > num3:
    if num2 > num1 > num3:
        print(f"Colocando em ordem decrescente {num2} - {num1} - {num3}")
    else:
        print(f"Colocando em ordem decrescente {num2} - {num3} - {num1}")
else:
    if num2 < num1 < num3:
        print(f"Colocando em ordem decrescente {num3} - {num1} - {num2}")
    else:
        print(f"Colocando em ordem decrescente {num3} - {num2} - {num1}")
