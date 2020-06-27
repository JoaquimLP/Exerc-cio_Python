import codecs
def zenit_pelar(x):
    with codecs.open(x, "r+") as abrir:
        for linha in abrir.readlines():

            texto = linha.upper().replace("A", "I").replace("B", "D").replace("C", "C").replace("D", "B")\
                .replace("E", "O").replace("F", "H").replace("G", "G").replace("I", "A").replace("H", "F")\
                .replace("J", "J").replace("K", "Q").replace("L", "N").replace("M", "V").replace("N", "L")\
                .replace("O", "E").replace("P", "Z").replace("Q", "K").replace("R", "T").replace("S", "S")\
                .replace("T", "R").replace("U", "U").replace("V", "M").replace("W", "X").replace("X", "W")\
                .replace("Z", "P")
            crip = texto
            print(crip, end=" ")


print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse progama só aceita arquivos .txt")
nome = input("Informe o arquivo: ")
zenit_pelar(nome)