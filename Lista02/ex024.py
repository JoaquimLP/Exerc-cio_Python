"""
24. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg          Acima de 5 Kg
        File Duplo   R$ 4,90 por Kg    R$ 5,80 por Kg
        Alcatra      R$ 5,90 por Kg    R$ 6,80 por Kg
        Picanha      R$ 6,90 por Kg    R$ 7,80 por Kg
    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne
    da promoção, porém não há limites para a quantidade de carne por cliente. Se compra
    for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total
    da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
    pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e
    quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""
from time import sleep
print("==============Hipermercado Tabajara==============")
print("Escolha a opção:"
      "\n[1]-> escolher dois tipo de carne"
      "\n[2]-> escolher dois tipo de carne"
      "\n-------------------Até 5 Kg          Acima de 5 Kg"
      "\n[1]-> File Duplo   R$ 4,90 por Kg    R$ 5,80 por Kg"
      "\n[2]-> Alcatra      R$ 5,90 por Kg    R$ 6,80 por Kg"
      "\n[3]-> Picanha      R$ 6,90 por Kg    R$ 7,80 por Kg"
      "\n-----------------Tipo de pagamento-----------------"
      "\n[5]-> Cartão de Credito Tabajara"
      "\n[6]-> Cartãp de Credito"
      "\n[7]-> Dinheiro"
      )
din = "Dinheiro"
cc = "Cartãp de Credito"
cct = "Cartão de Credito Tabajara"
print("--"*30)
print("Fazendo o pedido-----")
escolha = int(input("Quantos Tipo de carne deseja compra: "))
fp = int(input("Informe a forma de pagamento: "))
print("---"*20)
if escolha == 1:
    opcao = int(input("Que tipo de carne deseja compra: "))
    if opcao == 1 or opcao == 2 or opcao == 3:
        peso = float(input("Quantos quilos de carde deseja comprar: "))
        if opcao == 1:
            carne = "File Duplo"
            if peso <= 5:
                preco = 4.90
            else:
                preco = 5.80
        elif opcao == 2:
            carne = "Alcatra"
            if peso <= 5:
                preco = 5.90
            else:
                preco = 6.80
        elif opcao == 3:
            carne = "Picanha"
            if peso <= 5:
                preco = 6.90
            else:
                preco = 7.80
        valor = preco * peso
        if fp == 5 or fp == 6 or fp == 7:
            if fp == 5:
                fpagamento = cct
                des = "5%"
                total = valor - ((valor * 5) / 100)
            elif fp == 6:
                des = "0%"
                fpagamento = din
                total = preco * peso
            else:
                des = "0%"
                fpagamento = cc
                total = preco * peso
            print("--" * 20)
            print("Carregando...")
            sleep(2)
            print("-----------CUPOM FISCAL-----------")
            print(f"Tipo de carne: {carne}"
                  f"\nQuantidade: {peso:.2f}Kg"
                  f"\nForma de pagamento: {fpagamento}"
                  f"\nValor descontado: {des}"
                  f"\nTotal a pagar: {total:.2f}")
        else:
            print("Forma de Pagamento Invalido....")
    else:
        print("Opção Invalida")
# opção 2  -----------------------------
elif escolha == 2:
    opcao1 = int(input("Qual é a primeiro tipo de carne deseja compra: "))
    opcao2 = int(input("Qual é a segundo tipo de carne deseja compra: "))
    print("__"*30)
    if opcao1 == 1 or opcao1 == 2 or opcao1 == 3 and opcao2 == 1 or opcao2 == 2 or opcao2 == 3:
        if opcao1 == 1 and opcao2 == 2 or opcao1 == 2 and opcao2 == 1:
            tipo1 = "File Duplo"
            tipo2 = "Alcatra"
            peso1 = float(input(f"Quantos quilos de {tipo1} deseja compra: "))
            peso2 = float(input(f"Quantos quilos de {tipo2} deseja compra: "))
            if peso1 <= 5:
                preco1 = 4.90

            else:
                preco1 = 5.80

            if peso2 <= 5:
                preco2 = 5.90
            else:
                preco2 = 6.80
        elif opcao1 == 1 and opcao2 == 3 or opcao1 == 3 and opcao2 == 1:
            tipo1 = "File Duplo"
            tipo2 = "Picanha"
            peso1 = float(input(f"Quantos quilos de {tipo1} deseja compra: "))
            peso2 = float(input(f"Quantos quilos de {tipo2} deseja compra: "))
            if peso1 <= 5:
                preco1 = 4.90

            else:
                preco1 = 5.80

            if peso2 <= 5:
                preco2 = 6.90
            else:
                preco2 = 7.80
        else:
            tipo1 = "Alcatra"
            tipo2 = "Picanha"
            peso1 = float(input(f"Quantos quilos de {tipo1} deseja compra: "))
            peso2 = float(input(f"Quantos quilos de {tipo2} deseja compra: "))
            if peso1 <= 5:
                preco1 = 5.90
            else:
                preco1 = 6.80

            if peso2 <= 5:
                preco2 = 6.90
            else:
                preco2 = 7.80
        print("__" * 30)
        valor = (preco1 * peso1) + (preco2 * peso2)
        if fp == 5 or fp == 6 or fp == 7:
            if fp == 5:
                fpagamento = cct
                des = "5%"
                total = valor - ((valor * 5) / 100)
            elif fp == 6:
                des = "0%"
                fpagamento = din
                total = valor
            else:
                des = "0%"
                fpagamento = cc
                total = valor
            print("--" * 20)
            print("Carregando...")
            sleep(2)
            print("-----------CUPOM FISCAL-----------")
            print(f"Tipo de carne: {tipo1} e {tipo2}"
                  f"\nQuantidade: {peso1:.2f}Kg de {tipo1} e {peso2:.2f}Kg de {tipo2}"
                  f"\nForma de pagamento: {fpagamento}"
                  f"\nValor descontado: {des}"
                  f"\nTotal a pagar: {total:.2f}")
        else:
            print("Forma de Pagamento Invalido....")

    else:
        print("Umas das opções escolhida está invalida")

else:
    print("Escolha Invalida")
