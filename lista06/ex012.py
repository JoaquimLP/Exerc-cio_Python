"""
12. Dado um arquivo contendo um conjunto de nome e data de nascimento (DD MM AAAA, isto
e, 3 inteiros em sequência), faça um programa que leia o nome do arquivo e a data de hoje e
construa outro arquivo contendo o nome e a idade de cada pessoa do primeiro arquivo.
"""
import codecs
from datetime import date
def novo_arquivo(x,y):
    with codecs.open("pessoa_idade.txt", "a") as adicionar:
        for i in range(len(x)):
            adicionar.write(f"{x[i]} tem {y[i]} anos\n")
    with codecs.open("pessoa_idade.txt", "r") as abrir:
        a = abrir.read()
    print(a)
    adicionar.closed
    abrir.closed

def abri_arquivo(x):
    data_atual = date.today()
    idade = []
    ano_str = []
    pessoa = []
    with codecs.open(x, "r+", "utf-8") as abrir:
        for linha in abrir.readlines():
            char = linha.replace("\n", "").replace("\r", "")
            ano_str.append(char.split("/")[-1])
            pessoa.append(char.split("->")[0])
    ano_nasc = list(map(int, ano_str))
    for i in range(len(ano_nasc)):
        ano_atual = data_atual.year
        id = ano_atual - ano_nasc[i]
        idade.append(id)
    novo_arquivo(pessoa, idade)
    #print(idade)
    abrir.closed
print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse progama só aceita arquivos .txt")
nome = input("Informe o arquivo: ")
abri_arquivo(nome)