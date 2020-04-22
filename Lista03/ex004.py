"""
4. Faça um programa que leia 5 números e informe o maior número.
"""
lista = []

for c in range(0,5):
    n = int(input('Digite um numero: '))
    lista.append(n)
    c += 1
if lista[0]>lista[1] and lista[0]>lista[2] and  lista[0]>lista[3] and  lista[0]>lista[4]:
    maior = lista[0]
elif lista[1]>lista[0] and lista[1]>lista[2] and  lista[1]>lista[3] and  lista[1]>lista[4]:
    maior = lista[1]
elif lista[2]>lista[0] and lista[2]>lista[1] and  lista[2]>lista[3] and  lista[2]>lista[4]:
    maior = lista[2]
elif lista[3]>lista[0] and lista[3]>lista[2] and  lista[3]>lista[1] and  lista[3]>lista[4]:
    maior = lista[3]
elif lista[4]>lista[0] and lista[4]>lista[2] and  lista[4]>lista[3] and  lista[4]>lista[1]:
    maior = lista[4]
print(f"Os numero informado foi {lista}")
print(f'E o numero maior digitado foi {maior}')