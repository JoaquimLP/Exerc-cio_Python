"""
8. Faça um programa que pergunte o preço de três produtos e informe qual produto você
    deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
from time import sleep
print("-------------MERCADO PONTO CERTO-------------")
produto1 = str(input("Informe o Primeiro produto: "))
preco1 = float(input("Agora informe o preço do mesmo: R$"))

produto2 = str(input("Informe o Segundo produto: "))
preco2 = float(input("Agora informe o preço do mesmo: "))

produto3 = str(input("Informe o Terceiro produto: "))
preco3 = float(input("Agora informe o preço do mesmo: "))
print("--"*20)
print("Carregando...")
sleep(2)
print("-----------Resultado-----------")

if preco2 > preco1 < preco3 :
    print(f"deve comprar o produto {produto1}, no valor R${preco1:.2f}")
elif preco1 > preco2 < preco3:
    print(f"deve comprar o produto {produto2}, no valor R${preco2:.2f}")
else:
    print(f"deve comprar o produto {produto3}, no valor R${preco3:.2f}")

