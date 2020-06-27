"""
1. Faça um programa que receba do usuário um arquivo texto e mostre na tela quantas linhas
esse arquivo possui.
"""
from time import sleep
print("Obs: Digite o caminho do arquivo com a barra invertida [/]\nnesse progama só aceita arquivos .txt")
print("-"*25)
arquivo = input("Informe o arquivo: ")

with open(arquivo) as f:
    cont = sum(1 for _ in f)

print("Aguarde so um momento o sistema está processado...")
sleep(2)
print(f'O arquivo informado tem: {cont} linhas')

print(f"Fechando o arquivo {f.closed}")