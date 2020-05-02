"""
16.	 Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
    Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""
num = int(input('Digite um numero: '))
tot = 0
for c in range(1,num+1):
    if num % c == 0:
        tot+=1
print(f"O numero digitado é {num} e ")
if tot == 2:
    print('É UM NÚMERO PRIMO!')
else:
    print('NAO É UM NÚMERO PRIMO!')
