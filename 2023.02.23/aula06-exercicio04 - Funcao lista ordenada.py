
"""
Created on 23/02/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 4 - Aula 6

Título: Função lista ordenada

Objetivo:
    • Crie uma função com 3 parâmetros: limite inferior, limite superior e tamanho da lista;
    • Preencha a lista com números aleatórios dentro dos limites estabelecidos nos parâmetros;
    • Ordene a lista em ordem crescente;
    • NÃO UTILIZAR A FUNÇÃO "sort()";
    • DICA: Utilize a biblioteca "random";
"""

import random

# Função que cria lista com valores aleatórios
def cria_lista(inferior, superior, tamanho):
    global lista
    lista = []

    for i in range(tamanho):
        lista.append(random.randint(inferior, superior))

# Função que ordena uma lista
def ordenar(list):
    '''
        A cada item na lista(i) ele compara com todos os itens da mesma lista(j)
        Se o item j for maior que o item i:
            Salva o valor antigo do i em uma variavel 'save'
            Passa o valor de j para o i
            Passa o valor salvo anteriormente para o j
    '''
    for i in range(len(list)):
        for j in range(len(list)):
            if list[j] > list[i]:
                save = list[i]
                list[i] = list[j]
                list[j] = save
    return list

# Cria uma lista com os valores passados e mostra o resultado
cria_lista(int(input('Digite o limite inferior:')), int(input('Digite o limite superior:')), int(input('Digite o tamanho da lista:')))
print(f'lista original: {lista}')

# Ordena a lista e mostra o resultado
print(f'lista ordenada: {ordenar(lista)}')