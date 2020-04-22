"""
10. Faça um programa que leia um nome composto e depois informe qual é o
comprimento do nome (em caracteres).
"""
nome = input("Digite seu nome completo? ")

print("<>"*20)
print("Olá, ", nome.strip(), " o tamanho do seu nome é ", len(nome.strip()))