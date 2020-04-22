"""
3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra
    escrever: F - Feminino, M – Masculino ou Sexo Inválido.
"""
sexo = input("Digite F - Feminino ou M – Masculino: ")
if sexo == "f" or sexo == "F":
    print("Sexo Feminino")
elif sexo == "m" or sexo == "M":
    print("Sexo Masculino")
else:
    print('Sexo Inválido')