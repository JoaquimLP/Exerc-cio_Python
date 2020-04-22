"""
9. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
inteiro entre 1 a 10. O usuário deve informar de qual número ele deseja ver a tabuada.
A saída deve ser conforme o exemplo abaixo:
"""
n = 0
while True:
    n = int(input('Digite um numero para vermos a sua tabuada: ou informe {-1} para sair'))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c}= {n * c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. volte sempre!')