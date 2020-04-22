"""
14. Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""
n = int(input("Digite a quantidade de numero deseja informa: "))
lista = []
c = 0
maior = 0
menor = 0
while c < n:
    num = int(input("Informe um numero: "))
    while 0 > num or num > 1000:
        num = int(input("Informe um numero: [ERRO!!!!] "))
    lista.append(num)
    c += 1
maior = max(lista)
menor = min(lista)
print(f"O maior valor enviado é {maior}")
print(f"O menor valor enviado é {menor}")