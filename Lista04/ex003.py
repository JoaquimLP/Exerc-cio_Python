"""
3. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram
lidas. Imprima as consoantes.
"""
c = 0
consoante = 0
listaC = []
while c < 5:
    letra = input("Digite uma Letra: ").upper().strip()
    if letra not in 'AEIOU':
        listaC.append(letra)
        consoante += 1
    c += 1
print(f"Foram informado {consoante}: ")
print(listaC)
