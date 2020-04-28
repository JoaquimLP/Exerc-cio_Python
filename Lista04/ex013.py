"""
13. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são:
    a. "Telefonou para a vítima?"
    b. "Esteve no local do crime?"
    c. "Mora perto da vítima?"
    d. "Devia para a vítima?"
    e. "Já trabalhou com a vítima?"
    O programa deve no final emitir uma classificação sobre a participação da
    pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
    ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
    "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
from time import  sleep
print("Vou lhe Fazer 5 perguntas sobre o crime ocorrido digite [S] sim é [N] para não")
p1 = input("Telefonou para a vítima? (S/N) ").upper()
p2 = input("Esteve no local do crime? (S/N) ").upper()
p3 = input("Mora perto da vítima? (S/N) ").upper()
p4 = input("Devia para a vítima? (S/N) ").upper()
p5 = input("Já trabalhou com a vítima? (S/N) ").upper()
res = []

print("--"*20)
print("Carregando...")
sleep(2)
print("-----------Resultado-----------")

if p1 in "S/N" and p2 in "S/N" and p3 in "S/N" and p4 in "S/N" and p5 in "S/N":
    if p1 == 'S':
        res.append(p1)
    if p2 == "S":
        res.append(p2)
    if p3 == "S":
        res.append(p3)
    if p4 == "S":
        res.append(p4)
    if p5 == "S":
        res.append(p5)
#-------------------------------------------------------
    if len(res) == 2:
        print("Supeita")
    elif len(res) == 3 or len(res) == 4:
        print("Cúmplice ")
    elif len(res) == 5:
        print("Assassino")
    else:
        print("Inocente")
else:
    print("Umas das Resposta está invalida...")


