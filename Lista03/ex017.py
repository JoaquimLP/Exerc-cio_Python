"""
17.	 Altere o programa de cálculo dos números primos, informando,
    caso o número não seja primo, por quais número ele é divisível.
"""
num = int(input('Digite um numero: '))
tot = 0
for c in range(1,num+1):
    if num  %  c == 0:
        tot+=1
print(f'Numero {num} foi divisível {tot} vezes.')
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    for i in range(1, num + 1):
        if num % i == 0:
            print(f' {i}', end=' ')
    print('\nE por isso ele NAO É PRIMO!')