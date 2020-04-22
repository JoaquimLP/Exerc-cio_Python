"""
14. Faça um programa que leia um número indeterminado de valores, correspondentes a
    notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que
    não deve ser armazenado). Após esta entrada de dados, faça:
        a. Mostre a quantidade de valores que foram lidos;
        b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
        c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
        d. Calcule e mostre a soma dos valores;
        e. Calcule e mostre a média dos valores;
        f. Calcule e mostre a quantidade de valores acima da média calculada;
        g. Calcule e mostre a quantidade de valores abaixo de sete;
        h. Encerre o programa com uma mensagem;
"""
from time import sleep
c = 0
cont = 0
cont1 = 0
lista = list()
while True:
    print("<>"*30)
    numero = int(input(f"informe um numero para posição {c+1}: "))
    if numero == -1:
        break
    else:
        if numero != -1:
            lista.append(numero)
    c += 1
    print("Para sair do Programa digite [ -1 ]")

print()
print("Gerando resultado...")
sleep(2)
print()
print("=============Resultado=============")
print(f"A) A quantida de valores infomado foi: {c}")
print("__"*20)
print("B) Exiba todos os valores na ordem em que\nforam informados, um ao lado do outro: ", end= '')
for i in range(len(lista)):
    print(f" {lista[i]}", end = " - ")
print("Fim")
print("__"*20)
print("C) Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;")
lista = lista[::-1]
for i in range(len(lista)):
    print(f" {lista[i]}")
print("__"*20)
print(f"D) A soma de todos os valores informado: {sum(lista)}")
print("__"*20)
media =  sum(lista)/len(lista)
print(f"E) A média de todos os valores informado: {media}")
print("__"*20)
for i in range(len(lista)):
    if lista[i] > media:
        cont += 1
for i in range(len(lista)):
    if lista[i] < 7:
        cont1 += 1
print(f"F) A quantidade de valores acima da média calculada: {cont}")
print("__"*20)
print(f"G) A quantidade de valores digitado abaixo de sete: {cont1}")
print("__"*20)
print("Finalizando o programa....")
sleep(2)
print("Inovação distingue o líder de um seguidor. Obrigado por usar nossos sitesma")
