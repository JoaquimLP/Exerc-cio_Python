"""
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
char = input("Informe uma Letra para saber se é VOGAL ou CONSOANTE: ")

if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or \
    char=='A' or char=='E' or char=='I' or char=='O' or char=='U':
           print('VOGAL')
else:
    print('CONSOANTE')