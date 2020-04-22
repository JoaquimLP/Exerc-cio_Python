"""
2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
    ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
    informações.
"""
nome = input("Informe o seu usuário: ")
senha = input('Digite sua senha: ')
senhaCadastrada = "csd123"
c = 0
while senha != senhaCadastrada:
    print("Senha Invalida...")
    senha = input('Digite sua senha: ')
    c += 1
print("Login efetuado com sucesso")