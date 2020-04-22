"""
5. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor
    a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""
listaNotas = []
aluno = []
notasAluno = []
mediaFinal = []
print ('Notas dos Alunos')
for i in range(2):
    nome = input("Nome do aluno: ")
    aluno.append(nome)
    media = 0
    notasAluno = []
    print ('Aluno: ' + nome)
    for j in range(2):
        notasAluno.append(float(input(f'Nota {j+1}º: ')))
        media += notasAluno[j]
    media = media / 2
    print (media)
    if media >= 7:
        mediaFinal.append(media)
    listaNotas.append(media)

print (listaNotas)
print(f"A medias dos alunos aprovado {mediaFinal}")