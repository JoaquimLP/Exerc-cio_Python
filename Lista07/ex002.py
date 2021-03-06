"""
2. Faça um programa que receba como entrada o nome de um arquivo de entrada e outro de
saída. O arquivo de entrada contem em cada linha o nome de uma cidade (ocupando 40
caracteres) e o seu número de habitantes. O programa deverá ler o arquivo de entrada e gerar
um arquivo de saída onde aparece o nome da cidade mais populosa seguida pelo seu número
de habitantes. Caso a cidade tenha mais de 40 caracteres, identifique o tipo de erro gerado e
trate-o, a gerar uma mensagem adequada ao usuário.
"""
from time import sleep
import codecs
try:
    def tamanho(x,y,t):
        try:
            habitantes = list(map(int, y))
            maior = max(habitantes)
            maior_cidade = len(x[0])
            pos = habitantes.index(maior)
            for i in range(len(x)):
                if len(x[i]) > maior_cidade:
                    print(len(x[i]))
                    maior_cidade = len(x[i])
            if maior_cidade > t:
                raise Exception
            else:
                with codecs.open("maior.txt", "a") as novo:
                    novo.write(f"A Cidade com mais habitante é {x[pos]} com {y[pos]}\n")
                with codecs.open("maior.txt") as n:
                    mostra = n.read()
                    print(mostra)
                n.closed
                novo.closed
        except Exception:
            print(f"Ops, esse programa so aceita arquivo com {t} caracteres")

    def cidade(nome):
        lista = []
        cidades = []
        print("Analizando dados.....")
        sleep(2)
        with codecs.open(nome, 'r+') as abrir:
            for linha in abrir.readlines():
                x = linha.replace("\n", "").replace("\r", "").replace("    ", "").replace(".", "")
                lista.append(x.split("\t")[-1])
                cidades.append(x.split('\t')[0])
        cidades.pop(0)
        cidades.pop(0)
        lista.pop(0)
        lista.pop(0)
        tamanho(cidades, lista, 40)
        abrir.closed


    print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse programa só aceita arquivos .txt")
    nome_cidade = input("Informe o arquivo: ")
    cidade(nome_cidade)
except FileNotFoundError:
    print("Arquivo não encontrado")