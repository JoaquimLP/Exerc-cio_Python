"""
18. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade
    de centenas, dezenas e unidades do mesmo.
    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    a. 326 = 3 centenas, 2 dezenas e 6 unidades
    b. 12 = 1 dezena e 2 unidades
    c. Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
numero = int(input("Digite um numero inteiro e positivo: "))

unidade = numero % 10
dezena = ((numero - unidade) // 10)%10
centena = (numero - dezena)// 100

print(f"{numero} = {centena} centenas, {dezena} dezenas e {unidade} unidades")