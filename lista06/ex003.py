"""
3. Faça um programa que receba do usuário um arquivo texto e um caractere. Mostre na tela
quantas vezes aquele caractere ocorre dentro do arquivo.
"""
from time import sleep
def abrir_arquivo(f, car):
    cont = 0
    print("Aguarde so um momento o sistema está processado...")
    sleep(2)
    with open(f) as abrir:
        x = abrir.read()
        #texto = x.replace('\n', ''').replace('/', '')).replace(' ', '
        lista = list(x.upper())
        for c in range(len(lista)):
            if lista[c] == car:
                cont += 1
        print(x)
    print(f"O caratere {car}, aparece: {cont} vezes no arquivo")
    abrir.closed

print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse progama só aceita arquivos .txt")
print("-"*25)
vogais = 0
arquivo = input("Informe o arquivo: ")
caractere = input("Qual caractere, deseja consulta no arquivo: ").upper().strip()
print("=="*20)
abrir_arquivo(arquivo, caractere)

