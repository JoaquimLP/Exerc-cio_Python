"""
5. Faça um programa que leia um arquivo contendo o nome e o preço de diversos produtos
(separados por linha), e calcule o total da compra. Faça um tratamento de erro para verificar se
o arquivo a ser lido existe. Em caso contrário, identifique o tipo de erro gerado e trate-o, a gerar
uma mensagem adequada ao usuário.
"""
import codecs
try:
    def compra(x):
        try:
            lista_preco_str = []
            with codecs.open(x, "r+") as abrir:
                for linha in abrir.readlines():
                    lista = linha.replace(",", ".").replace("\n", "").replace("\r", "")
                    lista_preco_str.append(lista.split("R$")[-1])
            lista_preco = list(map(float, lista_preco_str))
            if sum(lista_preco) > 0:
                with codecs.open(x, "r") as ler:
                    l = ler.read()
                print(l)
                print(f"total da compra: {sum(lista_preco)}")
            else:
                TypeError
        except TypeError:
            print("Não existe preço para somar.")

    print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse programa só aceita arquivos .txt")
    nome = input("Informe o arquivo: ")
    compra(nome)
except FileNotFoundError:
    print("Arquivo não encontrado")