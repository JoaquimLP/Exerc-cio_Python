"""
8. Altere o programa anterior para mostrar no final a soma dos números.
"""
num1=int(input("digite um numero: "))
num2=int(input("digite outro numero: "))
n = 0
while num1 > num2:
    num1 = int(input("digite um numero: "))
    num2 = int(input("digite outro numero: "))
else:
    for c in range(num1, num2 +1):
        n += c
        print(c, end=" + ")
        c += 1

print(f"FIM total = {n}")