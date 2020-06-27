"""
7. Faça um programa que receba dois arquivos do usuario, e crie um terceiro arquivo com o
conteúdo dos dois primeiros juntos (o conteudo do primeiro seguido do conteudo do segundo).
"""
from time import sleep
import codecs
def arquivo(f,a):
    with codecs.open(f, "r+") as arq1:
        x = arq1.read()
    with codecs.open(a, "r+") as arq2:
        y = arq2.read()
    with codecs.open("novo.txt", "a") as novo:
        novo.write(x)
        novo.write("\n")
        novo.write(y)
    with codecs.open("novo.txt") as n:
        mostra = n.read()
    print("Carregando....")
    sleep(2)
    print(mostra)
    arq1.closed
    arq2.closed
    novo.closed
    n.closed
print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse progama só aceita arquivos .txt")
a1 = input("Informe o primeiro arquivo: ")
a2 = input("Informe o segundo arquivo: ")
print("=="*20)
arquivo(a1, a2)