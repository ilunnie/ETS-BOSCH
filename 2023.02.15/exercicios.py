"""
Created on 15/02/2023

@author: Luis Gustavo Caris dos Santos
"""

import tkinter as tk

# Cria a janela principal
janela = tk.Tk()
janela.title("Exercícios 15/02/2023")

# Exercício 01
def ex01():
    janela = tk.Tk()
    janela.title("exercicio 3")
    janela.minsize(300, 200)

    celsius_label = tk.Label(janela, text="Graus Celsius:")
    celsius_label.pack()
    celsius_entry = tk.Entry(janela)
    celsius_entry.pack()

    fahrenheit_label = tk.Label(janela, text="Graus Fahrenheit:")
    fahrenheit_label.pack()
    fahrenheit_entry = tk.Entry(janela, state="readonly")
    fahrenheit_entry.pack()

    def converter():
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_entry.config(state="normal")
        fahrenheit_entry.delete(0, "end")
        fahrenheit_entry.insert(0, fahrenheit)
        fahrenheit_entry.config(state="readonly")
        
    converter_button = tk.Button(janela, text="Converter", command=converter)
    converter_button.pack()

    janela.mainloop()

# Exercício 02
def ex02():
    janela = tk.Tk()
    janela.title("exercício 2")
    janela.minsize(300, 200)
    
    texto_label = tk.Label(janela, text="Digite uma palavra ou frase:")
    texto_label.pack()
    texto_entry = tk.Entry(janela)
    texto_entry.pack()
    
    def cortar():
        corte_entry.config(state="normal")
        corte_entry.delete(0, "end")
        corte_entry.insert(0, (texto_entry.get())[:3].upper())
        corte_entry.config(state="readonly")
    
    corte_entry = tk.Entry(janela, state="readonly")
    corte_entry.pack()
        
    cortar_button = tk.Button(janela, text="Cortar", command=cortar)
    cortar_button.pack()

    janela.mainloop()
    
# Exercício 03
def ex03():
    janela = tk.Tk()
    janela.title("exercício 3")
    janela.minsize(300, 200)
    
    texto_label = tk.Label(janela, text="Digite seu nome completo:")
    texto_label.pack()
    texto_entry = tk.Entry(janela)
    texto_entry.pack()
    
    def formatar():
        nomeCompleto = (texto_entry.get())[:3].lower()
        nome = nomeCompleto.split(' ')
        formatado = ""
        
        for palavra in nome:
            formatado += palavra.capitalize() + " "
            
        texto_entry.delete(0, "end")
        texto_entry.insert(0, formatado)
        
    format_button = tk.Button(janela, text="Formatar", command=formatar)
    format_button.pack()
    
    
# Botões dos exercícios    

ex01_button = tk.Button(janela, text="Exercício 01", command=ex01)
ex01_button.pack()

ex02_button = tk.Button(janela, text="Exercício 02", command=ex02)
ex02_button.pack()

ex03_button = tk.Button(janela, text="Exercício 03", command=ex03)
ex03_button.pack()

janela.mainloop()