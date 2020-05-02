"""
26.	O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as
    um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas
    informadas, bem como a média das temperaturas.
"""
n_temperatura = int(input("Quantidade de temperaturas que irá digitar: "))
maior = 0
menor = 0
soma = 0
for i in range(n_temperatura):
    print(f"Temperatura n° {n_temperatura}")
    dados = int(input(f"Informe a {i+1}º temperatura: "))
    soma += dados
    if i == 0:
        maior = dados
        menor = dados
    else:
        if dados > maior:
            maior = dados
        if dados < menor:
            menor = dados
media = soma / n_temperatura
print(f"Maior temperatura informada: {maior}")
print(f"Menor temperatura informada: {menor}")
print(f"Média das temperatura informada: {media}")

