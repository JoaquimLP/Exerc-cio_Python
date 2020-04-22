"""
15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se
    os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o
    mesmo é: equilátero, isósceles ou escaleno.
    Dicas:
        a. Três lados formam um triângulo quando a soma de quaisquer dois lados for
        maior que o terceiro;
        b. Triângulo Equilátero: três lados iguais;
        c. Triângulo Isósceles: quaisquer dois lados iguais;
        d. Triângulo Escaleno: três lados diferentes;
"""
ladoA = float(input("Informe o Primeiro lado do Triângulo: "))
ladoB = float(input("Informe o Primeiro lado do Triângulo: "))
ladoC = float(input("Informe o Primeiro lado do Triângulo: "))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoB + ladoA:
    print('Os segmentos acima PODEM FORMA UM TRIANGULO!', end=' ')
    if ladoA == ladoB == ladoC:
        print('EQUILÁTERO!')
    elif ladoA != ladoB != ladoC and ladoA != ladoC:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMA TRIANGULO!')