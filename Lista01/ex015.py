"""
15. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) – 58
"""
altura = float(input("Informa o seu altura? "))

peso = (72.7*altura) - 58

print("###"*20)
print("A sua altura é {:.2f} seu peso ideal é, {:.2f}.".format(altura,peso))
