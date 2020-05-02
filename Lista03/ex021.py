"""
21. Faça um programa que calcule o valor total investido por um colecionador em sua
    coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a
    quantidade de CDs e o valor para em cada um.
"""
soma = 0

quantCd = int(input("Informe quantidade de CDs tem sua coleção: "))
while quantCd <= 0:
    print("Deve ser informando pelo menos um CD!")
    quantCd = int(input("Informe quantidade de CDs tem sua coleção: "))
for c in range(quantCd):
    valorCd = float(input(f"Quantos você pagou no {c + 1}º cd: "))
    soma += valorCd
media = soma / quantCd
print("=="*20)
print(f"Sua coleção tem {quantCd}.")
print(f"Valor total pago em sua coleção é {soma}")
print(f"O valor médio gasto por cada CD foi de: R$ {media}")