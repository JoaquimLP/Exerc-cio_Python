"""
11. As Organizações Tabajara resolveram dar um aumento de salário aos seus
    colaboradores e lhe contrataram para desenvolver o programa que calculará o
    Linguagem de Programação Python reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste
        segundo o seguinte critério, baseado no salário atual:
            a. salários até R$ 280,00 (incluindo) : aumento de 20%
            b. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
            c. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
            d. salários de R$ 1500,00 em diante : aumento de 5%
        Após o aumento ser realizado, informe na tela:
            o salário antes do reajuste;
            o percentual de aumento aplicado;
            o valor do aumento;
            o novo salário, após o aumento.
"""
from time import sleep
print('--------------Grupo Tabajara--------------')
sal = float(input("Digite o salario do Funcionario: "))
print("--"*20)
print("Carregando...")
sleep(2)
print("-----------Resultado-----------")
if sal <= 280:
    aumento = (sal * 20)/100
    novo = sal+aumento
    print(f"Salario antigo: R${sal:.2f}"
          f"\no percentual de aumento aplicado 20%\nValor do Aumento R${aumento}\no novo salário R${novo}")
elif sal > 280 and sal <= 700:
    aumento = (sal * 15)/100
    novo = sal+aumento
    print(f"Salario antigo: R${sal:.2f}"
          f"\no percentual de aumento aplicado 15%\nValor do Aumento R${aumento}\no novo salário R${novo}")
elif sal > 700 and sal <= 1500:
    aumento = (sal * 10) / 100
    novo = sal + aumento
    print(f"Salario antigo: R${sal:.2f}"
          f"\nO percentual de aumento aplicado 10%\nValor do Aumento R${aumento}\nO novo salário R${novo}")
else:
    aumento = (sal * 5) / 100
    novo = sal + aumento
    print(f"Salario antigo: R${sal:.2f}"
          f"\no percentual de aumento aplicado 5%\nValor do Aumento R${aumento}\no novo salário R${novo}")
