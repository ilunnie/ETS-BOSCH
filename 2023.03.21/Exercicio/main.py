from Luis import *
from LuizMod import *
from Vini import *

def recebe_int(texto, erro="Valor inválido!"):
    while True:
        try:
            return float(input(texto))
        except:
            print(erro)

while True:
    print('\n'*30)
    num1 = recebe_int("\nDigite o primeiro número\n> ")
    num2 = recebe_int("\nDigite o segundo número\n> ")

    operacao = input("\nQual operação deseja fazer?\n> ").replace('*', 'x')

    match operacao:
        case "+":
            print(f"Resultado: {soma(num1, num2)}")
            break
        case "-":
            print(f"Resultado: {subtracao(num1, num2)}")
            break
        case "x":
            print(f"Resultado: {x(num1, num2)}")
            break
        case "/":
            print(f"Resultado: {div(num1, num2)}")
            break
        case "fs":
            print(f'Resultado: {fatorialsoma(num1, num2)}')
            break
        case other:
            print('\nEssa operação não existe.')
            break