"""
20. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação
    ele deseja realizar. O programa deve apresentar o resultado da operação
"""
num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite outro numero inteiro: "))
print("[1] para somar\n"
      "[2] para subtrair\n"
      "[3] para multiplicar\n"
      "[4] para dividir")
op = int(input("Qual a operação deseja realisar: "))

if op == 1:
    res = num1 + num2
    print(f"A soma de {num1} + {num2} = {res}")
elif op == 2:
    if num1 > num2:
        res = num1 - num2
        print(f"A subtraindo {num1} - {num2} = {res}")
    else:
        res = num2 - num1
        print(f"A subtraindo  {num2} - {num1} = {res}")
elif op == 3:
    res = num1 * num2
    print(f"A multiplicando {num2} x {num1} = {res}")
elif op == 4:
    if num1 > num2:
        res = num1 / num2
        print(f"A divisão de {num1} ÷ {num2} = {res}")
    else:
        res = num2 / num1
        print(f"A multiplicando {num2} ÷ {num1} = {res}")
else:
    print("OPERAÇÃO Inválida.....")