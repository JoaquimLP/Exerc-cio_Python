"""
6. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
    multiplicação e os números.
"""
lista = []
m = 1 #mutiplicação
s = 0 #somatorio
print("======Sistema de Caculos======")
for c in range(1, 6):
    num = int(input(f"Digite um numero a posição {c}º: "))
    lista.append(num)
    s += num
    m *= num

print(f'Os numeros informados foram {lista}')
print(f"A soma de todos os numeros da lista {s}")
print(f'A mutiplicação de todos os numeros da lista {m}')
