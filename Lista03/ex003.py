"""
3. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
   Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""
for c in range(1,21):
    print('\n', end=' ')
    print(c, end=' ')
for c in range(1,21):
    print('.', end=' ')
    print(c, end=' ')
print('Fim')
