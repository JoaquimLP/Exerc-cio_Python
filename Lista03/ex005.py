"""
5. Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
i = 0
lista = []
for c in range(0,5):
    num = int(input("Digite um numero: "))
    i += num
    lista.append(num)
media = i/len(lista)
print(f"Os numero digitado foram {lista}, e a soma entre eles {i}, e a media {media}")