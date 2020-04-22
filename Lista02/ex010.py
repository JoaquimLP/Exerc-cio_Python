"""
10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-
    matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa
    Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
print("---------------Escola Bom Saber---------------")
print("[M]- matutino\n[V] - Vespertino\n[N] - Noturno")
nome = input("Qual e o seu nome: ")
turno = input("Em que turno você estuda: ")

if turno in 'Mm':
    print(f"Bom dia! {nome}")
elif turno in 'Vv':
    print(f"Boa Tarde! {nome}")
elif turno in 'Nn':
    print(f"Boa noite! {nome}")
else:
    print("Valor Inválido!")