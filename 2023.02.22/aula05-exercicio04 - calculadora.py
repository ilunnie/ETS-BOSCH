
"""
Created on 22/02/2023

@author: Luis Gustavo Caris dos Santos
"""

num = float(input("Digite um número: "))

while True:
    op = int(input("Escolha uma operação:\n1. Adição\n2. Subtração\n3. Multiplicação\n4. Divisão\nDigite qualquer outra tecla para sair\n"))
    
    print('\n\n\n\n\n')
    if op == 1:
        num += float(input("Digite outro número: "))
    elif op == 2:
        num -= float(input("Digite outro número: "))
    elif op == 3:
        num *= float(input("Digite outro número: "))
    elif op == 4:
        num /= float(input("Digite outro número: "))
    else:
        break
    print(f'R: {num}')