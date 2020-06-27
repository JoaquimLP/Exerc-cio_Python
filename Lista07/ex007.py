"""
7. Faça um programa que leia um arquivo que contenha o nome e o Saldo de diversos clientes
de um banco (da seguinte forma: NOME: JOAO SALDO: 100.00). Permita que o usuário digite o
nome do cliente e um valor de deposito. Faça um tratamento de erro e controle se o valor do
depósito é positivo. Em caso contrário, identifique o tipo de erro gerado e trate-o, a gerar uma
mensagem adequada ao usuário.
"""
from time import sleep
import codecs
print("*****CASA DA MOEDA*****")
def paserFloate(valor):
    valor = float(valor.replace(",", "."))
    return valor

def tempo():
    print("=="*20)
    print("Carregando....")
    sleep(2)

#Cadastra um novo cliente
def cadastraCliente(nome, valor, arquivo):
    try:
        deposito = paserFloate(valor)
        tempo()
        if deposito >= 0:
            with codecs.open(arquivo, "a") as adicionar:
                adicionar.write(f"\nNOME: {nome.upper()} SALDO: {str(deposito)}")
            print("Cliente adicionado com sucesso")
        else:
            raise RuntimeError
    except FileNotFoundError:
        print("Arquivo não encontrado")
    except RuntimeError:
        print("Não foi possível realizar o depósito, pois o sistema não aceita valor negativo")


#Pesquisa pelo o nome do cliente
def pesquisarCliente(cliente, arquivo):
    nome = []
    saldo = []
    with codecs.open(arquivo, "r+") as abrir:
        for linha in abrir.readlines():
            lista = linha.upper().replace("\n", "").replace("\r", "").replace(".", ",")
            nome.append(lista.split("NOME: ")[-1].split(" SALDO:")[0])
            saldo.append(lista.split("SALDO: ")[-1])
    for i in range(len(nome)):
        if cliente.upper() in nome[i]:
            print("=="*20)
            print(f"NOME: {nome[i]} SALDO: {saldo[i]}")

def saldoBanco(arquivo):
    try:
        nome = []
        saldo = []
        with codecs.open(arquivo, "r+") as abrir:
            for linha in abrir.readlines():
                lista = linha.upper().replace("\n", "").replace("\r", "")
                nome.append(lista.split("NOME: ")[-1].split(" SALDO:")[0])
                saldo.append(lista.split("SALDO: ")[-1])
        print("deposito -> [1]\nconsultar -> [2]\nsair -> [3]")
        while True:
            try:
                print("---"*20)
                menuOpcao = int(input("Informe o serviço desejado: "))
                while 0 <= menuOpcao > 3:
                    print("ERRO: Deve ser informado de acordo com o menu:")
                    print("---"*20)
                    print("deposito -> [1]\nconsultar -> [2]\nsair -> [3]")
                    print("---"*20)
                    menuOpcao = int(input("Informe o serviço desejado: "))
                if menuOpcao == 1:
                    print("---"*20)
                    cliente = input("Informe o nome do cliente: ")
                    depositoTexto = input("Informe o valor do depósito: R$ ")

                    #funão para adicionar dados no arquivo
                    cadastraCliente(cliente, depositoTexto, arquivo)
                elif menuOpcao == 2:
                    print("---" * 20)
                    pesquisar = input("Informe o nome do cliente que deseja pesquisar: ")
                    tempo()
                    pesquisarCliente(pesquisar, arquivo)
                elif menuOpcao == 3:
                    print("---"*20)
                    print("Saindo do sistema.....")
                    break
            except TypeError:
                print("não suportado entre instâncias de 'int' e 'str'")
                print("---"*20)
                print("deposito -> [1]\nconsultar -> [2]\nsair -> [3]")

    except FileNotFoundError:
        print("Arquivo não encontrado")

print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse programa só aceita arquivos .txt")
nome = input("Informe o arquivo: ")
saldoBanco(nome)
print("O mundo precisa de mais gênios humildes! Hoje em dia somos poucos...")
