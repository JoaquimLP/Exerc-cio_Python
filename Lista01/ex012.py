"""
12. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a
temperatura em graus Celsius.
C = (5 * (F-32) / 9).
"""

f = float(input("Qual e a temperatura hoje em graus Farenheit? "))
c = (5 * (f-32)/9)
print("Convertendo ", f, "f em graus ", c,"c")