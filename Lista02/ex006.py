"""
6. Faça um Programa que leia três números e mostre o maior deles.
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
    print(f"O numero maior é {num1}")
elif num1 < num2 > num3:
    print(f"O numero maior é {num2}")
else:
    print(f"O numero maior é {num3}")