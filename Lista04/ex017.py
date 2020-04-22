"""
17. Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de
    modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses
    carros, isto é, quantos quilômetros cada um desses carros faz com um litro de
    combustível. Calcule e mostre:
        a.  O modelo do carro mais econômico;

        b.  Quantos litros de combustível cada um dos carros cadastrados consome para
            percorrer uma distância de 1000 quilômetros e quanto isto custará,
            considerando um que a gasolina custe R$ 2,25 o litro.
    Abaixo segue uma tela de exemplo. O disposição das informações deve ser o
    mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada
    execução do programa.
"""
from time import sleep
carros = [[], [], [], []]
c = 0
km = 1000
preco = 2.25
menor = 0
p = 0
while c < 5:
    print(f"Veículo {c+1}:")
    modelo = input("Nome: ").upper().strip()
    kmlitro = float(input("Km por litro: "))
    carros[0].append(modelo)
    carros[1].append(kmlitro)
    c += 1
for c in range(len(carros[0])):
    kmfeito = km / carros[1][c]
    valorPago = kmfeito * preco
    carros[2].append(kmfeito)
    carros[3].append(valorPago)
print("=="*15)
print("Carregando...")
print()
sleep(2)
for i in range(len(carros[0])):
    print(f"modelo: {carros[0][i]}"
          f"\nKm por litro: {carros[1][i]}"
          f"\nFez {round(carros[2][i], 1)} em 1000km"
          f"\nGasto R${carros[3][i]:.2f}")
    print("=="*15)
    sleep(2)

menor = min(carros[3])
pos = carros[3].index(menor)
print(f"O menor consumo é do {carros[0][pos]}")