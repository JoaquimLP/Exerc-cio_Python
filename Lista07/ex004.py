"""
4. Faça um programa que permita que o usuário entre com diversos nomes e telefone para
cadastro, e crie um arquivo com essas informações, uma por linha. O usuário finaliza a entrada
com ‘0’ para o telefone. Faça o tratamento de erro para verificar se o numero de telefone está
composto apenas por números. Caso contrário, identifique o tipo de erro gerado e trate-o, a
gerar uma mensagem adequada ao usuário.
"""
from time import sleep
import codecs
try:
    def lista_telefone(nome, telefone):
        try:
            if len(str(telefone)) > 11:
                raise TypeError
            else:
                with codecs.open("lista_telefone.txt", "a") as adicionar:
                    adicionar.write(f"{nome} -> {telefone}\n")
                adicionar.closed
        except TypeError:
            print("Ops: Número de telefone inválido....")
    def mostrar_lista(x):
        print("Números adicionado à lista: ")
        if x == 0:
            with codecs.open("lista_telefone.txt") as abrir:
                x = abrir.read()
            print(x)
            abrir.closed
except FileNotFoundError:
    print("Arquivo não encontrado")


while True:
    try:
        print('Número adicionado com sucesso,\npressione zero para sair do sistema: ')
        nome = input("Informe o nome da pessoa: ")
        telefone = int(input("Informe o número de telefone do mesmo: "))
        if int(telefone) == 0:
            mostrar_lista(0)
            break
        else:
            lista_telefone(nome, telefone)
            print("Adicionando.....")
            sleep(2)
    except ValueError:
        print("**"*20)
        print("Você não pode digitar carácter especiais no campo número de telefone, somente os números: ")