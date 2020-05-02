"""
24. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora
possui uma loja de conveniências. Faça um programa que implemente uma caixa
registradora rudimentar. O programa deverá receber um número desconhecido de
valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo
operador para indicar o final da compra. O programa deve então mostrar o total da
compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e
mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
    Lojas Tabajara
    Produto 1: R$ 2.20
    Produto 2: R$ 5.80
    Produto 3: R$ 0
    Total: R$ 9.00
    Dinheiro: R$ 20.00
    Troco: R$ 11.00
"""
from time import sleep
print("==========Lojas Tabajara==========")
loja = []
totalP = 0
res = ''
def limpar():
    print("\n"*2)
    print("Gerar um novo Pedido")
    sleep(2)

while True:
    # Preechendo o valores dos produtos
    c = 1
    while True:
        print("A o Digitar [ 0 ] em um dos produtos o programa encerra.")
        produto = float(input(f"Digite o preço do Produto {c}: R$"))
        loja.append(produto)
        totalP += produto
        if produto == 0:
            break
        c += 1
    valorPago = float(input("Dinheiro: R$"))
    print("Gerando o Cumpon Fiscal...")
    sleep(2)
    print("-=-"*20)
    for i in range(len(loja)):
        print(f"Produto {i}: R${loja[i]:.2f}")
    troco = valorPago - totalP
    print(f"Total: R${totalP:.2f}")
    print(f"Dinheiro: R${valorPago:.2f}")
    print(f"Troco: R${troco:.2f}")

    res = input("Deseja continuar S/N: ").strip().upper()
    while res not in 'SsNn':
        print("Erro deve informa S para sim e N para não.")
        res = input("Deseja continuar S/N: ").strip().upper()
    if res in 'Nn':
        break
    else:
        limpar()
print("Fim")