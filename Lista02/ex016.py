"""
16. Faça um Programa que peça um número correspondente a um determinado ano e em
        seguida informe se este ano é ou não bissexto.
"""
from datetime import  date
ano = int(input("Digite o ANO que você quer analisar: digite 0 para analiza no ano atual "))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 or ano % 400 == 0:
    print(f"O ano de {ano}, BISSEXTO")
else:
    print(f"O ano de {ano}, não é BISSEXTO")