"""
22. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    Álcool:
        • até 20 litros, desconto de 3% por litro
        • acima de 20 litros, desconto de 5% por litro
    Gasolina:
        • até 20 litros, desconto de 4% por litro
        • acima de 20 litros, desconto de 6% por litroLinguagem de Programação Python
        11
    Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
    (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago
    pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,50 o preço do litro do
    álcool é R$ 1,90.
"""
from time import  sleep
print("+++++++++++++++POSTO POR DO SOL+++++++++++++++")
print("Escolha qual combustivel deseja abastecer"
      "\nopção [G] para Gasolina"
      "\nopçãp [A] para Alcoool")
combustivel = input("Vai abastecer com Alcool ou Gasolina: (G/A) ")
litro = float(input("Quando litro vai ser? "))
print("Carregando...")
sleep(2)
print("-----------Resultado-----------")
if combustivel in 'Gg':
    c = "G-gasolina"
    preco = 3.50
    valor = litro * preco
    if litro <= 20:
        des = 4
        total = valor - ((valor*des)/100)
    else:
        des = 6
        total = valor - ((valor*des)/100)
elif combustivel in 'Aa':
    c = "A-álcool"
    preco = 1.90
    valor = litro * preco
    if litro <= 20:
        des = 3
        total = valor - ((valor * des) / 100)
    else:
        des = 5
        total = valor - ((valor * des) / 100)

print(f"O combustivel escolhido foi {c}, vai ser abastecido {litro}l"
      f"\nEstá no valor de R${preco:.2f} o litro"
      f"\ncom o desconto de {des}%, ficar no total R${total:.2f}")