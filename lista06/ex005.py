"""
5. Faça um programa que receba do usuário um arquivo texto. Crie outro arquivo texto contendo
o texto do arquivo de entrada, mas com as vogais substituídas por ‘*’.
"""
from time import sleep
def arquivo(f, n):
    with open(f, "r+") as abrir:
        x = abrir.read()
        texto = x.replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")\
                .replace("a", "*").replace("a", "*").replace("i", "*").replace("o", "*").replace("u", "*")
    print("==============Arquivo Atual==============")
    print(x)
    print()
    print("Gerando um novo arquivo....")
    sleep(2)
    print("==============Novo Aquivo==============")

    with open(n, "a") as f:
         f.write(texto)
    with open(n) as novo:
        y = novo.read()
    print(y)
    abrir.closed
    f.closed

print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse progama só aceita arquivos .txt")
a = input("Informe o arquivo: ")
novo_arquivo = input("Informe o nome do arquivo que vair ser gerado: ")
print("=="*20)
arquivo(a, novo_arquivo)