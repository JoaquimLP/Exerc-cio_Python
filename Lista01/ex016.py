"""
16. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
    o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que
    o estabelecido pelo regulamento de pesca do estado do Paraná (50 quilos) deve pagar
    uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa
    que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso
    a quantidade de quilos além do limite e na variável multa o valor da multa que João
    deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""
print("=-=-=-=--=-=-=-=-=-=-João Papo-de-Pescador=-=-=-=-=-=-=-=-=-=-=-=")

peso = float(input("Informe peso do peixe: "))

if 50 < peso :
    total = (peso - 50) * 4
    print("O peso passou pelo do limite estabelecido pelo regulamento\nde pesca do estado do Paraná (50 quilos) deve pagar\numa multa de R$ 4,00 por quilo excedente.")
    print("E o valor da multa vai ser. {:.2f}".format(total))
else:
    print("Peso esta no limite estabelecido pelo regulamento\nde pesca do estado do Paraná (50 quilos) deve pagar\numa multa de R$ 4,00 por quilo excedente.")
    print("Não precisa pagar a multa.")