"""
14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
    ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
    tabela abaixo:
            Média de Aproveitamento   Conceito
            __________________________________
            Entre 9.0 e 10.0   -->       A
            Entre 7.5 e 9.0    -->       B
            Entre 6.0 e 7.5    -->       C
            Entre 4.0 e 6.0    -->       D
            Entre 4.0 e zero   -->       E

    O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
    mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for
    D ou E.Linguagem de Programação Python

"""
from time import  sleep
print("=================ESCOOLA BOM SABER=================")

nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))

media = (nota1 + nota2)/2
print("--"*20)
print("Carregando...")
sleep(2)
print("-----------Resultado-----------")
if 6 <= media <= 10:
    if 6 <= media <= 7.5:
        print("O Aluno ficou com media C, está APROVADO")
    elif 7.5 < media <= 9:
        print("O Aluno ficou com media B, está APROVADO")
    else:
        print("O Aluno ficou com media A, está APROVADO")
else:
    if 4 <= media < 6:
        print("O Aluno ficou com media D, está REPROVADO")
    else:
        print("O Aluno ficou com media E, está REPROVADO")