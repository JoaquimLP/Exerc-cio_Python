import codecs
try:
    def arquivo_nota(x):
        try:
            nota_str = []
            aluno = []
            with codecs.open(x, "r+") as abrir:
                for linha in abrir.readlines():
                    lista = linha.upper().replace(",", ".").replace("\n", "").replace("\r", "")
                    nota_str.append(lista.split("NOTA: ")[-1])
                    aluno.append(lista.split("ALUNO: ")[-1].split(" NOTA:")[0])
            nota = list(map(float, nota_str))
            pos = nota.index(max(nota))
            if nota[pos] >= 0:
                print(f"A maior nota foi {nota[pos]} e é do aluno {aluno[pos]}")
            else:
                raise RuntimeError
        except FileNotFoundError:
            print("Arquivo não encontrado")
        except RuntimeError:
            print("Não foi possível realizar o cálculo, pois os valores estão negativos")


    print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse programa só aceita arquivos .txt")
    nome = input("Informe o arquivo: ")
    arquivo_nota(nome)
except FileNotFoundError:
    print("Arquivo não encontrado")