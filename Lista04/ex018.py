"""
18. Sua organização acaba de contratar um estagiário para trabalhar no Suporte de
    Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta
    área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá,
    testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar
    deles. Foi requisitado que você desenvolva um programa para registrar este
    levantamento. O programa deverá receber um número indeterminado de entradas,
    cada uma contendo:
        a. um número de identificação do mouse o tipo de defeito, QUE PODE SER:
            i. necessita da esfera;
            ii. necessita de limpeza;
            iii. necessita troca do cabo ou conector;
            iv. quebrado ou inutilizado
    Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o
    seguinte relatório:
"""
mouse = [0, 0, 0, 0]
lis = []
cont = 0
while True:
    print("[ 1 ] necessita da esfera;"
          "\n[ 2 ] necessita de limpeza;"
          "\n[ 3 ] necessita troca do cabo ou conector;"
          "\n[ 4 ] quebrado ou inutilizado")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 0:
        break
    else:
        while opcao > 4:
            print("Erro...")
            opcao = int(input("Escolha uma Opção: "))
        if opcao == 1:
            quant = int(input("Quantos necessita da esfera: "))
            mouse[0] += quant

        elif opcao == 2:
            quant = int(input("Quantos necessita de limpeza: "))
            mouse[1] += quant

        elif opcao == 3:
            quant = int(input("Quantos necessita troca do cabo ou conector: "))
            mouse[2] += quant

        elif opcao == 4:
            quant = int(input("Quantos quebrado ou inutilizado: "))
            mouse[3] += quant


    print("Digite [0] para finalizar")
    cont += 1
print()
for i in range(len(mouse)):
    pocen = (mouse[i] * (sum(mouse))) / 100
    lis.append(pocen)
print(f"Situação                           Quantidade  Percentual", end=""
      f"\nnecessita da esfera:                  {mouse[0]}          {lis[0]}%"
      f"\nnecessita de limpeza:                 {mouse[1]}          {lis[1]}%"
      f"\nnecessita troca do cabo ou conector:  {mouse[2]}          {lis[2]}%"
      f"\nquebrado ou inutilizado:              {mouse[3]}          {lis[3]}%")