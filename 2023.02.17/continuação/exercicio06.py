menu = {'HAMBURGUER' : 10,
        'HOTDOG' : 6.5,
        'SALADA' : 4,
        'SUCO' : 4,
        'REFRIGERANTE' : 4.5,
        'ÁGUA' : 2}
escolha = ' '
preco = 0

def cardapio():
    print("\n\n")
    print("\t    Menu FastFood")
    for item, precos in menu.items():
        print('\t{:12} | R${:.2f}'.format(item.capitalize(), precos))
    print("\n")

while escolha != '':
    cardapio()
    escolha = input('Faça o seu pedido: ').upper()
    try:
        preco += menu[escolha]
    except:
        if escolha != '':
            print(f'Item "{escolha.capitalize()}" não foi encontrado, verifique a ortografia.')

print(f'\n\n\n\nPedido finalizado!\nTotal: R${preco:.2f}')