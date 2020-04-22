'''
17. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendose
que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o
sindicato. Enfim, faça um programa que mostre:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido
'''
from time import sleep
print("===================Simulador de folhas de Pagamento===================")
valor = float(input("Quantos você ganhar por horas trabalhado? "))
horas = int(input("Quantas horas trabalhou esse mes? "))
print("--"*20)
print("Carregando...")
sleep(2)
print("-----------Resultado-----------")
salBruto = valor * horas
inss = (salBruto * 8) / 100
sind = (salBruto * 5) / 100
ir = (salBruto * 11) / 100

totdesc = inss + sind + ir

saLiq = salBruto - totdesc

print(f"Salario Bruto: (R${valor:.2f} x {horas}) = {salBruto}"
      f"\nIR(11%):   R${ir:.2f}"
      f"\nINSS(8%):  R${inss:.2f}"
      f"\nSindicato (5%): R${sind:.2f}"
      f"\nTotal de descontos: R${totdesc:.2f}"
      f"\nSalário Liquido: R${saLiq:.2f}")


