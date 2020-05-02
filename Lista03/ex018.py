"""
18.	Faça um programa que calcule o mostre a média aritmética de N notas
"""
print("=======Calculadora de média aritmética=======\n")
num = int(input("Digite a quantidade de valores deseja calcular"
                "\na média aritmética: "))
soma = 0
while num <= 0:
    print("Deve ser informado pelo menos um valor.")
    num = int(input("Digite a quantidade de valores deseja calcular"
                    "\na média aritmética: "))
for i in range(num):
    nota = float(input(f"Digite a {i + 1} nota: "))
    while nota < 0:
        print("Erro... não pode digitar valores negativos.")
        nota = float(input(f"Digite a {i + 1} nota: "))
    soma += nota
media = soma / num
print(f"Foram digitado {num} notas,"
      f"\na média aritmética dos valores informados é {media}.")