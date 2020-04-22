'''
2. Faça um Programa que leia 4 notas, mostre as notas e a média na tela
'''

i = 0
lista = []
for c in range(0,4):
    num = int(input(f"Digite a {c+1}º nota: "))
    i += num
    lista.append(num)
media = i/len(lista)
print(f"As notas informada foram {lista} e á media {media}")