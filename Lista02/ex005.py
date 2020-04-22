"""
5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve
    calcular a média alcançada por aluno e apresentar:
        a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
        b. A mensagem "Reprovado", se a média for menor do que sete;
        c. A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""
from time import sleep
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a Segunda nota: "))
media = (nota1 + nota2)/ 2

print("--"*20)
print("Carregando....")
sleep(2)
print("><"*20)
if media == 10:
    print(f"PARABENS... sua media foi {media:.2f}, Aprovado com Distinção")
elif media >= 7 and media < 10:
    print(f"PARABENS... sua media foi {media:.2f}, Aprovado")
elif media < 7:
    print(f"REPROVADO... sua media foi {media:.2f}.")
else:
    print("Media muito alta do valor sugerido")