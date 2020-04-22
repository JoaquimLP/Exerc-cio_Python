"""
15. Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores
    com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas
    vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de
    $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de
    $470. Escreva um programa (usando um array de contadores) que determine quantos
    vendedores receberam salários nos seguintes intervalos de valores:
        a. $200 - $299
        b. $300 - $399
        c. $400 - $499
        d. $500 - $599
        e. $600 - $699
        f. $700 - $799
        g. $800 - $899
        h. $900 - $999
        i. $1000 em diante
"""
res = ''
c = 0
lista  = [["$200 - $299", "$300 - $399", "$400 - $499",
           "$500 - $599", "$600 - $699", "$700 - $799",
           "$800 - $899", "$900 - $999", "$1000 em diante"],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
while True:
    sal = float(input("Quantos você recebeu esse mês: "))
    if sal < 200:
        print("Valor invalido..")
    else:
        if sal >= 200 and sal <= 299:
            lista[1][0] += 1

        elif sal >= 300 and sal <= 399:
            lista[1][1] += 1

        elif sal >= 400 and sal <= 499:
            lista[1][2] += 1

        elif sal >= 500 and sal <= 599:
            lista[1][3] += 1

        elif sal >= 600 and sal <= 699:
            lista[1][4] += 1

        elif sal >= 700 and sal <= 799:
            lista[1][5] += 1

        elif sal >= 800 and sal <= 899:
            lista[1][6] += 1

        elif sal >= 900 and sal <= 999:
            lista[1][7] += 1
        else:
            lista[1][8] += 1
    res = input("Deseja continuar S/N: ").upper().strip()
    while res not in 'SN':
        print("Erro...")
        res = input("Deseja continuar S/N: ").upper().strip()
    if res in 'Nn':
        break
for i in range(len(lista[1])):
    print(f"Foram {lista[1][i]} que receberam um salario em {lista[0][i]}")