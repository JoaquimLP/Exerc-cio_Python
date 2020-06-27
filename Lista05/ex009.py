"""
9. Data com mês por extenso. Construa uma função que receba uma data no
formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de
AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
"""
mes_por_extenso=[' ','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
def mesPorExtenso(data):
    global dia,mes, ano
    data = data.split('/')
    mes = int(data[1])
    dia = int(data[0])
    ano = int(data[2])
    if mes > 0 or mes < 13:
        if mes == 2:
            if mes == 2:
                if dia == 29:
                    if (ano%4 == 0 and ano%100!= 0) or (ano%400==0):  # ano bissexto
                        return "VALIDA"
                    else:
                        return "NULL"
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia > 0 and dia <= 31:
                return "VALIDA"
            else:
                return "NULL"
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia > 0 and dia <= 30:
                return "VALIDA"
            else:
                return "NULL"
        else:
            return "NULL"
    else:
        return "NULL"

print("===========DATA COM O MES ESCRITO POR EXTENSO===========")
data=input("Digite uma data com o seguinte formato dd/mm/aaaa: ")
data_valida = mesPorExtenso(data)
if data_valida == "VALIDA":
    print(f"Você informou a data: {str(dia)} de {mes_por_extenso[mes]} de {str(ano)}")
else:
    print("Data inválida!")

