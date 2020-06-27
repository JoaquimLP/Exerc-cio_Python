"""
12. Faça uma função para um código secreto que se baseie na estrutura “ZENIT POLAR”.
Ao digitar uma palavra ou frase, o programa deve inverter as letras conforme a
estrutura “ZENIT POLAR”. Exemplo: Se você digitar “LUIZ”, o resultado deve ser
“NUAP”. Se digitar “JOSE”, o resultado deve ser “JESO”. Se digitar “CORCINI”, o
resultado deve ser “CETCALA”.
"""
from random import sample
def zenit_polar(letra):
    x = list(letra)
    y = list()
    for c in range(len(x)):
        if x[c] == "A":
            y.append("I")
        elif x[c] == "B":
            y.append("D")
        elif x[c] == "C":
            y.append("C")
        elif x[c] == "D":
            y.append("B")
        elif x[c] == "E":
            y.append("O")
        elif x[c] == "F":
            y.append("H")
        elif x[c] == "G":
            y.append("G")
        elif x[c] == "I":
            y.append("A")
        elif x[c] == "H":
            y.append("F")
        elif x[c] == "J":
            y.append("J")
        elif x[c] == "K":
            y.append("Q")
        elif x[c] == "L":
            y.append("N")
        elif x[c] == "M":
            y.append("V")
        elif x[c] == "N":
            y.append("L")
        elif x[c] == "O":
            y.append("E")
        elif x[c] == "P":
            y.append("Z")
        elif x[c] == "Q":
            y.append("K")
        elif x[c] == "R":
            y.append("T")
        elif x[c] == "S":
            y.append("S")
        elif x[c] == "T":
            y.append("R")
        elif x[c] == "U":
            y.append("U")
        elif x[c] == "V":
            y.append("M")
        elif x[c] == "W":
            y.append("X")
        elif x[c] == "X":
            y.append("W")
        elif x[c] == "Z":
            y.append("P")
    a = "".join(y)
    print(a)
nome = input("Informe um nome: ").upper()
print(nome)
zenit_polar(nome)