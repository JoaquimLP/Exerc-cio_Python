"""
5- Faça um programa com uma função chamada soma_Imposto. A função possui dois
parâmetros formais: taxa_Imposto, que é a quantia de imposto sobre vendas expressa
em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera”
o valor de custo para incluir o imposto sobre vendas.
"""
def soma_imposto(custo, taxa_Imposto):
    taxa = ((custo * taxa_Imposto)/100 )
    valor_final = custo + taxa
    print("__" * 20)
    print(f"Seu produto custou R${custo:.2f}\nImposto sobre o produto é {taxa_Imposto}%"
          f"\nVai ser acrecentado o valor de R${taxa:.2f}"
          f"\nO Valor de venda vai ser R${valor_final:.2f}")

produto = input("Iforme o produto que deseja fazer o calculo: ")
c = float(input("Informe o valor de compra do produto: "))
i = int(input("Digite a taxa de imposto %: "))
print("============Resultado Final============")
print(f'O produto {produto}: ')
soma_imposto(c,i)