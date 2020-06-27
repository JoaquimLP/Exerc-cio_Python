from time import sleep
import codecs
def lista_telefone(nome, telefone):
    with codecs.open("lista_telefone.txt", "a") as adicionar:
        adicionar.write(f"{nome} -> {telefone}\n")
    adicionar.closed
def mostrar_lista(x):
    print("numeros adicionado na lista: ")
    if x == 0:
        with codecs.open("lista_telefone.txt") as abrir:
            x = abrir.read()
        print(x)
        abrir.closed
while True:
    print('Numero adicionado com sucesso,\npressione zero para sair do sistema: ')
    nome = input("Informe o nome da pessoa: ")
    telefone = input("Informe o numero de telefone do mesmo: ")
    if int(telefone) == 0:
        mostrar_lista(0)
        break
    else:
        lista_telefone(nome, telefone)
        print("Adiciocnando.....")
        sleep(2)

