"""
7. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação
no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
"""
altura = []
idade = []
for c in range(5):
    id = int(input(f"Digite a idade da pessoa {c+1}: "))
    alt = float(input(f"Digite a altura da pessoa {c + 1}: "))
    idade.append(id)
    altura.append(alt)
print(f"Ordem lida {altura}")
print(f"Ordem lida {idade}")
print("=="*20)
print(f"Ordem inversa {altura[::-1]}")
print(f"Ordem inversa {idade[::-1]}")
