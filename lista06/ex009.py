"""
9. Faça um programa no qual o usuário informa o nome do arquivo e uma palavra, e retorne o
número de vezes que aquela palavra aparece no arquivo.
"""

import codecs
def pesquisar(x):
    cont = 0
    lista = []
    with codecs.open(x, 'r+') as abrir:
        for linha in abrir.readlines():
            p = linha.replace("\n", "").upper()
            lista.append(p.split(' '))
    print("=="*20)
    with codecs.open(x, "r") as f:
        text = f.read()
    print(text)
    palavra = input("Digite a palavra que deseja pesquisa: ")
    for i in range(len(lista)):
        if palavra.upper() in lista[i]:
            cont += 1
    #print(lista)
    print(f"A palavra informada foi {palavra}"
          f"\nE o numero de vezes que ela aparece é: {cont}")

print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse progama só aceita arquivos .txt")
nome = input("Informe o arquivo: ")

pesquisar(nome)