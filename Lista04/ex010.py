"""
10. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""
print("======VAMOS INTERCALAR======")
lista1 = []
lista2 = []
lista3 = []
lista4 = []

for c in range(10):
    num1 = int(input(f"Lista 1 posição {c}: "))
    num2 = int(input(f"Lista 2 posição {c}: "))
    num3 = int(input(f"Lista 2 posição {c}: "))
    lista1.append(num1)
    lista2.append(num2)
    lista3.append(num3)
    lista4.append(lista1[c])
    lista4.append(lista2[c])
    lista4.append(lista3[c])
print("=======Lista 1 e 2=======")
print(lista1)
print("=======Lista 2=======")
print(lista2)
print("=======Lista 3=======")
print(lista3)
print("=======Lista4=======")
print(lista4)
