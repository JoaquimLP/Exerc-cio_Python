"""
6. Faça um programa que use a função valor_Pagamento para determinar o valor a ser
pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor
da prestação e o número de dias em atraso e passar estes valores para a função
valor_Pagamento, que calculará o valor a ser pago e devolverá este valor ao programa
que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a
execução o programa deverá voltar a pedir outro valor de prestação e assim continuar
até que seja informado um valor igual a zero para a prestação. Neste momento o
programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade
e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da
seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando
houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""
from time import sleep
from datetime import date
def boleto(valo_paragemento, dia_atrasado):
         juros_atrasado = 0
         if dia_atrasado > 0:
            for cont in range(1, dia_atrasado +1):
                juros_atrasado += 0.1
            valor_multa = (valo_paragemento * 3)/100
            valor_juros = (valo_paragemento * juros_atrasado)/100
            total_pago = valo_paragemento + valor_multa + valor_juros
            print(f'Valor a pagar: R${valo_paragemento:.2f}'
                  f'\nQuantidade de dias atrasado: {dia_atrasado}.'
                  f'\nValor da multa 3%: R${valor_multa:.2f}'
                  f'\nValor do juros de {juros_atrasado:.2f}%: R${valor_juros:.2f}'
                  f'\ntotal a ser pago: R${total_pago:.2f}')
         else:
             print(f"Não ouver atraso, vai ser cobrado apenas o valor do boleto.."
                   f"\nValor a pagar: R${valo_paragemento:.2f}")

def pagar(pagar):
    if pagar in "Ss":
        print("Efetuando o pagramento...")
        sleep(2)
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("Pagamento relizado com suscesso")

c = 0
p = 0
while True:
    print("--"*20)
    print("Digite zero(0) para finalizar o programa: ")
    parcela = float(input("Informe o valor da Parcela: R$"))
    if parcela == 0:
        break
    dia = int(input("Informe a quantidade de dias em atrasos: "))
    print("--"*20)
    boleto(parcela, dia)
    print("--" * 20)
    efetuando = input("Deseja fazer o pagamento: [S/N] ").upper().strip()
    while efetuando not in 'SsNn':
        efetuando = input("Deseja fazer o pagamento: [S/N] ").upper().strip()
    if efetuando in 'Ss':
        pagar(efetuando)
        p += 1
    c += 1
print("Carrengando....")
sleep(2)
data_atual = date.today()
np = c - p
print("--=--=--=--=--=--=RELATORIO=--=--=--=--=--=--")
print(f'No dia {data_atual.day}/{data_atual.month}/{data_atual.year}')
print(f'Foram processado {c} boletos'
      f'\n{p} boletos pagos'
      f'\n{np} boletos pendentes.')
