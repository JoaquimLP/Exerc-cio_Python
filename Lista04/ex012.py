"""
12. Faça um programa que receba a temperatura média de cada mês do ano e armazeneas em uma lista.
    Após isto, calcule a média anual das temperaturas e mostre todas as
    temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por
    extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
temperatura = []
meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio',
         'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']
mediaMes = 0
anual = {}
for c in range(len(meses)):
    temp = float(input(f'Informe a Temperatura media de {meses[c]}: '))
    temperatura.append(temp)
    mediaMes += temperatura[c]
media = mediaMes/len(meses)
for i in range(len(meses)):
    if (temperatura[i] > media):
        anual.update({meses[i]: temperatura[i]})
print(f'Media das temperaturas : Anual -> {media}')
print(f'Meses com temperaturas acima da media: {anual}')
