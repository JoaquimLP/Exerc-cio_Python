"""
28.	Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado
    pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor
    inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
    Montar a tabuada de: 5
        Começar por: 4
        Terminar em: 7
        Vou montar a tabuada de 5 começando em 4 e terminando em 7:
        5 X 4 = 20
        5 X 5 = 25
        5 X 6 = 30
        5 X 7 = 35
        Obs: Você deve verificar se o usuário não digitou o final menor que o inicial
"""
print("======Tabuada======")

tabuada = int(input("Digite uma numero inteiro para ver sua tabuada: "))
inicio = int(input("Digite o inicio da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))
multi = 0
while inicio > fim:
    print("Erro...  numero inicial não pode ser maior do que o numero final.")
    inicio = int(input("Digite o inicio da tabuada: "))
    fim = int(input("Digite o fim da tabuada: "))
print("=="*20)
print(f"Montar a tabuada de: {tabuada}")
print(f"Começar por: {inicio}")
print(f"Terminar em: {fim}")
print("__"*20)
print(f"Vou montar a tabuada de {tabuada} começando em {inicio} e terminando em {fim}:")
for i in range(inicio,fim + 1):
    multi = tabuada * i
    print(f"{tabuada} X {i} = {multi}")