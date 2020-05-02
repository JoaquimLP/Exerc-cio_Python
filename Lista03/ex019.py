"""
19.	Faça um programa que peça para n pessoas a sua idade, ao final o programa
    deverá verificar se a média de idade da turma varia entre 0 e 25,26 e 60
    e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa,
    conforme a média calculada.
"""
soma = 0
turma = int(input("Digite quantas pessoas serão registradas: "))
while turma <= 0:
    print("Deve ser informado pelo menos um integrante.")
    turma = int(input("Digite quantas pessoas serão registradas: "))
for c in range(turma):
    aluno = int(input(f"Informe a idade do {c +1} aluno: "))
    while aluno < 0:
        print("Erro... não pode digitar valores negativos.")
        aluno = int(input(f"Informe a idade do {c +1} aluno: "))
    soma += aluno
media = soma / turma
print("=="*20)
print(f"A média de idade de um turma de {turma}, é {media}")
if 0 <= media <= 25:
    print("A turma é jovem.")
elif 26 <= media <= 60:
    print("A turma é adulta.")
else:
    print("A turma é idosa.")

