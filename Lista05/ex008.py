"""
8. Descreva o que faz cada linha do programa abaixo:
"""
def funcao_secreta(N): # Nessa linha eu definir um paramento N, que vai ser recaber o valor informado pelo o usario
    x = list(str(N)) # Pega valor de N e amarzenda numa lista de guada numa  variavel x
    x.reverse() #  inverti sequência do valores armazenado na lista X
    y = ' '.join(x) # Junta, todos os elemento da variavel x adicionando um espaço com separador
    print(y) # Imprimir os valores que está armazenado na variavel Y

funcao_secreta(123) # Valores informado pelo usuario

