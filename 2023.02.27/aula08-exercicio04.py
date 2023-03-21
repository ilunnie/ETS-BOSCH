
"""
Created on 27/02/2023

@author: Luis Gustavo Caris dos Santos
""""""
    Exercício 4 - Aula 8

Objetivo:
     • Crie uma estrutura para abrir e controlar as contas de um banco;
     • As contas corrente, poupança e salário, devem possuir uma classe Conta como herança;
     • Herdando informações e métodos na qual todos os tipos de conta possuam. Ex: Abrir conta;
     • Utilizando do encapsulamento. Ex: Valor da conta.
"""

# Classe mãe
class Conta():
    def __init__(self, cliente, saldo) -> None:
        self.__cliente = cliente
        self.__saldo = saldo

    def getSaldo(self):
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print('Saldo insuficiente!')

    def imprimirSaldo(self):
        print(f'cliente: {self.__cliente}')
        print(f'Saldo: R${self.__saldo}')

class ContaCorrente(Conta):
    def __init__(self, cliente, saldo, limite) -> None:
        super().__init__(cliente, saldo)
        self.limite = limite

class ContaPoupanca(Conta):
    def __init__(self, cliente, saldo, juros) -> None:
        super().__init__(cliente, saldo)
        self.juros = juros

    def aplicar_juros(self):
        self.set_saldo(self.get_saldo() * (1 + self.juros))

class ContaSalario(Conta):
    def __init__(self, cliente, saldo, empresa) -> None:
        super().__init__(cliente, saldo)
        self.empresa = empresa