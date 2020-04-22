'''
20. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de
download do arquivo usando este link (em minutos).
'''
tamanho = float(input('Tamanho do arquivo (MB): '))
velocidade = float(input('Velocidade de Internet (MBps): '))
download = (tamanho / velocidade) * 60
print(f'Tempo aproximado de download: {download:.2f} Minutos ')
