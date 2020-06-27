"""
10. Embaralha palavra. Construa uma função que receba uma string como parâmetro e
    devolva outra string com os caracteres embaralhados. Por exemplo: se função
    receber a palavra “python”, pode retornar “npthyo”, “ophtyn” ou qualquer outra
    combinação possível, de forma aleatória. Padronize em sua função que todos os
    caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de
    como foram digitados.
"""
from random import sample
def embaralhar(p):
    e = sample(p, len(p))
    x = " ".join(e)
    print(x.lower())
nome = input('Digite algo: ')
embaralhar(nome)