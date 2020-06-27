"""
13. Faça um programa que leia um arquivo contendo o nome e o preço de diversos produtos
(separados por linha), e calcule o total da compra.
"""
import codecs
def compra(x):
    lista_preco_str = []
    with codecs.open(x, "r+") as abrir:
        for linha in abrir.readlines():
            lista = linha.replace(",", ".").replace("\n", "").replace("\r", "")
            lista_preco_str.append(lista.split("R$")[-1])
    lista_preco = list(map(float, lista_preco_str))
    with codecs.open(x, "r", "utf-8") as ler:
        l = ler.read()
    print(l)
    print(f"total da compra: {sum(lista_preco)}")

print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse programa só aceita arquivos .txt")
nome = input("Informe o arquivo: ")
compra(nome)