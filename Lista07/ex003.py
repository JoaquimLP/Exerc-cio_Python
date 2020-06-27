"""
3.  Faça um programa no qual o usuário informa o nome do arquivo e uma palavra, e retorne o
    número de vezes que aquela palavra aparece no arquivo. Faça o tratamento de erro para
    verificar se o arquivo está vazio. Em caso positivo, identifique o tipo de erro gerado e trate-o, a
    gerar uma mensagem adequada ao usuário.
"""
import codecs
try:
    def pesquisar(x):
        try:
            cont = 0
            lista = []
            with codecs.open(x, 'r+') as abrir:
                for linha in abrir.readlines():
                    p = linha.replace("\n", "").upper()
                    lista.append(p.split(' '))
            print("==" * 20)
            with codecs.open(x, "r+") as f:
                text = f.read()
            print(text)
            if len(text) > 0:
                palavra = input("Digite a palavra que deseja pesquisa: ").strip()
                for i in range(len(lista)):
                    if palavra.upper() in lista[i]:
                        cont += 1
                # print(lista)
                print(f"A palavra informada foi {palavra}"
                      f"\nE o numero de vezes que ela aparece é: {cont}")
            else:
                raise Exception
        except:
            print("O arquivo informado está vazio.")

    print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse programa só aceita arquivos .txt")
    nome = input("Informe o arquivo: ")

    pesquisar(nome)
except FileNotFoundError:
    print("Arquivo não encontrado")