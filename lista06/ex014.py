"""
14. Faça um programa que receba do usuário um arquivo que contenha o nome e a nota de
diversos alunos (da seguinte forma: NOME: JOAO NOTA: 8), um aluno por linha. Mostre na tela
o nome e a nota do aluno que possui a maior nota.
"""
import codecs
def arquivo_nota(x):
    nota_str = []
    aluno = []
    with codecs.open(x, "r+") as abrir:
        for linha in abrir.readlines():
            lista = linha.upper().replace(",", ".").replace("\n", "").replace("\r", "")
            nota_str.append(lista.split("NOTA: ")[-1])
            aluno.append(lista.split("ALUNO: ")[-1].split(" NOTA:")[0])
    nota = list(map(float, nota_str))
    pos = nota.index(max(nota))
    print(f"A maior nota foi {nota[pos]} e pertence a o aluno {aluno[pos]}")
print("Obs: Digite o caminho do arquivo com a barra invertida [/] \nnesse programa só aceita arquivos .txt")
nome = input("Informe o arquivo: ")
arquivo_nota(nome)