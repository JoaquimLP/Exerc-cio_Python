"""
13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-
    Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
print("======DIAS DA SEMANA======")

dia = int(input("Digite um numero para saber o dia da Semana: "))
if dia == 1:
    print("DOMINGO")
elif dia == 2:
    print("SEGUNDA")
elif dia == 3:
    print("TERÇA")
elif dia == 4:
    print("QUARTA")
elif dia == 5:
    print("QUINTA")
elif dia == 6:
    print("SEXTA")
elif dia == 7:
    print("SABADO")
else:
    print("valor inválido")