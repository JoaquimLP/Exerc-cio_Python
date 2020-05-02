"""
11. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine
    quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses
    alunos.
"""
import random
alunos = [[], []]
soma = 0
cont = 0
for c in range(5):
    idade = random.randint(6,40)
    altura = round(random.uniform(1,2), 2)
    alunos[0].append(idade)
    alunos[1].append(altura)
media = round(sum(alunos[1]) /len(alunos[1]), 2)
for j in range(len(alunos[0])):
    if alunos[0][j] > 13 and alunos[1][j] < media:
        cont += 1
    print(f"aluno {j+1}: idade {alunos[0][j]}, altura {alunos[1][j]}")
print("<>"*12)
print(f"A media de altura de todos os alunos é {media}")
print(f'A quantidade de alunos acima de 13 anos possuem altura inferior à média {cont}')