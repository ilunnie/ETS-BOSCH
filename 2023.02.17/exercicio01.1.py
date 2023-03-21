import time
import tkinter as tk

# Função para gerar números aleatórios
def generate_random_number(seed, min_val, max_val):
    a = 1103515245
    c = 12345
    m = 2**31
    seed = (a * seed + c) % m
    return min_val + (max_val - min_val) * seed / m

# Função que é executada quando o botão "Jogar" é clicado
def jogar():
    global random_number
    num = int(entry.get())
    if (num == int(random_number)):
        label_resultado.config(text=f'Parabéns, você acertou!\nO número sorteado era {random_number:.0f}')
        entry.config(state='disabled')
        botao.config(state='disabled')
    elif (num > random_number):
        label_resultado.config(text=f'O número sorteado é menor que {num}.')
    else:
        label_resultado.config(text=f'O número sorteado é maior que {num}.')

# Cria a janela principal
janela = tk.Tk()
janela.title('Jogo de Adivinhação')

# Usa o tempo atual como semente para a geração de números aleatórios
seed = time.time()
seed = int((seed - int(seed)) * 1000000)

# Gera um número aleatório dentro do intervalo especificado
min_val = 0
max_val = 99
random_number = generate_random_number(seed, min_val, max_val)

# Cria os widgets da interface
label_instrucoes = tk.Label(janela, text='Tente adivinhar o número entre 0 e 99:')
label_instrucoes.pack()

entry = tk.Entry(janela)
entry.pack()

botao = tk.Button(janela, text='Jogar', command=jogar)
botao.pack()

label_resultado = tk.Label(janela, text='')
label_resultado.pack()

# Inicia o loop de eventos da janela
janela.mainloop()