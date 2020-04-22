"""
9. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor
    de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados
    dos dois outros vetores.
"""
print("======VAMOS INTERCALAR======")
lista1 = []
lista2 = []
lista3 = [[], []]
lista4 = []

for c in range(10):
    num1 = int(input(f"Lista 1 posição {c}: "))
    num2 = int(input(f"Lista 2 posição {c}: "))
    lista1.append(num1)
    lista2.append(num2)
    lista4.append(lista1[c])
    lista4.append(lista2[c])
    lista3[0].append(num1)
    lista3[1].append(num2)
print("=======Lista 1 e 2=======")
print(lista1)
print(lista2)
print("=======Lista 3=======")
print(lista3)
print("=======Lista4=======")
print(lista4)
