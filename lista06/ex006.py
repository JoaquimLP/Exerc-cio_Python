"""
6. Desenvolver um programa que leia o conteúdo de um arquivo e cria um arquivo com o mesmo
conteúdo, mas com todas as letras minúsculas convertidas para maiúsculas. Os nomes dos
arquivos (de entrada e saída) devem ser fornecidos, via teclado, pelo usuário.
"""
from time import sleep
def arquivo(f, n):
    with open(f, "r+") as abrir:
        x = abrir.read()
        texto = x.lower()
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

print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse progama só aceita arquivos .txt")
a = input("Informe o arquivo: ")
novo_arquivo = input("Informe o nome do arquivo que vair ser gerado: ")
print("=="*20)
arquivo(a, novo_arquivo)