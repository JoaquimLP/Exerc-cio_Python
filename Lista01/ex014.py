"""
14. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo .
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo.
"""
num1 = int(input("Informe o primeiro numero: "))
num2 = int(input("Informe o segundo numero: "))
num3 = float(input("Informe o terceiro numero: ")) #{:.2f}

a = (num1*2)*(num2/2)
b = (num1*3)+ num3
c = pow(num3,3)

print("<>"*30)
print("o produto do dobro do primeiro com metade do segundo {:.2f}.".format(a))
print("<>"*25)
print("a soma do triplo do primeiro com o terceiro {:.2f}.".format(b))
print("<>"*20)
print("o terceiro elevado ao cubo {:.2f}.".format(c))
print("<>"*20)
