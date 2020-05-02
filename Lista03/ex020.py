"""
20.	Faça um programa que calcule o número médio de alunos por turma. Para isto,
    peça a quantidade de turmas e a quantidade de alunos para cada turma.
    As turmas não podem ter mais de 40 alunos:
"""
soma = 0
turma = int(input("Digite quantas turmas serão registradas: "))
while turma <= 0:
    print("Deve ser informado pelo menos um turmas.")
    turma = int(input("Digite quantas turmas serão registradas: "))
for c in range(turma):
    alunos = int(input(f"Digite quantos alunos tem na {c + 1}º turma: "))
    while 0 >= alunos or alunos > 40:
        if alunos > 40:
            print("Erro... só é permitido no máximo 40 alunos por turma!!")
        elif 0 >= alunos:
            print("Erro... não pode digitar valores negativos.")
        alunos = int(input(f"Digite quantos alunos tem na {c + 1}º turma: "))
    soma += alunos
media = soma / turma
print("=="*20)
print(f"Número de turmas: {turma}")
print(f"Total de alunos: {soma}")
print(f"Média de alunos: {media}")