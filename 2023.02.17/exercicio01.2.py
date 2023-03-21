
"""
Created on 17/02/2023

@author: Luis Gustavo Caris dos Santos
"""

import time
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivymd.app import MDApp
from kivy.core.window import Window

KV = """
Screen:
    BoxLayout:
        orientation: 'vertical'

        MDLabel:
            id: num_label
            halign: 'center'
            font_style: 'H3'
            theme_text_color: 'Custom'
            text: 'Vamos jogar?'
            size_hint_y: 0.7
            text_color: (0.49, 0.18, 0.55, 1)

        MDTextField:
            id: num_input
            hint_text: 'Digite um número:'
            helper_text: 'Entre 0 e 99'
            helper_text_mode: 'on_focus'
            input_filter: 'int'
            size_hint_y: 0.5
            size_hint_x: None
            width: dp(250)
            multiline: False
            pos_hint: {'center_x': 0.5}

        MDLabel:
            id: resultado_label
            halign: 'center'
            theme_text_color: 'Custom'
            text: 'Chute um número'
            size_hint_y: 0.4
            pos_hint: {'center_y': 0.5}
            text_color: (0.49, 0.18, 0.55, 0.5)

        MDFlatButton:
            text: 'Tentar'
            pos_hint: {'center_x': 0.5}
            size_hint_y: 0.7
            on_release: app.check_num()
            theme_text_color: 'Custom'
            text_color: (0.49, 0.18, 0.55, 1)
"""


class JogoDeAdivinhacao(MDApp):
    vitoria = BooleanProperty(False)

    def build(self):
        # Define o tamanho da janela como 400x300
        Window.size = (400, 300)
        # Define o fundo como Claro
        self.theme_cls.theme_style = 'Light'
        # Define a paleta primaria como DeepPurple(Roxo escuro)
        self.theme_cls.primary_palette = 'DeepPurple'
        return Builder.load_string(KV)

    # Quando iniciar, usa o horario para salvar um número aleatório
    def on_start(self):
        seed = time.time()
        seed = int((seed - int(seed)) * 1000000)
        # Valor minimo
        self.min_val = 0
        # Valor máximo
        self.max_val = 99
        # Chama a função de gerar o número
        self.random_number = int(self.generate_random_number(seed, self.min_val, self.max_val))
        self.root.ids.num_label.text = 'Vamos jogar?'

    # Gera um número aleatório
    def generate_random_number(self, seed, min_val, max_val):
        a = 1103515245
        c = 12345
        m = 2**31
        seed = (a * seed + c) % m
        return min_val + (max_val - min_val) * seed / m

    # Checa se o número digitado é igual ao número aleatório
    def check_num(self):
        if not self.vitoria:
            num_input = self.root.ids.num_input
            try:
                num = int(num_input.text)
            except ValueError:
                num_input.text = ''
                return

            if num == int(self.random_number):
                self.vitoria = True
                self.root.ids.num_label.text = 'Parábens!!!'
                self.root.ids.resultado_label.text = f'\nO número sorteado era {self.random_number:.0f}'
                self.root.ids.resultado_label.text_color = (0.49, 0.18, 0.55, 1)
                num_input.disabled = True
            elif num > self.random_number:
                self.root.ids.resultado_label.text = f'O número sorteado é menor que {num}'
            else:
                self.root.ids.resultado_label.text = f'O número sorteado é maior que {num}'

if __name__ == '__main__':
    JogoDeAdivinhacao().run()