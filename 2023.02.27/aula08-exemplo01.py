
class Carro:
    def __init__(self, cor) -> None:
        self.cor = cor
        self.ligado = False

    def ligar(self):
        if self.ligado:
            print('Já está ligado')
        else:
            print('Carro ligando')
            self.ligado = True

    def desligar(self):
        if self.ligado:
            print('Carro desligando')
            self.ligado = False
        else:
            print('Carro já está desligado')

carro1 = Carro('Vermelho')
print(carro1.cor)