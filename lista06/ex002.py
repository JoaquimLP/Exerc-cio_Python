"""
2. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas letras
são vogais e quantas são consoantes
"""
from time import sleep
def abrir_arquivo(f):
    vogais = 0
    consoante = 0
    cont = 0
    print("Aguarde so um momento o sistema está processado...")
    sleep(2)
    with open(f) as abrir:
        x = abrir.read()
        texto = x.replace('\n', '').replace(' ', '').replace('/', '')
        lista = list(texto.upper())
        for c in range(len(lista)):
            if lista[c] in 'AEIOU':
                vogais += 1
            elif lista[c] in 'BCDFGHJKLMNPQRSTVWXYZ':
                consoante += 1
            else:
                cont += 1
    print(f'Vogais: {vogais}')
    print(f'Consoantes: {consoante}')
    print(f"Carateres não contabilzado: {cont}")
    abrir.closed

print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse progama só aceita arquivos .txt")
print("-"*25)
vogais = 0
arquivo = input("Informe o arquivo: ")
print("=="*20)
abrir_arquivo(arquivo)

