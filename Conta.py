class Conta:
    def __init__(self, t, n, saldo):

        self._titular = t
        self._numero = n
        self._saldo = saldo


    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo<0:
            print('O saldo nao pode ser negativo!')
        else:
            self._saldo += saldo

    def saque(self, valor):
        if self._saldo >= valor:
            print(f'Saldo Realizado! no valor de {valor}')
            self._saldo -= valor
        else:
            print('Saque não realizado')

    def deposita(self, valor):
        self._saldo += valor

    def extrato(self):
        print(f'Cleinte: {self._titular} com o saldo {self._saldo}')