
"""
Created on 22/02/2023

@author: Luis Gustavo Caris dos Santos
"""

import random

vitorias, derrotas, record, seguidas = 0, 0, 0, 0

def jogada(lado, mao, bot):
    if ((mao+bot)%2 == 0):
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print(f'\n\n\n\n\nVocê jogou: {mao}\nO adversário jogou: {bot}\n')
    resultado_jogada(lado, resultado)

def resultado_jogada(lado, resultado):
    global vitorias, derrotas, record, seguidas
    if (lado == resultado):
        print('Parabéns!!!\nVocê ganhou')
        vitorias += 1
        seguidas += 1
        if (seguidas > record):
            record = seguidas
    else:
        print('Que pena...\nVocê perdeu')
        derrotas += 1
        seguidas = 0

def tabela():
    print('\n\n')
    print(f'Vitórias: {vitorias}    record: {record}')
    print(f'Derrotas: {derrotas}')

while True:
    tabela()
    lado, mao = 0, -1
    while lado != 'PAR' and lado != 'IMPAR':
        lado = input('\nPAR ou IMPAR?\n').upper()
        if (lado == 'P' or lado == 'PAR'):
            lado = 'PAR'
        elif (lado == 'I' or lado == 'IMPAR'):
            lado = 'IMPAR'
        else:
            print('\n\nComando não reconhecido, tente novamente...')
    while (mao < 1 or mao > 10):
        mao = int(input('\nDigite um número de 1 a 10: '))
        if (mao < 1 or mao > 10):
            print('\n\nValor inválido, tente novamente...')
    
    bot = random.randint(1, 10)
    jogada(lado, mao, bot)