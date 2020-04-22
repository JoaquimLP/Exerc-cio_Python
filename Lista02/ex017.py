"""
17. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
    mesma é uma data válida.
"""
dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = int(input("ano: "))
valida = False

if  mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
    if 0 < dia <= 31:
        valida = True
elif mes==4 or mes==6 or mes==9 or mes==11:
    if 0 < dia <= 30:
        valida = True
elif mes == 2:
    if ano % 4 == 0 and ano % 100 or ano % 400 == 0:
        if 0 < dia <= 29:
            valida = True
    elif 0 < dia <= 28:
        valida = True

if valida:
    print(f"A data {dia}/{mes}/{ano}, e uma data valida")
else:
    print("não é um formato de data valida")