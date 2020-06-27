"""
4. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas vezes
cada letra do alfabeto aparece dentro do arquivo.
"""
from time import sleep
from collections import defaultdict
def abrir_arquivo(f):
    cont = 0
    print("Aguarde so um momento o sistema está processado...")
    sleep(2)
    with open(f) as abrir:
        x = abrir.read()
        #texto = x.replace('\n', '').replace(' ', '').replace('/', '')
        lista = list(x.upper())
        alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                    'Y', 'Z']
        cont = []

        for i in range(len(alfabeto)):
            for c in range(len(lista)):
                if alfabeto[i] == lista[c]:
                    cont.append(alfabeto[i])

        keys = defaultdict(list)

        for key, value in enumerate(cont):
            keys[value].append(key)
        for value in keys:
            if len(keys[value]) >= 1:
                print(f"{value} => {len(keys[value])}")
        print("-=-"*20)
        print(x)

    #print(f"O caratere {car}, aparece: {cont} vezes no arquivo")
    abrir.closed

print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse progama só aceita arquivos .txt")
print("-"*25)
vogais = 0
arquivo = input("Informe o arquivo: ")
print("=="*20)
abrir_arquivo(arquivo)

