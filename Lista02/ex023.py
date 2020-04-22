"""
23. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                    Até 5 Kg     Acima de 5 Kg
        Morango R$ 2,50 por Kg   R$ 2,20 por Kg
        Maçã    R$ 1,80 por Kg   R$ 1,50 por Kg
    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$
    25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para
    ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e
    escreva o valor a ser pago pelo cliente.
"""
print("==============Loja de Fruta==============")
print("Escolha a opção:"
      "\n[1]Morango"
      "\n[2]Maçã")
opcao = int(input("Qual fruta deseja comprar: "))
if opcao == 1 or opcao == 2:
    peso = float(input("Quantos quilos vai comprar: "))

    if opcao == 1:
        fruta = "MORANGO"
        if peso <= 5:
            preco = 2.50
        else:
            preco = 2.20
    elif opcao == 2:
        fruta = "MAÇÃ"
        if peso <= 5:
            preco = 1.80
        else:
            preco = 1.50
    valor = preco * peso
    if peso > 8 or valor > 25:
        total = valor - ((valor *10)/100)
        print(f"O cliente vai compra {peso}Kg de {fruta} com o deconto de 10% vai ficar no total de R${total:.2f}")
    else:
        print(f"O cliente vai compra {peso}Kg de {fruta} e o valor final é de R${valor:.2f}")
else:
    print("Opção Invalida")
