"""
12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela
abaixo) e 3% para o Vale Refeição e que o FGTS corresponde a 11% do Salário Bruto,
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao
Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua
hora e a quantidade de horas trabalhadas no mês.
"""
from time import sleep
print("===================Simulador de folhas de Pagamento===================")
valor = float(input("Quantos você ganhar por horas trabalhado? "))
horas = int(input("Quantas horas trabalhou esse mes? "))
print("--"*20)
print("Carregando...")
sleep(2)
print("-----------Resultado-----------")
salBruto = valor * horas
inss = (salBruto * 10) / 100
vr = (salBruto * 3) / 100
fgts = (salBruto * 11) / 100
if salBruto <= 900:
    i = 0
    total = inss + vr
    ir = 0
    print("Isento")
elif salBruto > 900 and salBruto <= 1500:
    i = 5
    ir = (salBruto * i) / 100
    total = inss +  ir + vr
elif salBruto > 1500 and salBruto <= 2500 :
    i = 10
    ir = (salBruto * i) / 100
    total = inss + ir + vr
else:
    i = 20
    ir = (salBruto * 20) / 100
    total = inss +  ir + vr


salLiquido = salBruto - total
print(f"Salario Bruto: (R${valor:.2f} x {horas}) = {salBruto}"
      f"\nIR({i}%):   R${ir:.2f}"
      f"\nINSS(10%):  R${inss:.2f}"
      f"\nFGTS(11%):  R${fgts:.2f}"
      f"\nVale Refeição (3%): R${vr:.2f}"
      f"\nTotal de descontos: R${total:.2f}"
      f"\nSalário Liquido: R${salLiquido:.2f}")

