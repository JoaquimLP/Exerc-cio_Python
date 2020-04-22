"""
1. Faça um Programa que peça dois números e imprima o maior deles
"""
num1 = int(input("informe um numero qualquer"));
num2 = int(input("infomrme um numero qualquer"));

if num1 > num2:
    print("o numero maior é ", num1)
elif num1 == num2:
    print ("ambos os numeros são iguais ")
else:
    print("o numero maior é ", num2)
